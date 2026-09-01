PRAGMA foreign_keys = ON;

CREATE TABLE DimCliente (
    ClienteKey INTEGER PRIMARY KEY AUTOINCREMENT,
    NombreCompleto TEXT NOT NULL,
    Genero TEXT NOT NULL,
    Ciudad TEXT NOT NULL,
    Segmento TEXT NOT NULL
);

ALTER TABLE HechoVentas
ADD COLUMN ClienteKey INTEGER REFERENCES DimCliente(ClienteKey);
