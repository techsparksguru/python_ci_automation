import json 

from datetime import timedelta
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import safe_str_cmp
from flask_url_discovery import url_discovery
from flask_jwt import JWT, jwt_required, current_identity
from flask import Flask, jsonify, make_response, request, abort, Blueprint, url_for


class User(object):
    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email

        self.username = username
        self.password = password

    def __repr__(self):
         return json.dumps({'id':self.id, 'username':self.username, 'email':self.email})

users = [
    User(1, 'suhas.manju89@gmail.com', 'Suhas', 'abcxyz'),
    User(2, 'pradeep.macharla@gmail.com', 'Pradeep', 'abcxyz'),
    User(3, 'testuser@gmail.com', 'Test', 'abcxyz'),
    User(4, 'techsparksuser1@gmail.com', 'Techsparks1', 'abcxyz'),
    User(5, 'techsparksuser2@gmail.com', 'Techsparks2', 'abcxyz')
]

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

email_table = {u.email: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(email, password):
    user = email_table.get(email, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['id'] = task['id']
            new_task['uri'] = url_for('get_tasks_v1', id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'techsparksuser':
        return 'Test@123'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=36000)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_AUTH_URL_RULE'] = '/login'


url_discovery(app)

app_bp = Blueprint('my_bp', __name__)
jwt = JWT(app, authenticate, identity)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/user-identity')
@jwt_required()
def user_identified():
    return '%s' %current_identity

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks_v1():
    args = request.args
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

@app.route('/todo/api/v2.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks_v2():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v3.0/tasks', methods=['GET'])
@jwt_required()
def get_tasks_v3():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task_v1(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v2.0/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task_v2(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v3.0/tasks/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task_v3(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task_v1():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v2.0/tasks', methods=['POST'])
@auth.login_required
def create_task_v2():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v3.0/tasks', methods=['POST'])
@jwt_required()
def create_task_v3():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task_v1(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v2.0/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task_v2(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v3.0/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task_v3(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_v1(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.route('/todo/api/v2.0/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task_v2(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.route('/todo/api/v3.0/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task_v3(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.route("/index")
def all_links():
    links = {}
    for rule in app.url_map.iter_rules():
        links.update((url, rule.endpoint))
    return render_template("index.html", links=links)
    
if __name__ == '__main__':
    app.register_blueprint(app_bp)
    app.run()