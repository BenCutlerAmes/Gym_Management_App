from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.client import Client
import repositories.client_repository as client_repo

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
