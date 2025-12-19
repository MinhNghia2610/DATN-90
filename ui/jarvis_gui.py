# ui/jarvis_gui.py
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
import time
import os

class JarvisGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("J.A.R.V.I.S Assistant")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        icon_path = "assets/icon.ico"
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.running = False

        self._build_ui()

    def _build_ui(self):
        # ===== TITLE =====
        title = tk.Label(
            self.root,
            text="J.A.R.V.I.S",
            font=("Consolas", 22, "bold"),
            fg="#00ffe1"
        )
        title.pack(pady=10)

        # ===== STATUS =====
        self.status_label = tk.Label(
            self.root,
            text="Status: Idle",
            font=("Consolas", 12),
            fg="yellow"
        )
        self.status_label.pack()

        # ===== LOG AREA =====
        self.log_box = ScrolledText(
            self.root,
            width=70,
            height=15,
            bg="black",
            fg="#00ff99",
            font=("Consolas", 10)
        )
        self.log_box.pack(pady=10)
        self.log("Jarvis GUI initialized.")

        # ===== BUTTONS =====
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        self.start_btn = tk.Button(
            btn_frame,
            text="▶ Start",
            width=12,
            command=self.start_jarvis
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(
            btn_frame,
            text="■ Stop",
            width=12,
            command=self.stop_jarvis,
            state=tk.DISABLED
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

    # ===== LOG FUNCTION =====
    def log(self, message):
        timestamp = time.strftime("[%H:%M:%S] ")
        self.log_box.insert(tk.END, timestamp + message + "\n")
        self.log_box.see(tk.END)

        with open("logs/jarvis.log", "a", encoding="utf-8") as f:
            f.write(timestamp + message + "\n")

    # ===== CONTROL =====
    def start_jarvis(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Listening...", fg="#00ff00")
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self.log("Jarvis started.")

            Thread(target=self._fake_listener, daemon=True).start()

    def stop_jarvis(self):
        self.running = False
        self.status_label.config(text="Status: Stopped", fg="red")
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.log("Jarvis stopped.")

    # ===== PLACEHOLDER AI LOOP =====
    def _fake_listener(self):
        while self.running:
            time.sleep(3)
            self.log("🎧 Waiting for wake word: 'Quan Gia'...")

    def run(self):
        self.root.mainloop()
