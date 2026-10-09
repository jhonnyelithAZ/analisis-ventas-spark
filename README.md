# 📊 Análisis de Ventas con Apache Spark (PySpark)

Este proyecto es un pipeline ETL (Extracción, Transformación y Carga) construido con **Apache Spark** (PySpark) para procesar y analizar registros de transacciones de ventas. El objetivo es identificar registros válidos e inválidos según reglas de negocio específicas y generar resúmenes agregados para la toma de decisiones.

## 🚀 Requisitos Previos

Para ejecutar este proyecto localmente, necesitas tener instalado:
* **Entorno Linux** (Recomendado: WSL 2 con Ubuntu si usas Windows).
* **Python 3.x**
* **Java (JDK/JRE)**: Spark requiere la Máquina Virtual de Java para ejecutarse.

## 🛠️ Instalación y Configuración

Sigue estos pasos en tu terminal de Linux/WSL para levantar el proyecto desde cero:

**1. Clonar el repositorio:**
```bash
git clone https://github.com/jhonnyelithAZ/analisis-ventas-spark.git
cd analisis-ventas-spark

**2. Configurar Java:**
Asegúrate de tener Java instalado y configura la variable de entorno `JAVA_HOME`. En Ubuntu, puedes hacerlo así:
```bash
sudo apt update && sudo apt install default-jre default-jdk -y
export JAVA_HOME=/usr/lib/jvm/default-java
```

**3. Crear y activar el entorno virtual de Python:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Instalar las dependencias (PySpark):**
```bash
pip install pyspark
```

## ⚙️ Ejecución del Análisis

Una vez configurado el entorno, ejecuta el script principal:

```bash
python analisis_ventas.py
```

### ¿Qué hace el script?
1. **Lee** los datos desde `sales.csv`.
2. **Filtra** los datos aplicando reglas de negocio (sin nulos, cantidades > 0, precios > 0).
3. **Calcula** el ingreso total por transacción.
4. **Agrupa** y genera indicadores de las ventas por ciudad y por producto.
5. **Escribe** los resultados en la carpeta `output/` en formato CSV.

## 📁 Estructura del Proyecto

* `sales.csv` : Archivo de entrada con los datos crudos de prueba.
* `analisis_ventas.py` : Script principal con la lógica de PySpark.
* `resumen_entregable.md` : Documento con la respuesta a las preguntas de negocio y justificación de registros inválidos.
* `output/` : Carpeta autogenerada que contiene los CSV con los resultados (ventas válidas, ventas inválidas, resúmenes por producto y ciudad).