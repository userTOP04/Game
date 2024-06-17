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
        self.window['padx'] = 20
        self.window['pady'] = 20
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        self.font_size = min(
            self.window.winfo_screenwidth(),
            self.window.winfo_screenheight()
        ) // 50
        self.window.option_add('*Font', ('Impact', self.font_size))

        self.image_size = self.window.winfo_screenwidth() // 3

        self.img_dict = dict()

        self.player = Player('Vasia Python', 'Player.png', 1, 100, 0, Weapon('Клавиатура', 2))
        self.enemy = Player('A-19', 'A-19.png', 1, 100, 0)

        self.player_frame = tk.Frame(self.window)
        self.player_frame.pack(side='left')

        self.combat_frame = tk.Frame(self.window)
        self.combat_frame.pack(side='left', expand=True, fill='both')
        self.combat_masseges = tk.Listbox(self.combat_frame)
        self.combat_masseges.pack(expand=True, fill='both')
        self.button = tk.Button(self.combat_frame, text='атака', command=self.attack)
        self.button.pack()

        self.enemy_frame = tk.Frame(self.window)
        self.enemy_frame.pack(side='left')

        self.redraw_hero_widgets(self.player, self.player_frame)
        self.redraw_hero_widgets(self.enemy, self.enemy_frame)

        self.window.mainloop()

    def attack(self) -> None:
        self.combat_turn(self.player, self.enemy)
        self.combat_turn(self.enemy, self.player)    
        self.redraw_hero_widgets(self.player, self.player_frame)
        self.redraw_hero_widgets(self.enemy, self.enemy_frame)

    def combat_turn(self, attacker, defender) -> None:
        if attacker.hp <= 0:
            return
        if defender.hp <= 0:
            text = f'{attacker.name} убил {defender.name}'
            self.combat_masseges.insert(tk.END, text)
            text = f'{attacker.name} победил в бою'
            self.combat_masseges.insert(tk.END, text)
            self.battle_results(attacker)
            return
        defender.hp -= attacker.attack
        text = f'{attacker.name} ударил {defender.name} на {attacker.attack}'
        self.combat_masseges.insert(tk.END, text)

    def redraw_hero_widgets(self, hero, frame) -> None:
        for widget in frame.winfo_children():
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

    def battle_results(self, winner) -> None:
        winner.hp += 50
        winner.xp += 20
        text = f'{winner.name} получил 50 жизней и 20 опыта'
        self.combat_masseges.insert(tk.END, text)
        self.redraw_hero_widgets(self.player, self.player_frame)
        self.redraw_hero_widgets(self.enemy, self.enemy_frame)
        self.button.destroy()



    
Game()
