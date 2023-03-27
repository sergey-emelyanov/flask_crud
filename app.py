from flask import Flask, render_template, request, redirect, url_for
from validate import validation
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


@app.route("/user/<string:id>")
def show_user(id):
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)

    user = [x for x in data['users'] if x['id'] == id][0]

    return render_template("/users/show.html", user=user)


@app.route("/users/new")
def new_user():
    user = {
        "id": "",
        "name": "",
        "email": ""
    }
    errors = {}
    return render_template("/users/new_user.html", errors=errors, user=user)


@app.post("/users")
def post_users():
    user = request.form.to_dict()
    user_id = uuid.uuid4()
    new_user = {
        "id": str(user_id)[:8],
        "name": user["name"],
        "email": user["email"]
    }
    errors = validation(user)
    if errors:
        return render_template("/users/new_user.html", errors=errors, user=new_user)
    with open("data_file.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        data["users"].append(new_user)

    with open("data_file.json", "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, ensure_ascii=False)

    return redirect(url_for('show_users'), 302)


if __name__ == "__main__":
    app.run(debug=True)
