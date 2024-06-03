import customtkinter as ctk
import requests
import re

def create_signup_frame(frame, show_frame):
    title_font = ctk.CTkFont(family="NanumBarunpenR", size=24, weight="bold")
    description_font = ctk.CTkFont(family="NanumBarunpenR", size=16, weight="bold")

    # 제목 라벨 생성
    title_label = ctk.CTkLabel(frame, text="회원가입", font=title_font)
    title_label.pack(pady=20, padx=60)

    # 설명 라벨 생성
    description_label = ctk.CTkLabel(frame, text="정보를 입력하세요", font=description_font)
    description_label.pack(pady=10, padx=60)

    # 학번/교직원 번호 입력 필드 생성
    entry_number = ctk.CTkEntry(frame, placeholder_text="학번 또는 교직원 번호", font=description_font, width=200)
    entry_number.pack(pady=10, padx=60)

    # 사용자 이름 입력 필드 생성
    entry_username = ctk.CTkEntry(frame, placeholder_text="사용자 이름", font=description_font, width=200)
    entry_username.pack(pady=10, padx=60)

    entry_password = ctk.CTkEntry(frame, placeholder_text="비밀번호         (한영주의!)", show="*", font=description_font, width=200)
    entry_password.pack(pady=10, padx=10)

    entry_confirm_password = ctk.CTkEntry(frame, placeholder_text="비밀번호 확인 (한영주의!)", show="*", font=description_font, width=200)
    entry_confirm_password.pack(pady=10, padx=10)

    # 이메일 입력 필드 생성
    entry_email = ctk.CTkEntry(frame, placeholder_text="이메일 주소", font=description_font, width=200)
    entry_email.pack(pady=10, padx=10)

    # 회원가입 함수
    def signup(event=None):
        
        # 입력 필드가 비어 있는지 확인
        if not entry_number.get() or not entry_username.get() or not entry_password.get() or not entry_confirm_password.get() or not entry_email.get():
            show_alert("모든 필드를 채우세요.")
            return
        
        # 이메일 유효성 검사
        email = entry_email.get()
        email_pattern = r'^[^@]+@[^@]+\.[^@]+$'
        if not re.match(email_pattern, email):
            show_alert("유효한 이메일 주소를 입력하세요.")
            return

        # 비밀번호 일치 여부 확인
        if entry_password.get() != entry_confirm_password.get():
            show_alert("비밀번호가 일치하지 않습니다.")
            return
        
        # 학번/교직원 번호 유효성 검사 (예시: 숫자만 허용)
        if not entry_number.get().isdigit():
            show_alert("학번 또는 교직원 번호는 숫자여야 합니다.")
            return

        data = {
            'student_staff_number': entry_number.get(),
            'username': entry_username.get(),
            'password': entry_password.get(),
            'confirm_password': entry_confirm_password.get(),
            'email': entry_email.get()
        }

        try:
            response = requests.post('http://61.255.152.191:5000/signup', json=data)
            try:
                response_data = response.json()
            except requests.exceptions.JSONDecodeError:
                show_alert("서버로부터 올바르지 않은 응답을 받았습니다.")
                return

            if response.status_code == 200 and response_data.get("status") == "success":
                show_alert("회원가입 성공!")
                show_frame('login')
            else:
                error_detail = response_data.get("detail", "알 수 없는 오류가 발생했습니다.")
                show_alert(error_detail)

        except requests.RequestException as e:
            show_alert(f"요청 중 오류가 발생했습니다: {e}")

    # 경고창 생성 함수
    def show_alert(message):
        alert = ctk.CTkToplevel(frame)
        alert.title("경고")
        alert.geometry("300x150")

        alert_label = ctk.CTkLabel(alert, text=message, font=description_font)
        alert_label.pack(pady=20)

        close_button = ctk.CTkButton(alert, text="닫기", command=alert.destroy)
        close_button.pack(pady=20)

        alert.transient(frame)
        alert.grab_set()
        alert.lift()
        alert.attributes('-topmost', True)
        alert.resizable(False, False)

        parent_window = frame.winfo_toplevel()
        window_width = alert.winfo_width()
        window_height = alert.winfo_height()
        screen_width = parent_window.winfo_screenwidth()
        screen_height = parent_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        alert.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 이메일 치고 엔터 누르면 회원가입 되게
    entry_email.bind('<Return>', signup)

    # 회원가입 버튼 생성
    signup_button = ctk.CTkButton(frame, text="회원가입", command=signup, font=description_font)
    signup_button.pack(pady=20, padx=60)

    # 로그인 페이지로 돌아가는 링크 버튼 생성
    login_link = ctk.CTkButton(frame, text="로그인 페이지로 돌아가기", fg_color="transparent", text_color="#0487f9", hover_color="#E0E0E0", command=lambda: show_frame('login'), font=description_font)
    login_link.pack(pady=10, padx=60)

# 필요 할 시 이 코드를 사용하여 창을 개별적으로 불러냄.
# frame = ctk.CTkFrame(root)
# create_signup_frame(frame, show_frame)
# frame.pack(fill="both", expand=True)
