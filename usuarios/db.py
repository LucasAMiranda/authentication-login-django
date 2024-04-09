import sqlite3

# Se o arquivo não existir ele cria e conecta, senão só conecta
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# Seleciona os dados da tabela do banco de dados e imprime na tela
for row in cur.execute('SELECT * FROM usuarios'):
    print(row[0])
 # criei isso só para formatar a saída para dd/mm/yyyy
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    #print(row)
con.close()