USE Hospital_DWH;
GO

-- 1. Especialidad mas costosa y con mas dias de estancia.
SELECT TOP (1)
    d.Especialidad,
    SUM(h.CostoTratamiento) AS CostoTotal,
    SUM(h.DiasEstancia) AS DiasTotalesEstancia,
    COUNT(h.HospitalizacionID) AS Atenciones
FROM dbo.Hechos_Hospitalizaciones AS h
INNER JOIN dbo.Dim_Doctor AS d
    ON h.DoctorKey = d.DoctorKey
GROUP BY d.Especialidad
ORDER BY CostoTotal DESC, DiasTotalesEstancia DESC;

-- 2. Comparacion entre ninos y adultos mayores atendidos.
SELECT
    CASE
        WHEN p.Edad < 18 THEN 'Ninos'
        WHEN p.Edad >= 65 THEN 'Adultos mayores'
    END AS GrupoEdad,
    COUNT(h.HospitalizacionID) AS TotalAtenciones
FROM dbo.Hechos_Hospitalizaciones AS h
INNER JOIN dbo.Dim_Paciente AS p
    ON h.PacienteKey = p.PacienteKey
WHERE p.Edad < 18 OR p.Edad >= 65
GROUP BY
    CASE
        WHEN p.Edad < 18 THEN 'Ninos'
        WHEN p.Edad >= 65 THEN 'Adultos mayores'
    END
ORDER BY TotalAtenciones DESC;

-- 3. Doctor que realiza mas atenciones mensualmente.
WITH AtencionesDoctorMes AS (
    SELECT
        t.Anio,
        t.Mes,
        t.NombreMes,
        d.NombreCompleto AS Doctor,
        COUNT(h.HospitalizacionID) AS TotalAtenciones,
        ROW_NUMBER() OVER (
            PARTITION BY t.Anio, t.Mes
            ORDER BY COUNT(h.HospitalizacionID) DESC
        ) AS RankingMensual
    FROM dbo.Hechos_Hospitalizaciones AS h
    INNER JOIN dbo.Dim_Doctor AS d
        ON h.DoctorKey = d.DoctorKey
    INNER JOIN dbo.Dim_Tiempo AS t
        ON h.TiempoKey = t.TiempoKey
    GROUP BY t.Anio, t.Mes, t.NombreMes, d.NombreCompleto
)
SELECT
    Anio,
    NombreMes,
    Doctor,
    TotalAtenciones
FROM AtencionesDoctorMes
WHERE RankingMensual = 1
ORDER BY Anio, Mes;

-- 4. Genero mas atendido por gravedad.
SELECT
    CASE WHEN dg.Gravedad = 1 THEN 'Grave' ELSE 'No grave' END AS NivelGravedad,
    p.Genero,
    COUNT(h.HospitalizacionID) AS TotalAtenciones
FROM dbo.Hechos_Hospitalizaciones AS h
INNER JOIN dbo.Dim_Paciente AS p
    ON h.PacienteKey = p.PacienteKey
INNER JOIN dbo.Dim_Diagnostico AS dg
    ON h.DiagnosticoKey = dg.DiagnosticoKey
GROUP BY dg.Gravedad, p.Genero
ORDER BY NivelGravedad, TotalAtenciones DESC;

-- 5. Enfermedad mas atendida en los primeros 6 meses.
SELECT TOP (1)
    dg.CodigoEnfermedad,
    dg.Descripcion,
    COUNT(h.HospitalizacionID) AS TotalAtenciones
FROM dbo.Hechos_Hospitalizaciones AS h
INNER JOIN dbo.Dim_Diagnostico AS dg
    ON h.DiagnosticoKey = dg.DiagnosticoKey
INNER JOIN dbo.Dim_Tiempo AS t
    ON h.TiempoKey = t.TiempoKey
WHERE t.Mes BETWEEN 1 AND 6
GROUP BY dg.CodigoEnfermedad, dg.Descripcion
ORDER BY TotalAtenciones DESC;

-- 6. Costo total facturado por mes en el ultimo anio cargado.
SELECT
    t.Anio,
    t.NombreMes,
    SUM(h.CostoTratamiento) AS CostoTotalFacturado
FROM dbo.Hechos_Hospitalizaciones AS h
INNER JOIN dbo.Dim_Tiempo AS t
    ON h.TiempoKey = t.TiempoKey
WHERE t.Anio = (SELECT MAX(Anio) FROM dbo.Dim_Tiempo)
GROUP BY t.Anio, t.Mes, t.NombreMes
ORDER BY t.Anio, t.Mes;

-- 7. Promedio de estancia por especialidad medica.
SELECT
    d.Especialidad,
    AVG(CAST(h.DiasEstancia AS DECIMAL(10,2))) AS PromedioDiasEstancia
FROM dbo.Hechos_Hospitalizaciones AS h
INNER JOIN dbo.Dim_Doctor AS d
    ON h.DoctorKey = d.DoctorKey
GROUP BY d.Especialidad
ORDER BY PromedioDiasEstancia DESC;

-- 8. Cinco diagnosticos mas comunes del hospital.
SELECT TOP (5)
    dg.CodigoEnfermedad,
    dg.Descripcion,
    COUNT(h.HospitalizacionID) AS TotalAtenciones
FROM dbo.Hechos_Hospitalizaciones AS h
INNER JOIN dbo.Dim_Diagnostico AS dg
    ON h.DiagnosticoKey = dg.DiagnosticoKey
GROUP BY dg.CodigoEnfermedad, dg.Descripcion
ORDER BY TotalAtenciones DESC;
