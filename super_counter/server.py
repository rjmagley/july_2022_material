from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "lol super counter demo wheeeeeeee"

@app.route('/')
def index():

    if 'counter_1' not in session:
        session['counter_1'] = 0
        session['counter_2'] = 0
        session['counter_3'] = 0
        session['counter_4'] = 0
        session['counter_5'] = 0
        session['activity_log'] = []

    return render_template('counters.html')

@app.route('/counter/<int:counter_number>')
def update_counter(counter_number):

    session[f'counter_{counter_number}'] += 1
    session['activity_log'].append(f"u click counter {counter_number}")

    session.modified = True

    print(session['activity_log'])

    return redirect('/')

@app.route('/reset')
def reset_session():

    session.clear()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)