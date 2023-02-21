number1 = 10
number2 = 5

sum = number1 + number2
print(sum)  # 15

subtraction = number1 - number2
print(subtraction)  # 5

# O * é para multiplicação
multplication = number1 * number2
print(multplication)  # 50

# O ** é para potenciação
potentiation = number1 ** number2
print(potentiation)  # 100000

# Com o / a divisão é float
division_float = number1 / number2
print(division_float)  # 2.0

# Com // a divisão é inteiro
division_integer = number1 // number2
print(division_integer)  # 2

# O modulo retorna o que resta em uma divisão:
# Ex: 4 % 2 = 0 ou 5 % 2 = 1
module = number1 % number2
print(module)  # 0

# Incremento ou Decremento em Python não aceita essa sintaxe ++ e --
counter = 10

# Os exemplos de sintaxe validas são

# Incremento
# counter = counter + 1
counter += 1
print(counter)  # 11

# Decremento
# counter = counter - 1
counter -= 1
print(counter)  # 10


# Operadores >, <, and e or:

temperature = 24

# Maneira extensa
print(temperature < 25 and temperature > 18)  # True

# Maneira "Pythonica"
print(18 < temperature < 25)  # True

age = 32

print(age <= 5 or age >= 65)  # False
