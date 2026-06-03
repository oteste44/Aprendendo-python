notas = [ ['joao', 2.3, 3.3],
          ['mario', 5.7, 8.0],
          ['beto', 9.0, 7.0]

]
mediaAlunos = []
for i in notas:
    media = (i[1] + i[2])/2
    lista = (i[0],media)
    mediaAlunos.append(lista)
print(f'lista de notas do alunos: {notas}')
print(f'lista de media de alunos:{mediaAlunos}')