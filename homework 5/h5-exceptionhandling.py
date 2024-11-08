# problem 1
# def divide(x: float, y: float) -> float:
#     try:
#         print(x / y)
#     except ZeroDivisionError:
#         print('ZeroDivisionError occured!')

# divide(10, 0)

# problem 2
# def integer() -> int:
#     try:
#         num = int(input('Enter an integer: '))
#         print(num)
#     except ValueError:
#         print('Value error occured!')

# integer()

# problem 3
# def open_file(filename: str):
#     try:
#         f = open(filename, 'r')
#         f.close()
#     except FileNotFoundError:
#         print('FileNotFoundError occured!')

# open_file('demofile.txt')

# problem 4
# def integers():
#     try:
#         x = float(input())
#         y = float(input())
#         print(x, y)
#     except ValueError:
#         print('ValueError occured!')

# integers()

# problem 5
# def open_file(filename: str):
#     try:
#         f = open(filename, 'r')
#         print(f.read())
#         f.close()
#     except PermissionError:
#         print('PermissionError occured!')

# open_file('demofile.txt')


# problem 6
# def check_list(lst: list, index: int):
#     try:
#         print(lst[index])
#     except IndexError:
#         print('Indexerror occured!')

# check_list([1, 2, 3], 4)

# problem 7
# def interrupt():
#     try:
#         x = float(input())
#         print(x)
#     except KeyboardInterrupt:
#         print('\nKeyboardInterrupt occured!')

# interrupt()

# problem 8
# def divide(x: float, y: float) -> float:
#     try:
#         print(x / y)
#     except ArithmeticError:
#         print('ArithmeticError occured!')

# divide()

# problem 9
# def open_file(filename: str):
#     try:
#         f = open(filename, 'r', encoding = 'encoding')
#         print(f.read())
#         f.close()
#     except UnicodeEncodeError:
#         print('UnicodeEncodeError occured!')

# problem 10
# def list_operation(nums: list[float]):
#     try:
#         print(nums.upper())
#     except AttributeError:
#         print('AttributeError occured!')

# list_operation([])