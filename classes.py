from time import sleep



class Character():
    def __init__(self, name, hp, weapon, behavior, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.behavior = behavior
        self.armor = armor

    def deal_hit(self, enemy):
        enemy.hp -= self.weapon.damage * ((100 - enemy.armor.resist) / 100) 
        if enemy.hp < 0:
            enemy.hp = 0
        print(f'{self.name} нанес урон {enemy.name} равный {self.weapon.damage} \nтеперь {enemy.name} имеет {enemy.hp}')

class Player(Character):
    def __init__(self, name, hp, weapon, behavior, armor, money, inventory = []):
        super().__init__(name, hp, weapon, behavior, armor)
        self.money = money
        self.inventory = inventory
    
    def show_inventory(self):
        counter = 1
        print('Инвентарь игрока:')
        for i in self.inventory:
            print(f'{counter}  -  {i.name}')
            counter += 1
        print(f'\nЭкипировка игрока: \n оружие = {self.weapon.name}\n броня = {self.armor.name}')
        

    def player_manager(self):
        while True:
            self.show_inventory()
            choose = int(input(f'1 - заменить предмет\n2 - выход\n'))
            if choose == 1:
                a = int(input(f'номер предмета:')) -1
                self.change(a)
            elif choose == 2:
                break
            else:
                pass

    def change(self, item):
        while True:
            if type(self.inventory[item]) == Weapon:
                self.inventory.append(self.weapon)
                self.weapon = self.inventory[item]
                self.inventory.pop(item)
                break
            elif type(self.inventory[item]) == Armor:
                self.inventory.append(self.armor)
                self.armor = self.inventory[item]
                self.inventory.pop(item)
                break
            elif type(self.inventory[item]) == Heal_potion:
                self.hp += item.hp
                self.inventory.pop(item)
            else:
                pass
        

class Weapon():
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def show_characteristics(self):
        return f'{self.name},  cost = {self.cost}, damage = {self.damage}'
    

class Armor():
    def __init__(self, name, resist, cost, hp):
        self.name = name
        self.resist = resist
        self.cost = cost
        self.hp = hp
    
    def show_characteristics(self):
        return f'{self.name},  cost = {self.cost}, resist = {self.resist}, hp = {self.hp}'

class Heal_potion():
    def __init__(self, name, hp, cost):
        self.name = name
        self.hp = hp
        self.cost = cost

class Heal_potion_small(Heal_potion):
    def __init__(self, name = 'Heal potion small', hp = 25, cost = 20):
        super().__init__(name, hp, cost)

class Heal_potion_medium(Heal_potion):
    def __init__(self, name = 'Heal potion medium', hp = 75, cost = 60):
        super().__init__(name, hp, cost)

class Heal_potion_big(Heal_potion): 
    def __init__(self, name = 'Heal potion big', hp = 150, cost = 120):
        super().__init__(name, hp, cost)

class Room():
    def __init__(self, enemy, money,):
        self.enemy = enemy
        self.money = money

    def enter_room(self, player, time_nosleep):
        print(f'{player.name} вошел в комнату\nв комнате {self.enemy.name}')
        return self.fight(player, time_nosleep)

    def fight(self, player: Player, time_nosleep):
        
        enemy = self.enemy
        while player.hp > 0 and enemy.hp > 0:
            player.deal_hit(enemy)
            sleep(3 * (time_nosleep/100))
            if enemy.hp > 0:
                enemy.deal_hit(player)
                sleep(3 * (time_nosleep/100))
        if player.hp  <= 0:
            return False
        elif enemy.hp <= 0:
            player.money += self.money
            print(f'{enemy.name} повержен!\nВ комнате было {self.money} монет.\nТеперь у {player.name} имеет {player.money}')
            sleep(3 * (time_nosleep/100))
            player.inventory.append(enemy.weapon)
            print(f'Еще теперь у вас есть {enemy.weapon.name} за {enemy.weapon.cost}.')
            return True

        

class Dungeon():
    def __init__(self, rooms, name):
        self.rooms = rooms
        self.name = name
        self.counter = 0
        self.passed = False
    
    def next_room(self, player, time_nosleep):
        if self.counter < len(self.rooms):
            is_alive = self.rooms[self.counter].enter_room(player, time_nosleep)
            self.counter += 1
            return is_alive
        else:
            self.passed = True

class Trader():
    def __init__(self, trader_inventory, trader_money, heal_potion_small, heal_potion_medium, heal_potion_big):
        self.trader_inventory = trader_inventory
        self.trader_money = trader_money
        self.heal_potion_small = heal_potion_small
        self.heal_potion_medium = heal_potion_medium
        self.heal_potion_big = heal_potion_big


    def trader_manager(self,player):
        while True:
            self.show_inventory()
            action = input(f'1.продать\n2.купить\n3.выход\n')
            if action == '1':
                self.buy_item(player)
            elif action == '2':
                self.sell_item(player)
            elif action == '3':
                break
            

    def show_inventory(self):
        number_cicle = 0
        print(f'\nТорговец:')
        for i in self.trader_inventory:
            number_cicle += 1
            print(f'{number_cicle}. {i.show_characteristics()}')
        print(f'\n')

    def sell_item(self, player:Player):
        self.show_inventory()
        position = int(input()) - 1
        product = self.trader_inventory[position]
        if self.trader_money >= product.cost:
            self.trader_inventory.pop(position)
            player.inventory.append(product)
            player.money -= product.cost
            self.trader_money += product.cost
            self.show_inventory()
            player.show_inventory()
        else:
            print('У вас не хватает денег')

    def buy_item(self, player:Player):
        player.show_inventory()
        position = int(input()) - 1
        product = player.inventory[position]
        if self.trader_money >= product.cost:
            player.inventory.pop(position)
            self.trader_inventory.append(product)
            self.trader_money -= product.cost
            player.money += product.cost
            self.show_inventory()
            player.show_inventory()
        else:
            print('У торговца не хватает денег')
            

    def hpreg(self):
        small = 0
        medium = 0
        big = 0
        heals = [small, medium, big]
        for i in self.trader_inventory:
            pass