import customtkinter as ctk
from PIL import Image
import os

# CustomTkinter 초기 설정
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# 메인 윈도우 생성
app = ctk.CTk()
app.title("전주대학교 메일")

# 배경 이미지 경로 확인 및 로드
background_image_path = os.path.join(os.path.dirname(__file__), "background.jpg")

# PIL을 사용하여 이미지를 로드하고 크기 조정
background_image = Image.open(background_image_path)
background_image_resized = background_image.resize((1218, 685), Image.LANCZOS)

# CTkImage로 변환
background_photo = ctk.CTkImage(light_image=background_image_resized, size=(1218, 685))

# 배경 이미지 레이블 생성 및 배치
background_label = ctk.CTkLabel(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# 창 크기를 배경 이미지에 맞게 조정
window_width, window_height = background_image_resized.size
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

app.geometry(f"{window_width}x{window_height}+{x}+{y}")
app.resizable(False, False)  # 창 크기 고정

# 페이지별 크기 설정
page_sizes = {
    'login': (400, 500),
    'signup': (400, 645),
    'password_reset': (405, 450),
}

# 외곽 프레임 생성
outer_frame = ctk.CTkFrame(app, corner_radius=13, fg_color="black")
outer_frame.place(relx=0.5, rely=0.5, anchor='center')

# 페이지 전환 함수
def show_frame(frame_name):
    # 페이지에 맞는 프레임 크기 가져오기
    width, height = page_sizes[frame_name]
    outer_frame.configure(width=width - 75, height=height - 162)
    
    for frame in frames.values():
        frame.place_forget()
    frames[frame_name].place(relx=0.5, rely=0.5, anchor='center')

# 메인 프레임 생성
frames = {}

# 각 페이지별 프레임 생성 및 저장
for F in ('login', 'signup', 'password_reset'):
    frame = ctk.CTkFrame(outer_frame, corner_radius=10, fg_color="white")
    frames[F] = frame

# 각 페이지 생성 함수 호출
from login import create_login_frame
from signup import create_signup_frame
from password_reset import create_password_reset_frame

create_login_frame(frames['login'], show_frame)
create_signup_frame(frames['signup'], show_frame)
create_password_reset_frame(frames['password_reset'], show_frame)

# 초기 페이지 설정
show_frame('login')

# 메인 루프 시작
app.mainloop()