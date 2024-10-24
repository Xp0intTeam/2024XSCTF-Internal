from flask import Flask, request, render_template_string

app = Flask(__name__)

black_list = ['import','os','.','exec','eval']
def waf(name):
    for x in black_list:
        if x in name.lower():
            print(x)
            return True
    return False


@app.route('/')
def index():
    return open(__file__).read()


@app.post('/exec')
def user():
    code = request.form.get("code")
    if not code:
        return 'exp'
    if waf(code):
        return "No hacker"
    try:
        exec(code)
    except:
        pass
    return 'ok'


if __name__ == '__main__':
    app.run("0.0.0.0", port=11111)