for i in range(1,101): #loop para imprimir los numeros del 1 al 100
    if i%3 == 0 and i%5 != 0: #que sea multiplo de 3 y no de 5
        print('Fizz')
    elif i%5 == 0 and i%3 != 0: #que sea de 5 y no de 3
        print('Buzz')
    elif i%3 == 0 and i%5 == 0: #que sea de 3 Y de 5
        print('FizzBuzz')
    else: #Cuando no es multiplo de 3 ni de 5 y se imprime de forma normal
        print(i)           
