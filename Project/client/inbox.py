import customtkinter as ctk
import socketio
import requests

class Inbox:
    def __init__(self, username, user_fullname):
        self.sio = socketio.Client()
        self.username = username
        self.user_fullname = user_fullname
        self.friends = []
        self.inbox_window = None
        self.description_font = ctk.CTkFont(size=15)
        self.frame = None
        self.app_running = True
        self.SERVER_URL = "http://61.255.152.191:5000"

        self.setup_socketio()
        
    def setup_socketio(self):
        self.sio.on('connect', self.on_connect)
        self.sio.on('connect_error', self.on_connect_error)
        self.sio.on('disconnect', self.on_disconnect)
        
        # 서버와의 연결 시도
        try:
            self.sio.connect(self.SERVER_URL)
        except Exception as e:
            print(f"서버 연결 중 오류 발생: {e}")
    
    def on_connect(self):
        print("서버에 연결되었습니다.")
        self.sio.emit("join", {"username": self.username})

    def on_connect_error(self, data):
        print("서버 연결 실패:", data)

    def on_disconnect(self):
        print("서버와의 연결이 끊어졌습니다.")

    def on_closing(self):
        self.app_running = False
        if self.inbox_window:
            self.inbox_window.destroy()

    def show_alert(self, message):
        if self.app_running:
            try:
                alert = ctk.CTkToplevel(self.frame)
                alert.title("경고")
                alert.geometry("300x150")

                alert_label = ctk.CTkLabel(alert, text=message, font=self.description_font)
                alert_label.pack(pady=20)

                close_button = ctk.CTkButton(alert, text="닫기", command=alert.destroy)
                close_button.pack(pady=20)

                alert.transient(self.frame)
                alert.grab_set()
                alert.lift()
                alert.attributes('-topmost', True)
                alert.resizable(False, False)

                alert.update_idletasks()
                parent_window = self.frame.winfo_toplevel()
                window_width = alert.winfo_width()
                window_height = alert.winfo_height()
                screen_width = parent_window.winfo_screenwidth()
                screen_height = parent_window.winfo_screenheight()
                x = (screen_width // 2) - (window_width // 2)
                y = (screen_height // 2) - (window_height // 2)
                alert.geometry(f"{window_width}x{window_height}+{x}+{y}")
            except Exception as e:
                print(f"Alert 창을 생성하는 동안 오류 발생: {e}")

    def custom_input_dialog(self, title, prompt):
        dialog = ctk.CTkToplevel(self.frame)
        dialog.title(title)
        dialog.geometry("300x150")

        label = ctk.CTkLabel(dialog, text=prompt, font=self.description_font)
        label.pack(pady=20)

        entry = ctk.CTkEntry(dialog)
        entry.pack(pady=5)

        def on_submit():
            self.input_result = entry.get()
            dialog.destroy()

        submit_button = ctk.CTkButton(dialog, text="확인", command=on_submit)
        submit_button.pack(pady=10)

        dialog.transient(self.frame)
        dialog.grab_set()
        dialog.lift()
        dialog.attributes('-topmost', True)
        dialog.resizable(False, False)

        dialog.update_idletasks()
        parent_window = self.frame.winfo_toplevel()
        window_width = dialog.winfo_width()
        window_height = dialog.winfo_height()
        screen_width = parent_window.winfo_screenwidth()
        screen_height = parent_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        dialog.wait_window()
        return self.input_result

    def create_inbox_window(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.inbox_window = ctk.CTk()
        self.inbox_window.title("메일함 - 전주대학교 메일")
        self.inbox_window.geometry("800x600")
        self.inbox_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.inbox_window.resizable(False, False)

        # Header
        header_frame = ctk.CTkFrame(self.inbox_window, height=50, fg_color="#78aedd")
        header_frame.pack(side="top", fill="x")
        header_label = ctk.CTkLabel(header_frame, text=f"반갑습니다 {self.user_fullname}!", text_color="white", font=ctk.CTkFont(size=20, weight="bold"))
        header_label.pack(pady=10)

        # Main Content
        main_frame = ctk.CTkFrame(self.inbox_window)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        self.frame = main_frame

        # Sidebar
        sidebar_frame = ctk.CTkFrame(main_frame, width=200, fg_color="#f7f7f7")
        sidebar_frame.pack(side="left", fill="y", padx=(0, 10))

        menu_label = ctk.CTkLabel(sidebar_frame, text="Friends", font=ctk.CTkFont(size=15))
        menu_label.pack(pady=10)

        # Friend List
        self.friend_listbox = ctk.CTkTextbox(sidebar_frame, state='disabled')
        self.friend_listbox.pack(expand=True, fill="both", padx=10, pady=10)

        # Add Friend Button
        add_friend_button = ctk.CTkButton(sidebar_frame, text="친구 추가", command=self.add_friend)
        add_friend_button.pack(pady=5, fill="x")

        # Chat Content
        content_frame = ctk.CTkFrame(main_frame, fg_color="#ffffff")
        content_frame.pack(expand=True, fill="both")

        self.chat_listbox = ctk.CTkTextbox(content_frame, state='disabled')
        self.chat_listbox.pack(expand=True, fill="both", padx=10, pady=10)

        # Message Entry
        self.message_entry = ctk.CTkEntry(content_frame)
        self.message_entry.pack(side="left", fill="x", padx=(10, 0), pady=10, expand=True)

        send_button = ctk.CTkButton(content_frame, text="전송", command=self.send_message)
        send_button.pack(side="right", padx=10, pady=10)

        self.load_friends()

        self.inbox_window.mainloop()

    def add_friend(self):
        friend_name = self.custom_input_dialog("친구 추가", "친구의 사용자 이름을 입력하세요:")
        if friend_name:
            response = requests.post(f"{self.SERVER_URL}/add_friend", json={"username": self.username, "friend": friend_name})
            if response.status_code == 200:
                self.friends.append(friend_name)
                self.update_friend_list()
            else:
                self.show_alert("친구 추가에 실패했습니다.")

    def send_message(self):
        message = self.message_entry.get()
        if message:
            if self.sio.connected:
                self.sio.emit("message", {"username": self.username, "message": message})
                self.message_entry.delete(0, 'end')
            else:
                self.show_alert("서버에 연결되어 있지 않습니다.")

    def load_friends(self):
        response = requests.get(f"{self.SERVER_URL}/get_friends", params={"username": self.username})
        if response.status_code == 200:
            self.friends = response.json().get("friends", [])
            self.update_friend_list()
        else:
            self.show_alert("친구 목록을 불러오는데 실패했습니다.")

    def update_friend_list(self):
        if self.app_running:
            self.friend_listbox.configure(state='normal')
            self.friend_listbox.delete("1.0", "end")
            for friend in self.friends:
                self.friend_listbox.insert("end", friend + "\n")
            self.friend_listbox.configure(state='disabled')
