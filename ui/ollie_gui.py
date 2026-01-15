import tkinter as tk
from ui.theme import *
from ui.mic_meter import MicMeter

class OLLIEUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OLLIE – AI Assistant")
        self.root.geometry("540x460")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        # ===== TITLE =====
        self.title = tk.Label(
            self.root,
            text="O L L I E",
            fg=NEON,
            bg=BG,
            font=FONT_TITLE
        )
        self.title.pack(pady=8)

        # ===== STATUS =====
        self.status = tk.Label(
            self.root,
            text="SYSTEM IDLE",
            fg=NEON_SOFT,
            bg=BG,
            font=FONT_MAIN
        )
        self.status.pack()

        # ===== MIC =====
        self.mic = MicMeter(self.root)
        self.mic.pack(pady=12)

        # ===== LOG =====
        self.log = tk.Text(
            self.root,
            bg=PANEL,
            fg=TEXT,
            font=FONT_MAIN,
            height=12,
            insertbackground=TEXT,
            bd=0,
            padx=10,
            pady=10
        )
        self.log.pack(fill="both", padx=12, pady=10)
        self.log.config(state="disabled")

    # ===== STATES =====
    def ready(self):
        self.set_state("🎤 READY")

    def listening(self):
        self.set_state("🎧 LISTENING")

    def thinking(self):
        self.set_state("🤖 THINKING")

    def speaking(self):
        self.set_state("🔊 SPEAKING")

    def set_state(self, text):
        self.status.config(text=text)
        self.root.update_idletasks()

    # ===== LOG =====
    def log_text(self, text):
        self.log.config(state="normal")
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

    def update_mic(self, level):
        self.mic.update_level(level)
        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()
