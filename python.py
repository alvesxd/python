import statistics

# Perguntar a quantidade de alunos
qtd = int(input("Quantos alunos serão cadastrados? "))

# Listas para armazenar os dados
nomes = []
notas = []

# Receber os nomes e notas
for i in range(qtd):
nome = input(f"Nome do aluno {i + 1}: ")
nota = float(input(f"Nota de {nome}: "))
nomes.append(nome)
notas.append(nota)

# Média
media = sum(notas) / len(notas)

# Desvio padrão
desvio_padrao = statistics.stdev(notas)

# Alunos acima da média
acima_media = [nota for nota in notas if nota > media]

# Alunos com nota > 7
maior_que_7 = [nota for nota in notas if nota > 7]

# Aprovados (nota >= 6)
aprovados = [nota for nota in notas if nota >= 6]

# Maior e menor nota
indice_maior = notas.index(max(notas))
indice_menor = notas.index(min(notas))
aluno_maior = nomes[indice_maior]
aluno_menor = nomes[indice_menor]

# Resultados
print("\n--- RESULTADOS ---")
print(f"Média da turma: {media:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Alunos acima da média: {len(acima_media)}")
print(f"Porcentagem de alunos com nota > 7: {(len(maior_que_7) / qtd) * 100:.2f}%")
print(f"Quantidade de aprovados (nota >= 6): {len(aprovados)}")
print(f"Aluno com maior nota: {aluno_maior} ({max(notas)})")
print(f"Aluno com menor nota: {aluno_menor} ({min(notas)})")