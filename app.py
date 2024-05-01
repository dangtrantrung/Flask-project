from flask import Flask, make_response, render_template, request

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    # return "<h1> Flask AI Web App </h1>"
    myvalue='NeuralNine'
    myresult=10+50
    mylist=[10,20,30,40]
    return render_template('index.html',myvalue=myvalue,myresult=myresult,mylist=mylist)

@app.route('/other')
def other():
    # return "<h1> Flask AI Web App </h1>"
    myvalue='Trung'
    myresult=10+500
    mylist=[100,200,300,400]
    return render_template('other.html',myvalue=myvalue,myresult=myresult,mylist=mylist)

@app.route('/hello',methods=['POST','GET','PUT','DELETE'])
# $ curl -i http://127.0.0.1:9999/hello - response header
def hello():
    # if request.method=='GET':
    #     response=make_response
    #     return 'You make a GET request\n',501 # custom response, status code in HTTP response
    # elif request.method=='POST':
    #     return 'You make a POST request'
    # else:
    #     return 'Your method can not be accepted'
    response=make_response('Hello World custom response\n')
    response.status_code=202
    # response.headers['content-type']='application/octet-stream'
    response.headers['content-type']='text/plain'

    return response

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
