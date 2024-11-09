import tkinter as tk
from tkinter import messagebox
import sqlite3

# Main class for the Quiz Bowl App
class QuizBowlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl - Course Selection")
        self.selected_course = tk.StringVar()
        self.create_course_selection_window()

    def create_course_selection_window(self):
        tk.Label(self.root, text="Select a Course:").pack(pady=10)

        # Course selection using radio buttons
        courses = ['ACCT2110', 'BMGT3510', 'ECON4900', 'FIN3210','MKT3400']
        for course in courses:
            tk.Radiobutton(self.root, text=course, variable=self.selected_course, value=course).pack(anchor=tk.W)

        tk.Button(self.root, text="Start Quiz Now", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        course = self.selected_course.get()
        if not course:
            messagebox.showerror("Error", "Please select a course")
            return
        
        self.root.destroy()
        self.display_quiz_window(course)

    def display_quiz_window(self, course):
        quiz_window = tk.Tk()
        quiz_window.title(f"Quiz Bowl - {course}")

        conn = sqlite3.connect('quiz_bowl.db')
        cursor = conn.cursor()

        # Fetching 10 questions from the selected course
        cursor.execute(f"SELECT * FROM {course} ORDER BY RANDOM() LIMIT 10")
        questions = cursor.fetchall()
        conn.close()

        if not questions:
            tk.Label(quiz_window, text="No questions available for this course.").pack()
            return

        self.question_index = 0
        self.score = 0
        self.questions = questions
        self.quiz_window = quiz_window
        self.display_question()

    def display_question(self):
        for widget in self.quiz_window.winfo_children():
            widget.destroy()

        question_data = self.questions[self.question_index]
        question_text, *options, correct_option = question_data[1:]

        tk.Label(self.quiz_window, text=f"Q{self.question_index + 1}: {question_text}").pack(pady=10)
        self.selected_answer = tk.IntVar()

        for idx, option in enumerate(options, start=1):
            tk.Radiobutton(self.quiz_window, text=option, variable=self.selected_answer, value=idx).pack(anchor=tk.W)

        tk.Button(self.quiz_window, text="Submit", command=self.check_answer).pack(pady=20)

    def check_answer(self):
        if self.selected_answer.get() == self.questions[self.question_index][-1]:
            self.score += 1
        self.question_index += 1

        if self.question_index < len(self.questions):
            self.display_question()
        else:
            self.show_results()

    def show_results(self):
        for widget in self.quiz_window.winfo_children():
            widget.destroy()
        tk.Label(self.quiz_window, text=f"Quiz Completed! Your score: {self.score}/{len(self.questions)}").pack(pady=20)
        tk.Button(self.quiz_window, text="Exit", command=self.quiz_window.destroy).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizBowlApp(root)
    root.mainloop()
