# HKU-Calendar-Takeout

This little python script makes the life of a HKU student easier. You can copy-paste course timetable to your calendar client that supports import via `.ics`. 

## How to use

### Preparing the data
1. Go to Portal -> Timetables -> My Weekly Schedule -> List View.
2. Of each course, there should be a column *Section*, click it.
3. Copy the content of the Meeting Information table, excluding anything (table title and column headers) but the fields themselves.
4. Create a text file named as the course code, `COMPXXXX`, or any name you desire. This name will be the names of the calendar events.
5. Paste to the text file.
6. Repeat from Step 2 for each course.
7. All these text files should be placed under a `./data` directory relative to `main.py`.

### Prerequisites
`python3`, `pip3`, `venv` (recommended).

### Running the script
```zsh
python3 -m venv .ve
source .ve/bin/activate
pip3 install -r requirement.txt
python3 main.py
```
Lastly, import the newly created `courses.ics` to your favourite calendar client.
