USE Tienda_DW;
GO

-- A. Dinero ganado por categoria en el primer trimestre.
SELECT
    p.Categoria,
    SUM(h.TotalVenta) AS IngresosTotales,
    SUM(h.Cantidad) AS UnidadesVendidas
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimProducto AS p
    ON h.ProductoKey = p.ProductoKey
INNER JOIN dbo.DimTiempo AS t
    ON h.TiempoKey = t.TiempoKey
WHERE t.Trimestre = 1
GROUP BY p.Categoria
ORDER BY IngresosTotales DESC;

-- B. Ranking de ventas por categoria.
SELECT
    p.Categoria,
    SUM(h.TotalVenta) AS GranTotal,
    COUNT(h.VentaID) AS NumeroDeTransacciones
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimProducto AS p
    ON h.ProductoKey = p.ProductoKey
GROUP BY p.Categoria
ORDER BY GranTotal DESC;

-- C. Ventas por mes para ver tendencias.
SELECT
    t.Anio,
    t.Mes,
    SUM(h.TotalVenta) AS VentaMensual
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimTiempo AS t
    ON h.TiempoKey = t.TiempoKey
GROUP BY t.Anio, t.MesNumero, t.Mes
ORDER BY t.Anio, t.MesNumero;

-- D. Productos estrella y productos con bajo movimiento, sin mostrar IDs.
SELECT
    p.Nombre AS Producto,
    p.Categoria,
    SUM(h.Cantidad) AS UnidadesVendidas,
    SUM(h.TotalVenta) AS IngresosTotales,
    CASE
        WHEN SUM(h.Cantidad) >= 8 THEN 'Producto estrella'
        WHEN SUM(h.Cantidad) BETWEEN 3 AND 7 THEN 'Movimiento medio'
        ELSE 'Bajo movimiento'
    END AS PerfilProducto
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimProducto AS p
    ON h.ProductoKey = p.ProductoKey
GROUP BY p.Nombre, p.Categoria
ORDER BY UnidadesVendidas DESC, IngresosTotales DESC;

-- E. Ventas por periodo: anio, trimestre y mes.
SELECT
    t.Anio,
    t.Trimestre,
    t.Mes,
    SUM(h.TotalVenta) AS TotalVendido,
    COUNT(h.VentaID) AS TotalTransacciones
FROM dbo.HechoVentas AS h
INNER JOIN dbo.DimTiempo AS t
    ON h.TiempoKey = t.TiempoKey
GROUP BY t.Anio, t.Trimestre, t.MesNumero, t.Mes
ORDER BY t.Anio, t.Trimestre, t.MesNumero;
