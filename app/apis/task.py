from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import Response

from app.models.Task import Task

import json

db = SQLAlchemy()
mimetype = 'application/json'

class TaskList(Resource):
    def get(self):
        task_list = db.session.query(Task).all()
        db.session.close()
        res = json.dumps({
            'result': [data.to_json() for data in task_list]
        })
        return Response(res, status=400, mimetype=mimetype)

    def post(self):
        req = request.get_json(force=True)
        if 'name' not in req:
            return resopnse_parameter_error('name')
        try:
            new_task = Task(name=req['name'])
            db.session.add(new_task)
            db.session.commit()
        except Exception as e:
            print(e)
            error_message = json.dumps({ 'error': 'Error when insert into db' })
            return Response(error_message, status=500, mimetype=mimetype)
        
        result = json.dumps({
            'result': {'name': new_task.name, 'status': new_task.status, 'id': new_task.id}
        })
        return Response(result, status=201, mimetype=mimetype)

class Tasks(Resource):
    def put(self, id):
        req = request.get_json(force=True)
        if 'status' not in req:
            return resopnse_parameter_error('status')
        try:
            task = db.session.query(Task).filter(Task.id == id).one()
        except:
            error_message = json.dumps({ 'error': 'Can not find data' })
            db.session.close()
            return Response(error_message, status=400, mimetype=mimetype)
        
        task.name = req['name']
        task.status = req['status']
        db.session.commit()
        res = json.dumps({
            'name': task.name,
            'id': task.id,
            'status': task.status
        })
        return Response(res, status=200, mimetype=mimetype)

    def delete(self, id):
        try:
            task = db.session.query(Task).filter(Task.id == id).one()
            db.session.delete(task)
            db.session.commit()
        except Exception as e:
            error_message = json.dumps({ 'error': f'There no data in db: {id}' })
            return Response(error_message, status=400, mimetype=mimetype)
        
        res = json.dumps({ 'result': 'success' })
        return Response(res, status=200, mimetype=mimetype)


def resopnse_parameter_error(column:str) -> Response:
    error_message = json.dumps({ 'error': f'Please in put parameter: {column}' })
    return Response(error_message, status=400, mimetype=mimetype)