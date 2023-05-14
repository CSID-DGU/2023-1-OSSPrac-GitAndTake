from flask import Flask, render_template, request, session, redirect

app=Flask(__name__)
# my_secret_key의 기능 질문
app.secret_key = 'my_secret_key'

#mian page
@app.route('/')
def input():
    return render_template('main.html')

#main page로 이동하되, 초기화 함
# /home 페이지를 설정하는 이유
@app.route('/home')
def home():
    session.clear() # 초기화
    return render_template('main.html')

#check된 행 삭제
#request.json ? 왜 request.form 안쓰지?
@app.route('/delete', methods=['POST'])
def delete():
    if request.method == "POST":
        student_number = request.json['student_number']
        data_list = session['data_list']
        new_data_list = [data for data in data_list if data['Student Number'] != student_number]
        session['data_list'] = new_data_list
    return render_template('result.html', result=session['data_list'])

# GET 데이터를 받아와서 처리하겠다
# post 처리한 데이터를 포스팅(나열) 하겠다 
@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == "POST":
        # 딕셔너리 형태로 데이터 저장
        data = {
            "Name": request.form["Name"],
            "Student Number": request.form["Student Number"],
            "Major": request.form["Major"],
            "Email": request.form["Email"] + "@" + request.form["Email_domain"],
            "Gender": request.form.get("Gender"),
            "Programing Language": ", ".join(request.form.getlist("Pro_lang[]"))
        }
        
        # 세션에 데이터가 저장되어 있는지 확인
        if 'data_list' in session:
            data_list = session['data_list']
        # 저장되어 있는 데이터가 없으면, 새로운 리스트 생성
        else:
            data_list = []
        # 딕렉셔리 형태의 데이터를 추가
        data_list.append(data)
        # 학번으로 오름차순 정렬
        data_list = sorted(data_list, key=lambda x: x.get('Student Number', '').lower(), reverse=True)
        # 세션에 데이터 저장
        session['data_list'] = data_list
        #result.html로 반환
    return render_template('result.html', result=session['data_list'])

print('ex1.py is set to {}'.format(__name__))
if __name__ =='__main__':
    app.run(debug=True, port=8000)