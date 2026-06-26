USE Cine_DWH;
GO

IF OBJECT_ID('dbo.Hechos_Ventas', 'U') IS NOT NULL DROP TABLE dbo.Hechos_Ventas;
GO

CREATE TABLE dbo.Hechos_Ventas (
    ID_Venta INT NOT NULL PRIMARY KEY,
    FK_Pelicula INT NOT NULL,
    FK_Sucursal INT NOT NULL,
    FK_Tiempo INT NOT NULL,
    Cantidad_Tickets INT NOT NULL,
    Monto_Total DECIMAL(10,2) NOT NULL,
    CONSTRAINT FK_HechosVentas_Pelicula
        FOREIGN KEY (FK_Pelicula) REFERENCES dbo.Dim_Pelicula(ID_Pelicula),
    CONSTRAINT FK_HechosVentas_Sucursal
        FOREIGN KEY (FK_Sucursal) REFERENCES dbo.Dim_Sucursal(ID_Sucursal),
    CONSTRAINT FK_HechosVentas_Tiempo
        FOREIGN KEY (FK_Tiempo) REFERENCES dbo.Dim_Tiempo(ID_Tiempo)
);
