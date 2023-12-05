import tkinter as tk
from tkinter import ttk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg='blue')  # Set the background color to blue

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the result
        result_entry = ttk.Entry(self.root, textvariable=self.result_var, font=('Arial', 20), justify='right', state='disabled')
        result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Calculator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

        # Configure row and column weights
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
