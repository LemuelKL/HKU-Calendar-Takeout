import json
from ics import Calendar, Event
c = Calendar()

def hhmm2hh_mm_ss(hhmm: str):
    hh, mm = hhmm[:2], hhmm[2:]
    return '{}:{}:{}'.format(hh, mm, '00')

with open('courses.json', 'r') as courses_data:
    courses = json.load(courses_data)
    for i in courses:
        for a in i['arrangements']:
            e = Event()
            e.name = i['title'] + ' ' + i['type']
            e.begin = a['startDate'] + ' ' + hhmm2hh_mm_ss(a['startTime'])
            e.end = a['endDate'] + ' ' + hhmm2hh_mm_ss(a['endTime'])
            e.location = a['location']
            c.events.add(e)

with open('courses.ics', 'w') as courses_ics:
    courses_ics.writelines(c.serialize_iter())
  
print('Done')