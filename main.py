import os
from parsecourse import parse_course, Lesson
from ics import Calendar, Event
from datetime import datetime, timedelta

def main():
    course_codes = []

    mode = input("Manually enter course codes or automatically detect under /data? (m/A): ")

    if mode == 'm' or mode == 'M':
        print("Enter course codes one at a time, press enter to continue, enter nothing to finish:")
        while True:
            course_code = input("Enter course code: ")
            if course_code == '':
                break
            course_codes.append(course_code)

    else:
        for filename in os.listdir('data'):
            course_codes.append(filename.split('.')[0])

    c = Calendar()

    for course_code in course_codes:
        lessons = parse_course(course_code)

        lesson_days = []
        for lesson in lessons:
            if lesson.day_of_week not in lesson_days:
                lesson_days.append(lesson.day_of_week)
        lesson_days.sort()

        print(f'/// {course_code} ///')
        lecture_day = int(input(f'Enter the day of the week for lectures ({lesson_days[0]}/{lesson_days[1]}): '))

        for lesson in lessons:
            cursor_date = lesson.start_date
            lesson_type = 'Lecture' if lesson.day_of_week == lecture_day else 'Tutorial'
            print(f'Processing {course_code} {lesson_type}')
            while cursor_date <= lesson.end_date:
                if cursor_date.weekday() == lesson.day_of_week:
                    e = Event()
                    e.name = f'{course_code} {lesson_type}'
                    e.begin = datetime.combine(cursor_date, lesson.start_time) + timedelta(hours=-8)
                    e.end = datetime.combine(cursor_date, lesson.end_time) + timedelta(hours=-8)
                    e.location = lesson.location
                    c.events.add(e)
                cursor_date += timedelta(days=1)

    print(f"Processed {len(c.events)} lessons from {len(course_codes)} courses")
    with open('courses.ics', 'w') as courses_ics:
        courses_ics.writelines(c.serialize_iter())
    print("Saved to courses.ics")
    print("Bye!")

main()