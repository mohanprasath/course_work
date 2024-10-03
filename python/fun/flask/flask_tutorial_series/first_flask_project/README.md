# First Flask project

- Create a python virtual environment
- `python -m venv .venv`
- `source venv/bin/activate`
- `pip install flask`
- Code the app.py
- Run the app.py using `python app.py`
- A simple Hello world application
- to save the current project pypi packages `pip freeze > requirements.txt`

# Second Flask Project
## Static and Dynamic URLS

- For testing purposes, use `https://1127.0.0.1:5555/handle_url_params?greeting=Welcome&name=Satyaa`
- Other options `curl https://1127.0.0.1:5555/handle_url_params?greeting=Welcome&name=Satyaa`
- A sample POST in curl `curl -X POST https://1127.0.0.1:5555/handle_url_params?greeting=Welcome&name=Satyaa`
- declaring type of mothods in code is `@app.route("handle_url_params", methods=['GET', 'POST', 'PUT', 'DELETE'])"`
- Check the hello mwthods for example in ahndling multiple request types
- Sepcific content type with status code is also feasible check `hello`
- A sample curl request, ` curl -X POST -I http://127.0.0.1:5555/hello`
- `make_response` can be used to emulate the repsonse header and body programmatically in Flask

## Templating & HTML Files

- Keywords: templates, render html files, redirect, dynamic urls for specific end points, jinga filters & tempalting engines, custom filters
- Sample Projects - Secondapp
- ### Templates:
  - check the sample code in `index()` function
  - point out the templates folder while creating the `Flask` app
  - load the required template in any function using the `render_template`
  - Check `base.html` for sample code on how to use a page template
  - import a template using `extends` command. Check `index.html`
- ### Filters:
  - `template_filter` decorator helps you to implement custom filter
  - similar to functions - reusable
  - uses the `@app.template_filter('')`
- ### Redirect URLs & Dynamic Urls:
  - For dynamic Urls, i.e. where the url might change, `url_for` function is to the rescue 
  - For URL Redirection, use the `redirect` function as required

# Third Flask Project - thirdapp

- Keywords: Forms, File uploads & downloads, JS Post Requests, JSON Data
  - ### Forms:
    - include more methods in app routes `@app.route('/something', methods=['GET', 'POST'])` 
    - `request.method` and `request.form['variable_name´]` helps in fetching thr required values
    - type cast is required (?) how does types version looks like
    - use the typical html form and then in actions call the url `action="{{ url_for('/something') }}"`
    - get the variables from the form data using `request.form('form_variable_id')`
  - ### File Upload:
    - key flask functions: `request.files["FILE_NAME_HTML_INPUT]`, `file.content_type`
    - key html functions: `ecntype="multipart/form-data`, `<input type="file" accept="CONTENT-TYPES">`
  - ### File Download:
    - key flask function: `send_from_directory(directory='downloads', path=filename, download_name='results_two.csv')`
    - Sample return with Response: `Response(FILE_OBJ, mimetype="text/csv", headers={'Content-Disposition':'attachment'; filename=results.csv})`
    - `uuid` library can be used for generating almost non-repeating values
  - ### JSON Data:
    - key flask functions: `jsonify` library can help in the return values
  - ### JS POST Requests:
    - similar to form action use the `url_for{{ "SAMPLE_URL" }}`
    - learn about the fetch method in the JS. Example code contains an eventListener function call

# Static Files Project - fourthapp
  - Keywords: static files, integrating bootstrap js
  - http 2 support in flask (?)
  - ### Static Files:
    - simple map the directory and its path in the Flask app creation `Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')`

