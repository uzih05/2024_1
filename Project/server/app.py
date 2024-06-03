from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import os
import smtplib
from email.mime.text import MIMEText
import socketio
import uvicorn

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# Socket.IO 서버 생성
sio = socketio.AsyncServer(async_mode='asgi')
socket_app = socketio.ASGIApp(sio, app)

# 사용자 데이터 파일 경로
USER_DATA_FILE = 'C://Users//luvwl//OneDrive//문서//GitHub//university//Project//data//users.txt'

# Pydantic 모델 정의
class User(BaseModel):
    student_staff_number: str
    username: str
    password: str
    email: EmailStr

class LoginRequest(BaseModel):
    student_staff_number: str
    password: str

class SignupRequest(User):
    confirm_password: str

class PasswordResetRequest(BaseModel):
    email: EmailStr

class AddFriendRequest(BaseModel):
    username: str
    friend: str

def save_user(student_staff_number, username, password, email):
    with open(USER_DATA_FILE, 'a', encoding='utf-8') as file:
        file.write(f"{student_staff_number},{username},{password},{email}\n")

def load_users():
    users = {}
    if not os.path.exists(USER_DATA_FILE):
        return users
    with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            student_staff_number, username, password, email = line.strip().split(',')
            users[student_staff_number] = {'username': username, 'password': password, 'email': email, 'friends': []}
    return users

def save_all_users(users):
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as file:
        for student_staff_number, user in users.items():
            user_data = f"{student_staff_number},{user['username']},{user['password']},{user['email']}\n"
            file.write(user_data)

@app.post('/login')
async def login(request: LoginRequest):
    users = load_users()
    user = users.get(request.student_staff_number)
    if user and user['password'] == request.password:
        return {"status": "success", "message": "로그인 성공!", "username": user['username']}
    else:
        raise HTTPException(status_code=400, detail="로그인 실패! 학번/교직원 번호 또는 비밀번호가 잘못되었습니다.")

@app.post('/signup')
async def signup(request: SignupRequest):
    if request.password != request.confirm_password:
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
    users = load_users()
    if request.student_staff_number in users:
        raise HTTPException(status_code=400, detail="이미 등록된 학번/교직원 번호입니다.")
    save_user(request.student_staff_number, request.username, request.password, request.email)
    return {"status": "success", "message": "회원가입 성공!"}

@app.post('/password_reset')
async def password_reset(request: PasswordResetRequest):
    users = load_users()
    user_info = next((user for user in users.values() if user['email'] == request.email), None)
    if user_info:
        send_password_email(request.email, user_info['password'])
        return {"status": "success", "message": "비밀번호가 이메일로 전송되었습니다."}
    else:
        raise HTTPException(status_code=400, detail="등록되지 않은 이메일입니다.")

def send_password_email(email: str, password: str):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "luv.wlgjs@jj.ac.kr"
    smtp_password = "iiky iiox bxsl ygzr"

    msg = MIMEText(f"비밀번호는 다음과 같습니다: {password} \n비밀번호 수정을 원하시면 이 메일로 비밀번호와 함께 회신 바랍니다.")
    msg["Subject"] = "비밀번호 찾기 요청"
    msg["From"] = smtp_username
    msg["To"] = email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, email, msg.as_string())
        print("이메일이 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"이메일 전송 중 오류 발생: {e}")

@app.get('/check_user')
async def check_user(username: str):
    users = load_users()
    for user in users.values():
        if user['username'] == username:
            return {"status": "exists"}
    return {"status": "not_exists"}

@app.get('/get_friends')
async def get_friends(username: str):
    users = load_users()
    user = users.get(username)
    if user:
        friends = user.get('friends', [])
        return {"friends": friends}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post('/add_friend')
async def add_friend(request: AddFriendRequest):
    users = load_users()
    user = next((user for user in users.values() if user['username'] == request.username), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    friend = next((user for user in users.values() if user['username'] == request.friend), None)
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    
    user['friends'].append(request.friend)
    save_all_users(users)
    return {"status": "success", "message": "친구 추가 성공"}

@sio.event
async def connect(sid, environ):
    print('connect ', sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    uvicorn.run(socket_app, host='0.0.0.0', port=5000)
#test