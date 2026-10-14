# Консольный калькулятор с поддержкой нескольких вычислений подряд
# Практическая работа №2


# Функция для вывода приглашения и получения ввода от пользователя
def input_prompt(text):
    # Выводим текст приглашения и оставляем курсор на той же строке (end=" ")
    print(text, end=" ")
    # Читаем введённую строку и возвращаем её
    return input()

# Функция для вывода результата вычислений
def show_result(value):
    # Выводим слово "Результат:" и значение
    print(f"Результат: {value}")

# Функция для вывода сообщения об ошибке
def show_error(message):
    # Выводим "Ошибка:" и текст ошибки
    print(f"Ошибка: {message}")

# Функция для выполнения одного вычисления
# Возвращает True, если вычисление выполнено (или была ошибка, но пользователь не вышел)
# Возвращает False, если пользователь решил выйти (ввёл 'm')
def perform_calculation():
    # Шаг 1. Запрашиваем первое число
    first_input = input_prompt("Введите первое число (или 'm' для выхода):")
    # Проверяем, не хочет ли пользователь выйти
    if first_input.lower() == 'm':
        return False  # Сигнал о выходе

    # Пытаемся преобразовать ввод в число с плавающей точкой
    try:
        first_num = float(first_input)
    except ValueError:
        # Если введено не число, выводим ошибку и возвращаем True (цикл продолжится)
        show_error("Некорректное число. Попробуйте снова.")
        return True

    # Шаг 2. Запрашиваем математическую операцию
    operation = input_prompt("Введите операцию (+, -, *, /, //, %, ^):")
    # Проверяем выход
    if operation.lower() == 'm':
        return False

    # Список допустимых операций
    allowed_ops = ['+', '-', '*', '/', '//', '%', '^']
    # Проверяем, входит ли введённая операция в список
    if operation not in allowed_ops:
        show_error(f"Неизвестная операция '{operation}'. Допустимые: {', '.join(allowed_ops)}")
        return True

    # Шаг 3. Запрашиваем второе число
    second_input = input_prompt("Введите второе число (или 'm' для выхода):")
    if second_input.lower() == 'm':
        return False

    try:
        second_num = float(second_input)
    except ValueError:
        show_error("Некорректное число. Попробуйте снова.")
        return True

    # Шаг 4. Специальная обработка для операций // и % (требуют целых чисел)
    if operation in ['//', '%']:
        # Проверяем, что оба числа являются целыми
        if not first_num.is_integer() or not second_num.is_integer():
            show_error("Для целочисленного деления и остатка оба числа должны быть целыми.")
            return True
        # Преобразуем числа в тип int
        first_num = int(first_num)
        second_num = int(second_num)

    # Шаг 5. Выполняем выбранную операцию
    result = None  # Переменная для результата
    error = None   # Переменная для сообщения об ошибке

    # Блок try для перехвата возможных исключений
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

    return True  # Вычисление завершено, можно продолжать

# Главная функция программы
def main():
    # Приветствие
    print("Добро пожаловать в консольный калькулятор!")
    print("Доступные операции: +  -  *  /  //  %  ^ (степень)")
    print("Для выхода введите 'm' в любом поле.")
    print()  # Пустая строка для разделения

    # Бесконечный цикл, который прервётся только при выходе
    while True:
        # Выполняем одно вычисление
        keep_going = perform_calculation()
        # Если пользователь решил выйти — завершаем цикл
        if not keep_going:
            print("До свидания!")
            break

        # Спрашиваем, хочет ли пользователь продолжить
        answer = input_prompt("Хотите выполнить ещё одну операцию? (да/нет):")
        # Приводим ответ к нижнему регистру и убираем пробелы
        answer = answer.lower().strip()

        # Если ответ 'нет' — завершаем
        if answer == 'нет' or answer == 'no' or answer == 'n':
            print("Работа программы завершена.")
            break
        # Если ответ 'да' — продолжаем (цикл повторится)
        elif answer == 'да' or answer == 'yes' or answer == 'y':
            print()  # Пустая строка для разделения
            continue
        # Если ответ неправильный — сообщаем об ошибке и завершаем
        else:
            show_error("Неправильный ответ. Завершение программы.")
            break

# Точка входа
if __name__ == "__main__":
    main()
