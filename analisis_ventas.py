from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, desc

# 1. Iniciar sesión de Spark
spark = SparkSession.builder \
    .appName("AnalisisVentas") \
    .getOrCreate()

# 2. Leer el archivo CSV
df = spark.read.csv("sales.csv", header=True, inferSchema=True)

# 3. Validar reglas de negocio
# Un registro es válido si no tiene nulos y si cantidad y precio son mayores a 0
condicion_valida = (
    col("order_id").isNotNull() &
    col("order_date").isNotNull() &
    col("customer_id").isNotNull() &
    col("city").isNotNull() &
    col("product").isNotNull() &
    (col("quantity") > 0) &
    (col("unit_price") > 0)
)

# Separar válidos e inválidos
df_validos = df.filter(condicion_valida)
df_invalidos = df.filter(~condicion_valida)

# Calcular ingreso por cada venta válida (ingreso = cantidad * precio unitario)
df_validos = df_validos.withColumn("ingreso", col("quantity") * col("unit_price"))

# 4. Generar resúmenes
# Resumen por producto
resumen_producto = df_validos.groupBy("product").agg(
    spark_sum("quantity").alias("unidades_vendidas"),
    spark_sum("ingreso").alias("ingreso_total")
).orderBy(desc("ingreso_total"))

# Resumen por ciudad
resumen_ciudad = df_validos.groupBy("city").agg(
    spark_sum("ingreso").alias("ingreso_total")
).orderBy(desc("ingreso_total"))

# Mostrar indicadores en la consola
print("\n" + "="*30)
print("--- INDICADORES GENERALES ---")
print(f"Total de registros procesados: {df.count()}")
print(f"Total de registros válidos: {df_validos.count()}")
print(f"Total de registros inválidos: {df_invalidos.count()}")
print("="*30 + "\n")

# 5. Guardar los resultados en archivos de salida
# Se usa mode("overwrite") para que puedas ejecutar el script varias veces sin que arroje error
df_validos.write.mode("overwrite").csv("output/ventas_validas", header=True)
df_invalidos.write.mode("overwrite").csv("output/ventas_invalidas", header=True)
resumen_producto.write.mode("overwrite").csv("output/resumen_producto", header=True)
resumen_ciudad.write.mode("overwrite").csv("output/resumen_ciudad", header=True)

print("¡Proceso terminado! Revisa la carpeta 'output' en tu explorador de archivos.")


input("Presiona Enter en esta terminal para finalizar el programa y cerrar la web...")
spark.stop()
# Detener la sesión
spark.stop()