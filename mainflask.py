from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify, Response, send_from_directory
import mysql.connector
from datetime import timedelta
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()  # secret_key는 서버상에 동작하는 어플리케이션 구분하기 위해 사용하고 복잡하게 만들어야 합니다.

HOST="localhost"
USER="root"
PASSWORD="onlyroot"
PORT="3306"
DATABASE="jsgame"

#id가 없는 세션일 경우인가?
def firstAccess():
    if "id" in session:
        return False
    else:
        return True

#새 접속일 경우 session에 id와 nickname부여
def newAccess():
    session["id"] = "익명"
    session["nickname"] = "익명"

#세션은 접속 할때마다 갱신해줌.
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    print(session)

#메인 화면
@app.route('/', methods = ['POST', 'GET'])
@app.route('/index.html', methods = ['POST', 'GET'])
def index():
    if firstAccess():
        newAccess()
    if session["id"] == "익명":
        text=render_template("index.html")
    else:
        text=render_template("index.html")
    return text

#회원가입 화면
@app.route('/signUp.html', methods = ['POST', 'GET'])
def signUp():
    if firstAccess():
        return redirect(url_for('index'))
    text=render_template("signUp.html")
    return text

#로그인 화면
@app.route('/signIn.html', methods = ['POST', 'GET'])
def signIn():
    if firstAccess():
        return redirect(url_for('index'))
    text=render_template("signIn.html")
    return text

#게임 맵 리스트 화면
@app.route('/GameMapList.html', methods = ['POST', 'GET'])
def GameMapList():
    if firstAccess():
        return redirect(url_for('index'))
    text=render_template("GameMapList.html")
    return text

#유저 랭킹 화면
@app.route('/Rank.html', methods = ['POST', 'GET'])
def Rank():
    if firstAccess():
        return redirect(url_for('index'))
    text=render_template("Rank.html")
    return text

#중앙사냥터 화면
@app.route('/중앙사냥터.html', methods = ['POST', 'GET'])
def gameMiddleMap():
    if firstAccess():
        return redirect(url_for('index'))
    text=render_template("gameMaps/중앙사냥터.html")
    return text

#중앙사냥터_맵편집 화면
@app.route('/중앙사냥터_맵편집.html', methods = ['POST', 'GET'])
def gameMiddleMapEdit():
    if firstAccess():
        return redirect(url_for('index'))
    text=render_template("gameMaps/중앙사냥터_맵편집.html")
    return text

#이미지 response
@app.route('/image/<path:path>', methods = ['POST', 'GET'])
def image(path):
    return send_from_directory("templates/image", path)

#id, passwd, nickname을 받아 회원가입이 가능하다면 db에 insert, 아니면 오류메시지를 표시
@app.route('/canISignUp', methods = ['POST', 'GET'])
def canISignUp():
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database=DATABASE)
    mycursor = con.cursor(dictionary=True)
    id = request.args.get('id') #get방식에서 사용하는방법
    passwd = request.args.get('passwd')
    nickname = request.args.get('nickname')
    #중복된 id가 있다면 오류.
    mycursor.execute("select * from account where id='"+id+"';")
    myresult = mycursor.fetchall()
    if(len(myresult)!=0):
        return "idOverlapped"
    #중복된 nickname이 있다면 오류.
    mycursor.execute("select * from account where nickname='"+nickname+"';")
    myresult = mycursor.fetchall()
    if(len(myresult)!=0):
        return "nickNameOverlapped"
    #id와 nickname이 중복되지 않았다면 회원가입 성공.
    mycursor.execute("insert into account(id, passwd, nickname) values('"+id+"', '"+passwd+"', '"+nickname+"');")
    con.commit()
    mycursor.close()
    return "ok"

#id, passwd, nickname을 받아 회원가입이 가능하다면 db에 insert, 아니면 오류메시지를 표시
@app.route('/canISignIn', methods = ['POST', 'GET'])
def canISignIp():
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database=DATABASE)
    mycursor = con.cursor(dictionary=True)
    id = request.form["id"] #post방식에서 사용하는방법
    passwd = request.form["passwd"]
    mycursor.execute("select * from account where id='"+id+"';")
    myresult = mycursor.fetchall()
    if(len(myresult)==0):
        return "idDoesNotExist"
    print(myresult[0]["passwd"])
    if(myresult[0]["passwd"]!=passwd):
        return "incorrectPassword"
    else:
        #해당세션에 정보부여
        session["id"] = id
        session["nickname"] = myresult[0]["nickname"]
        return "ok"

#id, passwd, nickname을 받아 회원가입이 가능하다면 db에 insert, 아니면 오류메시지를 표시
@app.route('/getCharacterInfo', methods = ['POST', 'GET'])
def getCharacterInfo():
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database=DATABASE)
    mycursor = con.cursor(dictionary=True)
    mycursor.execute("select id, nickname, level, exp, speed, wbLimitQuantity, wbLen, money from account where id='"+session["id"]+"';")
    myresult = mycursor.fetchall()
    data = jsonify(myresult[0])
    mycursor.close()
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)