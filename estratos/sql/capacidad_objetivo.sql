-- Madurez objetivo por subcapacidad N3 (1 a 5). Vacío = sin objetivo definido.
-- Brecha = objetivo − promedio de las 5 dimensiones (procesos, tecnología, datos, organización, desempeño).
ALTER TABLE `capacidad_n3`
  ADD COLUMN `madurez_objetivo` tinyint(3) unsigned DEFAULT NULL AFTER `performance_justification`,
  ADD CONSTRAINT `chk_n3_madurez_objetivo` CHECK (`madurez_objetivo` IS NULL OR `madurez_objetivo` BETWEEN 1 AND 5);
