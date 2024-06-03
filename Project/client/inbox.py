import customtkinter as ctk
import socketio
import requests

# SocketIO 클라이언트 생성
sio = socketio.Client()
username = None  # 전역 변수로 username 선언
user_fullname = None  # 전역 변수로 사용자 이름 선언
friends = []  # 친구 목록을 저장할 리스트
inbox_window = None  # 전역 변수로 inbox_window 선언
description_font = None  # 전역 변수로 description_font 선언
frame = None  # 전역 변수로 frame 선언
app_running = True  # 애플리케이션 상태 관리 변수

# 서버 주소 설정
SERVER_URL = "http://61.255.152.191:5000"  # 서버의 주소와 포트를 설정하세요

# SocketIO 이벤트 핸들러
@sio.event
def connect():
    print("서버에 연결되었습니다.")
    sio.emit("join", {"username": username})

@sio.event
def connect_error(data):
    print("서버 연결 실패:", data)

@sio.event
def disconnect():
    print("서버와의 연결이 끊어졌습니다.")

# 애플리케이션 종료를 위한 함수
def on_closing():
    global app_running
    app_running = False
    if inbox_window:
        inbox_window.destroy()

# 경고 메시지를 표시하는 함수
def show_alert(message):
    global frame  # 전역 변수 사용
    if app_running:  # 애플리케이션이 실행 중일 때만 실행
        try:
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
        except Exception as e:
            print(f"Alert 창을 생성하는 동안 오류 발생: {e}")

# 사용자 정의 입력 대화 상자
def custom_input_dialog(title, prompt):
    dialog = ctk.CTkToplevel(frame)
    dialog.title(title)
    dialog.geometry("300x150")

    label = ctk.CTkLabel(dialog, text=prompt, font=description_font)
    label.pack(pady=20)

    entry = ctk.CTkEntry(dialog)
    entry.pack(pady=5)

    def on_submit():
        global input_result
        input_result = entry.get()
        dialog.destroy()

    submit_button = ctk.CTkButton(dialog, text="확인", command=on_submit)
    submit_button.pack(pady=10)

    dialog.transient(frame)
    dialog.grab_set()
    dialog.lift()
    dialog.attributes('-topmost', True)
    dialog.resizable(False, False)

    dialog.update_idletasks()
    parent_window = frame.winfo_toplevel()
    window_width = dialog.winfo_width()
    window_height = dialog.winfo_height()
    screen_width = parent_window.winfo_screenwidth()
    screen_height = parent_window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

    dialog.wait_window()
    return input_result

# 메일함 창 생성 함수
def create_inbox_window():
    global inbox_window, frame, description_font  # 전역 변수 사용
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light")
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue")

    inbox_window = ctk.CTk()
    inbox_window.title("메일함 - 전주대학교 메일")
    inbox_window.geometry("800x600")
    inbox_window.protocol("WM_DELETE_WINDOW", on_closing)
    inbox_window.resizable(False, False)

    # Header
    header_frame = ctk.CTkFrame(inbox_window, height=50, fg_color="#78aedd")  # rgba(120, 174, 221, 0.9)
    header_frame.pack(side="top", fill="x")
    header_label = ctk.CTkLabel(header_frame, text=f"반갑습니다 {user_fullname}!", text_color="white", font=ctk.CTkFont(size=20, weight="bold"))
    header_label.pack(pady=10)

    # Main Content
    main_frame = ctk.CTkFrame(inbox_window)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)
    frame = main_frame

    # Sidebar
    sidebar_frame = ctk.CTkFrame(main_frame, width=200, fg_color="#f7f7f7")  # rgba(247, 247, 247, 0.9)
    sidebar_frame.pack(side="left", fill="y", padx=(0, 10))

    menu_label = ctk.CTkLabel(sidebar_frame, text="Friends", font=ctk.CTkFont(size=15))
    menu_label.pack(pady=10)

    # Friend List
    global friend_listbox
    friend_listbox = ctk.CTkTextbox(sidebar_frame, state='disabled')
    friend_listbox.pack(expand=True, fill="both", padx=10, pady=10)

    # Add Friend Button
    add_friend_button = ctk.CTkButton(sidebar_frame, text="친구 추가", command=add_friend)
    add_friend_button.pack(pady=5, fill="x")

    # Chat Content
    content_frame = ctk.CTkFrame(main_frame, fg_color="#ffffff")  # rgba(255, 255, 255, 0.9)
    content_frame.pack(expand=True, fill="both")

    global chat_listbox
    chat_listbox = ctk.CTkTextbox(content_frame, state='disabled')
    chat_listbox.pack(expand=True, fill="both", padx=10, pady=10)

    # Message Entry
    global message_entry
    message_entry = ctk.CTkEntry(content_frame)
    message_entry.pack(side="left", fill="x", padx=(10, 0), pady=10, expand=True)

    send_button = ctk.CTkButton(content_frame, text="전송", command=send_message)
    send_button.pack(side="right", padx=10, pady=10)

    # 서버에서 친구 목록을 가져오는 함수 호출
    load_friends()

    inbox_window.mainloop()

def add_friend():
    friend_name = custom_input_dialog("친구 추가", "친구의 사용자 이름을 입력하세요:")
    if friend_name:
        response = requests.post(f"{SERVER_URL}/add_friend", json={"username": username, "friend": friend_name})
        if response.status_code == 200:
            friends.append(friend_name)
            update_friend_list()
        else:
            show_alert("친구 추가에 실패했습니다.")

def send_message():
    message = message_entry.get()
    if message:
        if sio.connected:
            sio.emit("message", {"username": username, "message": message})
            message_entry.delete(0, 'end')
        else:
            show_alert("서버에 연결되어 있지 않습니다.")

def load_friends():
    response = requests.get(f"{SERVER_URL}/get_friends", params={"username": username})
    if response.status_code == 200:
        global friends
        friends = response.json().get("friends", [])
        update_friend_list()
    else:
        show_alert("친구 목록을 불러오는데 실패했습니다.")

def update_friend_list():
    if app_running:
        friend_listbox.configure(state='normal')
        friend_listbox.delete("1.0", "end")
        for friend in friends:
            friend_listbox.insert("end", friend + "\\n")
        friend_listbox.configure(state='disabled')

# 서버와의 연결 시도
try:
    sio.connect(SERVER_URL)
except Exception as e:
    print(f"서버 연결 중 오류 발생: {e}")

# 메일함 창 생성
if __name__ == '__main__':
    login_response = requests.post(f'{SERVER_URL}/login', json={'student_staff_number': 'your_number', 'password': 'your_password'})
    if login_response.json().get("status") == "success":
        username = login_response.json().get("student_staff_number")
        user_fullname = login_response.json().get("username")
        create_inbox_window()
    else:
        print("로그인 실패!")
