import sqlite3

def initialize_db():
    conn = sqlite3.connect('data/agriculture_data.db')
    cursor = conn.cursor()
    
    with open('data/create_tables.sql', 'r') as f:
        cursor.executescript(f.read())

    with open('data/municipios_estados.csv', 'r') as f:
        next(f)  # Skip header
        for line in f:
            municipio_id, estado_id, estado_nome = line.strip().split(',')
            cursor.execute('''
            INSERT OR IGNORE INTO municipios_estados (municipio_id, estado_id, estado_nome)
            VALUES (?, ?, ?)
            ''', (municipio_id, estado_id, estado_nome))

    conn.commit()
    conn.close()
