from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Đường dẫn đến tập tin hình ảnh
image_paths = {
    'Búa': 'bua.png',
    'Bao': 'bao.png',
    'Kéo': 'keo.png'
}

choices_dict = {
    'Búa': 'Kéo',
    'Bao': 'Búa',
    'Kéo': 'Bao'
}

history = []

def determine_winner(player1_choice, computer_choice):
    if player1_choice == computer_choice:
        return "Kết quả: Hòa!"
    elif choices_dict[player1_choice] == computer_choice:
        return "Kết quả: Người chơi thắng!"
    else:
        return "Kết quả: Máy thắng!"

def minimax(board, depth, maximizing_player):
    if depth == 0:
        return None, 0  

    choices = list(choices_dict.keys())

    if maximizing_player:
        best_score = float('-inf')
        best_choice = None
        for choice in choices:
            score = minimax(board, depth - 1, False)[1]
            if score > best_score:
                best_score = score
                best_choice = choice
        return best_choice, best_score
    else:
        best_score = float('inf')
        best_choice = None
        for choice in choices:
            score = minimax(board, depth - 1, True)[1]
            if score < best_score:
                best_score = score
                best_choice = choice
        return best_choice, best_score

def get_computer_choice():
    return random.choice(list(choices_dict.keys()))

def play_game():
    player1_choice = player1_var.get()
    computer_choice = get_computer_choice()

    result = determine_winner(player1_choice, computer_choice)
    history.insert(0,f"Lượt chơi thứ {len(history) + 1}:\nNgười chơi chọn: {player1_choice} và Máy chọn: {computer_choice} \n=> {result}")
    messagebox.showinfo("Result", f"Lựa chọn của người chơi: {player1_choice}\nLựa chọn của máy: {computer_choice}\n{result}")

    history_text.config(state=NORMAL)
    history_text.delete(1.0, END)
    history_text.insert(END, "\n".join(history))
    history_text.config(state=DISABLED)

    reset_choices()

def reset_choices():
    player1_var.set("Búa")

# Code giao diện
root = Tk()
root.title("Búa Bao Kéo")

frame = Frame(root, bg="lightgreen")
frame.pack(pady=10)

Label(frame, text="Lựa chọn của người chơi:", bg="lightgreen", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3)

player1_var = StringVar()
player1_var.set("Búa")

# Tải ảnh và tạo đối tượng
image_dict = {choice: ImageTk.PhotoImage(Image.open(image_paths[choice]).resize((50, 50))) for choice in choices_dict.keys()}

for col, choice in enumerate(choices_dict.keys()):
    Radiobutton(
        frame,
        image=image_dict[choice],
        variable=player1_var,
        value=choice,
        bg="lightgreen",
        activebackground="lightgreen",
        selectcolor="lightgreen"
    ).grid(row=1, column=col, padx=15)

history_button = Button(frame, text="Bắt đầu chơi", command=play_game, bg="lightgreen", activebackground="lightgreen",
                        font=("Arial", 14, "bold"))
history_button.grid(row=2, column=0, columnspan=3, pady=10)

history_text = Text(root, width=50, height=20, bg="lightyellow", fg="darkblue", insertbackground="darkblue")
history_text.pack(pady=10)

root.config(bg="lightgray")
root.mainloop()

