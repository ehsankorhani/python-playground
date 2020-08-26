import random

def execute(number_of_try):
    doors = (1, 2, 3)
    change_success = 0
    unchange_success = 0

    count = 0
    while (count < number_of_try):
        count = count + 1

        car_door = random.choice(doors)
        player_choice = random.choice(doors)
        revealed_door = [d for d in doors if d != car_door if d != player_choice][0]

        if (player_choice == car_door):
            unchange_success += 1
        else:
            change_success += 1

    print (f'change success rate: {change_success/number_of_try}%')
    print (f'unchange success rate: {unchange_success/number_of_try}%')


execute(100)
