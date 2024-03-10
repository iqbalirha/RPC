import xml.etree.ElementTree as ET
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from socketserver import ThreadingMixIn
import requests

class NotebookServer:
    def __init__(self):
        self.database = "notebook.xml"

    def add_note(self, topic, text, timestamp):
        try:
            tree = ET.parse(self.database)
            root = tree.getroot()
        except ET.ParseError:
            # If the file does not exist or is not valid XML, create a new root element
            root = ET.Element("notes")

        # Check if topic exists, if not, create a new entry
        topic_exists = False
        for note in root.findall('note'):
            if note.find('topic').text == topic:
                topic_exists = True
                note_elem = ET.SubElement(note, 'text')
                note_elem.text = text
                timestamp_elem = ET.SubElement(note, 'timestamp')
                timestamp_elem.text = timestamp
                break

        if not topic_exists:
            note = ET.Element("note")
            topic_elem = ET.SubElement(note, 'topic')
            topic_elem.text = topic
            text_elem = ET.SubElement(note, 'text')
            text_elem.text = text
            timestamp_elem = ET.SubElement(note, 'timestamp')
            timestamp_elem.text = timestamp
            root.append(note)

        tree = ET.ElementTree(root)
        tree.write(self.database)
        return "Note added successfully."

    def get_notes(self, topic):
        try:
            tree = ET.parse(self.database)
            root = tree.getroot()
        except (ET.ParseError, FileNotFoundError):
            return "Database does not exist or is not valid XML format."

        notes = []
        for note in root.findall('note'):
            if note.find('topic').text == topic:
                notes.append({
                    'text': note.find('text').text,
                    'timestamp': note.find('timestamp').text
                })
        return notes

    def get_wikipedia_info(self, topic):
        url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={topic}&limit=1&format=json"
        response = requests.get(url)
        data = response.json()
        if len(data) >= 3:
            return data[3][0]  # Link to the Wikipedia article
        else:
            return "No additional information found on Wikipedia."

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

def main():
    server = ThreadedXMLRPCServer(("localhost", 8000), requestHandler=SimpleXMLRPCRequestHandler, logRequests=True)
    server.register_instance(NotebookServer())
    print("Server listening on port 8000...")
    server.serve_forever()

if __name__ == "__main__":
    main()
