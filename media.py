import csv

notas = []

with open("dados.csv") as f:
    reader = csv.DictReader(f)
    for linha in reader:
        notas.append(float(linha["nota"]))

media = sum(notas) / len(notas)

print(media)
