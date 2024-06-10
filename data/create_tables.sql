CREATE TABLE IF NOT EXISTS area_colhida (
    municipio_id INTEGER,
    municipio_nome TEXT,
    ano INTEGER,
    valor REAL,
    PRIMARY KEY (municipio_id, ano)
);

CREATE TABLE IF NOT EXISTS quantidade_produzida (
    municipio_id INTEGER,
    municipio_nome TEXT,
    ano INTEGER,
    valor REAL,
    PRIMARY KEY (municipio_id, ano)
);

CREATE TABLE IF NOT EXISTS municipios_estados (
    municipio_id INTEGER PRIMARY KEY,
    estado_id INTEGER,
    estado_nome TEXT
);

CREATE VIEW IF NOT EXISTS produtividade AS
SELECT 
    me.estado_nome,
    ac.ano,
    SUM(qp.valor) / SUM(ac.valor) AS produtividade
FROM 
    quantidade_produzida qp
JOIN 
    area_colhida ac ON qp.municipio_id = ac.municipio_id AND qp.ano = ac.ano
JOIN 
    municipios_estados me ON ac.municipio_id = me.municipio_id
GROUP BY 
    me.estado_nome, ac.ano;
