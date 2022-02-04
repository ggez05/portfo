import email
from email import message
from email.quoprimime import quote
from operator import delitem
import re
from flask import Flask, message_flashed , render_template, request,redirect
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/<page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode = 'a' , newline = '') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writehere = csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writehere.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong. Try again!'




