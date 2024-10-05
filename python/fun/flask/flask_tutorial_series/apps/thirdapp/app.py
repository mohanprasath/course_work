from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import pandas as pd
import os
import uuid
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return 'Great!. You have successfully logged in.'
        else:
            return 'Sorry!. Your Login is not allowed.'

@app.route('/fileupload', methods=['POST'])
def fileupload():
    file = request.files['file']
    file_content_type = file.content_type
    if file_content_type == 'text/plain':
        return  file.read().decode()
    elif file_content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file_content_type == 'application/vnd.ms-excel':
        return pd.read_excel(file).to_html()
    elif file_content_type == 'text/csv':
        return pd.read_csv(file).to_html()
    return file_content_type

@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    file_content_type = file.content_type
    if file_content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file_content_type == 'application/vnd.ms-excel':
        response = Response(
            pd.read_excel(file).to_csv(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=results.csv'}
        )
        return response
    return file_content_type + ' is not the expected format for conversion!'


@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.mkdir('downloads')
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(f'downloads/{filename}', index=False)
    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(directory='downloads', path=filename, download_name='results_two.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']
    with open('file.txt', 'w') as f:
        f.write(f'{greeting} {name}')
    return jsonify({'message': 'Greeting successfully written!'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555,debug=True)