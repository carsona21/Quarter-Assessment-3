class Question:
    def __init__(self, question_text, options, correct_option_index):
        self.question_text = question_text
        self.options = options
        self.correct_option_index = correct_option_index  # Assuming this is 1-based indexing

    def is_correct(self, selected_index):
        """Check if the selected answer is correct."""
        return selected_index == self.correct_option_index

    def get_correct_answer(self):
        """Return the correct answer text."""
        return self.options[self.correct_option_index - 1]  # Adjust for 0-based indexing

import tkinter as tk
from tkinter import messagebox
import sqlite3

class QuizWindow:
    def __init__(self, parent, selected_topic):
        self.root = parent
        self.selected_topic = selected_topic
        self.question_index = 0
        self.score = 0

        # Fetch questions for the selected topic
        self.questions = self.get_questions()
        self.current_question = None
        if not self.questions:
            tk.Label(self.root, text="No questions available for this topic.").pack()
            return

        self.display_question()

    def get_questions(self):
        conn = sqlite3.connect('quiz_bowl.db')
        cursor = conn.cursor()

        # Fetch 10 questions randomly from the selected topic
        query = f"SELECT * FROM {self.selected_topic} ORDER BY RANDOM() LIMIT 10"
        cursor.execute(query)
        question_data = cursor.fetchall()
        conn.close()

        # Convert each question row to a Question instance
        questions = []
        for data in question_data:
            question_text = data[1]  # Assuming second column is the question text
            options = data[2:6]  # Assuming options are in columns 2 to 5
            correct_option = data[-1]  # Assuming last column stores the correct option index
            questions.append(Question(question_text, options, correct_option))

        return questions

    def display_question(self):
        if self.question_index < len(self.questions):
            # Clear previous widgets
            for widget in self.root.winfo_children():
                widget.destroy()

            self.current_question = self.questions[self.question_index]

            tk.Label(self.root, text=f"Q{self.question_index + 1}: {self.current_question.question_text}").pack(pady=10)
            self.selected_answer = tk.IntVar()

            for idx, option in enumerate(self.current_question.options, start=1):
                tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx).pack(anchor=tk.W)

            tk.Button(self.root, text="Submit", command=self.check_answer).pack(pady=20)
        else:
            self.show_results()

    def check_answer(self):
        selected = self.selected_answer.get()
        if self.current_question.is_correct(selected):
            self.score += 1
            feedback = "Correct! Well done."
        else:
            correct_answer_text = self.current_question.get_correct_answer()
            feedback = f"Incorrect. The correct answer was: {correct_answer_text}."

        # Display feedback
        messagebox.showinfo("Feedback", feedback)

        # Move to the next question
        self.question_index += 1
        self.display_question()

    def show_results(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Quiz Completed! Your score: {self.score}/{len(self.questions)}").pack(pady=20)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=20)
