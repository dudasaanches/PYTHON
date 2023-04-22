P1 = [7.5, 8.0, 6.5, 9.0, 8.5] # Notas da turma na prova 1
P2 = [8.0, 9.0, 7.0, 8.5, 7.5] # Notas da turma na prova 2

media_p1 = sum(P1) / len(P1) # Calcula a média da turma na prova 1
media_p2 = sum(P2) / len(P2) # Calcula a média da turma na prova 2

if media_p1 > media_p2:
    print("A turma teve melhor média na prova 1: %.2f" % media_p1)
elif media_p2 > media_p1:
    print("A turma teve melhor média na prova 2: %.2f" % media_p2)
else:
    print("A turma teve a mesma média nas duas provas: %.2f" % media_p1)
 