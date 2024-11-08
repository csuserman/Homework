def convert_cel_to_far() -> float:
    C = float(input('Enter a temperature in degrees C: '))
    F = C * 9/5 + 32
    print(f'{C} degrees C = {round(F, 2)} degrees F')

def convert_far_to_cel() -> float:
    F = float(input('Enter a temperature in degrees F: '))
    C = (F - 32) * 5/9
    print(f'{F} degrees F = {round(C, 2)} degrees C')

convert_cel_to_far()
convert_far_to_cel()