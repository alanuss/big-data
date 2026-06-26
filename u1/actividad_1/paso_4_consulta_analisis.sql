USE Cine_DWH;
GO

SELECT
    p.Genero,
    s.Ciudad,
    SUM(v.Monto_Total) AS Ingresos_Totales,
    SUM(v.Cantidad_Tickets) AS Tickets_Vendidos
FROM dbo.Hechos_Ventas AS v
INNER JOIN dbo.Dim_Pelicula AS p
    ON v.FK_Pelicula = p.ID_Pelicula
INNER JOIN dbo.Dim_Sucursal AS s
    ON v.FK_Sucursal = s.ID_Sucursal
GROUP BY
    p.Genero,
    s.Ciudad
ORDER BY
    p.Genero,
    Ingresos_Totales DESC;
