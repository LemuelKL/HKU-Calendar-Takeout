# HKU-Calendar-Takeout

This little python script makes the life of a HKU student easier.

## How to use
1. Go to Portal -> Timetables -> My Weekly Schedule -> List View.
2. Of each course, there should be a column *Section*, click it.
3. Copy the content of the Meeting Information table, excluding anything (table title and column headers) but the fields themselves.
4. Create a text file named as the course code, `COMPXXXX`, or any name you desire. This name will be the names of the resulting calendar names.
5. Paste to the text file.
6. Repeat from Step 2 for each course.
7. All these text files should be placed under a `./data` directory relative to `main.py`.
8. `python main.py`
9. Import the newly created `courses.ics` to your favourite calendar client.
