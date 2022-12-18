import view                                                 # Подключение блока view
import model                                                # Подключение блока model
import parser                                               # Подключение блока parser

def input_first():                                          # Получение и присвоение значения первому числу
    number = view.input_number()
    if number.isdigit():
        number = int(number)
        model.set_first(number)
    else:
        model.set_expression(number)
        parser.parser(number)

def input_second():                                         # Получение и присвоение значения второму числу
    while True:
        number = int(view.input_number())
        if model.get_operation() == '/' and number == 0:    # проверка деления на ноль
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break


def input_operation():                                      # Получение и присвоение операции
    oper = view.input_operation()
    model.set_operation(oper)


def solution():                                             # Метод для произведения вычислений
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()

    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)                   # Вывод на печать
    model.set_first(model.get_result())                    # Результат стал первым числом для последующих операций
    return False


def start():                                               # Калькулятор (старт с обработчиком "=")
    input_first()
    if not model.get_exression():
        while True:
            input_operation()
            if model.get_operation() == '=':
                view.log_off()
                break
            input_second()
            solution()
