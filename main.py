all_win_coords = ((1, 2, 3), (1, 4, 7), (4, 5, 6), (2, 5, 8), (7, 8, 9), (3, 6, 9), (1, 5, 9), (3, 5, 7))
playing_field = list(range(1, 10))
counter = 0
status = False
while not status:
    for number in range(1, 10, 3):
        print(f"| {playing_field[number - 1]} | {playing_field[number]} | {playing_field[number + 1]} |")
    if counter % 2:
        player = "O"
    else:
        player = "X"
    counter += 1
    if counter > 9:
        print("Ничья")
        break
    print(f"Ход игрока {player}")
    valid = False
    while not valid:
        position = int(input(f"Куда вы хотите поставить {player}? "))
        if str(playing_field[position - 1]) not in "OX":
            playing_field[position - 1] = player
            valid = True
        else:
            print("Клетка занята!")
    if counter > 4:
        for win_coord in all_win_coords:
            if playing_field[win_coord[0] - 1] == playing_field[win_coord[1] - 1] == playing_field[win_coord[2] - 1]:
                print(f"Победил {player}")
                status = True