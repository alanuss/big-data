PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS HechoVentas;
DROP TABLE IF EXISTS DimCliente;
DROP TABLE IF EXISTS DimProducto;
DROP TABLE IF EXISTS DimTiempo;

CREATE TABLE DimProducto (
    ProductoKey INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Categoria TEXT NOT NULL,
    Precio REAL NOT NULL
);

CREATE TABLE DimTiempo (
    TiempoKey INTEGER NOT NULL PRIMARY KEY,
    Fecha TEXT NOT NULL,
    Anio INTEGER NOT NULL,
    Mes TEXT NOT NULL,
    MesNumero INTEGER NOT NULL,
    Trimestre INTEGER NOT NULL
);

CREATE TABLE HechoVentas (
    VentaID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductoKey INTEGER NOT NULL,
    TiempoKey INTEGER NOT NULL,
    Cantidad INTEGER NOT NULL,
    TotalVenta REAL NOT NULL,
    CONSTRAINT FK_HechoVentas_Producto
        FOREIGN KEY (ProductoKey) REFERENCES DimProducto(ProductoKey),
    CONSTRAINT FK_HechoVentas_Tiempo
        FOREIGN KEY (TiempoKey) REFERENCES DimTiempo(TiempoKey)
);
