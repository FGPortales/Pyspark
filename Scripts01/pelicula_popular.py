from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('ContarPalabras')
sc = SparkContext(conf=conf)


data_input = sc.textFile('file:///C:/Users/freddygpa/Documents/Courses/pyspark/github/Pyspark/Scripts01/data/ratings.data')
pelicula = data_input.map(lambda x: (int(x.split()[1]), 1))
pelicula_count = pelicula.reduceByKey(lambda x, y: x + y)

flipped = pelicula_count.map(lambda d: (d[1], d[0]))
sorted_pelicula = flipped.sortByKey()

result = sorted_pelicula.collect()

for rec in result:
	print(rec)