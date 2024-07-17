import tkinter as tk
from tkinter import font

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Frame Recorder")
root.geometry("600x300")
root.configure(bg='#DA70D6')  # Màu nền tùy chỉnh

# Hàm xử lý sự kiện
def pause():
    status_label.config(text="Recording Paused")

def start():    
    status_label.config(text="Recording Started")

def end():
    status_label.config(text="Recording Ended")

# Nhãn tiêu đề
title_label = tk.Label(root, text="Frame Recorder", font=("Helvetica", 24), bg='#DA70D6')
title_label.pack(pady=10)

# Khung cho phần nhập FPS
fps_frame = tk.Frame(root, bg='#DA70D6')
fps_frame.pack(pady=20)

fps_label = tk.Label(fps_frame, text="create an", font=("Helvetica", 14), bg='#DA70D6')
fps_label.pack(side=tk.LEFT)

fps_entry = tk.Entry(fps_frame, width=10, font=("Helvetica", 14))
fps_entry.pack(side=tk.LEFT, padx=5)

fps_text_label = tk.Label(fps_frame, text="fps video", font=("Helvetica", 14), bg='#DA70D6')
fps_text_label.pack(side=tk.LEFT)

# Khung cho các nút điều khiển
button_frame = tk.Frame(root, bg='#DA70D6')
button_frame.pack(pady=20)

pause_button = tk.Button(button_frame, text="Pause", font=("Helvetica", 14), command=pause)
pause_button.pack(side=tk.LEFT, padx=10)

start_button = tk.Button(button_frame, text="Start", font=("Helvetica", 14), command=start)
start_button.pack(side=tk.LEFT, padx=10)

end_button = tk.Button(button_frame, text="End", font=("Helvetica", 14), command=end)
end_button.pack(side=tk.LEFT, padx=10)

# Nhãn trạng thái
status_label = tk.Label(root, text="Recording Paused", font=("Helvetica", 14), bg='#DA70D6')
status_label.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
