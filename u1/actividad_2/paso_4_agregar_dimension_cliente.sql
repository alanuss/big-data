USE Tienda_DW;
GO

CREATE TABLE dbo.DimCliente (
    ClienteKey INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    NombreCompleto NVARCHAR(120) NOT NULL,
    Genero NVARCHAR(20) NOT NULL,
    Ciudad NVARCHAR(60) NOT NULL,
    Segmento NVARCHAR(20) NOT NULL
);

ALTER TABLE dbo.HechoVentas
ADD ClienteKey INT NULL;
GO

ALTER TABLE dbo.HechoVentas
ADD CONSTRAINT FK_HechoVentas_Cliente
    FOREIGN KEY (ClienteKey) REFERENCES dbo.DimCliente(ClienteKey);
