from flask import Flask, request, render_template
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/apps/<app_id>', methods=['GET'])
def app_detail(app_id=None):
    print(app_id)
    ret = {'app_id': app_id}
    return json.dumps(ret)


@app.route('/apps', methods=['GET', 'POST'])
def apps():
    ret = {}
    # ref: https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
    if request.method == 'POST':
        content = request.data
        print(request.args)
        print(request.form)
        print(content)
        json_str = content.decode('utf-8')
        print(json_str)
        print(type(json_str))
        dic = json.loads(json_str)
        print(dic)
        print(type(dic))
    else:
        ret = {"message": "hello world"}
    return json.dumps(ret)


