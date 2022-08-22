from db.run_sql import run_sql
from models.lessons import Lesson
from models.client import Client
from models.instructors import Instructor

def add_lesson(lesson):
    sql = "INSERT INTO lessons (activity, duration, lesson_date, lesson_time, instructor_id, capacity) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [lesson.activity, lesson.duration, lesson.lesson_date, lesson.lesson_time, lesson.instructor.id, lesson.capacity]
    results = run_sql(sql,values)
    id = results[0]['id']
    lesson.id = id

def select_all():
    lesson_list = []
    sql = "SELECT * FROM lessons WHERE lesson_date > now() and lesson_date < now() + interval '2 weeks' ORDER BY lesson_date, lesson_time ;"
    results = run_sql(sql)
    for result in results:
        lesson = Lesson(result['activity'], result['duration'], result['lesson_date'], result['lesson_time'], result['instructor_id'],result['capacity'],result['id'])
        lesson_list.append(lesson)
    return lesson_list

def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results != None:
        result = results[0]
        lesson = Lesson(result['activity'], result['duration'], result['lesson_date'], result['lesson_time'], result['instructor_id'],result['capacity'],result['id'])
    return lesson

def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(lesson):
    sql = "UPDATE lessons SET (activity, duration, lesson_date, lesson_time, instructor) = (%s,%s,%s,%s,%s) WHERE id = %s"
    values = [lesson.activity, lesson.duration, lesson.lesson_date, lesson.lesson_time, lesson.instructor_id,lesson.capacity,lesson.id]
    run_sql(sql, values)
