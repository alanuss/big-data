PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Hechos_Hospitalizaciones;
DROP TABLE IF EXISTS Dim_Paciente;
DROP TABLE IF EXISTS Dim_Doctor;
DROP TABLE IF EXISTS Dim_Diagnostico;
DROP TABLE IF EXISTS Dim_Tiempo;

CREATE TABLE Dim_Paciente (
    PacienteKey INTEGER PRIMARY KEY AUTOINCREMENT,
    NombreCompleto TEXT NOT NULL,
    Edad INTEGER NOT NULL,
    Genero TEXT NOT NULL,
    Ciudad TEXT NOT NULL,
    TipoSeguro TEXT NOT NULL
);

CREATE TABLE Dim_Doctor (
    DoctorKey INTEGER PRIMARY KEY AUTOINCREMENT,
    NombreCompleto TEXT NOT NULL,
    Especialidad TEXT NOT NULL
);

CREATE TABLE Dim_Diagnostico (
    DiagnosticoKey INTEGER PRIMARY KEY AUTOINCREMENT,
    CodigoEnfermedad TEXT NOT NULL,
    Descripcion TEXT NOT NULL,
    Gravedad INTEGER NOT NULL
);

CREATE TABLE Dim_Tiempo (
    TiempoKey INTEGER NOT NULL PRIMARY KEY,
    Fecha TEXT NOT NULL,
    Mes INTEGER NOT NULL,
    NombreMes TEXT NOT NULL,
    Anio INTEGER NOT NULL
);

CREATE TABLE Hechos_Hospitalizaciones (
    HospitalizacionID INTEGER PRIMARY KEY AUTOINCREMENT,
    PacienteKey INTEGER NOT NULL,
    DoctorKey INTEGER NOT NULL,
    DiagnosticoKey INTEGER NOT NULL,
    TiempoKey INTEGER NOT NULL,
    DiasEstancia INTEGER NOT NULL,
    CostoTratamiento REAL NOT NULL,
    TiempoEsperaMinutos INTEGER NOT NULL,
    CONSTRAINT FK_Hospitalizaciones_Paciente
        FOREIGN KEY (PacienteKey) REFERENCES Dim_Paciente(PacienteKey),
    CONSTRAINT FK_Hospitalizaciones_Doctor
        FOREIGN KEY (DoctorKey) REFERENCES Dim_Doctor(DoctorKey),
    CONSTRAINT FK_Hospitalizaciones_Diagnostico
        FOREIGN KEY (DiagnosticoKey) REFERENCES Dim_Diagnostico(DiagnosticoKey),
    CONSTRAINT FK_Hospitalizaciones_Tiempo
        FOREIGN KEY (TiempoKey) REFERENCES Dim_Tiempo(TiempoKey)
);
