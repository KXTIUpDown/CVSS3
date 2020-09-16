import math

def round_up(number):                                                            # Функция округления
    number_up = math.ceil(10*number)/10
    return number_up

def raiting(number):                                #Функция оценки

    if number == 0:
        rait = 'Информационный'
    elif number < 4:
        rait = 'Низкий'
    elif (number > 3.9) and (number < 7):
        rait = 'Средний'
    elif (number > 6.9) and (number < 9):
        rait = 'Высокий'
    else:
        rait = 'Критический'

    return rait
def start():
    try:                                              #Ввод и проверка данных
        AV = float(input('Введите AV --> '))
        AC = float(input('Введите AC --> '))
        PR = float(input('Введите PR --> '))
        UI = float(input('Введите UI --> '))
        S = int(input('Введите S --> '))
        if S>1:
            input('Ошибка при вводе данных ')
            start()
        C = float(input('Введите C --> '))
        I = float(input('Введите I --> '))
        A = float(input('Введите A --> '))

    except ValueError:
        input('Ошибка при вводе данных \n нажмите на Enter для повторного ввода данных')
        start()


    Exploitability = 8.22 * AV * AC * PR * UI
    ImpactBase = 1 - ((1 - C) * (1 - I) * (1 - A))
    if S == 0:
        Impact = 6.42 * ImpactBase
        BaseScore = round_up(round_up(min(Impact + Exploitability, 10)))
    elif S == 1:
        Impact = 7.52 * (ImpactBase - 0.029) - 3.25 * (ImpactBase - 0.02) ** 15
        BaseScore = round_up(min(1.08 * (Impact + Exploitability), 10)) #Каличественное значение базовой оценки
    print('Базовая оценка')
    print('Качественная оценка: ', raiting(BaseScore))
    print('Количественная оценка: ', BaseScore)

    print('Ввод данных для временной оценки')
    try:                                                  #Ввод доп. переменных для нажождения временной оценки
        E = float(input('Введите E --> '))
        RL = float(input('Введите RL --> '))
        RC = float(input('Введите RC --> '))
    except ValueError:
        input('Ошибка при вводе данных \n нажмите на Enter для повторного ввода данных')
        start()

    TempScore = round_up(BaseScore * E * RL * RC)       # Каличественное значение временной оценки
    print('Временная оценка')
    print('Качественная оценка: ', raiting(TempScore))
    print('Количественная оценка: ', TempScore)
    input('Нажмите на Enter для закрытия консоли')
if __name__=='__main__':
    start()


