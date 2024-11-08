def factors(n: int):
    for i in range(n//2 + 1):
        if n % (i + 1) == 0:
            print(f'{i + 1} is factor of {n}')
    print(f'{n} is factor of {n}')

factors(12)