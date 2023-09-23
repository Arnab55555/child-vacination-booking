from flask import Flask, render_template, request, redirect, url_for, session,get_flashed_messages
import tkinter
from tkinter import *

web = Flask(__name__)
web.secret_key='secretkey'
newQID=int(0)
userId=None

@web.route("/")
def login():
    return render_template("home.html")


@web.route("/calender/")
def schedule():
    return render_template("calender.html")

if __name__=="__main__":
    web.run(debug=True,port=7000)