CREATE TABLE IF NOT EXISTS Acoes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) UNIQUE NOT NULL,
    description VARCHAR(256),
    status BOOL
);

CREATE TABLE IF NOT EXISTS Cotacoes (
    id SERIAL PRIMARY KEY,
    value REAL,
    creation_date DATE,
    update_date DATE
);

ALTER TABLE Acoes
    ADD CONSTRAINT fk_creation_date_cotacoes
    FOREIGN KEY (price_creation_date)
        REFERENCES Cotacoes(creation_date),
    ADD CONSTRAINT fk_update_date_cotacoes
    FOREIGN KEY (price_update_date)
        REFERENCES Cotacoes(update_date);

ALTER TABLE Cotacoes
    ADD CONSTRAINT fk_stock_id_acoes
    FOREIGN KEY (stock_id)
        REFERENCES Acoes(id);
