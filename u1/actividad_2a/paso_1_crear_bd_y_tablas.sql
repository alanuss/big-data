IF DB_ID('Hospital_DWH') IS NULL
BEGIN
    CREATE DATABASE Hospital_DWH;
END;
GO

USE Hospital_DWH;
GO

IF OBJECT_ID('dbo.Hechos_Hospitalizaciones', 'U') IS NOT NULL DROP TABLE dbo.Hechos_Hospitalizaciones;
IF OBJECT_ID('dbo.Dim_Paciente', 'U') IS NOT NULL DROP TABLE dbo.Dim_Paciente;
IF OBJECT_ID('dbo.Dim_Doctor', 'U') IS NOT NULL DROP TABLE dbo.Dim_Doctor;
IF OBJECT_ID('dbo.Dim_Diagnostico', 'U') IS NOT NULL DROP TABLE dbo.Dim_Diagnostico;
IF OBJECT_ID('dbo.Dim_Tiempo', 'U') IS NOT NULL DROP TABLE dbo.Dim_Tiempo;
GO

CREATE TABLE dbo.Dim_Paciente (
    PacienteKey INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    NombreCompleto NVARCHAR(120) NOT NULL,
    Edad INT NOT NULL,
    Genero NVARCHAR(20) NOT NULL,
    Ciudad NVARCHAR(60) NOT NULL,
    TipoSeguro NVARCHAR(50) NOT NULL
);

CREATE TABLE dbo.Dim_Doctor (
    DoctorKey INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    NombreCompleto NVARCHAR(120) NOT NULL,
    Especialidad NVARCHAR(80) NOT NULL
);

CREATE TABLE dbo.Dim_Diagnostico (
    DiagnosticoKey INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    CodigoEnfermedad NVARCHAR(20) NOT NULL,
    Descripcion NVARCHAR(150) NOT NULL,
    Gravedad BIT NOT NULL
);

CREATE TABLE dbo.Dim_Tiempo (
    TiempoKey INT NOT NULL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Mes INT NOT NULL,
    NombreMes NVARCHAR(20) NOT NULL,
    Anio INT NOT NULL
);

CREATE TABLE dbo.Hechos_Hospitalizaciones (
    HospitalizacionID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    PacienteKey INT NOT NULL,
    DoctorKey INT NOT NULL,
    DiagnosticoKey INT NOT NULL,
    TiempoKey INT NOT NULL,
    DiasEstancia INT NOT NULL,
    CostoTratamiento DECIMAL(18,2) NOT NULL,
    TiempoEsperaMinutos INT NOT NULL,
    CONSTRAINT FK_Hospitalizaciones_Paciente
        FOREIGN KEY (PacienteKey) REFERENCES dbo.Dim_Paciente(PacienteKey),
    CONSTRAINT FK_Hospitalizaciones_Doctor
        FOREIGN KEY (DoctorKey) REFERENCES dbo.Dim_Doctor(DoctorKey),
    CONSTRAINT FK_Hospitalizaciones_Diagnostico
        FOREIGN KEY (DiagnosticoKey) REFERENCES dbo.Dim_Diagnostico(DiagnosticoKey),
    CONSTRAINT FK_Hospitalizaciones_Tiempo
        FOREIGN KEY (TiempoKey) REFERENCES dbo.Dim_Tiempo(TiempoKey)
);
