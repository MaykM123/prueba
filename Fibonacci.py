

iniFibo = 0
finFibo = 1
x = 1
while True:
    
    if x == 0:
        finFibo = 0
    elif x == 1:
        finFibo = 1

    sum = finFibo
    finFibo = finFibo + iniFibo
    iniFibo = finFibo - iniFibo

    print(f'\nPosición Final:{x+1} -- Valor en la serie de Fibonacci123:{sum}')