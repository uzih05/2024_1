import customtkinter as ctk
import requests
import inbox

def create_login_frame(frame, show_frame):
    title_font = ctk.CTkFont(family="NanumBarunpenR", size=24, weight="bold")
    description_font = ctk.CTkFont(family="NanumBarunpenR", size=16, weight="bold")

    # 제목 라벨 생성
    title_label = ctk.CTkLabel(frame, text="전주대학교 메일", font=title_font)
    title_label.pack(pady=20, padx=10)

    # 설명 라벨 생성
    description_label = ctk.CTkLabel(frame, text="로그인하세요", font=description_font)
    description_label.pack(pady=10, padx=10)

    # 학번/교직원 번호 입력 필드 생성
    entry_number = ctk.CTkEntry(frame, placeholder_text="학번 또는 교직원 번호", font=description_font, width=200)
    entry_number.pack(pady=10, padx=10)

    entry_password = ctk.CTkEntry(frame, placeholder_text="비밀번호", show="*", font=description_font, width=200)
    entry_password.pack(pady=10, padx=10)

    # 로그인 함수
    def login(event=None):
        data = {
            'student_staff_number': entry_number.get(),
            'password': entry_password.get()
        }
        response = requests.post('http://61.255.152.191:5000/login', json=data)
        if response.json().get("status") == "success":
            frame.winfo_toplevel().destroy()
            inbox.username = data['student_staff_number']
            inbox.create_inbox_window()
        else:
            show_alert("로그인 실패!")

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

        alert.update_idletasks()
        parent_window = frame.winfo_toplevel()
        window_width = alert.winfo_width()
        window_height = alert.winfo_height()
        screen_width = parent_window.winfo_screenwidth()
        screen_height = parent_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        alert.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # 비밀번호 치고 엔터 누르면 로그인
    entry_password.bind('<Return>', login)

    # 로그인 버튼 생성
    login_button = ctk.CTkButton(frame, text="로그인", command=login, font=description_font)
    login_button.pack(pady=20, padx=10)

    # 링크들을 담을 프레임 생성
    links_frame = ctk.CTkFrame(frame, fg_color="transparent")
    links_frame.pack(pady=10, padx=10)

    # 회원가입 링크 버튼 생성
    signup_link = ctk.CTkButton(links_frame, text="회원가입", fg_color="transparent", text_color="#0487f9", hover_color="#E0E0E0", command=lambda: show_frame('signup'), font=description_font)
    signup_link.pack(side="left", padx=5)

    # 비밀번호 찾기 링크 버튼 생성
    password_reset_link = ctk.CTkButton(links_frame, text="비밀번호 찾기", fg_color="transparent", text_color="#0487f9", hover_color="#E0E0E0", command=lambda: show_frame('password_reset'), font=description_font)
    password_reset_link.pack(side="left", padx=5)

if __name__ == '__main__':
    root = ctk.CTk()
    root.geometry("400x500")

    frame = ctk.CTkFrame(root)
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    create_login_frame(frame, lambda frame_name: print(f"Switch to {frame_name} frame"))

    root.mainloop()
