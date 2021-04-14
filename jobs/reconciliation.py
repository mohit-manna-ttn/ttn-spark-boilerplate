from pyspark.sql import Row
from pyspark.sql.functions import col, concat_ws, lit
import sys
import json
from dependencies.spark import start_spark
from utils.config import getMsrId, getParent
def say_hello(spark):
    print("Hello World")
    return True
def main(spark_config={'db':'pwcTest','spark.mongodb.input.uri':'mongodb://127.0.0.1:27017','spark.mongodb.output.uri':'mongodb://127.0.0.1:27017/'}):
    # start Spark application and get Spark session, logger and config
    spark, log, config = start_spark(
        app_name='msr_reconciliation',
        files=['configs/dev_config.json'],
        jar_packages=['org.mongodb.spark:mongo-spark-connector_2.12:2.4.2'],
        spark_config=spark_config
        )
    print(spark_config)
    # log that main ETL job is starting
    log.warn('reconciliation job is up-and-running')
    print(config)
    # print(dict(spark.sparkContext.getConf().getAll())['db'])#here the key of the json param will go
    say_hello(spark)
    getMsrId(spark,spark_config['spark.mongodb.input.uri']+'/'+spark_config['db']+'.'+'sales_financial_data')
    #print(getMsrId(spark))
    # getParent(spark)
    #print(getParent(spark))

    # log the success and terminate Spark application
    log.warn('reconciliation job is finished')
    spark.stop()
    return None
#from jobs.reconciliation import main
#main()
if __name__ == '__main__':
    main(json.loads(sys.argv[1]))