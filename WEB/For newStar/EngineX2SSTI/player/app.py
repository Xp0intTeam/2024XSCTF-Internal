from flask import Flask,request
from flask import render_template_string
import logging

app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

@app.route('/hello')
def hello_world():
    return 'Hello World'

#TODO REMOVE SECRET ROUTE
@app.route('/secret',methods=['POST'])
def secret():
    template = request.form.get("xscode")
    if template is None:
        return "error" , 400
    result=render_template_string(template)
    print(result)
    if result !=None:
        return "OK"
    else:
        return "error"
