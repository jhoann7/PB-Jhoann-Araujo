import sys
from awsglue.transforms import *
from pyspark.sql import functions as F
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from datetime import datetime
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

data_atual = datetime.now()
ano = data_atual.strftime('%Y')
mes = data_atual.strftime('%m')
dia = data_atual.strftime('%d')

input_path = args['S3_INPUT_PATH']
target_path = f"s3://jhoannsprint6/meubucket/Trusted/TMDB/PARQUET/{ano}/{mes}/{dia}"

df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path],"recurse": True},
    format="json",
    format_options={"multiline": True}
)

df_spark = df.toDF()

df_spark = df_spark.dropDuplicates()

df_spark = df_spark.coalesce(1)

df_spark.write.mode("overwrite").parquet(target_path)

job.commit()