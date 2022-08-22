from db.run_sql import run_sql
from models.instructors import Instructor

def add_instructor(instructor):
    sql = "INSERT INTO instructors (name,email_address) VALUES (%s,%s) RETURNING id"
    values = [instructor.name,instructor.email_address]
    results = run_sql(sql,values)
    id = results[0]['id']
    instructor.id = id

def select_all():
    instructor_list = []
    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    for result in results:
        instructor = Instructor(result['name'],result['email_address'],result['id'])
        instructor_list.append(instructor)
    return instructor_list

def select(id):
    instructor = None
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        instructor = Instructor(result['name'],result['email_address'],result['id'])
    return instructor

def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM instructors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(instructor):
    sql = "UPDATE instructors SET (name, date_of_birth, email_address) = (%s,%s,%s) WHERE id = %s"
    values = [instructor.name,instructor.email_address,instructor.id]
    run_sql(sql, values)
