import random
from entity import Entity

opps = {
    'kobold' : Entity('kobold', 25, ['rend'], 13, 14, 12),
    'goblin_minion_1' : Entity('goblin minion', 5, ['rend', 'greatsword'], 10, 10, 10),
    'goblin_minion_2' : Entity('goblin minion', 5, ['rend', 'greatsword'], 10, 10, 10),
    'goblin_minion_3' : Entity('goblin minion', 5, ['rend', 'greatsword'], 10, 10, 10)
}

hero =  Entity('bob', 10, ['rend', 'halberd'], 2, 10, 10)

def choose_target(enemies):
    enemy_list_str = f'Which enemy would you like to hit: '
    print(f'{len(enemies)} enemies face you: ', end="")
    for enemy_num, enemy in enumerate(enemies, 1):
        print(f'{enemy}({enemy_num})', end=", ")
    player_target = enemies[list(enemies)[int(input('which shall you attack?\n')) - 1]]
    return player_target

def choose_attack(hero):
    print('These are your attacks: ', end='')
    for attack in hero.attacks:
        print(attack, end=', ')
    return input('which do you pick?\n').lower()

def get_initiative_order(entities, player):
    initiative_order = {}
    for entity in entities:
        initiative_order[entity] = entities[entity].get_initiative_roll()
    initiative_order[player.name] = player.get_initiative_roll()
    return {k : v for k, v in sorted(initiative_order.items(), key = lambda item : item[1])}

initiative_order = get_initiative_order(opps, hero)

running = True
while running:
    for entity in initiative_order:
        print(f'\nit is {entity}\'s turn')
        if entity == hero.name:
            if not opps:
                running = False
            else:
                target = choose_target(opps)
                attack = choose_attack(hero) # rend
                hero.attack_target(attack, target.ac)
                if target.is_dead():
                    print(f'{target.name} is dead')
                    entity.remove(target)
                    initiative_order.remove(target)
                else:
                    print(f'{target} still alive at {target.health}HP')
        else:
            entity = opps[entity]
            attack = entity.attack_target(random.choice(list(entity.attacks)), hero.ac)
            hero.health -= attack
            if hero.is_dead():
                print('YOU LOSE')
                break
            else:
                print(f'{hero.name} still alive at {hero.health}HP')
            
    for opp in opps:
        print(f'{opp} health: {opps[opp].health}')
    print(f'{hero.name} health: {hero.health}')
# enemies = ['troll_1', 'troll_2', 'goblin', 'bear', 'angry_toadstool']


    # target = int(input(f'which enemy would you like to hit: {enemies[0]}(1), {enemies[1]}(2)'))
    # player_target.get_roll(1, 'd20')