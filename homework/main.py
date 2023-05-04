from flask import Flask, render_template, request, session

app=Flask(__name__)
app.secret_key = 'my_secret_key'

#mian page
@app.route('/')
def input():
    return render_template('main.html')

#main page로 이동하되, 초기화 함
@app.route('/home')
def home():
#check된 행 삭제
@app.route('/delete', methods=['POST'])
def delete():
# GET 데이터를 받아와서 처리하겠다
# post 처리한 데이터를 포스팅(나열) 하겠다 
@app.route('/result', methods=['GET','POST'])
def result():

print('ex1.py is set to {}'.format(__name__))
if __name__ =='__main__':
    app.run(debug=True, port=8000)