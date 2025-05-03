#import tkinter as tk
from flasker import app
from flask import render_template

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

class TimerApp:
    def __init__(self, root, duration):
        self.root = root
        self.duration = duration  # タイマー時間（秒）
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        self.initial_radius = 100  # 円の半径
        self.center_x, self.center_y = 150, 150  # 円の中心座標

        # 円の輪郭を描画
        self.circle = self.canvas.create_arc(
            self.center_x - self.initial_radius,
            self.center_y - self.initial_radius,
            self.center_x + self.initial_radius,
            self.center_y + self.initial_radius,
            start=90, extent=360, outline="blue", width=5
        )

        self.update_circle(self.duration)

    def update_circle(self, remaining_time):
        if remaining_time >= 0:
            scale_factor = remaining_time / self.duration
            new_extent = max(0, 360 * scale_factor)  # 線の長さを短縮

            self.canvas.itemconfig(self.circle, extent=new_extent)  # 線の長さを更新

            self.root.after(1000, self.update_circle, remaining_time - 1)

def countdown(count, timer_app):
    label['text'] = count
    if count > 0:
        root.after(1000, countdown, count-1, timer_app)
        timer_app.update_circle(count)

def start_timer():
    try:
        duration = int(entry.get())  # ユーザー入力を取得
        timer_app = TimerApp(root, duration)  # インスタンスを作成
        countdown(duration, timer_app)  # タイマー開始
    except ValueError:
        label['text'] = "数字を入力してください！"

def center_window(root, width, height):
    # 画面の幅と高さを取得
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # ウィンドウの位置を計算
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # 位置,サイズ
    root.geometry(f"{width}x{height}+{x}+{y}")
root = tk.Tk()
root.title("タイマーアプリ")
center_window(root, 270, 600)  # 幅、高さ


entry = tk.Entry(root, width=10)
entry.pack()

start_button = tk.Button(root, text="スタート", command=start_timer)
start_button.pack()

label = tk.Label(root, text="", font=("Helvetica", 48))
label.pack()

root.mainloop()
