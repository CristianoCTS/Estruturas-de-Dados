inicio_input = input()
termino_input = input()

dia_inicio, horario_inicio = inicio_input.split(" ")
dia_termino, horario_termino = termino_input.split(" ")
hora_inicio, minuto_inicio, segundo_inicio = horario_inicio.split(":")
hora_termino, minuto_termino, segundo_termino = horario_termino.split(":")

dia_inicio = int(dia_inicio)
dia_termino = int(dia_termino)
hora_inicio, minuto_inicio, segundo_inicio = int(hora_inicio), int(minuto_inicio), int(segundo_inicio)
hora_termino, minuto_termino, segundo_termino = int(hora_termino), int(minuto_termino), int(segundo_termino)
inicio = [dia_inicio, hora_inicio, minuto_inicio, segundo_inicio]
termino = [dia_termino, hora_termino, minuto_termino, segundo_termino]

#Verificando as variaveis:
if 0:
    print(f'inicio -> dia: {inicio[0]}, hora: {inicio[1]}, minuto: {inicio[2]}, segundo: {inicio[3]}')
    print(f'termino -> dia: {termino[0]}, hora: {termino[1]}, minuto: {termino[2]}, segundo: {termino[3]}')

#transformando para segundos desde o dia primeiro
tempo_do_mes_ate_o_inicio = ((inicio[0]-1)*24*3600) + (inicio[1]*3600) + (inicio[2]*60) + (inicio[3])
tempo_do_mes_ate_o_termino = ((termino[0]-1)*24*3600) + (termino[1]*3600) + (termino[2]*60) + (termino[3])
duracao_evento = tempo_do_mes_ate_o_termino - tempo_do_mes_ate_o_inicio
if duracao_evento > 0:
    dias = int(duracao_evento/(24*3600))
    horas = int((duracao_evento - (dias*24*3600))/3600)
    minutos = int((duracao_evento - (dias*24*3600) - (horas*3600))/60)
    segundos = int((duracao_evento - (dias*24*3600) - (horas*3600) - (minutos*60)))
    print(f'{dias} dia(s)')
    print(f'{horas} hora(s)')
    print(f'{minutos} minuto(s)')
    print(f'{segundos} segundo(s)')
else:
    print("Data inválida!")