a=[[], [], [], [], []]
b=[]
c=[[], [], [], [], []]
a[0]=input('Digite o gabarito do aluno 1:').split(' ')
a[1]=input('Digite o gabarito do aluno 2:').split(' ')
a[2]=input('Digite o gabarito do aluno 3:').split(' ')
a[3]=input('Digite o gabarito do aluno 4:').split(' ')
a[4]=input('Digite o gabarito do aluno 5:').split(' ')
b=input('Digite o gabarito:').split(' ')
p=-1
while (p<4):
    p=p+1
    q=-1
    rem=0
    while (q<9):
        q=q+1
        if (a[p][q]==b[q]):
            rem=rem+1
        c[p]=rem
v=0
while (v<5):
    v=v+1
    print('A nota do aluno', v, 'é' ,c[v-1])
#50 minutos
