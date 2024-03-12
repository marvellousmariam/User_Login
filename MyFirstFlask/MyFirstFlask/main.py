from flask import Flask, render_template, request, redirect, url_for, session, Response
import csv  #comma seperated value
#import secrets

app = Flask(__name__)
app.secret_key = '951d9f8150792ff6ed734d80b91508e3'

#print(secrets.token_hex(16))
#Function to check if the provided username and password are valid


def is_valid_login(username, password):
  with open('users.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      if row[0] == username and row[1] == password:
        return True
  return False


# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if is_valid_login(username, password):
      session['username'] = username
      return redirect(url_for('dashboard'))
    else:
      return render_template('login.html', error='Invalid login credentials')
  return render_template('login.html')


#Route for the dashboard page
@app.route('/dashboard')
def dashboard():
  if 'username' in session:
    return Response(f'Welcome,{session["username"]}! This is your dashboard', )
  return redirect(url_for('login'))


#Route to logout
@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('login'))


if __name__ == '__name__':
  app.run(debug=True)
