import os

class Player:
    def play(self, path):
        os.system(f"afplay {path}")
