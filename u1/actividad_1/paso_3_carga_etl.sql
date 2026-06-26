USE Cine_DWH;
GO

INSERT INTO dbo.Dim_Pelicula (ID_Pelicula, Titulo, Genero, Clasificacion) VALUES
(1, 'The Batman', 'Accion', 'PG-13'),
(2, 'Duna Parte Dos', 'Ciencia Ficcion', 'PG-13'),
(3, 'Intensamente 2', 'Animacion', 'TE'),
(4, 'El Conjuro', 'Terror', 'R'),
(5, 'Gladiador 2', 'Accion', 'PG-13');

INSERT INTO dbo.Dim_Sucursal (ID_Sucursal, Nombre_Cine, Ciudad, Pais) VALUES
(1, 'Cinepolis Central', 'Punta Arenas', 'Chile'),
(2, 'Cinepolis Costanera', 'Santiago', 'Chile'),
(3, 'Cinepolis Puerto', 'Valparaiso', 'Chile'),
(4, 'Cinepolis BioBio', 'Concepcion', 'Chile');

INSERT INTO dbo.Dim_Tiempo (ID_Tiempo, Fecha, Dia, Mes, Anio, Trimestre) VALUES
(20250105, '2025-01-05', 5, 1, 2025, 1),
(20250214, '2025-02-14', 14, 2, 2025, 1),
(20250312, '2025-03-12', 12, 3, 2025, 1),
(20250515, '2025-05-15', 15, 5, 2025, 2),
(20250720, '2025-07-20', 20, 7, 2025, 3),
(20251210, '2025-12-10', 10, 12, 2025, 4);

INSERT INTO dbo.Hechos_Ventas
    (ID_Venta, FK_Pelicula, FK_Sucursal, FK_Tiempo, Cantidad_Tickets, Monto_Total)
VALUES
(1001, 1, 1, 20250515, 2, 15000.00),
(1002, 2, 2, 20250105, 5, 42500.00),
(1003, 3, 2, 20250214, 8, 52000.00),
(1004, 4, 3, 20250312, 3, 24000.00),
(1005, 5, 4, 20250515, 4, 36000.00),
(1006, 1, 2, 20250720, 6, 51000.00),
(1007, 2, 1, 20251210, 2, 18000.00),
(1008, 3, 3, 20250720, 7, 45500.00),
(1009, 4, 4, 20251210, 4, 32000.00),
(1010, 5, 2, 20250312, 5, 45000.00),
(1011, 2, 3, 20250515, 3, 25500.00),
(1012, 1, 4, 20250214, 2, 17000.00);
