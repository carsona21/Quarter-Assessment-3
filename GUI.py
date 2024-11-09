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
        questions = cursor.fetchall()
        conn.close()
        return questions

    def display_question(self):
        if self.question_index < len(self.questions):
            # Clear previous widgets
            for widget in self.root.winfo_children():
                widget.destroy()

            question_data = self.questions[self.question_index]
            self.question_text = question_data[1]
            self.options = question_data[2:6]  # Assuming options are in columns 2 to 5
            self.correct_option = question_data[-1]  # Assuming last column stores the correct option index

            tk.Label(self.root, text=f"Q{self.question_index + 1}: {self.question_text}").pack(pady=10)
            self.selected_answer = tk.IntVar()

            for idx, option in enumerate(self.options, start=1):
                tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx).pack(anchor=tk.W)

            tk.Button(self.root, text="Submit", command=self.check_answer).pack(pady=20)
        else:
            self.show_results()

    def check_answer(self):
        selected = self.selected_answer.get()
        if selected == self.correct_option:
            self.score += 1
            feedback = "Correct! Well done."
        else:
            correct_answer_text = self.options[self.correct_option - 1]  # Adjust for 0-based indexing
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


class QuizBowlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self.root, text="Welcome to the Quiz Bowl!").pack(pady=10)
        tk.Label(self.root, text="Select a topic to begin:").pack(pady=5)

        # Example topics - replace with your database table names
        topics = ["ACCT2110", "BMGT3500", "ECON4900", "MKT3400", "FIN3210"]
        self.selected_topic = tk.StringVar(value=topics[0])

        for topic in topics:
            tk.Radiobutton(self.root, text=topic, variable=self.selected_topic, value=topic).pack(anchor=tk.W)

        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        selected_topic = self.selected_topic.get()
        if selected_topic:
            quiz_window = tk.Toplevel(self.root)
            QuizWindow(quiz_window, selected_topic)
        else:
            messagebox.showwarning("Selection Error", "Please select a topic to start the quiz.")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizBowlApp(root)
    root.mainloop()
