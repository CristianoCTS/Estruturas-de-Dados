letras_diferentes = 0
possivel_palindrome = input()
for i in range(int(len(possivel_palindrome)/2)):
#    print(f'{possivel_palindrome[i]} == {possivel_palindrome[-(i+1)]} -> {possivel_palindrome[i] == possivel_palindrome[-(i+1)]}')
    if possivel_palindrome[i] != possivel_palindrome[-(i+1)]:
        letras_diferentes += 1
if (len(possivel_palindrome) % 2 == 0):
    if letras_diferentes == 1:
        print("POSSÍVEL")
    else:
        print("IMPOSSÍVEL")
else:
    if letras_diferentes <= 1:
        print("POSSÍVEL")
    else:
        print("IMPOSSÍVEL")
