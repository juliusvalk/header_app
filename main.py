from flask import Flask,request,Response

import chal00
import chal01
import chal02
import chal03
import chal04



# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


FLAG = 'DB_CTF{my_f1r57_fl46}'

def process_request(params, req_headers, input_items, flag):
    for i in range(len(params)):
        item = params[i]
        if item[1] == "h":
           if item[0] not in req_headers:
               response = Response()
               response.headers["missing-header"] = item[0]
               return response
        elif item[1] == "p":
            if not isinstance(input_items, list):
                return "request input object should be an array"
            if item[0] not in input_items:
                return 'missing item in input: {}'.format(item[0])
    return flag
    

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'
    
@app.route('/baspzy5ti', methods=['POST'])
def baspzy5ti():
    return process_request(chal00.params, request.headers, request.get_json(), chal00.flag )

@app.route('/bncb8u37x', methods=['POST'])
def bncb8u37x():
    return process_request(chal01.params, request.headers, request.get_json(), chal01.flag )

@app.route('/wui32r2sp', methods=['POST'])
def wui32r2sp():
    return process_request(chal02.params, request.headers, request.get_json(), chal02.flag )

@app.route('/rax7bh0sy', methods=['POST'])
def rax7bh0sy():
    return process_request(chal03.params, request.headers, request.get_json(), chal03.flag )

@app.route('/rmhpbsvl1', methods=['POST'])
def rmhpbsvl1():
    return process_request(chal04.params, request.headers, request.get_json(), chal04.flag )
    
    
@app.route('/griphon', methods=['POST'])
def griphon():
    global params
    global griphon_params
    input_items = request.get_json()
    headers = request.headers
    for i in range(len(griphon_params)):
        item = griphon_params[i]
        if item[1] == "h":
           if item[0] not in headers:
               response = Response()
               response.headers["missing-header"] = item[0]
               return response
        elif item[1] == "p":
            if not isinstance(input_items, list):
                return "request input object should be array"
            if item[0] not in input_items:
                return 'missing item in input: {}'.format(item[0])
    return FLAG

        
        
        
    


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)