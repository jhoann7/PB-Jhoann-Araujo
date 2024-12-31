import sys
from awsglue.transforms import *
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from datetime import datetime
from pyspark.sql.functions import upper
from pyspark.sql.functions import count
from pyspark.sql.functions import col, sum
from pyspark.sql.functions import regexp_replace


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
target_path = f"s3://jhoannsprint6/meubucket/Trusted/Local/PARQUET/{ano}/{mes}/{dia}"

df = glueContext.create_dynamic_frame.from_options(
    's3',
    {
        'paths':[
            source_file
            ]
    },
    'csv',
    {'withHeader':True, 'separator':'|'}
)

df_spark = df.toDF()

#removendo as linhas duplicadas
df_spark = df_spark.dropDuplicates()

#removendo coluna indesejada
df_spark = df_spark.drop("tituloPincipal")

#removendo caracteres epeciais
df_spark = df_spark.withColumn("tituloOriginal", F.regexp_replace(F.col("tituloOriginal"), "[^\\w\\s]", ""))

#removendo linhas com valores nulos
df_spark = df_spark.dropna()

#salvando todo o conteúdo em um único arquivo
df_spark = df_spark.coalesce(1)

#salvando o arquivo no formato parquet no bucket
df_spark.write.mode("overwrite").parquet(target_path)

job.commit()