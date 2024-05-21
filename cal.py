import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2e2e2e")

        self.expression = ""

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total_label, self.label = self.create_display_labels()

        self.create_buttons()

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="#1f1f1f")
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.expression, anchor=tk.E, bg="#1f1f1f", fg="white", padx=24, font=("Arial", 18))
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text='', anchor=tk.E, bg="#1f1f1f", fg="white", padx=24, font=("Arial", 48, "bold"))
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self.root, bg="#333333")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons(self):
        buttons = {
            'C': (1, 0), '/': (1, 3), '*': (1, 2), '-': (1, 1),
            '7': (2, 0), '8': (2, 1), '9': (2, 2), '+': (2, 3),
            '4': (3, 0), '5': (3, 1), '6': (3, 2), '=': (3, 3, 2),
            '1': (4, 0), '2': (4, 1), '3': (4, 2),
            '0': (5, 0, 2), '.': (5, 2)
        }

        for btn_text, grid_value in buttons.items():
            self.create_button(btn_text, grid_value)

    def create_button(self, text, value):
        btn = tk.Button(self.buttons_frame, text=text, bg="#4c4c4c", fg="white", font=("Arial", 24, "bold"), borderwidth=0, highlightthickness=0, padx=20, pady=20)
        btn.grid(row=value[0], column=value[1], columnspan=value[2] if len(value) == 3 else 1, sticky=tk.NSEW)
        btn.bind('<Button-1>', self.on_button_click)

        # Adding hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg="#666666"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#4c4c4c"))

        for i in range(1, 6):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

    def on_button_click(self, event):
        text = event.widget.cget("text")

        if text == "C":
            self.expression = ""
        elif text == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += text

        self.update_display()

    def update_display(self):
        self.label.config(text=self.expression[:11])
        self.total_label.config(text=self.expression[:11])

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
