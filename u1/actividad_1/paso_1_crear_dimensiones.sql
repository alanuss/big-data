IF DB_ID('Cine_DWH') IS NULL
BEGIN
    CREATE DATABASE Cine_DWH;
END;
GO

USE Cine_DWH;
GO

IF OBJECT_ID('dbo.Hechos_Ventas', 'U') IS NOT NULL DROP TABLE dbo.Hechos_Ventas;
IF OBJECT_ID('dbo.Dim_Pelicula', 'U') IS NOT NULL DROP TABLE dbo.Dim_Pelicula;
IF OBJECT_ID('dbo.Dim_Sucursal', 'U') IS NOT NULL DROP TABLE dbo.Dim_Sucursal;
IF OBJECT_ID('dbo.Dim_Tiempo', 'U') IS NOT NULL DROP TABLE dbo.Dim_Tiempo;
GO

CREATE TABLE dbo.Dim_Pelicula (
    ID_Pelicula INT NOT NULL PRIMARY KEY,
    Titulo VARCHAR(100) NOT NULL,
    Genero VARCHAR(50) NOT NULL,
    Clasificacion VARCHAR(10) NOT NULL
);

CREATE TABLE dbo.Dim_Sucursal (
    ID_Sucursal INT NOT NULL PRIMARY KEY,
    Nombre_Cine VARCHAR(100) NOT NULL,
    Ciudad VARCHAR(50) NOT NULL,
    Pais VARCHAR(50) NOT NULL
);

CREATE TABLE dbo.Dim_Tiempo (
    ID_Tiempo INT NOT NULL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Dia INT NOT NULL,
    Mes INT NOT NULL,
    Anio INT NOT NULL,
    Trimestre INT NOT NULL
);
