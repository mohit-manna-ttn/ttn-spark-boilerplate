#Getting msr id from child source given to us
def getMsrId(spark,uri):
    print("Hitting Mongo collection Child")
    df = spark.read.format("mongo").option("uri",uri).load()
    df.show()
    df.printSchema()
    # msr=df.select('msrId')
    # return msr
#get parent collection corresponding to that msrId
def getParent(spark,uri):
    parent = spark.read.format("mongo").option("uri",uri).load()
    parent.show()
   # parent.select(parent["_class"] where parent["_id"]== getMsrId(spark)).show()
    # return parent


