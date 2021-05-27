from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])          #'/'는 정해준 포트값의 정의이다.
def hello_world():        # app.run(port=$$)
    return '<h1>Hello World!<h1>'

if __name__ == '__main__':
    app.run(*5000,debug=True)