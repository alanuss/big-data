PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Hechos_Ventas;

CREATE TABLE Hechos_Ventas (
    ID_Venta INTEGER NOT NULL PRIMARY KEY,
    FK_Pelicula INTEGER NOT NULL,
    FK_Sucursal INTEGER NOT NULL,
    FK_Tiempo INTEGER NOT NULL,
    Cantidad_Tickets INTEGER NOT NULL,
    Monto_Total REAL NOT NULL,
    CONSTRAINT FK_HechosVentas_Pelicula
        FOREIGN KEY (FK_Pelicula) REFERENCES Dim_Pelicula(ID_Pelicula),
    CONSTRAINT FK_HechosVentas_Sucursal
        FOREIGN KEY (FK_Sucursal) REFERENCES Dim_Sucursal(ID_Sucursal),
    CONSTRAINT FK_HechosVentas_Tiempo
        FOREIGN KEY (FK_Tiempo) REFERENCES Dim_Tiempo(ID_Tiempo)
);
