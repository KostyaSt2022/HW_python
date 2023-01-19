# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

# P.S. СПИСАЛ :(


# Инициализация карты
maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# Инициализация победных линий
win_lines = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Вывод карты на экран
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])    
 
# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
# Получить текущий результат игры
def get_result():
    win = ""
 
    for i in win_lines:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
 
# Основная программа
game_over = False
player1 = True

user_name1 = input('Имя первого игрока: ')
user_name2 = input('Имя второго игрока: ')

while game_over == False:
 
    # 1. Показываем карту
    print_maps()
 
    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input(f"{user_name1} - (X), ваш ход: "))
    else:
        symbol = "0"
        step = int(input(f"{user_name2} - (0), ваш ход: "))
 
    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
 
# Игра окончена. Покажем карту. Объявим победителя.        
print_maps()
print("Победил", win)