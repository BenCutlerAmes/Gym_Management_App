from flask import Flask, render_template, redirect, request
from flask import Blueprint
import repositories.lesson_booking_repository as booking_repo
import repositories.client_repository as client_repo
import repositories.lesson_repository as lesson_repo
from models.lesson_bookings import Lesson_Booking
from models.client import Client
from models.lessons import Lesson


booking_blueprint = Blueprint("bookings",__name__)

@booking_blueprint.route("/bookings/<client_id>/<lesson_id>")
def booking_confirmation(client_id,lesson_id):
    client = client_repo.select(client_id)
    lesson = lesson_repo.select(lesson_id)
    return render_template("/bookings/booking_form.html",client=client, lesson = lesson)

@booking_blueprint.route("/bookings", methods = ['POST'])
def create_booking():
    client_id = request.form['client_id']
    lesson_id = request.form['lesson_id']
    client = client_repo.select(client_id)
    lesson = lesson_repo.select(lesson_id)
    booking = Lesson_Booking(client,lesson)
    booking_repo.add_booking(booking)
    return redirect("/clients")

@booking_blueprint.route("/bookings/<client_id>/<lesson_id>/delete")
def confirm_booking_delete(client_id,lesson_id):
    return render_template("bookings/delete.html",client_id = client_id, lesson_id = lesson_id)

@booking_blueprint.route("/bookings/<client_id>/<lesson_id>/delete", methods = ['POST'])
def delete_booking(client_id,lesson_id):
    result = booking_repo.find_booking_id(client_id,lesson_id)
    booking_repo.delete(result)
    return  redirect("/clients")  
