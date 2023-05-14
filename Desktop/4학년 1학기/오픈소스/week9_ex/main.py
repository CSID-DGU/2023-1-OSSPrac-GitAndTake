from flask import Flask,render_template,request


app=Flask(__name__)
@app.route('/')
def input():
    return render_template('main.html')

@app.route('/result',methods=['POST','GET'])
# GET : 데이터를 받아와서 처리하겠다?
# POST : 처리한 데이터를 나열하겠다.
def result():
    if request.method =='POST':
        ex=dict()
        ex['Name']=request.form.get('name')
        return render_template('result.html',result=ex)
if __name__ =='__main__':
    app.run(debug=True)