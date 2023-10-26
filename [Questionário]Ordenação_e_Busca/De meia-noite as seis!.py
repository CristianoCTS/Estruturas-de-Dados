monitorando = False
numeroDEtestes = int(input())
for i in range(numeroDEtestes):
    faltou, sobrou = False, False
    plan, studied, faltaram, sobraram = {}, {}, {}, {}
    plano = input()
    matutino = input()
    vespertino = input()
    noturno = input()
    estudado = matutino + vespertino + noturno
    for i in plano:
        if i not in plan:
            plan[i] = 1
        else:
            plan[i] += 1
    for i in estudado:
        if i not in studied:
            studied[i] = 1
        else:
            studied[i] += 1
    #--------------------------------------------------------------------------#
    for i in plan:
        if i in studied:
            if plan[i] > studied[i]:
                sobraram[i] = plan[i] - studied[i]
        else:
            sobraram[i] = plan[i]
    for i in studied:
        if i in plan:
            if studied[i] > plan[i]:
                faltaram[i] = studied[i] - plan[i]
        else:
            faltaram[i] = studied[i]
    if monitorando:
        print("---------------------------------------------------------------")
        print(f"Plano:    {plan}")
        print(f"Cobrado:  {studied}")
        print("---------------------------------------------------------------")
        print(f"Sobraram: {sobraram}")
        print(f"Faltaram: {faltaram}")
        print("---------------------------------------------------------------")
    
    if (len(sobraram) == 0) and (len(faltaram) == 0):
        print("It's in the box!")
    elif (len(sobraram) > 0) and (len(faltaram) == 0):
        aux1, aux2 =[], ""
        for i in sobraram:
            aux1.append(i)
        aux1.sort()
        for i in aux1:
            aux2 += i
        print(f"Bora ralar: {aux2}")
    else:
        print("You died!")