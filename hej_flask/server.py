from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/another_route')
def another_route():
    return "this is another route :D!!!"

@app.route('/sample/<x>')
def third_route(x):
    return f"the route contains {x}"

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    return render_template("multiply.html", x = x, y = y, result = x * y)

@app.route('/multiplication_table/<int:x>/<int:y>')
def multiplication_table(x, y):
    results = []

    table_header = ['x']

    for i in range(0, y+1):
        table_header.append(i)

    results.append(table_header)

    for i in range(0, x+1):
        new_row = [i]
        for j in range(0, y+1):
            new_row.append(i * j)
        results.append(new_row)

    print(results)

    return render_template("table.html", results = results)


if __name__ == "__main__":
    app.run(debug=True)

# https://login.codingdojo.com/m/172/7219/52126