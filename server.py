from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)
app.secret_key='I am a seekrit'
@app.route('/')
def mainFunc():
    if 'visits' not in session:
        session['visits']=1
    else:
        session['visits']+=1
    return render_template('index.html')
@app.route('/deleteSesh', methods=['POST'])
def deleteSesh():
    session['visits']=0
    return redirect('/')
@app.route('/byTwo', methods=['POST'])
def byTwo():
    session['visits']+=1
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)