from flask import Flask, request, render_template, redirect, url_for, abort,session
import json
import dbdb

from random import *




app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/startgame') 
def startgame():
    if 'user' in session: 
        return render_template('startgame.html')
    else : 
        return redirect(url_for("login"))

@app.route('/join', methods=['GET', 'POST']) 
def join(): 
    if  request.method == 'GET':
        return render_template('join.html')
    else:
        dbdb.create_table()
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        a = dbdb.ckeck_id(id)
        if a != None:
            return '''
            <script> 
            alert('다른 아이디를 사용하세요');
            location.href="/join" 
            </script> 
            '''
        else :
            dbdb.insert_data(id,pw,name)
            return redirect(url_for('login'))
@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def helloovar(name):
    return 'Hello, {}!'.format(name)

@app.route('/getinfo') 
def getinfo(): 
     # 파일 입력 
    with open("static/save.txt", "r", encoding='utf-8') as file: 
        student = file.read().split(',') # 쉽표로 잘라서 student 에 배열로 저장 
    return '번호 : {}, 이름 : {}'.format(student[0], student[1])

@app.route('/input/<int:num>')
def input_num(num):
    a = randint (1,2)

    if num == 1:
        if a == 1:
            return render_template('1.html') 
        else:
            return render_template('2.html')
    elif num == 2:
        if a == 2:
            return render_template('4.html')
        else:
            return render_template('3.html')

    # return 'Hello, {}!'.format(name)

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        a = dbdb.select_user(id,pw)
        # id와 pw가 임의로 정한 값  이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        if a != None:
            session['user'] = id
            return ''' 
                <script> alert("안녕하세요~ {}님"); 
                location.href="/" 
                </script>
             '''.format(id) 
             # return redirect(url_for('form'))
        else:
            return "아이디 또는 패스워드를 확인 하세요."

#로그인 사용자만 접근 가능으로 만들면
@app.route('/form') 
def form(): 
    if 'user' in session: 
        return render_template('test.html') 
    return redirect(url_for('login'))

@app.route('/logout') 
def logout(): 
    session.pop('user', None) 
    return redirect(url_for('index'))



#@app.route('/move/<site>')
#def move_site(site):
#    if site == 'naver':
#        return redirect(url_for("naver"))
#    elif site == 'daum':
#        return redirect(url_for("daum"))
#    else:
#        abort(404)
#        # return '없는 페이지 입니다.'


@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인 하세요", 404

@app.route('/img')
def img():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)