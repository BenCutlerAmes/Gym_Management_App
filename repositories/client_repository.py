from db.run_sql import run_sql
from models.client import Client
from models.lessons import Lesson
import repositories.instructor_repository as instructor_repo

def add_client(client):
    sql = "INSERT INTO clients (name,date_of_birth,email_address) VALUES (%s,%s,%s) RETURNING id"
    values = [client.name,client.date_of_birth,client.email_address]
    results = run_sql(sql,values)
    id = results[0]['id']
    client.id = id

def select_all():
    client_list = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    for result in results:
        client = Client(result['name'],result['date_of_birth'],result['email_address'],result['id'])
        client_list.append(client)
    return client_list

def select(id):
    client = None
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        client = Client(result['name'],result['date_of_birth'],result['email_address'],result['id'])
    return client

def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM clients WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(client):
    sql = "UPDATE clients SET (name, date_of_birth, email_address) = (%s,%s,%s) WHERE id = %s"
    values = [client.name,client.date_of_birth,client.email_address,client.id]
    run_sql(sql, values)

def booked_lessons(client):
    lessons = []
    sql = """SELECT lessons.* from lessons
    INNER JOIN lesson_bookings
    on lessons.id = lesson_bookings.lesson_id
    WHERE client_id = %s
    """
    values = [client.id]
    results = run_sql(sql,values)
    for row in results:
        instructor = instructor_repo.select(row['instructor_id'])
        lesson = Lesson(row['activity'],row['duration'],row['lesson_date'],row['lesson_time'],instructor,row['capacity'],row['id'])
        lessons.append(lesson)
    return lessons

