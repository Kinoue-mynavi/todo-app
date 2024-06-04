from flask import request, jsonify
from src import app, ma
from src.service.tasks import get_all_tasks, create_task, get_task, update_task, delete_task
from src.models.tasks import Task

API_ENDPOINT = "/api"

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task

# 一覧
tasks_schema = TaskSchema(many=True)
# 単体
task_schema = TaskSchema()

@app.route(f"{API_ENDPOINT}/tasks/")
def get_all():
    tasks = get_all_tasks()
    return jsonify({
        "status": 200,
        "tasks": tasks_schema.dump(tasks)
    })

@app.route(f"{API_ENDPOINT}/tasks/<int:id>/")
def get(id):
    task = get_task(id)
    return jsonify({
        "status": 200,
        "task": task_schema.dump(task)
    })

@app.route(f"{API_ENDPOINT}/tasks/<int:id>", methods=["POST"])
def edit(id):
    if request.method != 'POST':
        return jsonify({
            "status": 401,
            "message": "不正なリクエストが送信されました"
        })

    json_data = request.json

    params_title = json_data["title"]
    params_description = json_data['description']
    params_deadline = json_data['deadline']
    params_status = json_data['status']

    result = update_task(
        id=id,
        title=params_title,
        description=params_description,
        deadline=params_deadline,
        status=params_status
    )

    if (result == "success"):
        return jsonify({
            "status": 201,
        })

    return jsonify({
        "status": 401,
    })

# POST@new
@app.route(f"{API_ENDPOINT}/new/", methods=["POST"])
def new():
    if request.method != 'POST':
        return jsonify({
            "status": 401,
            "message": "不正なリクエストが送信されました"
        })

    json_data = request.json
    
    params_title = json_data['title']
    params_description = json_data['description']
    params_deadline = json_data['deadline']

    result = create_task(
        title = params_title,
        description = params_description,
        deadline = params_deadline
    )

    if (result == "fail"):
        return jsonify({
            "status": 401,
        })

    return jsonify({
        "status": 201,
    })

@app.route(f"{API_ENDPOINT}/tasks/<int:id>/delete")
def delete(id):
    result = delete_task(id)

    if (result == "fail"):
        return jsonify({
            "status": 401
        })

    return jsonify({
        "status": 201
    })