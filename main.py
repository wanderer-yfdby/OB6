# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями
# с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки
# по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.


import random
import time

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name} на {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Computer"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        print("Битва героев")
        turn = 0

        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.")

            turn += 1
            time.sleep(3)

            if not self.player.is_alive():
                print(f"{self.player.name} проиграл! {self.computer.name} победил!")
            elif not self.computer.is_alive():
                print(f"{self.computer.name} проиграл! {self.player.name} победил!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()