import tkinter as tk
from tkcalendar import *

class CalendarWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Kalender")

        self.calendar = Calendar(self)
        self.calendar.pack(pady=10)

        self.minute_spinbox = tk.Spinbox(self, from_=0, to=59)
        self.minute_spinbox.pack(pady=5)

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
        selected_minute = self.minute_spinbox.get()
        event = self.event_entry.get()
        if event:
            self.event_entry.delete(0, tk.END)
            self.event_listbox.insert(tk.END, f"{selected_date} {selected_minute:02d}: {event}")
            self.save_event(selected_date, selected_minute, event)

    def delete_event(self):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.event_listbox.get(selected_index)
            self.event_listbox.delete(selected_index)
            self.delete_saved_event(selected_event)

    def load_events(self):
        # Laden gespeicherter Termine aus einer Datei oder Datenbank
        # Beispiel: Laden von "events.txt" mit dem Format: "Datum Minuten: Ereignis"
        try:
            with open("events.txt", "r") as file:
                events = file.readlines()
                for event in events:
                    self.event_listbox.insert(tk.END, event.strip())
        except FileNotFoundError:
            pass

    def save_event(self, date, minute, event):
        # Speichern der Termine in einer Datei oder Datenbank
        # Beispiel: Speichern in "events.txt" mit dem Format: "Datum Minuten: Ereignis"
        with open("events.txt", "a") as file:
            file.write(f"{date} {minute:02d}: {event}\n")

    def delete_saved_event(self, event):
        # Löschen des gespeicherten Ereignisses aus der Datei oder Datenbank
        # Beispiel: Löschen aus "events.txt" basierend auf dem Ereignis
        events = []
        with open("events.txt", "r") as file:
            events = file.readlines()

        with open("events.txt", "w") as file:
            for saved_event in events:
                if saved_event.strip() != event:
                    file.write(saved_event)