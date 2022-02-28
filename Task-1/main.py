    import sys
    #inputs
    n = int(input('Number of variables: '))
    print("Enter augmented matrix coefficients row by row:")
    a = []
    for i in range(n):
        a.append(list(map(float, input().split())))

    #Elimintation
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Error: Division By Zero')
    for j in range(i + 1 , n):
        factor = a[j][i] / a[i][i]
        for k in range(n + 1):
            a[j][k] = a[j][k] - factor * a[i][k]


    #Substitution
    x=[0]*n
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    #output
    for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
