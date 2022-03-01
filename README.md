# Overview Spark(Pyspark)

### Spark
- Es un framework open source para la computación en paralelo utilizando clusters.
- Motor para analizar grandes cantidades de datos.
- Spark es una solución de big data que ha demostrado ser más fácil y rápida que Hadoop MapReduce. Spark es un software de código abierto

### Pyspark
Spark es el nombre del motor para realizar la computación en clúster, mientras que PySpark es la biblioteca de Python para usar Spark.

### Funcionamiento Spark
Spark se basa en el motor computacional, lo que significa que se encarga de la programación, distribución y supervisión de la aplicación. Cada tarea se realiza en varios equipos de trabajo llamados clúster de computación.

### Componentes Spark
- **Spark Streaming:** Mostrar datos en tiempo real
- **Spark SQL:** Módulo de Spark para el procesamiento de datos estructurados.
- **MLLib:** Machine Learning
- **GraphX:** Ayuda a enterder gráficos
 
 ### Resilient Distributed Dataset(RDD)
 [RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-programming-guide)
 - La principal abstracción que proporciona Spark es un conjunto de datos distribuido resistente (RDD), que es una colección de elementos particionados en los nodos del clúster que se pueden operar en paralelo.
 - Representan un gran set de datos, puedes usar métodos para alterar o filtrar el RDD.
 
 ### Inicializando Spark
 [Initializing Spark](https://spark.apache.org/docs/latest/rdd-programming-guide.html#initializing-spark)
 - Lo primero que debe hacer un programa Spark es crear un objeto SparkContext, que le indica a Spark cómo acceder a un clúster. Para crear un SparkContext, primero debe crear un objeto SparkConf que contenga información sobre su aplicación.

### Transformando RDD's
- **map:** permite tomar un set de datos y transformarlo a otro dada una función que lo haga, por ejemplo si se desea sacar el cuadrado de tu set de datos, puedes crear un mapa que apunta a una función que multiplica los numeros por si mismos.
- - **flatmap:** Tiene la misma función que map() pero puede producir varios outputs dado 1 solo Input.
- - **filter:** Filtra datos que no quieres que sean procesados del set de datos.
- - **distinct:** Ayuda a obtener los datos específicos en un set de datos.
- - **sample:** Permite tomar muestras de datos del RDD para hacer un experimento.
- - **Union, Intersection, substract, cartesian:** Puedes hacer intersecciones entre RDD's, Por ejemplo **cartesian** te da las posibles combinaciones del RDD.

### Acciones en un RDD
- **collect:** recolecta todos los valores del RDD.
- **count:** cuenta valores.
- **countByValue:** Cuenta cuantas vecers un valor ocurre en un RDD.
- **take:** Toma valores de los resultados finales de un RDD.
- **top:** Toma valores de los resultados finales de un RDD.
- **reduce:** Combinar diferentes valores para un valor clave, permite hacer agregacion.

### Pares (clave, valor)
- **reduceByKey():** combina todos los valores encontrados para una clave.
- **groupByKey():** Agrupa valores con una misma clave.
- **sortByKey():** Clasifica RDD por clave.
- **keys(), values():** Crea un RDD con solo las claves o solo los valores.

### Mapeo en pares (clave, valor)
- **mapValues()
- **flatMapValues()

### Filtrado RDD (clave, valor)
- **filter()

## Scripts
##### contador_ratings
 > Se evalua la cantidad de ratings según las valoraciones dadas por usuario (1,2,3,4,5)
##### amigos_por_edad
 > Se evalua el promedio de amigos por edad.
##### tem_minima
 > Se evalua la temperatura minima por clave.
##### tem_maxima
 > Se evalua la temperatura máxima por clave.
