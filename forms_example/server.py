from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "lol secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_form', methods=['POST'])
def handle_form():

    session['full_name'] = request.form['full_name']
    session['email'] = request.form['email_address']
    session['maiden_name'] = request.form['mothers_maiden_name']
    session['ssn'] = request.form['social_number']
    return redirect('/show_result')

@app.route('/show_result')
def show_result():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)