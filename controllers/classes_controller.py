from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.lessons import Lesson
import repositories.lesson_repository as lesson_repo
import repositories.lesson_booking_repository as lesson_booking_repo

classes_blueprint = Blueprint("classes",__name__)

@classes_blueprint.route("/classes")
def show_all_classes():
    classes = lesson_repo.select_all()
    return render_template("classes/classes.html",classes = classes)

@classes_blueprint.route("/classes", methods = ['POST'])
def schedule_new_lesson(lesson):
    pass