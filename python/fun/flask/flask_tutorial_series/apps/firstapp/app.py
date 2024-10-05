from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome!</h1>"

@app.route("/hello", methods=['GET', 'POST', 'PUT', 'DELETE']) # static urls
def hello():
    if request.method == 'GET':
        return "<h1>Hello World! - From GET request</h1>", 200
    elif request.method == 'POST':
        return "<h1>Hello World! - From POST request</h1>", 200
    elif request.method == 'PUT':
        return "<h1>Hello World! - From PUT request</h1>", 200
    return "Something is wrong", 400 # Bad Request Example

@app.route('/hello_revamped', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def hello_revamped():
    response = make_response('Hello Revamped!')
    response.status_code = 202
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route("/greet/<name>") # dynamic urls
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route("/add_old/<number1>/<number2>")#without type cast
def add_without_typecast(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

@app.route("/add/<int:number1>/<int:number2>") # with type cast
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route('/handle_url_params')
def handle_url_params():
    greeting = request.args.get('greeting', '')
    name = request.args.get('name', '')
    if greeting and name:
        return f'{greeting}, {name}'
    else:
        return 'Some params are missing!'
    # return request.args.to_dict() # returns all arfuments as a dictionary


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)