import sys
from awsglue.transforms import *
from pyspark.sql import functions as F
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from datetime import datetime
from awsglue.job import Job
from pyspark.sql.types import DateType, IntegerType
from pyspark.sql.functions import to_date, col

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)

spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

data = datetime.now()
dia = data.strftime('%d')
mes = data.strftime('%m')
ano = data.strftime('%Y')

source_file = args['S3_INPUT_PATH']
target_path = f"s3://jhoannsprint6/meubucket/Trusted/TMDB/PARQUET/{ano}/{mes}/{dia}"

df = glueContext.create_dynamic_frame.from_options(
    connection_type = 's3',
    connection_options = {"paths": [source_file],"recurse": True},
    format = 'json',
    format_options = {"multiline": True}
)

df_spark = df.toDF()

#removendo as linhas duplicadas
df_spark = df_spark.dropDuplicates()

#removendo linhas com valores nulos
df_spark = df_spark.dropna()




#removendo "." das colunas "popularidade" e "mediaDeVotos"
df_spark = df_spark.withColumn("popularidade", F.regexp_replace(F.col("popularidade"), "\.", ""))
df_spark = df_spark.withColumn("mediaDeVotos", F.regexp_replace(F.col("mediaDeVotos"), "\.", ""))

#convertendo os tipos das colunas
df_spark = df_spark.withColumn("popularidade", df["popularidade"].cast(IntegerType()))
df_spark = df_spark.withColumn("dataDeLancamento", df["dataDeLancamento"].cast(DateType()))
df_spark = df_spark.withColumn("mediaDeVotos", df["mediaDeVotos"].cast(IntegerType()))
#trocando o separador da data
# df_spark = df_spark.withColumn("dataDeLancamento", F.regexp_replace(F.col("dataDeLancamento"), "-", "/"))
#salvando todo o conteúdo em um único arquivo
df_spark = df_spark.coalesce(1)

#salvando o arquivo no formato parquet no bucket
df_spark.write.mode("overwrite").option("header", "true").option("delimiter", "|").parquet(target_path)


job.commit()