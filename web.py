from flask import Flask, render_template, request, redirect, url_for, session,get_flashed_messages
import tkinter
from tkinter import *
import os
import email
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import messagebox


web = Flask(__name__)
web.secret_key='secretkey'

@web.route("/")
def login():
    return render_template("home.html")


@web.route("/About Us/")
def aboutUs():
    return render_template("about.html")


@web.route("/Services/")
def services():
    return render_template("service.html")


@web.route("/Vacination Schedule/", methods=["GET","POST"])
def schedule():
    print("Hello")
    if request.method == 'POST':
        global childname
        childname = request.form['patientname']
        global parentname
        parentname = request.form['Parent']
        global appointmentdate
        appointmentdate = request.form['appointment-date']
        global dob
        dob = request.form['dob']
        global childage
        childage = request.form['Age']
        global emailadd
        emailadd = request.form['em']
        # print(name)

        # email_reciever = request.form["em"]
        # try:

        #     email_sender = 'autolibpy@gmail.com'
        #     email_password = 'epemdruoebcgmtta'

        #     print(email_reciever)

        #     subject = 'Booking Confirmation'
        #     body = """
        #         Welcome!,"""+name+""" to our vacination center
        #         """

        #     em = EmailMessage()
        #     em['From'] = email_sender
        #     em['To'] = email_reciever
        #     em['subject'] = subject
        #     em.set_content(body)

        #     context = ssl.create_default_context()

        #     with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        #         smtp.login(email_sender, email_password)
        #         smtp.sendmail(email_sender, email_reciever, em.as_string())

        # except:
        #     print(email_reciever)
        #     print("incorrect automation")
    return render_template("schedule.html")


@web.route("/payment confirmation/", methods=["GET","POST"])
def paying():
    print(parentname)
    print(appointmentdate)
    email_reciever = emailadd
    try:

        email_sender = 'autolibpy@gmail.com'
        email_password = 'epemdruoebcgmtta'

        print(email_reciever)

        subject = 'Booking Confirmation'
        body = """
            Welcome!"""+parentname+""",
              to our vacination center

              Please Pay the amount to confirm your vaccination slot
                """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciever
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())

    except:
        print(email_reciever)
        print("incorrect automation")
    return render_template("paymentconfirmation.html")


@web.route("/Resources/")
def resources():
    return render_template("resources.html")


@web.route("/Doctors/")
def doctors():
    return render_template("doctor.html")


@web.route("/Contact Us/")
def contactUs():
    return render_template("contact.html")


@web.route("/successful payment/")
def successfulPayment():
    return render_template("thanku.html")


if __name__=="__main__":
    web.run(debug=True,port=7000)







