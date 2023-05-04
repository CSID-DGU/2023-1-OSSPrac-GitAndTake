from flask import Flask, render_template, request, session, redirect

app=Flask(__name__)
app.secret_key = 'my_secret_key'
dataLIst = []

#mian page
@app.route('/')
def input():
    return render_template('main.html')

#main page로 이동하되, 초기화 함    
@app.route('/home')
def home():
    global dataLIst
    dataLIst = []
    return render_template('main.html')

#check된 행 삭제
@app.route('/delete', methods=['POST'])
def delete():
    global dataLIst
    if request.method == "POST":
        studentNumber = request.json['student_number']
        new_data_list = [data for data in dataLIst if data['Student Number'] != studentNumber]
        dataLIst = new_data_list
    return render_template('result.html', result=dataLIst)
