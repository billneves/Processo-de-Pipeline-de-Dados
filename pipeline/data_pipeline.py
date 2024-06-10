import sqlite3
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def insert_or_update(year):
    conn = sqlite3.connect('data/agriculture_data.db')
    cursor = conn.cursor()

    area_colhida_url = f"https://apisidra.ibge.gov.br/values/t/5457/n6/all/v/216/p/{year}/c782/40124?formato=json"
    quantidade_produzida_url = f"https://apisidra.ibge.gov.br/values/t/5457/n6/all/v/214/p/{year}/c782/40124?formato=json"

    area_colhida_data = fetch_data(area_colhida_url)
    quantidade_produzida_data = fetch_data(quantidade_produzida_url)
    
    if area_colhida_data and quantidade_produzida_data:
        for entry in area_colhida_data:
            municipio_id = entry['D1C']
            municipio_nome = entry['D1N']
            valor = entry['V']
            cursor.execute('''
            INSERT OR REPLACE INTO area_colhida (municipio_id, municipio_nome, ano, valor)
            VALUES (?, ?, ?, ?)
            ''', (municipio_id, municipio_nome, year, valor))

        for entry in quantidade_produzida_data:
            municipio_id = entry['D1C']
            municipio_nome = entry['D1N']
            valor = entry['V']
            cursor.execute('''
            INSERT OR REPLACE INTO quantidade_produzida (municipio_id, municipio_nome, ano, valor)
            VALUES (?, ?, ?, ?)
            ''', (municipio_id, municipio_nome, year, valor))

        conn.commit()
    conn.close()

def delete(year):
    conn = sqlite3.connect('data/agriculture_data.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM area_colhida WHERE ano = ?', (year,))
    cursor.execute('DELETE FROM quantidade_produzida WHERE ano = ?', (year,))

    conn.commit()
    conn.close()
