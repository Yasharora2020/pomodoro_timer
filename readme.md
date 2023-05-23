# Pomodoro Timer

The Pomodoro Timer is a simple Python application that helps you manage your time using the Pomodoro Technique. It allows you to focus on work for a set period, followed by short breaks and longer breaks after a certain number of work intervals.

## Features

- Adjustable durations for work, short breaks, and long breaks
- Timer countdown display with customizable UI
- Sound notifications to indicate the end of a timer interval
- Check marks to track completed work intervals
- User-friendly graphical user interface (GUI) using Tkinter

## Prerequisites

- Python 3.x
- Tkinter package

## Getting Started

1. Clone the repository or download the source code files.

2. Install the required dependencies:
- pip install tkinter


3. Run the application:
- python pomodoro_timer.py


## Usage

1. The application window will open with the default settings.

2. Click the "Start" button to start the timer. The first timer interval will be a work session.

3. Once the work session is complete, the timer will switch to a short break session. After completing a certain number of work sessions, a long break session will be initiated.

4. The timer countdown will be displayed in minutes and seconds. The title label will indicate the current session type (work, short break, or long break).

5. Sound notifications will be played when each timer interval ends.

6. Check marks will appear below the timer to indicate completed work sessions.

7. To customize the durations, enter the desired values in the respective duration entry fields and click the "Apply Durations" button.

8. Click the "Reset" button to reset the timer and check marks.

9. Close the application window to exit the Pomodoro Timer.

## Customization

You can customize the application further by modifying the following variables/constants:

- `COLORS`: Modify the color codes in this dictionary to change the UI color scheme.
- `FONT_NAME`: Change the font name used for labels and text.
- `DURATIONS`: Adjust the default durations for work, short breaks, and long breaks.







