from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration form page
@app.route('/register')
def register():
    return render_template('register.html')

# Handle form submission (students will add JSON save code here)
@app.route('/submit', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    nationality = request.form['nationality']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    languages_spoken = request.form['languages_spoken']
    email_address = request.form['email_address']
    phone_number = request.form['phone_number']
    current_address = request.form['current_address']
    postal_code = request.form['postal_code']
    relationship = request.form['relationship']
    ec_first_name=request.form['ec_first_name']
    ec_last_name=request.form['ec_last_name']
    ec_phone_number=request.form['ec_phone_number']
    ec_email_address=request.form['ec_email_address']
    primary_needs=request.form['primary_needs']

    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new registration
    data.append({'first_name': first_name, 'last_name': last_name, 'nationality': nationality, 'gender': gender, 'date_of_birth': date_of_birth, 'languages_spoken': languages_spoken, 'email_address': email_address, 'phone_number': phone_number, 'current_address': current_address, 'postal_code': postal_code, 'relationship': relationship, 'ec_first_name': ec_first_name, 'ec_last_name': ec_last_name, 'ec_phone_number': ec_phone_number, 'ec_email_address': ec_email_address, 'primary_needs': primary_needs})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    flash('Registration submitted successfully!')
    return redirect(url_for('index'))

# Display stored registrations (students will add JSON reading code here)
@app.route('/view')
def view_registrations():
    with open('registrations.json', 'r') as file:
        data = json.load(file)
    return render_template('view.html', registrations=data)

if __name__ == '__main__':
    app.run(debug=True)



