from flask import render_template, redirect, flash, request
from src import app
from src.service.tasks import get_all_tasks, create_task, get_task, update_task, delete_task

@app.route("/")
def index():
    return render_template("index.html", tasks=get_all_tasks())

@app.route("/tasks/<int:id>")
def show_edit(id):
    return render_template("edit.html", task=get_task(id))

@app.route("/tasks/<int:id>", methods=["POST"])
def edit(id):
    if request.method != 'POST':
        flash("400: 不正なリクエストが送信されました")

    params_title = request.form['title']
    params_description = request.form['description']
    params_deadline = request.form['deadline']
    params_status = request.form['status']

    result = update_task(
        id=id,
        title=params_title,
        description=params_description,
        deadline=params_deadline,
        status=params_status
    )

    if (result == "success"):
        flash("タスクを更新しました！")
        return redirect("/")

    flash("タスクの更新に失敗しました")
    return render_template("edit.html", task=get_task(id))

# GET@new
@app.route("/new/")
def show_new():
    return render_template("new.html")

# POST@new
@app.route("/new/", methods=["POST"])
def new():
    if request.method != 'POST':
        flash("400: 不正なリクエストが送信されました")
    
    params_title = request.form['title']
    params_description = request.form['description']
    params_deadline = request.form['deadline']

    retult = create_task(
        title = params_title,
        description = params_description,
        deadline = params_deadline
    )

    if (retult == "success"):
        flash("タスクを追加しました！")
        return redirect("/")
    
    flash("タスクの追加に失敗しました")
    return render_template("new.html")

@app.route("/tasks/<int:id>/delete")
def delete(id):
    result = delete_task(id)
    if (result == "fail"):
        flash("タスクを削除できませんでした")
    return redirect("/")