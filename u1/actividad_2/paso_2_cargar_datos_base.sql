USE Tienda_DW;
GO

INSERT INTO dbo.DimProducto (Nombre, Categoria, Precio) VALUES
('Arroz 1kg', 'Abarrotes', 1800.00),
('Aceite 1L', 'Abarrotes', 2500.00),
('Detergente 3L', 'Limpieza', 5200.00),
('Jabon Liquido', 'Limpieza', 3200.00),
('Leche 1L', 'Lacteos', 1200.00),
('Queso 500g', 'Lacteos', 4500.00),
('Pan Molde', 'Panaderia', 2200.00);

INSERT INTO dbo.DimTiempo (TiempoKey, Fecha, Anio, Mes, MesNumero, Trimestre) VALUES
(20260103, '2026-01-03', 2026, 'Enero', 1, 1),
(20260118, '2026-01-18', 2026, 'Enero', 1, 1),
(20260207, '2026-02-07', 2026, 'Febrero', 2, 1),
(20260321, '2026-03-21', 2026, 'Marzo', 3, 1),
(20260411, '2026-04-11', 2026, 'Abril', 4, 2),
(20260502, '2026-05-02', 2026, 'Mayo', 5, 2),
(20260616, '2026-06-16', 2026, 'Junio', 6, 2),
(20260709, '2026-07-09', 2026, 'Julio', 7, 3),
(20260827, '2026-08-27', 2026, 'Agosto', 8, 3),
(20260912, '2026-09-12', 2026, 'Septiembre', 9, 3),
(20261020, '2026-10-20', 2026, 'Octubre', 10, 4),
(20261105, '2026-11-05', 2026, 'Noviembre', 11, 4);

INSERT INTO dbo.HechoVentas (ProductoKey, TiempoKey, Cantidad, TotalVenta) VALUES
(1, 20260103, 10, 18000.00),
(2, 20260118, 6, 15000.00),
(3, 20260207, 3, 15600.00),
(4, 20260321, 5, 16000.00),
(5, 20260411, 20, 24000.00),
(6, 20260502, 4, 18000.00),
(7, 20260616, 8, 17600.00),
(1, 20260709, 12, 21600.00),
(3, 20260827, 2, 10400.00),
(5, 20260912, 18, 21600.00),
(2, 20261020, 7, 17500.00),
(6, 20261105, 3, 13500.00);
