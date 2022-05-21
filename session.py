from flask import Flask, url_for, request, session, redirect, app
from markupsafe import escape
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secretkey'  # secret_key는 서버상에 동작하는 어플리케이션 구분하기 위해 사용하고 복잡하게 만들어야 합니다.
#app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1) # 로그인 지속시간을 정합니다. 현재 1분

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/')
def index():
    print(session)
    if 'username' in session:  # session안에 username이 있으면 로그인
        return '로그인 성공! 아이디는' + session['username'] + "<br><a href = '/logout'>로그아웃</a>"

    return "로그인 해주세요. <br><a href = '/login'> 로그인 하러가기! </a>" # 로그인이 안될 경우


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # request.method를 통해 GET & POST 인지 확인함.
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return ''' 
    <form action = "" method = "post">
        <p><input type = "text" name = "username" /></p>
        <p><input type = "submit" value = "Login" /></p>
    </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)