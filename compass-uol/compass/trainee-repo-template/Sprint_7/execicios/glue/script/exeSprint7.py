import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql.functions import upper
from pyspark.sql.functions import count
from pyspark.sql.functions import col, sum


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options(
    's3',
    {
        'paths':[
            source_file
            ]
    },
    'csv',
    {'withHeader':True, 'separator':','}
)

only_1934 = df.filter(lambda row: row["ano"] == "1934")

glueContext.write_dynamic_frame.from_options(
    frame=only_1934,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet")
    
spark_df = df.toDF()
spark_df.printSchema()
print("imprimido")

spark_df = spark_df.withColumn("nome",upper(df["nome"]))
print("Convertendo de minúsculo para maiúsculo.")


linhas = spark_df.count()
print(f"Quantidade total de linhas: {linhas}")

contagem_nomes_ano_sexo = spark_df.groupBy("ano", "sexo").agg(count("nome").alias("contagem_nomes")).orderBy("ano", ascending=False)
contagem_nomes_ano_sexo.show()

mais_nomes_feminino = spark_df.filter(spark_df["sexo"] == "F").groupBy("nome", "ano").agg(sum("total").alias("total_registros")).orderBy("total_registros", ascending=False).limit(1)

mais_nomes_masculino = spark_df.filter(spark_df["sexo"] == "M").groupBy("nome", "ano").agg(sum("total").alias("total_registros")).orderBy("total_registros", ascending=False).limit(1)

print(f"Nome feminino com mais registros e ano em que ocorreu:")
mais_nomes_feminino.show()
print(f"Nome masculino com mais registros e ano em que ocorreu:")
mais_nomes_masculino.show()

total_registros_por_ano = spark_df.groupBy("ano").agg(sum('total').alias('total_registros')).orderBy("ano", ascending=True).limit(10)

total_registros_por_ano.show()

spark_df.write.mode("overwrite").partitionBy("sexo", "ano").json(target_path)




job.commit()