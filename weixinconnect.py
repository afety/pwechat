#coding:utf8
#file is used to
import hashlib
import os
from flask import app,request,Flask, make_response

app = Flask(__name__)
__author__ = 'tanghan'

TOKEN = 'weixin'

@app.route('/weixin',methods=['POST','GET'])
def wechat_auth():
    if request.method=='GET':
        token = TOKEN
        data = request.args
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)


if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')