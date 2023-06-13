import tkinter as tk
from chatsysem import ChatSystem
from gui_calender import CalendarWindow
class LearnQuestGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LearnQuest Schulsystem")

        self.create_widgets()

    def create_widgets(self):
        calendar_button = tk.Button(self.root, text="Kalender", command=self.open_calendar)
        chatsystem_button = tk.Button(self.root, text="ChatSystem", command=self.open_ChatSystem)
        chatsystem_button.pack()
        calendar_button.pack()

    def open_calendar(self):
        calendar_window = CalendarWindow()
    
    def open_ChatSystem(self):
        chatsystem = ChatSystem()

    def run(self):
        self.root.mainloop()

gui = LearnQuestGUI()
gui.run()