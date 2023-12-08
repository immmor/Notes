m = 3
while m<10:
    n=2
    while n<=m-1:
        if m%n==0:
            break
        if n==m-1:
            print(m)
        n+=1
    m+=1