from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        # Read JSON file
        with open("students.json", "r") as file:
            students = json.load(file)

        # Add student
        students.append({
            "name": name,
            "email": email,
            "course": course
        })

        # Save JSON file
        with open("students.json", "w") as file:
            json.dump(students, file)

    # Read students
    with open("students.json", "r") as file:
        students = json.load(file)

    return render_template("index.html", students=students)


app.run(debug=True)