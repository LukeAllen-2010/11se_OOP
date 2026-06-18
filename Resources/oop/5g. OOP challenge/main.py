from entity import Entity
from print_line import print_line

enemies = {
    'kobold' : Entity('kobold', 25, ['rend'], 13, 14, 12),
    'goblin' : Entity('goblin minion', 5, ['rend', 'greatsword'], 10, 10, 10)
}

hero =  Entity('bob', 1000, ['rend', 'halberd'], 2, 10, 10)

def choose_target(enemies):
    enemy_list_str = f'Which enemy would you like to hit: '
    print_line(f'{len(enemies)} enemies face you: ')
    for enemy_num, enemy in enumerate(enemies, 1):
        print_line(f'{enemy}({enemy_num}), ')
    print_line('. Which shall you attack?')
    player_target = enemies[list(enemies)[int(input('which shall you attack?\n')) - 1]]
    return player_target

def get_initiative_order(entities, player):
    initiative_order = {}
    for entity in entities:
        initiative_order[entity] = entities[entity].get_initiative_roll()
    initiative_order[player.name] = player.get_initiative_roll()
    return {k : v for k, v in sorted(initiative_order.items(), key = lambda item : item[1])}

initiative_order = get_initiative_order(enemies, hero)

print(initiative_order)
print(enemies)
running = True
while running:
    for entity in initiative_order:

        print(f'\nit is {entity}\'s turn')
        if entity == hero.name:
            if not enemies:
                running = False
                print('\nYOU WIN!\n')
            else:
                target = choose_target(enemies)
                attack = hero.choose_attack # rend
                target.health -= hero.attack_target(attack, target.ac)
                if target.is_dead():
                    print(f'{target.name} is dead')
                    entity.remove(target)
                    initiative_order.remove(target)
                else:
                    print(f'{target} still alive at {target.health}HP')
        else:
            enemy = enemies[entity]
            hero.health -= enemy.get_turn()
            if hero.is_dead():
                print('\nYOU LOSE!\n')
                running = False
                break
            else:
                print(f'{hero.name} still alive at {hero.health}HP')
            
    for enemy in enemies:
        print(f'{enemy} health: {enemies[enemy].health}')
    print(f'{hero.name} health: {hero.health}')