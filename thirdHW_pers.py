import re

def print_info():
    print("Чтобы переместить персонажа, введите направление (в, н, п, л - (верх, низ, право, лево) и расстояние")
    print("Пример: команды")
    print("в 2" + "\n" + "п 3" + "\n" + "л 7" + "\n" + "приведут персонажа из точки (0, 0) в точку (-4, 2)")
    print("* примечание: пройденное расстояние не может быть нулевым и отрицательным")
    
def print_current_location():
    global x
    global y
    print("\n" + "Позиция персонажа: (", x, "; ", y,")", sep = "")

def try_parse_input_movement(input_movement):
    input_movement = input_movement.split()
    returned_array = [0, 0]
    try:
        if re.match(r"[внпл]", input_movement[0]) and int(input_movement[1]) > 0:
            if input_movement[0] == "в": returned_array[1] += int(input_movement[1])
            elif input_movement[0] == "н": returned_array[1] -= int(input_movement[1])
            elif input_movement[0] == "п": returned_array[0] += int(input_movement[1])
            else: returned_array[0] -= int(input_movement[1])
            return returned_array
        return "error"
    except:
        return "error"
        


def move(print_error_message):
    movement = try_parse_input_movement(input("[Ввод с консоли]: "))
    global x
    global y
    if type(movement) != type("str"):
        x += movement[0]
        y += movement[1]
        return 1
    else:
        if print_error_message == True: print("При обработке входных данных возникла ошибка, проверьте соответствие формату")
        return 0

x, y = 0, 0

print ("Первое задание: Переместить персонажа один раз")
print_info()
move(True)
print_current_location()

print("Второе задание: Переместить персонажа N раз. Стоп-слово: любой ввод не по формату")
while 1:
    if not move(False):
        print_current_location()
        break