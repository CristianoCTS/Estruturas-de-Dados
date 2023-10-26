def trunc (x,p):
    q=10**p
    r = int(x * q)
    y=float(r / q)
    return y
#--------------------------------------------------------------------------------------------------------------
def cIRA(x):
    materias=[]
    materias=input('Materias matriculadas:').split(' ')
    p=0
    while (p<len(materias)):
        print('Menção, Créditos e Número de períodos de', materias[p])
        print('SS=5 MS=4 MM=3 MI=2 II=1 SR=0')
        materias[p]=input().split(' ')
        materias[p]=[int(materias[p][x]) for x in range(len(materias[p]))]
        p=p+1
    p=0
    numerador=0
    denominador=0
    while (p<len(materias)):
        numerador=numerador+(materias[p][0]*materias[p][1]*materias[p][2])
        denominador=denominador+(materias[p][1]*materias[p][2])
        p=p+1
    materias=[]
    ira2p=numerador/denominador
    DTb=int(input('Número de disciplinas obrigatórias trancadas:'))
    DTp=int(input('Número de disciplinas optativas trancadas:'))
    DC=int(input('Número de disciplinas matriculadas (incluindo as trancadas):'))
    ira1p=1-(((0.6*DTb)+(0.4*DTp))/DC)
    ira=ira1p*ira2p
    return ira

#--------------------------------------------------------------------------------------------------------------
def qs(matricula, ano, semestre):
    ma,an,se=[str(x) for x in (matricula,ano,semestre)]
    semestres=((int(an)-2000-int(ma[0:2]))*2)-(int(ma[3])-(int(se)-1))
    return semestres

#Matrícula e data ---------------------------------------------------------------------------------------------
    
matricula=int(input('Matricula:'))
while not(1000000000>matricula>99999999):
    print('Número de matricula invalido, digite novamente')
    matricula=int(input('Matricula:'))
#-------------------------------------------------------------------------------------------------------------- 
dia, mes, ano=input('Data:').split('/')
dia, mes, ano =[int(x) for x in (dia, mes, ano)]
while not(0<dia<32 or 0<mes<13 or 1999<ano<2100):
    print('Data invalida, digite novamente')
    dia, mes, ano=input('Data:').split('/')
    dia, mes, ano =[int(x) for x in (dia, mes, ano)]
#-------------------------------------------------------------------------------------------------------------- 
semestre=int(input('Semestre:'))-1
while not(-1<semestre<2):
    print('Semestre invalido, digite novamente')
    semestre=int(input('Semestre:'))-1
    
#Resultados ---------------------------------------------------------------------------------------------
    
x=cIRA(7)
print(' ')
print('---------------')
print('Semestres:', qs(matricula, ano, semestre))
print('IRA:', trunc(x,0))
print('---------------')
