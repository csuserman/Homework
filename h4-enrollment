def enrollment_stats(x: list):
    enrollment_values: list[float] = []
    tutition_fees: list[float] = []
    for i in range(len(x)):
        enrollment_values.append(x[i][1])
        tutition_fees.append(x[i][2])
    return enrollment_values, tutition_fees


def mean(y: list[float]):
    return round(sum(y)/len(y), 2)

def median(z: list[float]):
    z.sort()
    lenght = len(z)
    if lenght % 2 == 1:
        m = int((lenght - 1)/2)
        return z[m]
    else:
        n = int(lenght/2)
        return (z[n] + z[n - 1])/2


a, b = enrollment_stats([
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
])

print(f'Total students: {sum(a)}')
print(f'Total tution: $ {sum(b)}\n')
print(f'Student mean: {mean(a)}')
print(f'Student median: {median(a)}\n')
print(f'Tuition mean: $ {mean(b)}')
print(f'Tuition median: $ {median(b)}')