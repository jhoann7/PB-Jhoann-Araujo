from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession \
        .builder \
        .master ("local[*]") \
        .appName ("Exercicio Intro") \
        .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.csv")

df_nomes.show(5)
df_nomes.limit(10).offset(5).show()
df_nomes.show_page(df_nomes, 5, 10)