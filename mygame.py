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

        self.img_dict = dict()

        self.player_frame = tk.Frame(self.window)
        self.player_frame.pack(side='left')

        self.combat_frame = tk.Frame(self.window)
        self.combat_frame.pack(side='left', expand=True)
        self.combat_masseges = tk.Listbox(self.combat_frame)
        self.combat_masseges.pack(ipadx=50)
        tk.Button(self.combat_frame, text='атака', command=self.attack).pack()
        
        self.enemy_frame = tk.Frame(self.window)
        self.enemy_frame.pack(side='left')

        self.redraw_hero_widgets(self.player, self.player_frame)
        self.redraw_hero_widgets(self.enemy, self.enemy_frame)

        self.window.mainloop()

    def attack(self) -> None:
        self.player.hp -= 10
        self.enemy.hp -= 10
        self.redraw_hero_widgets(self.player, self.player_frame)
        self.redraw_hero_widgets(self.enemy, self.enemy_frame)

    def redraw_hero_widgets(self, hero, frame) -> None:
        for widget in self.player_frame.winfo_children():
            widget.destroy() 
        image = Image.open(self.img_dir / hero.image)
        image = image.resize((self.image_size, self.image_size))
        self.img_dict[hero.name] = ImageTk.PhotoImage(image=image)
        tk.Label(frame, image=self.img_dict[hero.name]).pack()
        tk.Label(frame, text=hero.name).pack()
        tk.Label(frame, text=f'жизни: {hero.hp}').pack()
        tk.Label(frame, text=f'уровень: {hero.level}').pack()
        tk.Label(frame, text=f'опыт: {hero.xp}').pack()
        tk.Label(frame, text=f'атака: {hero.attack}').pack()
        tk.Label(frame, text=f'защита: {hero.defence}').pack()
        tk.Label(frame, text=f'оружие: {hero.weapon}').pack()


    
Game()
