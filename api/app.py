from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('data/agriculture_data.db')
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/area_colhida', methods=['GET'])
def get_area_colhida():
    municipio_id = request.args.get('municipio_id')
    ano = request.args.get('ano')

    result = query_db('''
    SELECT valor FROM area_colhida WHERE municipio_id = ? AND ano = ?
    ''', (municipio_id, ano), one=True)
    
    if result:
        return jsonify({"success": True, "data": result[0], "message": "Dados encontrados"})
    else:
        return jsonify({"success": False, "data": None, "message": "Dados não encontrados"})

@app.route('/produtividade', methods=['GET'])
def get_produtividade():
    estados = request.args.getlist('estado')
    ano = request.args.get('ano')

    placeholders = ','.join('?' * len(estados))
    query = f'''
    SELECT estado_nome, produtividade FROM produtividade WHERE estado_nome IN ({placeholders}) AND ano = ?
    '''
    
    result = query_db(query, (*estados, ano))
    
    if result:
        return jsonify({"success": True, "data": result, "message": "Dados encontrados"})
    else:
        return jsonify({"success": False, "data": None, "message": "Dados não encontrados"})

@app.route('/quantidade_produzida', methods=['GET'])
def get_quantidade_produzida():
    municipios = request.args.getlist('municipio')
    anos = request.args.getlist('ano')

    if len(municipios) * len(anos) > 100:
        return jsonify({"success": False, "data": None, "message": "Número de solicitações excede o limite de 100 dados"})
    
    municipios_placeholders = ','.join('?' * len(municipios
