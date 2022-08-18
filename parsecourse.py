from datetime import date, time, datetime, timezone
from typing import List

from dataclasses import dataclass

@dataclass
class Lesson:
    course_code: str
    start_date: date
    end_date: date
    day_of_week: int
    start_time: time
    end_time: time
    location: str
    def __str__(self):
        return f'{self.course_code} {self.start_date} {self.end_date} {self.day_of_week} {self.start_time} {self.end_time} {self.location}'

weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def parse_course(course_code: str) -> List[Lesson]:
    with open(f'data/{course_code}.txt', 'r') as raw:
        raw_lines = raw.readlines()

    info = []
    for line in raw_lines:
        data = line.split()
        if len(data) == 0 or '\t' in data:
            pass
        else:
            info.append(line.split('\n')[0])

    lessons = []
    for l_idx in range(0, len(info), 5):
        days_n_times, room, _, date_range, _  = info[l_idx:l_idx + 5]

        weekday = weekdays.index(days_n_times[:2])
        time_range = days_n_times[3:]
        start_time, end_time = [datetime.strptime(t, "%I:%M%p").time() for t in time_range.split(' - ')]
        start_date, end_date = [datetime.strptime(d, "%d/%m/%Y").date() for d in date_range.split(' - ')]

        lessons.append(Lesson(course_code, start_date, end_date, weekday, start_time, end_time, room))

    return lessons