from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster('local').setAppName('RatingsHistogram')
sc = SparkContext(conf = conf)

lines = sc.textFile('file:///C:/Users/freddygpa/Documents/Courses/pyspark/github/Pyspark/Scripts01/data/ratings.data')
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print('%s %i' % (key, value))

