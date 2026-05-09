def media(notas):
        return sum(notas) / len(notas)

def situacao(m):

        if m >= 6:
            return "aprovado"
        elif m>= 4:
            return "recuperação"
        else:
            return "reprovado"

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

m = media(notas)

print(f"Média {m}\nSituação: {situacao(m)}")