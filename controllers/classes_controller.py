from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.lessons import Lesson
from models.instructors import Instructor
import repositories.lesson_repository as lesson_repo
import repositories.lesson_booking_repository as lesson_booking_repo
import repositories.instructor_repository as instructor_repo
import repositories.client_repository as client_repo

classes_blueprint = Blueprint("classes",__name__)

@classes_blueprint.route("/classes")
def show_all_classes():
    classes = lesson_repo.select_all()
    return render_template("classes/classes.html",classes = classes)

@classes_blueprint.route("/classes", methods = ['POST'])
def schedule_new_lesson():
    activity = request.form['activity']
    duration = request.form['duration']
    lesson_date = request.form['lesson_date']
    lesson_time = request.form['lesson_time']
    capacity = request.form['capacity']
    instructor_id = request.form['instructor_id']
    instructor = instructor_repo.select(instructor_id)
    lesson = Lesson(activity,duration,lesson_date,lesson_time,instructor,capacity)
    if 'weekly' not in request.form:
        lesson_repo.add_lesson(lesson)
        return redirect ("/classes")
    else:
        i=0
        while i < 52:
            lesson_repo.add_lesson(lesson)
            old = datetime.fromisoformat(str(lesson.lesson_date))
            new = old +timedelta(7)
            lesson.lesson_date = new
            i += 1
        return redirect ("/classes")

@classes_blueprint.route("/classes/new")
def schedule_lesson_form():
    instructor_list = instructor_repo.select_all()
    return render_template("/classes/new.html",instructor_list = instructor_list)

@classes_blueprint.route("/classes/<id>")
def show_one_lesson(id):
    lesson = lesson_repo.select(id)
    clients =lesson_repo.booked_clients(lesson)
    return render_template('/classes/show.html', lesson = lesson, clients = clients)

@classes_blueprint.route('/classes/<id>/clients')
def lesson_booking_form(id):
    clients = client_repo.select_all()
    return render_template('clients/class_booking.html',clients = clients, lesson_id=id)

@classes_blueprint.route('/classes/<id>/update')
def class_update_form(id):
    lesson = lesson_repo.select(id)
    instructor_list = instructor_repo.select_all()
    return render_template('/classes/update.html',lesson = lesson, instructor_list = instructor_list)

@classes_blueprint.route('/classes/<id>/update', methods=['POST'])
def update_class(id):
    activity = request.form['activity']
    duration = request.form['duration']
    lesson_date = request.form['lesson_date']
    lesson_time = request.form['lesson_time']
    capacity = request.form['capacity']
    print(1)
    instructor_id = request.form['instructor_id']
    print(2)
    instructor = instructor_repo.select(instructor_id)
    print(3)
    lesson = Lesson(activity,duration,lesson_date,lesson_time,instructor,capacity,id)
    print(4)
    lesson_repo.update(lesson)
    print(5)
    return redirect("/classes")

@classes_blueprint.route('/classes/<id>/delete')
def delete_confirm(id):
    return render_template('/classes/delete.html', class_id = id)

@classes_blueprint.route('/classes/<id>/delete', methods = ['POST'])
def delete_lesson(id):
    lesson_repo.delete(id)
    return redirect ("/classes")