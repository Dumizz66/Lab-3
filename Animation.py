import tkinter as tk
from tkinter import messagebox
import random
import string
import pygame
from itertools import cycle


INTERVAL_MIN = 10
INTERVAL_MAX = 15


def setup_music():
    pygame.mixer.init()
    pygame.mixer.music.load("Csgomusic.mp3")
    pygame.mixer.music.play(-1)

def calculate_weight(char):
    if char.isdigit():
        return int(char)
    else:
        return ord(char) - ord('A') + 1


def generate_block(length, min_avg, max_avg):
    while True:
        block = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        weights = [calculate_weight(c) for c in block]
        avg_weight = sum(weights) / length
        if min_avg <= avg_weight <= max_avg:
            return block


def generate_key():
    block1 = generate_block(5, INTERVAL_MIN, INTERVAL_MAX)
    block2 = generate_block(4, INTERVAL_MIN, INTERVAL_MAX)
    block3 = generate_block(4, INTERVAL_MIN, INTERVAL_MAX)
    key = f"{block1}-{block2}-{block3}"
    key_label.config(text=key)


def animate_button():
    current_color = next(button_colors)
    generate_button.config(bg=current_color)
    root.after(500, animate_button)


root = tk.Tk()
root.title("Key Generator")
root.geometry("800x600")


bg_image = tk.PhotoImage(file="Csgo2.jpg")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


key_label = tk.Label(root, text="Ваш ключ появится здесь", font=("Consolas", 16), bg="white", fg="black", width=40)
key_label.pack(pady=50)


generate_button = tk.Button(root, text="Сгенерировать ключ", font=("Arial", 14), command=generate_key)
generate_button.pack(pady=20)


button_colors = cycle(["#ff9999", "#99ccff", "#99ff99", "#ffcc99"])


setup_music()
animate_button()


root.mainloop()
