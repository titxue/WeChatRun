from prop import ProductionConfig
from wechat_mi import send
from flask import Flask, render_template, request

app = Flask(__name__)

config = {
    'prop': ProductionConfig,
}
# 设置配置类
Config = config['prop']
# 加载配置
app.config.from_object(Config)




@app.route('/wechat',methods=['POST','GET'])
def wechat():
    userName = request.form.get('userName')#表单提交的数据用form
    #链接提交的数据用arg
    userPwd = request.form.get('userPwd')
    stepNumber = request.form.get("stepNumber")
    msg = "登录小米账号"
    if(userName!="" and userPwd!="" and stepNumber!=""):
        try:
            msg = send(userName,userPwd,stepNumber)
        except:
            pass
    else:
        msg = "登录小米账号"
    return render_template('default.html', page_title='刷微信步数',message=msg)


@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了哈哈哈'

@app.errorhandler(404)
def internal_server_error(e):
    return '瞎请求什么路径呢'

if __name__ == '__main__':
    app.run(debug=False,port=5000,host="0.0.0.0")
