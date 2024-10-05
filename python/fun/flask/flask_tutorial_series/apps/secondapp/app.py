from flask import Flask, render_template, url_for, redirect

import random

app = Flask(__name__, template_folder='templates') # poitns out to templates

@app.route('/')
def index():
    name = "Flask Application #2"
    version = "0.0.2"
    dataList = [random.randrange(1, 200, 5) for i in range(10)]
    return render_template('index.html', name=name, version=version, dataList=dataList) # awesome

@app.route('/other')
def other():
    return render_template('other.html')


@app.template_filter('alternate_text')
def alternate_text(s):
    return [c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)]
@app.route('/filters')
def filters():
    some_text = "Hello World"
    return render_template('filters.html', some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)