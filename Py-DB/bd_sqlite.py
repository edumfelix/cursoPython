import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Criando a tabela (schema)
cursor.execute("""
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    peso REAL
  )
  """)

# Inserindo dados na tabela
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#   {"nome": "Marcos", "peso": 90}
#   )
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#   {'id': None, 'nome': 'Fernando', 'peso': 70}
#   )
cursor.execute('UPDATE clientes SET nome = :nome WHERE id = :id',
  {'nome': 'Maria', 'id': 2})
conexao.commit()

cursor.execute('SELECT * FROM clientes')

for c in cursor.fetchall():
  identificador, nome, peso = c
  print(identificador, nome, peso)
cursor.close()
conexao.close()