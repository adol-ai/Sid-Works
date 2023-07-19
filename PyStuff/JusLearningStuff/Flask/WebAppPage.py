from flask import Flask, redirect, url_for, request, render_template
app=Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return render_template('Template.html',x=name)

@app.route('/portal', methods=['POST','GET'])
def portal():
    if request.method=='POST':
        y=request.form['x']
        return redirect(url_for('greet',name=y))
    else:
        y=request.args.get('x')
        return redirect(url_for('greet',name=y))
    
if __name__=='__main__':
    app.run(debug=True)