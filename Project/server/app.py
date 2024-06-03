import json
import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
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
USER_DATA_FILE = 'C://Users//luvwl//OneDrive//문서//GitHub//university//Project//data//users.json'
FRIENDS_DIR = 'C://Users//luvwl//OneDrive//문서//GitHub//university//Project//data//friends'

if not os.path.exists(FRIENDS_DIR):
    os.makedirs(FRIENDS_DIR)

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
    student_staff_number: str
    friend_username: str

def save_user(student_staff_number, username, password, email):
    users = load_users()
    users[student_staff_number] = {
        'username': username,
        'password': password,
        'email': email
    }
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_friends(student_staff_number):
    friends_file = os.path.join(FRIENDS_DIR, f"{student_staff_number}.txt")
    if not os.path.exists(friends_file):
        return []
    with open(friends_file, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def save_friends(student_staff_number, friends):
    friends_file = os.path.join(FRIENDS_DIR, f"{student_staff_number}.txt")
    with open(friends_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(friends))

@app.post('/signup')
async def signup(request: SignupRequest):
    if request.password != request.confirm_password:
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
    users = load_users()
    if request.student_staff_number in users:
        raise HTTPException(status_code=400, detail="이미 등록된 학번/교직원 번호입니다.")
    save_user(request.student_staff_number, request.username, request.password, request.email)
    return {"status": "success", "message": "회원가입 성공!"}

@app.post('/login')
async def login(request: LoginRequest):
    users = load_users()
    user = users.get(request.student_staff_number)
    if user and user['password'] == request.password:
        return {"status": "success", "message": "로그인 성공!", "username": user['username']}
    else:
        raise HTTPException(status_code=400, detail="로그인 실패! 학번/교직원 번호 또는 비밀번호가 잘못되었습니다.")

@app.get('/get_friends')
async def get_friends(student_staff_number: str = Query(..., alias="username")):
    friends = load_friends(student_staff_number)
    return {"friends": friends}

@app.post('/add_friend')
async def add_friend(request: AddFriendRequest):
    users = load_users()
    user = users.get(request.student_staff_number)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    friend = next((u for u in users.values() if u['username'] == request.friend_username), None)
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    
    friends = load_friends(request.student_staff_number)
    if request.friend_username in friends:
        raise HTTPException(status_code=400, detail="Friend already added")
    
    friends.append(request.friend_username)
    save_friends(request.student_staff_number, friends)
    return {"status": "success", "message": "친구 추가 성공"}

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

@app.post('/password_reset')
async def password_reset(request: PasswordResetRequest):
    users = load_users()
    user_info = next((user for user in users.values() if user['email'] == request.email), None)
    if user_info:
        send_password_email(request.email, user_info['password'])
        return {"status": "success", "message": "비밀번호가 이메일로 전송되었습니다."}
    else:
        raise HTTPException(status_code=400, detail="등록되지 않은 이메일입니다.")

@sio.event
async def connect(sid, environ):
    print('connect ', sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    uvicorn.run(socket_app, host='0.0.0.0', port=5000)
