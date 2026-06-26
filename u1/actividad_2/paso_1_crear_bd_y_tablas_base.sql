IF DB_ID('Tienda_DW') IS NULL
BEGIN
    CREATE DATABASE Tienda_DW;
END;
GO

USE Tienda_DW;
GO

IF OBJECT_ID('dbo.HechoVentas', 'U') IS NOT NULL DROP TABLE dbo.HechoVentas;
IF OBJECT_ID('dbo.DimCliente', 'U') IS NOT NULL DROP TABLE dbo.DimCliente;
IF OBJECT_ID('dbo.DimProducto', 'U') IS NOT NULL DROP TABLE dbo.DimProducto;
IF OBJECT_ID('dbo.DimTiempo', 'U') IS NOT NULL DROP TABLE dbo.DimTiempo;
GO

CREATE TABLE dbo.DimProducto (
    ProductoKey INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Categoria NVARCHAR(50) NOT NULL,
    Precio DECIMAL(10,2) NOT NULL
);

CREATE TABLE dbo.DimTiempo (
    TiempoKey INT NOT NULL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Anio INT NOT NULL,
    Mes NVARCHAR(20) NOT NULL,
    MesNumero INT NOT NULL,
    Trimestre INT NOT NULL
);

CREATE TABLE dbo.HechoVentas (
    VentaID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    ProductoKey INT NOT NULL,
    TiempoKey INT NOT NULL,
    Cantidad INT NOT NULL,
    TotalVenta DECIMAL(18,2) NOT NULL,
    CONSTRAINT FK_HechoVentas_Producto
        FOREIGN KEY (ProductoKey) REFERENCES dbo.DimProducto(ProductoKey),
    CONSTRAINT FK_HechoVentas_Tiempo
        FOREIGN KEY (TiempoKey) REFERENCES dbo.DimTiempo(TiempoKey)
);
