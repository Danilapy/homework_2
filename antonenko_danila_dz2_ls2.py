arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate(arr):
    if s.isdigit():
        arr[i] = f'"{int(s):02d}"'
    elif s[1:].isdigit():
        arr[i] = f'"{s[0]}{int(s[1:]):02d}"'
    print(s, end=' ')
print(arr)
