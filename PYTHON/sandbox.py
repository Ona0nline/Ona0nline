from flask import Flask,request
import sqlite3

app = Flask(__name__)

# What are the parameters for app route?
# Route for form submission
@app.route('/submit-form', methods=['POST'])

# Initialize SQLite database
conn = sqlite3.connect('responses.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS form_responses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              email TEXT,
              q1 TEXT,
              q2 TEXT,
              q3 TEXT,
              q4 TEXT,
              q5 TEXT,
              q6 TEXT,
              q7 TEXT,
              q8 TEXT,
              q9 TEXT,
              q10 TEXT)''')
conn.commit()

# Define a route for the root URL to serve the form
@app.route('/')
def form():
    return render_template('sandcastle.html')

# Storing data in a database. Referring to name elements from the form
# Define a route to handle the form submission
@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Extract form data
    form_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'q1': request.form['q1'],
        'q2': request.form['q2'],
        'q3': request.form['q3'],
        'q4': request.form['q4'],
        'q5': request.form['q5'],
        'q6': request.form['q6'],
        'q7': request.form['q7'],
        'q8': request.form['q8'],
        'q9': request.form['q9'],
        'q10': request.form['q10']
    }
  # Insert form data into SQLite database
    c.execute('''INSERT INTO form_responses (name, email, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (form_data['name'], form_data['email'], form_data['q1'], form_data['q2'],
               form_data['q3'], form_data['q4'], form_data['q5'], form_data['q6'],
               form_data['q7'], form_data['q8'], form_data['q9'], form_data['q10']))
    conn.commit()

    return 'Form submitted successfully!'
# Route for sending to server

# Insert form data into SQLite database
    c.execute('''INSERT INTO form_responses (name, email, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (form_data['name'], form_data['email'], form_data['q1'], form_data['q2'],
               form_data['q3'], form_data['q4'], form_data['q5'], form_data['q6'],
               form_data['q7'], form_data['q8'], form_data['q9'], form_data['q10']))
    conn.commit()

    return 'Form submitted successfully!'
# @app.route('/')
# def form():
#   return '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <link rel="stylesheet" href="sandcastle.css">
    
# </head>

# <body>
    
#     <p class="hey" onclick="this.innerHTML='So nosy'">Hey</p>
#     <p class="question" onclick="this.innerHTML='*clicks in frustration'"><span class="are">Are</span> <span class="you">you</span> 
#         <span class="calm">calm</span> <span class="yet">yet?</span></p>

#         <!-- Secret check in form -->

        
#         <button class="play" id="play" onclick="play()">Play this</button>

#         <button id="open-me-button" class="open-me-button">Open me if you want</button>

# <div class="overlay" id="overlay">
#     <div class="popup">
#       <span class="close-btn" id="closePopupBtn">&times;</span>
#       <div class="form-container">

#         <!-- action attribute will point to relevant backend server side place -->
#               <form id="check-in" class="check-in" method="POST" action="/submit-form">
                
#                 <p class="secret">SHHHHHH this is a secret check in form</p>
#               <label for="full-name">Full name</label>
#               <input type="text" id="full-name" name="name" required><br><br>

#               <label for="email">Email</label>
#               <input type="text" id="email" name="email" required><br><br>

#               <p>Brain dump questions</p>
#               <label for="q1">Tell me a fun fact about yourself</label>
#               <input type="text" id="q1" name="q1" required><br><br>

#               <label for="q2">If you had to be made of metal, what kind would it be?</label>
#               <input type="text" id="q2" name="q2" required><br><br>

#               <label for="q3">Match a flavour of icecream to your personality. why
#                 that one?</label>
#               <input type="text" id="q3" name="q3" required><br><br>

#               <label for="q4">A new holiday is added. What are we celebrating?</label>
#               <input type="text" id="q4" name="q4" required><br><br>

#               <label for="q5">If you could be any age for a week, which would it be
#                 and why?
#               </label>
#               <input type="text" id="q5" name="q5" required><br><br>

#               <p>Okie now time for *real* questions</p>

#               <label for="q6">What was the last thing you did that made you 
#                 proud [of yourself]</label>
#               <input type="text" id="q6" name="q6" required><br><br>

#               <label for="q7">How do you define happiness?</label>
#               <input type="text" id="q7" name="q7" required><br><br>

#               <label for="q8">What qualities in others inspire you to love more deeply?</label>
#               <input type="text" id="q8" name="q8" required><br><br>

#               <label for="q9">How can you show yourself a little extra love today?</label>
#               <input type="text" id="q9" name="q9" required><br><br>

#               <label for="q10">How do you feel right now? (details &lt;3) </label>
#               <input type="text" id="q10" name="q10" requiredv><br><br>

#               <p>Thank you for participating. This is me practicing backend and also
#                 generally checking on you. I cannot specify which one takes
#               precedency. </p>

#               <button id="submit" class="submit">Submit</button>
#             </form>
#             </div>
#     </div>
#     </div>
# '''

if __name__ == '__main__':
    app.run(debug=True)
