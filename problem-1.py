def cal():
    x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide')
    print(x)
cal()

cal1 = input('Enter your choice: ')

num1 = float(input('Enter First number: '))
num2 = float(input('Enter Second number: '))

if cal1 == '1':
    x1 = num1 + num2
    print('Total number: ' + str(x1))
elif cal1 == '2':
    x2 = num1 - num2
    print('Total number: ' + str(x2))
elif cal1 == '3':
    x3 = num1 * num2
    print('Total number: ' + str(x3))
elif cal1 == '4':
    x4 = num1 / num2
    print('Total number: ' + str(x4))
else:
    print("Invalid input")  