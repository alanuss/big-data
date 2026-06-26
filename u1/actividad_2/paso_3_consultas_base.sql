USE Tienda_DW;
GO

-- Ranking de ventas por categoria de producto.
SELECT
    p.Categoria,
    SUM(h.TotalVenta) AS TotalVentas,
    SUM(h.Cantidad) AS UnidadesVendidas
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimProducto AS p
    ON h.ProductoKey = p.ProductoKey
GROUP BY p.Categoria
ORDER BY TotalVentas DESC;

-- Ventas por mes para ver tendencias.
SELECT
    t.Anio,
    t.Mes,
    SUM(h.TotalVenta) AS VentaMensual
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimTiempo AS t
    ON h.TiempoKey = t.TiempoKey
GROUP BY t.Anio, t.MesNumero, t.Mes
ORDER BY t.Anio, t.MesNumero;

-- Ventas por periodo: anio y mes.
SELECT
    t.Anio,
    t.Mes,
    COUNT(h.VentaID) AS TotalTransacciones,
    SUM(h.TotalVenta) AS TotalVendido
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimTiempo AS t
    ON h.TiempoKey = t.TiempoKey
GROUP BY t.Anio, t.MesNumero, t.Mes
ORDER BY t.Anio, t.MesNumero;
