from flask import Flask, render_template, request, redirect, url_for
import uuid
import json

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("users/base.html")


@app.route("/users")
def show_users():

    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        users = data['users']

    return render_template("/users/index.html", users=users)


@app.route("/users/new")
def new_user():
    return render_template("/users/new_user.html")


@app.post("/users")
def post_users():
    user = request.form.to_dict()
    new_user = {
        "name": user["name"],
        "email": user["email"]
    }
    with open("data_file.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        data["users"].append(new_user)

    with open("data_file.json", "w", encoding="utf-8") as write_file:
        json.dump(data, write_file)

    return redirect(url_for('show_users'), 302)


if __name__ == "__main__":
    app.run(debug=True)
