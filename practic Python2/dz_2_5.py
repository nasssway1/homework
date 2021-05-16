a = [57.8, 46.51, 97, 55.81, 56.9, 55, 34.34, 43, 43.43, 56.56, 56, 98.9]
i = 0
a.sort()
while i < len(a):
    b = a[i]
    b = str(b)
    b = [s.strip()  for s in b.split('.') if s.strip()]
    if len(b) > 1:
        o = b[1]
        list(o)
        n=len(list(o))
        p = '0'
        o1 = p+o
        if n == 1:
            print(b[0], "рублей ", o1, "копеек ")
        else:
            print(b[0], "рублей ", b[1], "копеек ")
    else:
        print(b[0], "рублей ","00 копеек ")
    i+=1