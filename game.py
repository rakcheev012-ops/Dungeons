from classes import Character, Player, Armor, Weapon, Room, Dungeon, Trader, Heal_potion_small, Heal_potion_medium, Heal_potion_big
import time


baby_dragon_s_skin = Armor("baby dragon's skin",25 ,10 , 50)
none = Armor('none', 0, 0, 0)
dragon_s_skin = Armor("dragon's skin",25,10,50)
goblin_leather = Armor("Гоблинская кожаная броня", 10, 5, 20)
goblin_chainmail = Armor("Гоблинская кольчуга", 20, 10, 40)
hobgoblin_armor = Armor("Броня хобгоблина", 30, 15, 60)
goblin_shaman_robes = Armor("Одеяния гоблина-шамана", 15, 20, 35)
goblin_king_armor = Armor("Доспехи короля гоблинов", 50, 25, 100)
skeleton_bones = Armor("Костяная броня скелета", 15, 5, 25)
rusted_armor = Armor("Ржавые доспехи скелета", 25, 10, 45)
skeleton_knight_armor = Armor("Доспехи скелета-рыцаря", 40, 15, 75)
skeleton_mage_cloak = Armor("Плащ скелета-мага", 10, 25, 30)
skeleton_lich_robes = Armor("Одеяния скелета-лича", 35, 40, 65)
orc_hide = Armor("Орочья шкура", 30, 10, 55)
orc_chain = Armor("Орочья кольчуга", 45, 15, 80)
orc_plate = Armor("Орочий латный доспех", 60, 20, 110)
orc_shaman_robes = Armor("Одеяния орка-шамана", 25, 35, 60)
orc_warlord_armor = Armor("Доспехи орка-полководца", 75, 30, 140)

baby_dragon_s_arm = Weapon("baby dragon's arm",25, 0)
dragon_s_arm = Weapon("baby dragon's arm",25, 0)
small_slime_weapon = Weapon('small slime weapon', 2, 0)
medium_slime_weapon = Weapon('medium slime weapon', 20, 0)
big_slime_weapon = Weapon('big_slime_weapon', 40, 0)
giant_slime_weapon = Weapon('giant_slime_weapon', 120, 0)
wooden_sword = Weapon('wooden sword', 15, 10)
steal_sword = Weapon('steal sword', 50, 50)
rotten_wood_sword = Weapon('"great" sword', 0.0001, 100)
goblin_dagger = Weapon("Гоблинский кинжал", 15, 0)
goblin_axe = Weapon("Гоблинский топор", 35, 0)
goblin_bow = Weapon("Гоблинский лук", 25, 0)
hobgoblin_club = Weapon("Дубина хобгоблина", 55, 0)
goblin_king_sword = Weapon("Меч короля гоблинов", 80, 0)
skeleton_bone = Weapon("Кость скелета", 10, 0)
skeleton_sword = Weapon("Ржавый меч скелета", 25, 0)
skeleton_archer_bow = Weapon("Лук скелета-лучника", 30, 0)
skeleton_warrior_axe = Weapon("Топор скелета-воина", 45, 0)
skeleton_mage_staff = Weapon("Посох скелета-мага", 60, 0)
orc_club = Weapon("Дубина орка", 40, 0)
orc_axe = Weapon("Топор орка", 65, 0)
orc_berserker_axe = Weapon("Топор орка-берсерка", 85, 0)
orc_shaman_staff = Weapon("Посох орка-шамана", 70, 0)
orc_warlord_sword = Weapon("Меч орка-полководца", 110, 0)

heal_potion_small = Heal_potion_small()
heal_potion_medium = Heal_potion_medium()
heal_potion_big = Heal_potion_big()

#player==================================================================================================
player = Player('player_1', 100, wooden_sword, 'control', none, 100, [rotten_wood_sword])

#inventory========================================
first_trder_inventory = [steal_sword, rotten_wood_sword, baby_dragon_s_skin, heal_potion_small,
 heal_potion_medium, heal_potion_medium ]

#trader========================================
first_trader = Trader(first_trder_inventory, 999999999999999999999999999999, heal_potion_small, heal_potion_medium, heal_potion_big)
first_trader.heal_potion_res()

#slimes--------------------------------------------------------------------------------------------------
small_slime = Character('small slime', 5, small_slime_weapon, 'enemy', none)
medium_slime = Character('medium slime', 20, medium_slime_weapon, 'enemy', none)
big_slime = Character('big slime', 70, medium_slime_weapon, 'enemy', none)
giant_slime = Character('giant slime', 30, giant_slime_weapon, 'enemy', none)
goblin_scout = Character("Гоблин-разведчик", 25, goblin_dagger, 'enemy', goblin_leather)
goblin_warrior = Character("Гоблин-воин", 40, goblin_axe, 'enemy', goblin_chainmail)
goblin_archer = Character("Гоблин-лучник", 35, goblin_bow, 'enemy', goblin_leather)
hobgoblin = Character("Хобгоблин", 80, hobgoblin_club, 'enemy', hobgoblin_armor)
goblin_king = Character("Король гоблинов", 150, goblin_king_sword, 'enemy', goblin_king_armor)
skeleton = Character("Скелет", 30, skeleton_bone, 'enemy', skeleton_bones)
skeleton_warrior = Character("Скелет-воин", 60, skeleton_sword, 'enemy', rusted_armor)
skeleton_archer = Character("Скелет-лучник", 50, skeleton_archer_bow, 'enemy', skeleton_bones)
skeleton_knight = Character("Скелет-рыцарь", 90, skeleton_warrior_axe, 'enemy', skeleton_knight_armor)
skeleton_mage = Character("Скелет-маг", 70, skeleton_mage_staff, 'enemy', skeleton_mage_cloak)
orc_grunt = Character("Орк-пехотинец", 65, orc_club, 'enemy', orc_hide)
orc_warrior = Character("Орк-воин", 100, orc_axe, 'enemy', orc_chain)
orc_berserker = Character("Орк-берсерк", 120, orc_berserker_axe, 'enemy', orc_hide)
orc_shaman = Character("Орк-шаман", 85, orc_shaman_staff, 'enemy', orc_shaman_robes)
orc_warlord = Character("Орк-полководец", 180, orc_warlord_sword, 'enemy', orc_warlord_armor)

#dragons-------------------------------------------------------------------------------------------------
baby_dragon = Character('baby_dragon', 100, baby_dragon_s_arm, 'enemy', baby_dragon_s_skin)
dragon = Character('dragon', 125, dragon_s_arm, 'enemy', dragon_s_skin)

#rooms===================================================================================================
room1 = Room(small_slime, 5)
room2 = Room(medium_slime, 10)
room3 = Room(big_slime, 50)
room4 = Room(baby_dragon, 50)
room5 = Room(dragon, 75)
goblin_room1 = Room(goblin_scout, 15)
goblin_room2 = Room(goblin_warrior, 25)
goblin_room3 = Room(goblin_archer, 20)
goblin_room4 = Room(hobgoblin, 50)
goblin_room5 = Room(goblin_king, 100)
skeleton_room1 = Room(skeleton, 20)
skeleton_room2 = Room(skeleton_warrior, 35)
skeleton_room3 = Room(skeleton_archer, 30)
skeleton_room4 = Room(skeleton_knight, 60)
skeleton_room5 = Room(skeleton_mage, 45)
orc_room1 = Room(orc_grunt, 40)
orc_room2 = Room(orc_warrior, 65)
orc_room3 = Room(orc_berserker, 75)
orc_room4 = Room(orc_shaman, 55)
orc_room5 = Room(orc_warlord, 120)

slime_rooms_list = [room1, room2, room3]
dragon_rooms_list = [room4]
goblin_rooms_list = [goblin_room1, goblin_room2, goblin_room3, goblin_room4, goblin_room5]
skeleton_rooms_list = [skeleton_room1, skeleton_room2, skeleton_room3, skeleton_room4, skeleton_room5]
orc_rooms_list = [orc_room1, orc_room2, orc_room3, orc_room4, orc_room5]

slime_dungen = Dungeon(slime_rooms_list, 'подземелье слаймов')
dragon_dungen = Dungeon(dragon_rooms_list, 'подземелье драконов')
goblin_dungeon = Dungeon(goblin_rooms_list, 'Подземелье гоблинов')
skeleton_dungeon = Dungeon(skeleton_rooms_list, 'Подземелье скелетов')
orc_dungeon = Dungeon(orc_rooms_list, 'Подземелье орков')

def time_nosleeps(time_nosleep):
    print(f'Сейчас {time_nosleep} %')
    time_nosleep = int(input(f'Задайть процент для времени ожидания:'))
    return(time_nosleep)

choose = 0
all_dungeon = [slime_dungen, dragon_dungen, goblin_dungeon, skeleton_dungeon, orc_dungeon]
print(f'Вы провалились в подземелье')
time_nosleep = int(input(f'Задайте процент для времени ожидания: '))
time.sleep(3*time_nosleep)
for dungen in all_dungeon:
    print(f'Вы, вошли в подземелье {dungen.name}')
    while dungen.passed == False:
        print(f'1.торговец\n2.инвентарь\n3.в бой!\n4.задать процент для времени ожидания')
        choose = int(input('1, 2, 3, 4? '))
        if choose == 1:
            first_trader.trader_manager(player)
        elif choose == 2:
            player.player_manager()
        elif choose == 3:
            is_alive = dungen.next_room(player, time_nosleep)
            if is_alive == False:
                print(f'К сожелению Вы умерли, но вы можете снова пройти тот же путь...')
                break
        elif choose == 4:
            time_nosleep = time_nosleeps(time_nosleep)
        elif dungen.passed == True:
            break
        else :
            print('непонял')
if is_alive == True:
    print(f'Вы прошли уровень {dungen.name},\nтак держать!\n вы нашли 100 монет')
    player.money += 100
    print(f'теперь у вас {player.money}')
if is_alive == True:
    print('Поздрвляю, вы прошли подземелье и выбрались на поверхность!')