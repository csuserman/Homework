# problem 1
# def read_file(filename: str):
#     f = open(filename)
#     print(f.read())
#     f.close()

# read_file('demo.txt')

# problem 2
# def read_n_lines(filename: str, n: int):
#     f = open(filename, 'r')
#     for i in range(n):
#         print(f.readline().strip())
#     f.close()

# read_n_lines('demo.txt', 3)

# problem 3
# def append_file(filename: str):
#     n = open(filename, 'a')
#     n.write('\nnothing')
#     n.close()
#     k = open(filename, 'r')
#     print(k.read())
#     k.close()

# append_file('demo.txt')

# problem 4
# def last_n_lines(filename: str, n: int):
#     f = open(filename, 'r')
#     lst = f.readlines()
#     f.close()
#     for object in lst[-n:]:
#         print(object.strip())

# last_n_lines('demo.txt', 2)

# problem 5
# def lines(filename):
#     f = open(filename, 'r')
#     print(f.readlines())
#     f.close()

# lines('demo.txt')

# problem 6
# def lines(filename):
#     lines = []
#     f = open(filename, 'r')
#     for line in f:
#         lines.append(line.strip())
#     f.close()
#     print(lines)

# lines('demo.txt')

# problem 7
# def lines(filename):
#     lines = []
#     f = open(filename, 'r')
#     for line in f:
#         lines.append(line.strip())
#     f.close()
#     print(lines)

# lines('demo.txt')

# problem 8
# def lines(filename):
#     f = open(filename, 'r')
#     words = f.read().split()
#     f.close()
#     lst = []
#     for i in words:
#         lst.append(len(i))
#     max_len = max(lst)
#     [print(word) for word in words if max_len == len(word)]
# lines('demo.txt')

# problem 9
# def number_of_lines(filename: str):
#     lines = []
#     f = open(filename, 'r')
#     for line in f:
#         lines.append(line.strip())
#     f.close()
#     print(len(lines))

# number_of_lines('demo.txt')

# problem 10
# def frequency_of_word(filename: str):
#     f = open(filename, 'r')
#     lst = f.read().split()
#     f.close()
#     st = set(lst)
#     dct = dict()
#     for uword in st:
#         i = 0
#         for word in lst:
#             if uword == word:
#                 i = i + 1
#         dct[uword] = i
#     print(dct)

# frequency_of_word('demo.txt')

# problem 11
# def file_size(fname):
#     import os
#     statinfo = os.stat(fname)
#     print(statinfo.st_size)

# file_size('demo.txt')

# problem 12
# def file_list(filename: str, lst: list):
#     f = open(filename, 'w')
#     f.write(str(lst[0]))
#     for i in range(1, len(lst)):
#         f.write(f'\n{lst[i]}')
#     f.close()
#     f = open(filename, 'r')
#     print(f.read())
#     f.close()

# file_list('demo.txt', [1, 2, 6, 'sdfg', 'ergh'])

# problem 13
# def copy_txt(filename: str):
#     f = open(filename, 'r')
#     lst = f.readlines()
#     f.close()
#     x = open('x.txt', 'x')
#     for line in lst:
#         x.write(line)
#     x.close()
#     x = open('x.txt', 'r')
#     print(x.read())
#     x.close()

# copy_txt('demo.txt')

# problem 15
# import random
# def random_line(filename):
#     lines = []
#     f = open(filename, 'r')
#     for line in f:
#         lines.append(line.strip())
#     f.close()
#     print(random.choice(lines))

# random_line('demo.txt')