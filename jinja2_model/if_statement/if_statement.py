from flask import Flask,render_template

app = Flask(__name__)


@app.route('/<is_login>/')
def index(is_login):
    if is_login == '1':
        user = {
            'username': u'张鼎鼎',
            'gender': u'男',

            # 若年龄<=18则http://127.0.0.1:5000/1/的界面为登录 注册，而非张鼎鼎 注销
            'age': 20

        }

        return render_template('index.html', user = user)
    else:
        return render_template('index.html', )


if __name__ == '__main__':
    app.run()
