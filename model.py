import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0
def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        next_id = int(entries[0]["id"])
    except:
        entries = []
        next_id = 0

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    next_id += 1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(delete_id):
    global next_id
    print(delete_id)
    global entries
    for entry in entries:
        if int(entry["id"]) == int(delete_id):
            entries.remove(entry)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        print(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")