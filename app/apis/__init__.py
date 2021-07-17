from flask_restful import Api
from flask import Blueprint
from .task import Tasks, TaskList

api_blueprint = Blueprint('api', __name__)
api = Api()
api.init_app(api_blueprint)

#task route
api.add_resource(TaskList, '/task')
api.add_resource(Tasks, '/task/<int:id>')