arquivo = open("arqText.txt", "w")

arquivo.write("curso py \n")
arquivo.write('aula pratica')
arquivo.close()

#leitura do arquivo texto

leitura=open("arqText.txt", 'r')
print(leitura.read())
leitura.close()

