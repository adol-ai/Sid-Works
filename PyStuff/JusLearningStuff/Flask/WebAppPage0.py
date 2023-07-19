from flask import Flask, redirect, url_for, request
app=Flask(__name__)

c1='''<html><head><title>WebPage</title></head><style>
    *{background-color: black}
    span{
	color: #0008F0;
	font-size: 105px;
	font-family: Vivaldi;}
      .s{
	color: white;
	font-size: 135px;
	font-family: Edwardian Script ITC;}
      '</style><h1><span>'''
c2='</span><span class="s">'
c3='</span></body></html>'

@app.route('/greet/<name>')
def greet(name):
    greet='Hey Hii'
    name+='!'
    return c1+greet+'  '+c2+name+c3

@app.route('/portal', methods=['POST','GET'])
def portal():
    if request.method=='POST':
        x=request.form['x']
        return redirect(url_for('greet',name=x))
    else:
        x=request.args.get('x')
        return redirect(url_for('greet',name=x))
    
if __name__=='__main__':
    app.run(debug=True)
