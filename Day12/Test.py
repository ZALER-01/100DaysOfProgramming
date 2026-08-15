enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function :{enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

def drink_portion():
    portion_strength = 2
    print(portion_strength)

game_level = 3
enemies = ['Skeleton', 'Dagger','Alien']

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
    print(enemies)

#modify Global scope
#Avoid Modifying global Variables




