#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печатаем заголовок таблицы
    header = "   |"
    for col in range(1, num_columns + 1):
        header += f" {col:2} |"
    print(header)
    
    # Печатаем разделитель
    separator = "---+" + "---+" * num_columns
    print(separator)
    
    # Печатаем строки таблицы
    for row in range(1, num_rows + 1):
        row_str = f"{row:2} |"
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            row_str += f" {result:2} |"
        print(row_str)
    
    # Печатаем разделитель
    print(separator)

# Пример использования: умножение чисел
def multiply(x, y):
    return x * y

print("Таблица умножения:")
print_operation_table(multiply)