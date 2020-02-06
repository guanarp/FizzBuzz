def impresor(min, max, mod1, mod2):
    for i in range(min,max+1): #loop para imprimir los numeros del 1 al 100
        if i% mod1 == 0 and i% mod2 != 0: #que sea multiplo de 3 y no de 5
            print('Fizz')
        elif i% mod2 == 0 and i% mod1 != 0: #que sea de 5 y no de 3
            print('Buzz')
        elif i% mod1 == 0 and i% mod2 == 0: #que sea de 3 Y de 5
            print('FizzBuzz')
        else: #Cuando no es multiplo de 3 ni de 5 y se imprime de forma normal
            print(i) 
impresor(1,100,3,5)     
