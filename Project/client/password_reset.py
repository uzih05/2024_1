import customtkinter as ctk
import requests
import re

def create_password_reset_frame(frame, show_frame):
    title_font = ctk.CTkFont(family="NanumBarunpenR", size=24, weight="bold")
    description_font = ctk.CTkFont(family="NanumBarunpenR", size=16, weight="bold")

    title_label = ctk.CTkLabel(frame, text="비밀번호 찾기", font=title_font)
    title_label.pack(pady=20, padx=60)

    description_label = ctk.CTkLabel(frame, text="이메일 주소를 입력하세요", font=description_font)
    description_label.pack(pady=10, padx=60)

    entry_email = ctk.CTkEntry(frame, placeholder_text="이메일 주소", font=description_font, width=200)
    entry_email.pack(pady=10, padx=60)

    def show_alert(message):
        alert = ctk.CTkToplevel(frame)
        alert.title("경고")
        alert.geometry("350x150")

        alert_label = ctk.CTkLabel(alert, text=message, font=description_font)
        alert_label.pack(pady=20)

        close_button = ctk.CTkButton(alert, text="닫기", command=alert.destroy)
        close_button.pack(pady=20)

        alert.transient(frame)
        alert.grab_set()
        alert.lift()
        alert.attributes('-topmost', True)
        alert.resizable(False, False)

        alert.update_idletasks()
        parent_window = frame.winfo_toplevel()
        window_width = alert.winfo_width()
        window_height = alert.winfo_height()
        screen_width = parent_window.winfo_screenwidth()
        screen_height = parent_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        alert.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def reset_password(event=None):
        email = entry_email.get()
        if not email:
            show_alert("이메일 주소를 입력하세요.")
            return
        
        # 특수문자 검사
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            show_alert("유효한 이메일 주소를 입력하세요.")
            return

        data = {'email': email}
        try:
            response = requests.post('http://61.255.152.191:5000/password_reset', json=data)
            response_data = response.json()
            print(response_data)  # 응답 데이터 출력하여 디버깅
            if response.status_code == 200:
                show_alert("비밀번호 재설정 링크가 이메일로 전송되었습니다.")
            else:
                error_detail = response.json().get("detail", "알 수 없는 오류가 발생했습니다.")
                if isinstance(error_detail, list):
                    error_messages = "\n".join([error.get('msg', '알 수 없는 오류가 발생했습니다.') for error in error_detail])
                    show_alert(error_messages)
                else:
                    show_alert(error_detail)
        except requests.RequestException as e:
            show_alert(f"요청 중 오류가 발생했습니다: {e}")

    # 이메일 치고 엔터 누르면 리셋버튼 눌리게
    entry_email.bind('<Return>', reset_password)

    reset_button = ctk.CTkButton(frame, text="비밀번호 받기", command=reset_password, font=description_font)
    reset_button.pack(pady=20, padx=60)

    back_to_login_link = ctk.CTkButton(frame, text="로그인 페이지로 돌아가기", fg_color="transparent", text_color="#0487f9", hover_color="#E0E0E0", command=lambda: show_frame('login'), font=description_font)
    back_to_login_link.pack(pady=10, padx=60)

# 예시: 이 코드를 호출하여 프레임을 생성합니다.
# frame = ctk.CTkFrame(root)
# create_password_reset_frame(frame, show_frame)
# frame.pack(fill="both", expand=True)
