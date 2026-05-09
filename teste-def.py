def media(num):
    return sum(num) / len(num)

def maior(num):
    m = num[0]
    for n in num:
        if n > m:
            m = n
    return m

def menor(num):
    m = num[0]
    for n in num:
        if n < m:
            m = n
    return m

num = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    num.append(numero)

m_media = media(num)
m_maior = maior(num)
m_menor = menor(num)

print(f"Média: {m_media}\nMaior: {m_maior}\nMenor: {m_menor}")