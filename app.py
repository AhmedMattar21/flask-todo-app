from flask import Flask, render_template, request, redirect
from datetime import datetime
from DB_CONN import conn


# GET ALL ACTIVE TASKS
def get_data():
    data = conn.returnQuery("SELECT * FROM tasks where is_completed=0")
    return data


# GET ALL COMPLETED TASKS
def get_cdata():
    data = conn.returnQuery("SELECT * FROM tasks where is_completed=1")
    return data


# APPLIACTION NAME
app = Flask(__name__)


# HOME PAGE METHOD
@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        # GET TASK CONTENT FROM POST REQUEST
        task_content = request.form["content"]
        # GET THE CURRENT DATE AND TIME AND FORMATTING THEM
        date = datetime.now().date()
        time_h = datetime.now().time().hour
        time_m = datetime.now().time().minute
        formatted_time = str.format(f"{ date } {time_h}:{time_m}")
        # COLLECT ALL DATA IN A LIST
        mydata = [conn.get_nextID("tasks", "id"), task_content, formatted_time]
        # ADDING TASK INTO THE DATABASE
        conn.NonReturnQuery(
            f"INSERT INTO tasks(id,task,add_date) VALUES ({mydata[0]},'{mydata[1]}','{mydata[2]}')"
        )
        return redirect("/")
    else:
        # UPDATEING TASKS
        tasks = get_data()
        ctasks = get_cdata()
        return render_template(
            "index.html", title="Task Manager", Task=tasks, done_tasks=ctasks
        )


@app.route("/delete/<int:x>")
def delete_item(x):
    conn.NonReturnQuery(f"DELETE FROM tasks WHERE id={x}")
    return redirect("/")


@app.route("/done/<int:x>")
def item_completed(x):
    conn.NonReturnQuery(f"UPDATE tasks SET is_completed=1 WHERE id={x}")
    return redirect("/")


@app.route("/undone/<int:x>")
def item_notcompleted(x):
    conn.NonReturnQuery(f"UPDATE tasks SET is_completed=0 WHERE id={x}")
    return redirect("/")


@app.route("/update/<int:x>", methods=["POST", "GET"])
def update_item(x):
    if request.method == "POST":
        conn.NonReturnQuery(
            f"UPDATE tasks SET task='{request.form['content']}' WHERE id={x}"
        )
        return redirect("/")
    else:
        currItem = conn.returnQuery(f"SELECT task from tasks where id={x}")
        return render_template("update.html", Task=currItem, index=x)


if __name__ == "__main__":
    # print(tasks[0][1])
    conn.init_db()
    cr = conn.connect()
    conn.get_nextID("tasks", "id")
    time = str.format(f"{datetime.now()}")
    print()
    app.run(debug=True)
