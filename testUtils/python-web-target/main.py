# coding=UTF-8
from flask import  Flask, request, render_template,jsonify,redirect,Response,make_response
import sys, getopt
import logging
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


logger = logging.getLogger("app.module")

@app.route('/csrf', methods=["GET", "POST"])
def csrf():
    return '<html><body>隐藏了csrf的页面<input type="hidden" name="csrf" value="csrfsecr"/></body></html>'



@app.route('/', methods=["GET", "POST", "PUT", "DELETE", "OPTION"])
def index():
    print(printDetail())
    return render_template("index.html") 


@app.route('/test', methods=["GET", "POST"])
def test():
    return printDetail()

@app.route('/desc', methods=["GET", "POST"])
def test1():
    return printDetail()

@app.route('/db', methods=["GET", "POST"])
def db():
    return printDetail()

@app.route('/testDocument', methods=["GET", "POST"])
def testDocument():

    resp = printDetail()
    print(resp)
    return resp


@app.route('/jsonLogin', methods=["GET", "POST"])
def jsonLogin():

    data = {
        "code": "201",
    }
    res = make_response(data) # 设置响应体
    res.status = '200' # 设置状态码
    res.headers['token'] = "123456" # 设置响应头
    res.headers['City'] = "shenzhen" # 设置响应头

    return res

@app.route('/wait', methods=["GET", "POST"])
def wait():

    time.sleep( 3 )


    return Response(), 504, {"msg": "timeout"}


@app.route('/json', methods=["GET", "POST"])
def json():
    return jsonObj()


@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username=="user" and password == "pwd":
        return redirect("/")

    username = request.args.get("username")
    password = request.args.get("password")

    if username=="user" and password == "pwd":
        return redirect("/")

    response = Response()

    return response, 401, {"msg": "fidden"}

def jsonObj():
      
    data = {
        "code": -1,
        "msg": "hello world",
        "data": "hello world"
    }

    return jsonify(data)


def printDetail():
    
    outHeader = "-----------------host------------------<br>"
    outHeader+=str(request.host+"<br>")

    outHeader += "-----------------path------------------<br>"
    outHeader+=str(request.path+"<br>")

    outHeader += "-----------------header------------------<br>"
    for header in request.headers:
        outHeader += (str(header[0]) +str(header[1])+"<br>")

    outParams="-----------------param------------------<br>"
    outParams+="args:"+str(request.args)+"<br>"
    outParams+="form:"+str(request.form)+"<br>"
    outParams+="json:"+str(request.json)+"<br>"

    outParams+="-----------------cookies------------------<br>"
    outParams+="cookies:"+str(request.cookies)+"<br>"
    
    httpBody = outHeader+ outParams

    httpBody+='<a href="https://bs.across.com/test" >to child</a>'
    
    logger.info(httpBody)
    print(httpBody)
    return httpBody

if __name__ == '__main__':
    argv = sys.argv[1:]
    opt_ip = '0.0.0.0'
    opt_port = 5001
    
    try:
        options, args = getopt.getopt(argv, "p:i:", ["help", "ip=", "port="])

        print(options)
        print(args)
    except getopt.GetoptError:
        app.run(host=opt_ip,port=opt_port)
        sys.exit()
        
    for option, value in options:
        if option in ("-i", "--ip"):
            opt_ip = value
        if option in ("-p", "--port"):
            opt_port = value
    app.debug =True
    app.run(host=opt_ip,port=opt_port)
    


@app.errorhandler(Exception)
def error_handler(e):
  
    data = {
        "code": -1,
        "msg": str(e),
        "data": None
    }

    return jsonify(data)
