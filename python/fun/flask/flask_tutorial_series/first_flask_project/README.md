# First Flask project

- Create a python virtual environment
- `python -m venv .venv`
- `source venv/bin/activate`
- `pip install flask`
- Code the app.py
- Run the app.py using `python app.py`
- A simple Hello world application
- to save the current project pypi packages `pip freeze > requirements.txt`

## Static and Dynamic URLS

- For testing purposes, use `https://1127.0.0.1:5555/handle_url_params?greeting=Welcome&name=Satyaa`
- Other options `curl https://1127.0.0.1:5555/handle_url_params?greeting=Welcome&name=Satyaa`
- A sample POST in curl `curl -X POST https://1127.0.0.1:5555/handle_url_params?greeting=Welcome&name=Satyaa`
- declaring type of mothods in code is `@app.route("handle_url_params", methods=['GET', 'POST', 'PUT', 'DELETE'])"`
- Check the hello mwthods for example in ahndling multiple request types
- Sepcific content type with status code is also feasible check `hello`
- A sample curl request, ` curl -X POST -I http://127.0.0.1:5555/hello`
- `make_response` can eb used to emulate the repsonse header and body programmatically in Flask
- 