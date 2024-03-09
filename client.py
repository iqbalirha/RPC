import xmlrpc.client
import requests

class NotebookClient:
    def __init__(self):
        self.server = xmlrpc.client.ServerProxy('http://localhost:8000')

    def add_note(self, topic, text):
        self.server.add_note(topic, text)
        print("Note added successfully!")

    def get_notes(self, topic):
        notes = self.server.get_notes(topic)
        if notes:
            print(f"Notes for topic {topic}:")
            for note in notes:
                print(f"Timestamp: {note['timestamp']}")
                print(f"Text: {note['text']}")
        else:
            print(f"No notes found for topic {topic}")

    def search_wikipedia(self, term):
        response = requests.get(f'https://en.wikipedia.org/w/api.php?action=opensearch&search={term}&limit=1&namespace=0&format=json')
        if response.status_code == 200:
            data = response.json()
            if data[3]:
                print("Wikipedia link:", data[3][0])
            else:
                print("No Wikipedia article found for the given term.")
        else:
            print("Failed to retrieve Wikipedia data.")

def main():
    client = NotebookClient()

    while True:
        print("\n1. Add Note")
        print("2. Get Notes for a Topic")
        print("3. Search Wikipedia")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            topic = input("Enter topic: ")
            text = input("Enter note text: ")
            client.add_note(topic, text)
        elif choice == "2":
            topic = input("Enter topic: ")
            client.get_notes(topic)
        elif choice == "3":
            term = input("Enter search term: ")
            client.search_wikipedia(term)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
