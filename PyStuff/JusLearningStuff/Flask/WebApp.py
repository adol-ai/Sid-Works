from flask import Flask
app=Flask(__name__)

@app.route('/app/<name>')
def hello(name):
    return 'Hello '+name+'!'

@app.route('/page')
def hey():
    return 'Hey Hiiiiiii!'

@app.route('/site/<name>')
def hii(name):
    return 'Hii '+name+'!'

if __name__=='__main__':
    app.run(debug=True)