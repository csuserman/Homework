def invest(amount: float, rate: float, years: int) -> float:
    for i in range(years):
        amount = amount * (1 + rate/100)
        print(f'year {i + 1}: ${round(amount, 2)}')

invest(100, 5, 4)