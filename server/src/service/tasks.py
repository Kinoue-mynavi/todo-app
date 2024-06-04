from src import db
from src.models.tasks import Task
from datetime import datetime

def get_all_tasks():
    try: 
        return Task.query.all()
    except Exception as e:
        print(e)
        print('データの取得に失敗しました')

def get_task(id):
    try: 
        return Task.query.get(id)
    except Exception as e:
        print(e)
        print('取得に失敗しました')

def create_task(title, description, deadline):
    try: 
        task = Task(
            title = title,
            status = "todo",
            description = description,
            deadline = deadline
        )
        db.session.add(task)
        db.session.commit()
        return "success"
    except Exception as e:
        db.session.rollback()
        print(e)
        return "fail"
    
def update_task(id, title, description, deadline, status):
    try: 
        task = get_task(id)
        task.title = title or task.title
        task.description = description or task.description
        task.deadline = deadline or task.deadline
        task.status = status or task.status

        db.session.merge(task)
        db.session.commit()

        return "success"
    except Exception as e:
        db.session.rollback()
        print(e)
        return "fail"
    
def delete_task(id):
    try: 
        task = get_task(id)
        db.session.delete(task)
        db.session.commit()
        return "success"
    except Exception as e:
        db.session.rollback()
        print(e)
        return "fail"