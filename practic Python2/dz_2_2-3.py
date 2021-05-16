a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(a)

def get_plus(a):
    if a[0] in '+':
        return a[0]

i=0

while i < len(a):
    y=get_plus(a[i])
    if a[i].isdigit() or (y and a[i][1:].isdigit()):
        if y:
            a[i] = y + a[i][1:].zfill(2)
        else:
            a[i] = a[i].zfill(2)
        a.insert(i, '"')
        a.insert(i + 2, '"')
        i+=2

    i+=1
string = ' '.join(a)
print(string)