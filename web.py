from flask import Flask, render_template, request, redirect, url_for, session,get_flashed_messages
import tkinter
from tkinter import *

web = Flask(__name__)


@web.route("/")
def login():
    return render_template("home.html")


@web.route("/About Us/")
def aboutUs():
    return render_template("")


@web.route("/Services/")
def services():
    return render_template("")


@web.route("/Vacination Schedule/")
def schedule():
    return render_template("schedule.html")


@web.route("/Resources/")
def resources():
    return render_template("resources.html")


@web.route("/Doctors/")
def doctors():
    return render_template("doctor.html")


@web.route("/Contact Us/")
def contactUs():
    return render_template("")



if __name__=="__main__":
    web.run(debug=True,port=7000)