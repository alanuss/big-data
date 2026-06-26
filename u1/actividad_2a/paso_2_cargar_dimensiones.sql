USE Hospital_DWH;
GO

INSERT INTO dbo.Dim_Paciente (NombreCompleto, Edad, Genero, Ciudad, TipoSeguro) VALUES
('Lucas Marin', 8, 'Masculino', 'Santiago', 'Fonasa'),
('Sofia Vega', 14, 'Femenino', 'Valparaiso', 'Isapre'),
('Ana Morales', 34, 'Femenino', 'Concepcion', 'Fonasa'),
('Pedro Fuentes', 45, 'Masculino', 'Temuco', 'Isapre'),
('Elena Castro', 72, 'Femenino', 'Santiago', 'Fonasa'),
('Roberto Silva', 81, 'Masculino', 'Valdivia', 'Fonasa'),
('Camila Rios', 29, 'Femenino', 'Puerto Montt', 'Isapre'),
('Miguel Araya', 67, 'Masculino', 'Concepcion', 'Fonasa');

INSERT INTO dbo.Dim_Doctor (NombreCompleto, Especialidad) VALUES
('Dra. Paula Herrera', 'Cardiologia'),
('Dr. Andres Soto', 'Pediatria'),
('Dra. Fernanda Lopez', 'Traumatologia'),
('Dr. Marco Diaz', 'Medicina Interna'),
('Dra. Claudia Perez', 'Neurologia'),
('Dr. Nicolas Rojas', 'Urgencia');

INSERT INTO dbo.Dim_Diagnostico (CodigoEnfermedad, Descripcion, Gravedad) VALUES
('I21', 'Infarto agudo al miocardio', 1),
('J18', 'Neumonia', 1),
('S72', 'Fractura de femur', 1),
('J06', 'Infeccion respiratoria alta', 0),
('E11', 'Diabetes tipo 2 descompensada', 1),
('G43', 'Migrana', 0),
('K35', 'Apendicitis aguda', 1),
('A09', 'Gastroenteritis', 0);

INSERT INTO dbo.Dim_Tiempo (TiempoKey, Fecha, Mes, NombreMes, Anio) VALUES
(20260105, '2026-01-05', 1, 'Enero', 2026),
(20260211, '2026-02-11', 2, 'Febrero', 2026),
(20260308, '2026-03-08', 3, 'Marzo', 2026),
(20260417, '2026-04-17', 4, 'Abril', 2026),
(20260522, '2026-05-22', 5, 'Mayo', 2026),
(20260613, '2026-06-13', 6, 'Junio', 2026),
(20260719, '2026-07-19', 7, 'Julio', 2026),
(20260804, '2026-08-04', 8, 'Agosto', 2026),
(20260916, '2026-09-16', 9, 'Septiembre', 2026),
(20261009, '2026-10-09', 10, 'Octubre', 2026),
(20261127, '2026-11-27', 11, 'Noviembre', 2026),
(20261203, '2026-12-03', 12, 'Diciembre', 2026);
