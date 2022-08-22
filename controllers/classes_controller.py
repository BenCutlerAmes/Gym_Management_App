from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.lessons import Lesson
from models.instructors import Instructor
import repositories.lesson_repository as lesson_repo
import repositories.lesson_booking_repository as lesson_booking_repo
import repositories.instructor_repository as instructor_repo

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
    lesson_repo.add_lesson(lesson)
    return redirect ("/classes")

@classes_blueprint.route("/classes/new")
def schedule_lesson_form():
    instructor_list = instructor_repo.select_all()
    return render_template("/classes/new.html",instructor_list = instructor_list)