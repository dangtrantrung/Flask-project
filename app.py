import os
import uuid

import pandas as pd
from flask import (Flask, Response, flash, jsonify, make_response, redirect,
                   render_template, request, send_from_directory, session,
                   url_for)

app=Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')
# session & cookies - secret_key
app.secret_key='SOME_KEY'

@app.route('/set_data')
def set_data():
    session['name']='Trung'
    session['other']='Hello world'
    return render_template('index.html',message='Session data set')
@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other= session['other']
        return render_template('index.html',message=f'name: {name}, Other: {other}')
    else:
        return render_template('index.html',message=f'No session found!!!')
@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html',message=f'session cleared!!!')
@app.route('/set_cookie')
def set_cookie():
    response=make_response(render_template('index.html',message='Cookie set'))
    response.set_cookie('cookie_name','cookie_value:sfdfgg',samesite=None)
    return response
@app.route('/get_cookie')
def get_cookie():
    cookie_value=request.cookies['cookie_name']

    return render_template('index.html',message=f'Cookie value: {cookie_value}')
@app.route('/remove_cookie')
def remove_cookie():
    response=make_response(render_template('index.html',message='Cookie removed'))
    response.set_cookie('cookie_name',expires=0)
    return response

@app.route('/')
def index():
    # # return "<h1> Flask AI Web App </h1>"
    myvalue='NeuralNine'
    myresult=10+50
    mylist=[10,20,30,40]
    return render_template('index.html',myvalue=myvalue,myresult=myresult,mylist=mylist,message='Index')
    # if request.method=='GET':
    #     return render_template('form.html')
    # elif request.method=='POST':
    #     return ''
@app.route('/form',methods=['POST','GET'])
def form():
    # # return "<h1> Flask AI Web App </h1>"
    # myvalue='NeuralNine'
    # myresult=10+50
    # mylist=[10,20,30,40]
    # return render_template('index.html',myvalue=myvalue,myresult=myresult,mylist=mylist)
    if request.method=='GET':
        return render_template('form.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='Trung' and password=='pass':
            return 'Success'
        else:
            return 'Failure'

@app.route('/file_upload',methods=['POST'])
def file_upload():
    file=request.files['file']

    if file.content_type=='text/plain':
        return file.read().decode()
    elif file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','application/vnd.ms-excel'] and not file.filename.endswith('.csv'):
        df=pd.read_excel(file)
        return df.to_html()
    elif file.filename.endswith('.csv'):
        df=pd.read_csv(file)
        print(file.filename)
        return df.to_html(header=None)


@app.route('/ASSFFGHHGggggg')
def other():
    # return "<h1> Flask AI Web App </h1>"
    myvalue='Trung'
    myresult=10+500
    mylist=[100,200,300,400]
    return render_template('other.html',myvalue=myvalue,myresult=myresult,mylist=mylist)

@app.route('/filters')
def filters():
    # return "<h1> Flask AI Web App </h1>"
    myvalue='Trung'
    myresult=1000+500
    mylist=[1000,2000,3000,4000]
    some_text='Hello Trung xyz'
    return render_template('filters.html',some_text=some_text,myvalue=myvalue,myresult=myresult,mylist=mylist)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]
@app.template_filter('repeat')
def repeat(s,times=2):
    return s*times
@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i%2==0 else c.lower() for i,c in enumerate(s)])
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

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
# dynamic Urls params ?greeting=...&name=...&age=...
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greet=request.args['greeting']
        name=request.args['name']
        age=request.args['age']
        return f'{greet} {name} {age} year old'
    else:
        return 'Missing some params'


@app.route('/convert_csv',methods=['POST'])
def convert_csv():
    file=request.files['file']
    df=pd.read_excel(file)
    response=Response(df.to_csv(),mimetype='text/csv',headers={
        'Content-Disposition':'attachment;filename=result.csv'
    })
    return response

@app.route('/convert_csv_two',methods=['POST'])
def convert_csv_two():
    file=request.files['file']
    df=pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    filename=f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))
    return render_template('download.html',filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name='result_csv')
@app.route('/handle_post',methods=['POST'])
def handle_post():
    greeting=request.json['greeting']
    name=request.json['name']
    with open('file.txt','a') as f:
        f.write(f'{greeting},{name}'+'\n')
    return jsonify({'message':'Successfully written!'})

# static files

# flash messages
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template('login.html')
    elif request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='Trung' and password=='123':
            flash('Login Successful')
            flash(f'user: {username}')
            flash(f'pass: {password}')
            return render_template('index.html',message='')
        else:
            flash(['Login failed!!!','Are you missing your account name or password?','Plz Try with another account'])
            return render_template('index.html',message='')

# Databases & SQLAlchemy

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)
