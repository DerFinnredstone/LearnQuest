import tkinter as tk
from tkcalendar import Calendar

class CalendarWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Kalender")

        self.calendar = Calendar(self)
        self.calendar.pack(pady=10)

        self.event_entry = tk.Entry(self)
        self.event_entry.pack(pady=5)

        add_event_button = tk.Button(self, text="Termin hinzufügen", command=self.add_event)
        add_event_button.pack(pady=5)

        self.event_listbox = tk.Listbox(self)
        self.event_listbox.pack(pady=10)

        delete_event_button = tk.Button(self, text="Termin löschen", command=self.delete_event)
        delete_event_button.pack(pady=5)

        self.load_events()

    def add_event(self):
        selected_date = self.calendar.selection_get().strftime("%Y-%m-%d")
        event = self.event_entry.get()
        if event:
            self.event_entry.delete(0, tk.END)
            self.event_listbox.insert(tk.END, f"{selected_date}: {event}")
            self.save_event(selected_date, event)

    def delete_event(self):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.event_listbox.get(selected_index)
            self.event_listbox.delete(selected_index)
            self.delete_saved_event(selected_event)

    def load_events(self):
        try:
            with open("events.txt", "r") as file:
                events = file.readlines()
                for event in events:
                    self.event_listbox.insert(tk.END, event.strip())
        except FileNotFoundError:
            pass

    def save_event(self, date, event):
        with open("events.txt", "a") as file:
            file.write(f"{date}: {event}\n")

    def delete_saved_event(self, event):
        events = []
        with open("events.txt", "r") as file:
            events = file.readlines()

        with open("events.txt", "w") as file:
            for saved_event in events:
                if saved_event.strip() != event:
                    file.write(saved_event)

class LearnQuestGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LearnQuest Schulsystem")

        self.create_widgets()

    def create_widgets(self):
        calendar_button = tk.Button(self.root, text="Kalender", command=self.open_calendar)
        calendar_button.pack()

    def open_calendar(self):
        calendar_window = CalendarWindow()

    def run(self):
        self.root.mainloop()