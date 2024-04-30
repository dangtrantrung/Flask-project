from flask import Flask,request




app=Flask(__name__)

@app.route('/')
def index():
    return "<h1> Flask AI Web App </h1>"

@app.route('/hello')
def hello():
    return "Hello World"
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"
@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    result=int(number1)+int(number2)
    result2=f"kết quả là: {number1 +number2}"
    return result2
# dynamic Urls params
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greet=request.args['greeting']
        name=request.args['name']
        age=request.args['age']
        return f'{greet} {name} {age} year old'
    else:
        return 'Missing some params'


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)
