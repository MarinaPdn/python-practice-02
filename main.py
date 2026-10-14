# Задание 1. Консольный калькулятор

# Определяем розовый цвет через 256-цветную палитру (код 205 — насыщенный розовый)
PINK = "\033[38;5;205m"
# Сброс цвета: используем краткую форму \033[m (эквивалент \033[0m)
RESET = "\033[m"

# Функция для вывода приглашения и получения ввода от пользователя
def input_prompt(text):
    # Выводим текст розовым цветом, затем сбрасываем цвет.
    # Параметр end=" " оставляет курсор на той же строке для ввода.
    print(f"{PINK}{text}{RESET}", end=" ")
    # Читаем введённую строку и возвращаем её
    return input()

# Функция для вывода результата вычислений
def show_result(value):
    # Выводим слово "Результат:" и значение розовым цветом, затем сбрасываем
    print(f"{PINK}Результат: {value}{RESET}")

# Функция для вывода сообщения об ошибке
def show_error(message):
    # Выводим "Ошибка:" и текст ошибки розовым цветом, затем сбрасываем
    print(f"{PINK}Ошибка: {message}{RESET}")

# Главная функция, вся логика калькулятора
def calculate():
    print(f"{PINK}Добро пожаловать в консольный калькулятор!{RESET}")
    print(f"{PINK}Доступные операции: +  -  *  /  //  %  ^ (степень){RESET}")
    print(f"{PINK}Для выхода введите 'm' в любом поле.{RESET}")
    # Пустая строка для отделения от последующих запросов
    print()

    # Бесконечный цикл, который будет работать, пока пользователь не введёт 'm'
    while True:
        # Шаг 1. Запрашиваем первое число
        first_input = input_prompt("Введите первое число (или 'm' для выхода):")
        # Проверяем, не хочет ли пользователь выйти
        if first_input.lower() == 'm':
            print(f"{PINK}До свидания!{RESET}")
            break  # Выход из цикла

        # Пытаемся преобразовать ввод в число с плавающей точкой
        try:
            first_num = float(first_input)
        except ValueError:
            # Если преобразование не удалось, значит, введено не число
            show_error("Некорректное число. Попробуйте снова.")
            # Переходим к следующей итерации цикла, не выполняя остальной код
            continue

        # Шаг 2. Запрашиваем математическую операцию
        operation = input_prompt("Введите операцию (+, -, *, /, //, %, ^):")
        if operation.lower() == 'm':
            print(f"{PINK}До свидания!{RESET}")
            break

        # Список допустимых операций
        allowed_ops = ['+', '-', '*', '/', '//', '%', '^']
        # Проверяем, входит ли введённая операция в список
        if operation not in allowed_ops:
            show_error(f"Неизвестная операция '{operation}'. Допустимые: {', '.join(allowed_ops)}")
            # Перезапускаем цикл, не запрашивая второе число
            continue

        # Шаг 3. Запрашиваем второе число
        second_input = input_prompt("Введите второе число (или 'm' для выхода):")
        if second_input.lower() == 'm':
            print(f"{PINK}До свидания!{RESET}")
            break

        try:
            second_num = float(second_input)
        except ValueError:
            show_error("Некорректное число. Попробуйте снова.")
            continue

        # Шаг 4. Специальная обработка для операций // и % (требуют целых чисел)
        if operation in ['//', '%']:
            # Проверяем, что оба числа являются целыми (метод is_integer() возвращает True для 5.0)
            if not first_num.is_integer() or not second_num.is_integer():
                show_error("Для целочисленного деления и остатка оба числа должны быть целыми.")
                continue
            # Преобразуем числа в тип int, чтобы операции // и % работали корректно
            first_num = int(first_num)
            second_num = int(second_num)

        # Шаг 5. Выполняем выбранную операцию
        result = None  # Переменная для хранения результата
        error = None   # Переменная для хранения сообщения об ошибке

        # Блок try для перехвата возможных исключений (например, деление на ноль)
        try:
            if operation == '+':
                result = first_num + second_num
            elif operation == '-':
                result = first_num - second_num
            elif operation == '*':
                result = first_num * second_num
            elif operation == '/':
                if second_num == 0:
                    error = "Деление на ноль!"
                else:
                    result = first_num / second_num
            elif operation == '//':
                if second_num == 0:
                    error = "Деление на ноль!"
                else:
                    result = first_num // second_num
            elif operation == '%':
                if second_num == 0:
                    error = "Деление на ноль!"
                else:
                    result = first_num % second_num
            elif operation == '^':
                # Возведение в степень: в Python используется оператор **
                result = first_num ** second_num
        except Exception as e:
            # Если произошла другая ошибка, сохраняем её текст
            error = str(e)
        # Шаг 6. Вывод результата или сообщения об ошибке
        if error:
            show_error(error)
        else:
            show_result(result)

        # Пустая строка для визуального разделения между вычислениями
        print()

# Проверяем, запущен ли файл как основная программа
if __name__ == "__main__":
    calculate()