USE Tienda_DW;
GO

INSERT INTO dbo.DimProducto (Nombre, Categoria, PrecioUnitario) VALUES
('iPhone 15', 'Telefonia', 900.00),
('Samsung Galaxy S24', 'Telefonia', 850.00),
('MacBook Air M2', 'Computacion', 1100.00),
('Dell XPS 13', 'Computacion', 1000.00),
('Monitor LG 27', 'Accesorios', 300.00),
('Teclado Mecanico RGB', 'Accesorios', 80.00),
('Audifonos Bluetooth', 'Accesorios', 120.00);

INSERT INTO dbo.DimTiempo (TiempoKey, Fecha, Anio, Mes, MesNumero, Trimestre, Semestre) VALUES
(20260101, '2026-01-01', 2026, 'Enero', 1, 1, 1),
(20260115, '2026-01-15', 2026, 'Enero', 1, 1, 1),
(20260205, '2026-02-05', 2026, 'Febrero', 2, 1, 1),
(20260310, '2026-03-10', 2026, 'Marzo', 3, 1, 1),
(20260403, '2026-04-03', 2026, 'Abril', 4, 2, 1),
(20260518, '2026-05-18', 2026, 'Mayo', 5, 2, 1),
(20260622, '2026-06-22', 2026, 'Junio', 6, 2, 1),
(20260714, '2026-07-14', 2026, 'Julio', 7, 3, 2),
(20260809, '2026-08-09', 2026, 'Agosto', 8, 3, 2),
(20260925, '2026-09-25', 2026, 'Septiembre', 9, 3, 2),
(20261012, '2026-10-12', 2026, 'Octubre', 10, 4, 2),
(20261120, '2026-11-20', 2026, 'Noviembre', 11, 4, 2),
(20261206, '2026-12-06', 2026, 'Diciembre', 12, 4, 2);
