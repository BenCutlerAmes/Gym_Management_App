from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.client import Client
import repositories.client_repository as client_repo
import repositories.lesson_repository as lesson_repo

clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def show_all_clients():
    clients = client_repo.select_all()
    return render_template("clients/clients.html", clients = clients)

@clients_blueprint.route("/clients/<id>")
def show_one_client(id):
    client = client_repo.select(id)
    lessons = client_repo.booked_lessons(client)
    return render_template("clients/show.html",client = client,lessons = lessons)

@clients_blueprint.route("/clients/searchname/", methods=['POST'])
def search_by_name():
    term = request.form['term']
    clients = client_repo.search_by_name(term)
    return render_template("/clients/clients.html", clients = clients)

@clients_blueprint.route("/clients/searchemail/", methods=['POST'])
def search_by_email():
    term = request.form['term']
    clients = client_repo.search_by_email(term)
    return render_template("/clients/clients.html", clients = clients)

@clients_blueprint.route("/clients/new")
def new_client_form():
    return render_template("/clients/new.html")

@clients_blueprint.route("/clients", methods = ['POST'])
def add_new_client():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    email_address = request.form['email_address']
    client = Client(name, date_of_birth,email_address)
    client_repo.add_client(client)
    return redirect("/clients")

@clients_blueprint.route("/clients/classes/<client_id>")
def lesson_booking_form(client_id):
    classes = lesson_repo.select_all()
    return render_template("/classes/class_booking.html",client_id = client_id,classes = classes)


@clients_blueprint.route("/clients/<id>/update")
def client_update_form(id):
    client = client_repo.select(id)
    return render_template("/clients/update.html",client = client)

@clients_blueprint.route('/clients/<id>/update', methods =['POST'])
def update_client(id):
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    email_address = request.form['email_address']
    client = Client(name,date_of_birth,email_address,id)
    client_repo.update(client)
    return redirect('/clients')

@clients_blueprint.route("/clients/<id>/delete", methods = ['POST'])
def delete_client(id):
    client_repo.delete(id)
    return redirect('/clients')

@clients_blueprint.route("/clients/<id>/delete")
def delete_confirm(id):
    return render_template("/clients/delete.html",client_id = id)