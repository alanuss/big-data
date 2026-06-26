USE Tienda_DW;
GO

INSERT INTO dbo.DimCliente (NombreCompleto, Genero, Ciudad, Segmento) VALUES
('Ana Torres', 'Femenino', 'Santiago', 'premium'),
('Carlos Diaz', 'Masculino', 'Valparaiso', 'regular'),
('Maria Rojas', 'Femenino', 'Concepcion', 'nuevo'),
('Jorge Perez', 'Masculino', 'Santiago', 'premium'),
('Camila Soto', 'Femenino', 'Temuco', 'regular'),
('Felipe Herrera', 'Masculino', 'Concepcion', 'nuevo');

UPDATE dbo.HechoVentas SET ClienteKey = 1 WHERE VentaID IN (1, 5, 8);
UPDATE dbo.HechoVentas SET ClienteKey = 2 WHERE VentaID IN (2, 9);
UPDATE dbo.HechoVentas SET ClienteKey = 3 WHERE VentaID IN (3, 10);
UPDATE dbo.HechoVentas SET ClienteKey = 4 WHERE VentaID IN (4, 11);
UPDATE dbo.HechoVentas SET ClienteKey = 5 WHERE VentaID IN (6, 12);
UPDATE dbo.HechoVentas SET ClienteKey = 6 WHERE VentaID IN (7);

-- Ranking de ventas totales por ciudad y genero.
SELECT
    c.Ciudad,
    c.Genero,
    SUM(h.TotalVenta) AS TotalVentas,
    COUNT(h.VentaID) AS Transacciones
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimCliente AS c
    ON h.ClienteKey = c.ClienteKey
GROUP BY c.Ciudad, c.Genero
ORDER BY TotalVentas DESC;

-- Mejor cliente segun monto total comprado.
SELECT TOP (1)
    c.NombreCompleto,
    c.Ciudad,
    c.Segmento,
    SUM(h.TotalVenta) AS TotalComprado,
    SUM(h.Cantidad) AS UnidadesCompradas,
    COUNT(h.VentaID) AS Transacciones
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimCliente AS c
    ON h.ClienteKey = c.ClienteKey
GROUP BY c.NombreCompleto, c.Ciudad, c.Segmento
ORDER BY TotalComprado DESC;
