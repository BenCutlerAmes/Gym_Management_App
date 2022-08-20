from db.run_sql import run_sql
from models.lessons import Lesson
from models.client import Client
from models.instructors import Instructor
from models.lesson_bookings import Lesson_Booking
from models.lesson_bookings import Lesson_Booking
import repositories.client_repository as client_repo
import repositories.lesson_repository as lesson_repo

def add_booking(booking):
    sql = "INSERT INTO lesson_bookings (client_id, lesson_id) VALUES (%s,%s) RETURNING id"
    values = [booking.client.id, booking.lesson.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    booking.id = id

def select_all():
    lesson_bookings =[]
    sql = "SELECT * FROM lesson_bookings"
    results = run_sql(sql)
    for result in results:
        client = client_repo.select(result['client_id'])
        lesson = lesson_repo.select(result['lesson_id'])
        booking = Lesson_Booking(client,lesson,result['id'])
        lesson_bookings.append(booking)
    return lesson_bookings

def select_id(id):
    lesson_booking = None
    sql = "SELECT * FROM lesson_bookings where id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results != None:
        result = results[0]
        client = client_repo.select(result['client_id'])
        lesson = lesson_repo.select(result['lesson_id'])
        lesson_booking = Lesson_Booking(client,lesson,result['id'])
    return lesson_booking
        
def delete_all():
    sql = "DELETE FROM lesson_bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM lesson_bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

