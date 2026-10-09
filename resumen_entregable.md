# Resumen de Análisis de Ventas con Apache Spark

## 1. Indicadores Generales del Procesamiento
Tras ejecutar el pipeline de datos en PySpark, se procesó el lote de transacciones con los siguientes resultados generales:
* **Total de registros procesados:** 15
* **Total de transacciones válidas:** 12
* **Total de transacciones inválidas (rechazadas):** 3

## 2. Respuestas a Preguntas de Negocio (Sobre registros válidos)
* **¿Cuál fue el ingreso total de las ventas válidas?** 
  $3,580,000
* **¿Cuántas unidades se vendieron?** 
  22 unidades
* **¿Qué producto generó más ingresos?** 
  El Monitor.
* **¿Qué ciudad registró el mayor ingreso?** 
  Bogotá.

## 3. Nota sobre Validación de Datos
Durante el proceso de filtrado y aplicando las reglas de negocio, se identificaron y separaron 3 registros inválidos para evitar alteraciones en los indicadores finales. Los motivos de exclusión fueron los siguientes:

* **Transacción 1008 (Cali):** Se rechazó porque registra una cantidad vendida de `0`, lo que incumple la regla de negocio que exige que las unidades sean mayores a cero.
* **Transacción 1009 (Barranquilla):** Se rechazó porque registra una cantidad negativa (`-1`), lo cual es un error en los datos de origen (anomalía).
* **Transacción 1012 (Cali):** Se rechazó porque registra un precio unitario negativo (`-780000`), incumpliendo la regla que exige que los precios sean mayores a cero.