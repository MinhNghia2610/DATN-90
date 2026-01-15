import tkinter as tk
from ui.theme import *

class MicMeter(tk.Canvas):
    def __init__(self, parent):
        super().__init__(
            parent, width=420, height=60,
            bg=BG, highlightthickness=0
        )
        self.bars = []
        for i in range(20):
            bar = self.create_rectangle(
                10 + i*20, 40,
                20 + i*20, 40,
                fill=NEON, width=0
            )
            self.bars.append(bar)

    def update_level(self, level):
        level = min(max(level, 0), 1)
        for i, bar in enumerate(self.bars):
            height = level * 40 * (i % 5 + 1) / 5
            self.coords(
                bar,
                10 + i*20, 40 - height,
                20 + i*20, 40
            )
