import csv
from datetime import datetime

class ChatSystem:
    def __init__(self):
        self.users = []
        self.groups = []

    def load_users(self, filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            self.users = list(reader)

    def load_groups(self, filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            self.groups = list(reader)

    def send_message(self, sender, receiver, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if receiver.lower() == "all":
            self.send_group_message(sender, "all", message, timestamp)
        elif self.is_user(receiver):
            self.send_private_message(sender, receiver, message, timestamp)

    def send_private_message(self, sender, receiver, message, timestamp):
        filename = f"{sender}_{receiver}.csv"
        self.save_message(filename, sender, receiver, message, timestamp)

    def send_group_message(self, sender, group, message, timestamp):
        for user in self.get_group_users(group):
            if user != sender:
                filename = f"{sender}_{group}.csv"
                self.save_message(filename, sender, user, message, timestamp)

    def save_message(self, filename, sender, receiver, message, timestamp):
        with open(filename, "a") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, sender, receiver, message])

    def read_messages(self, user):
        messages = []
        for filename in self.get_user_files(user):
            with open(filename, "r") as file:
                reader = csv.reader(file)
                messages += list(reader)
        messages.sort(key=lambda x: x[0])  # Sort by timestamp
        return messages

    def is_user(self, user):
        return user in [row[0] for row in self.users]

    def is_group(self, group):
        return group in [row[0] for row in self.groups]

    def get_group_users(self, group):
        if self.is_group(group):
            return [row[1] for row in self.groups if row[0] == group]
        return []

    def get_user_files(self, user):
        files = []
        for row in self.users:
            sender, receiver = row
            if sender == user:
                files.append(f"{sender}_{receiver}.csv")
            if receiver == user:
                files.append(f"{receiver}_{sender}.csv")
        return files
