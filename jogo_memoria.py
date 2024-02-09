import random
import tkinter as tk

# Define as cores para as cartas
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'red', 'blue', 'green', 'yellow', 'purple', 'orange']

# Embaralha as cores
random.shuffle(colors)

# Cria uma janela Tkinter
window = tk.Tk()
window.title("Jogo da Memória")

# Cria uma lista para armazenar os botões das cartas
card_buttons = []

# Cria uma lista para armazenar as cartas viradas
flipped_cards = []

# Cria uma função para lidar com os cliques nas cartas
def card_click(index):
    """
    Função que é chamada quando uma carta é clicada.

    Parâmetros:
    - index: O índice da carta clicada.

    Retorna:
    - None
    """

    # Verifica se a carta já está virada ou já foi combinada
    if index in flipped_cards:
        return

    # Verifica se já existem duas cartas viradas
    if len(flipped_cards) == 2:
        return

    # Vira a carta
    button = card_buttons[index]
    button.config(bg=colors[index])

    # Adiciona a carta à lista de cartas viradas
    flipped_cards.append(index)

    # Verifica se duas cartas estão viradas
    if len(flipped_cards) == 2:
        # Obtém os índices das cartas viradas
        index1, index2 = flipped_cards

        # Verifica se as cartas são iguais
        if colors[index1] == colors[index2]:
            # Mantém as cartas viradas
            flipped_cards.clear()
            # Verifica se todas as cartas foram encontradas
            if len(flipped_cards) == len(colors):
                # Exibe uma mensagem de parabéns
                tk.messagebox.showinfo("Parabéns!", "Você conseguiu!")
        else:
            # Atrasa o retorno das cartas à posição original
            window.after(1000, flip_back_cards)

def flip_back_cards():
    # Volta as cartas para a posição original
    index1, index2 = flipped_cards
    button1 = card_buttons[index1]
    button2 = card_buttons[index2]
    button1.config(bg='white')
    button2.config(bg='white')

    # Remove as cartas da lista de cartas viradas
    flipped_cards.clear()

def restart_game():
    # Embaralha as cores
    random.shuffle(colors)

    # Volta as cartas para a posição original
    for button in card_buttons:
        button.config(bg='white')

    # Limpa a lista de cartas viradas
    flipped_cards.clear()

restart_button = tk.Button(window, text="Reiniciar", command=restart_game)
restart_button.grid(row=len(colors) // 4 + 1, columnspan=4)

# Cria os botões das cartas e os adiciona à janela
for i, color in enumerate(colors):
    button = tk.Button(window, bg='white', width=10, height=5,
                       command=lambda index=i: card_click(index))
    button.grid(row=i // 4, column=i % 4)
    card_buttons.append(button)

# Inicia o loop de eventos do Tkinter
window.mainloop()
