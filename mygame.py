import tkinter as tk
from PIL import Image, ImageTk
import random
from pathlib import Path
from classes import Player, Weapon


class Game:
    def __init__(self) -> None:
        self.img_dir = Path(__file__).parent / 'img'
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        self.font_size = min(
            self.window.winfo_screenwidth(),
            self.window.winfo_screenheight()
        ) // 50
        self.window.option_add('*Font', ('Impact', self.font_size))

        self.image_size = self.window.winfo_screenwidth() // 3

        self.player = Player('Vasia Python', 'Player.png', 1, 100, 0)
        self.enemy = Player('A-19', 'A-19.png', 1, 100, 0)

        self.player_frame = tk.Frame(self.window)
        self.player_frame.pack(side='left')

        self.redraw_player_widgets()
		
        self.enemy_frame = tk.Frame(self.window)
        self.enemy_frame.pack(side='left')
        
        self.combat_frame = tk.Frame(self.window)
        self.combat_frame.pack(side='left')
        tk.Button(self.combat_frame, text='атака', command=self.attack).pack()

        self.window.mainloop()

    def attack(self) -> None:
        self.player.hp -= 10
        self.enemy.hp -= 10
        self.redraw_player_widgets()

    def redraw_player_widgets(self) -> None:
        for widget in self.player_frame.winfo_children():
            widget.destroy() 
        self.creation_widgets(self.player, self.player_frame)
        self.creation_widgets(self.enemy, self.enemy_frame)

    def creation_widgets(self, character, character_frame) -> None:
        self.character = character
        self.character_frame = character_frame
        image = Image.open(self.img_dir / self.character.image)
        image = image.resize((self.image_size, self.image_size))
        self.character_image_tk = ImageTk.PhotoImage(image=image)
        tk.Label(self.character_frame, image=self.character_image_tk).pack()
        tk.Label(self.character_frame, text=self.character.name).pack()
        tk.Label(self.character_frame, text=f'жизни: {self.character.hp}').pack()
        tk.Label(self.character_frame, text=f'уровень: {self.character.level}').pack()
        tk.Label(self.character_frame, text=f'опыт: {self.character.xp}').pack()
        tk.Label(self.character_frame, text=f'атака: {self.character.attack}').pack()
        tk.Label(self.character_frame, text=f'защита: {self.character.defence}').pack()
        tk.Label(self.character_frame, text=f'оружие: {self.character.weapon}').pack()

Game()
