def fibonacci():
    fibonacci_list = [0, 1]
    for i in range(2, 10):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    return fibonacci_list

print(f"Los primeros 10 números de la sucesión de Fibonacci son:")
print(fibonacci())
