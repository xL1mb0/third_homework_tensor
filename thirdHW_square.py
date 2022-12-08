a, b, c = 0, 0, 0

def input_abc():
    global a, b, c
    while 1:
        try:
            a, b, c = map(int, input("Введите коэфициенты квадратного уравнения через пробел: ").split())
            return
        except:
            print("На входе должно быть 3 рациональных числа, записанных через пробелы. Повторите попытку ввода")
            continue

def sqrt_D(): # дискриминант
    global a, b, c
    D = b**2 - 4*a*c
    if D >= 0: return D**0.5
    else: return (D+0j)**0.5

def get_x1(sqrt_D):
    global a, b, c
    if type(sqrt_D) == type(0+0j):
        return ((-b+0j) + sqrt_D)/(2*(a+0j))
    else:
        return (-b + sqrt_D)/(2*a)
    
def get_x2(sqrt_D):
    global a, b, c
    if type(sqrt_D) == type(0+0j):
        return ((-b+0j) - sqrt_D)/(2*(a+0j))
    else:
        return (-b - sqrt_D)/(2*a) 
        
def print_solve(x1, x2):
    print("Корни квадратного уравнения: ", x1, "; ", x2, sep = "")
    
def solve_square_equation():
    input_abc()
    s_D = sqrt_D()
    print_solve(get_x1(s_D), get_x2(s_D))

solve_square_equation()