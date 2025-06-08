
-- -----------------------------------------------------
-- Base de Datos: Hélice - Sistema de gestión de pasajes aéreos
-- -----------------------------------------------------
-- *** PARA ENTORNO DE PRUEBAS ***
-- Elimina la base existente y la recrea limpia:
DROP DATABASE IF EXISTS helice;
CREATE DATABASE helice;
USE helice;


-- -----------------------------------------------------
-- Tabla: Cliente
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    razon_social VARCHAR(100),
    cuit VARCHAR(20) UNIQUE,
    correo VARCHAR(100)
);

-- -----------------------------------------------------
-- Tabla: Usuario
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    rol VARCHAR(50)
);

-- -----------------------------------------------------
-- Tabla: Destino
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Destino (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(100),
    pais VARCHAR(100),
    costo_base DECIMAL(10,2)
);

-- -----------------------------------------------------
-- Tabla: Venta
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Venta (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_usuario INT,
    fecha_venta DATETIME,
    estado ENUM('Activa', 'Anulada'),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- -----------------------------------------------------
-- Tabla: Pasaje
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Pasaje (
    id_pasaje INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT,
    id_destino INT,
    fecha_viaje DATE,
    costo_final DECIMAL(10,2),
    FOREIGN KEY (id_venta) REFERENCES Venta(id_venta),
    FOREIGN KEY (id_destino) REFERENCES Destino(id_destino)
);

-- -----------------------------------------------------
-- Tabla: Anulacion
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Anulacion (
    id_anulacion INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT UNIQUE,
    fecha_anulacion DATETIME,
    motivo VARCHAR(255),
    FOREIGN KEY (id_venta) REFERENCES Venta(id_venta)
);

-- -----------------------------------------------------
-- Inserción de datos de ejemplo
-- -----------------------------------------------------

-- Clientes
INSERT INTO Cliente (razon_social, cuit, correo) VALUES
('Empresa Alfa', '20-12345678-9', 'contacto@alfa.com'),
('Empresa Beta', '27-87654321-0', 'info@beta.com'),
('Empresa Gamma', '30-11223344-5', 'ventas@gamma.com');

-- Usuarios
INSERT INTO Usuario (nombre, correo, rol) VALUES
('Ana Torres', 'ana@helice.com', 'Administrador'),
('Luis Gómez', 'luis@helice.com', 'Vendedor'),
('Clara Díaz', 'clara@helice.com', 'Soporte');

-- Destinos
INSERT INTO Destino (ciudad, pais, costo_base) VALUES
('Salta', 'Argentina', 50000),
('Santiago', 'Chile', 80000),
('São Paulo', 'Brasil', 95000);

-- Ventas
INSERT INTO Venta (id_cliente, id_usuario, fecha_venta, estado) VALUES
(1, 1, '2025-06-01 14:00:00', 'Activa'),
(2, 2, '2025-06-02 15:30:00', 'Activa'),
(3, 3, '2025-06-03 16:45:00', 'Anulada');

-- Pasajes
INSERT INTO Pasaje (id_venta, id_destino, fecha_viaje, costo_final) VALUES
(1, 1, '2025-07-01', 52000),
(2, 2, '2025-07-05', 83000),
(3, 3, '2025-07-10', 97000);

-- Anulaciones
INSERT INTO Anulacion (id_venta, fecha_anulacion, motivo) VALUES
(3, '2025-06-03 17:00:00', 'Error en los datos del pasajero');

-- -----------------------------------------------------
-- Consultas SELECT útiles
-- -----------------------------------------------------

-- 1. Listar todos los clientes
SELECT * FROM Cliente;

-- 2. Mostrar las ventas realizadas en una fecha específica
SELECT * FROM Venta WHERE DATE(fecha_venta) = '2025-06-02';

-- 3. Obtener la última venta de cada cliente
SELECT v.*
FROM Venta v
INNER JOIN (
    SELECT id_cliente, MAX(fecha_venta) AS ultima_venta
    FROM Venta
    GROUP BY id_cliente
) ult ON v.id_cliente = ult.id_cliente AND v.fecha_venta = ult.ultima_venta;

-- 4. Listar todos los destinos que empiezan con “S”
SELECT * FROM Destino WHERE ciudad LIKE 'S%';

-- 5. Mostrar cuántas ventas se realizaron por país
SELECT d.pais, COUNT(*) AS total_ventas
FROM Pasaje p
JOIN Destino d ON p.id_destino = d.id_destino
GROUP BY d.pais;
