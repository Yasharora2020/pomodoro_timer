import math
import platform
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# Constants
COLORS = {"pink": "#e2979c", "red": "#e7305b", "green": "#9bdeac", "yellow": "#f7f5dd"}
FONT_NAME = "Courier"
DURATIONS = {"work": 25, "short_break": 5, "long_break": 20}  # Default durations

def resource_path(relative_path):
    """ Get absolute path to resource, works for both development and PyInstaller executable """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        # Use the current working directory for development
        base_path = os.path.abspath("")

    return os.path.join(base_path, relative_path)


class PomodoroTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=COLORS["yellow"])
        self.tomato_img = tk.PhotoImage(file=resource_path("tomato.png"))
        # Keep a reference to the image
        self.setup_ui()

    def reset_timer(self):
        # Reset the timer and check marks
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer")
        self.check_marks.config(text="")
        self.reps = 0

    def start_timer(self):
        self.reps += 1

        if self.reps % 8 == 0:
            self.count_down(DURATIONS["long_break"] * 60)
            self.title_label.config(text="Break", fg=COLORS["red"])
        elif self.reps % 2 == 0:
            self.count_down(DURATIONS["short_break"] * 60)
            self.title_label.config(text="Break", fg=COLORS["pink"])
        else:
            self.count_down(DURATIONS["work"] * 60)
            self.title_label.config(text="Work", fg=COLORS["green"])

    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.complete_timer()

    def complete_timer(self):
        # Timer completed
        if platform.system() == 'Windows':
            # Play Windows system sound
            subprocess.Popen(["powershell", "-c", "(New-Object Media.SoundPlayer 'SystemAsterisk').PlaySync()"])
        else:
            # Play system beep sound
            subprocess.Popen(["afplay", "/System/Library/Sounds/Glass.aiff"])

        self.start_timer()
        marks = "✔" * (math.floor(self.reps / 2))
        self.check_marks.config(text=marks)

    def setup_ui(self):
        self.title_label = tk.Label(text="Timer", fg=COLORS["green"], bg=COLORS["yellow"], font=(FONT_NAME, 50))
        self.title_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=200, height=224, bg=COLORS["yellow"], highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato_img)  # Use self.tomato_img reference
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        start_button = tk.Button(text="Start", highlightthickness=0, command=self.start_timer)
        start_button.grid(column=1, row=2)

        reset_button = tk.Button(text="Reset", highlightthickness=0, command=self.reset_timer)
        reset_button.grid(column=1, row=3)

        self.check_marks = tk.Label(fg=COLORS["green"], bg=COLORS["yellow"])
        self.check_marks.grid(column=1, row=4)

        # Duration Customization
        self.work_duration = tk.StringVar()
        self.short_break_duration = tk.StringVar()
        self.long_break_duration = tk.StringVar()

        work_duration_label = tk.Label(text="Work duration:", bg=COLORS["yellow"])
        work_duration_label.grid(column=0, row=5)
        work_duration_entry = tk.Entry(textvariable=self.work_duration)
        work_duration_entry.grid(column=1, row=5)

        short_break_duration_label = tk.Label(text="Short break duration:", bg=COLORS["yellow"])
        short_break_duration_label.grid(column=0, row=6)
        short_break_duration_entry = tk.Entry(textvariable=self.short_break_duration)
        short_break_duration_entry.grid(column=1, row=6)

        long_break_duration_label = tk.Label(text="Long break duration:", bg=COLORS["yellow"])
        long_break_duration_label.grid(column=0, row=7)
        long_break_duration_entry = tk.Entry(textvariable=self.long_break_duration)
        long_break_duration_entry.grid(column=1, row=7)

        apply_button = tk.Button(text="Apply Durations", command=self.apply_durations)
        apply_button.grid(column=1, row=8)

    def apply_durations(self):
        global DURATIONS  # Specify DURATIONS as global
        try:
            DURATIONS = {
                "work": int(self.work_duration.get()),
                "short_break": int(self.short_break_duration.get()),
                "long_break": int(self.long_break_duration.get())
            }
        except ValueError:
            messagebox.showerror("Invalid Duration", "Please enter numeric values for durations.")  # Requires tkinter.messagebox

    def run(self):
        self.reps = 0
        self.window.mainloop()

if __name__ == "__main__":
    pomodoro_timer = PomodoroTimer()
    pomodoro_timer.run()
