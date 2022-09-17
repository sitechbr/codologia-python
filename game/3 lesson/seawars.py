import random


def print_area(area):
    for i in range(len(area)):
        if area[i] == 1:
            print("#", end=' ')
        else:
            print('*', end=' ')


def gen_area(enemmy):
    ships = 3
    while (ships > 0):
        pos = random.randint(0, len(enemmy) - 1)
        if enemmy[pos] == 0:
            enemmy[pos] = 1
            ships -= 1
    return enemmy


def cheak_ship(pos,arrea):
    if arrea[pos]==1:
        return True
    else:
        return False


if __name__ == '__main__':
    enemmy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    enemmy=gen_area(enemmy)
    print_area(player)
    ship=1
    while ship<=3:
        print("Введите координату ", ship, "корабля")
        pos = int(input())
        if (pos<len(enemmy)):
            if cheak_ship(pos,enemmy) and not cheak_ship(pos,player) :
                player[pos] = 1
                ship+=1
                print("Попали")
            else:
                print("Промах")
        else:
            print ("Введите значение от 0 до ", len(enemmy)-1)
        print_area(player)
    print("Вы победили!")
