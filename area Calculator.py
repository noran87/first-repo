import math

print('==================\nArea Calculator 📐\n==================\n')
print('1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n')

shape = int(input('Which shape: '))

if shape == 1:
    height = int(input('\nHeight: '))
    base = int(input('Base: '))
    triangle_area = (height * base) / 2
    print(f'\nthe area is: {triangle_area}')
elif shape == 2:
    length = int(input('\nLength: '))
    width = int(input('Width: '))
    rectanglet_area = length * width
    print(f'\nthe area is: {rectanglet_area}')
elif shape == 3:
    side = int(input('\nSide: '))
    square_area = side ** 2
    print(f'\nthe area is: {square_area}') 
elif shape == 4:
    radius = int(input('\nRadius: '))
    circle_area = math.pi * (radius ** 2)
    print(f'\nthe area is: {circle_area}')
else:
    print('\nQuit')   
    
               