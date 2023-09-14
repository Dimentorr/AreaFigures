import findspark
import pyspark
from pyspark.sql import SparkSession, SQLContext
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.shell import spark

from pyspark.sql import SparkSession

# scSpark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example: Reading CSV file without mentioning schema") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()
#
# sdfData = scSpark.read.csv("product.csv", header=True, sep=";")
# sdfData.show()


schema_product = StructType(fields=[
    StructField("id", IntegerType()),
    StructField("name", StringType())
])

schema_category = StructType(fields=[
    StructField("id", IntegerType()),
    StructField("name", StringType())
])

schema_product_with_category = StructType(fields=[
    StructField("id", IntegerType()),
    StructField("id_product", StringType()),
    StructField("id_category", StringType())
])

df_product = spark.read.csv(
    "product.csv",
    schema=schema_product,
    sep=";",
    header=True)
df_category = spark.read.csv(
    "category.csv",
    schema=schema_category,
    sep=";",
    header=True)
df_product_with_category = spark.read.csv(
    "product_with_category.csv",
    schema=schema_product_with_category,
    sep=";",
    header=True)

# работает, но для экономии времени закоментированно
# df_product.show()
# df_category.show()
# df_product_with_category.show()

# tmp = [[] for i in df_product_with_category.collect()]
prod = dict(map(lambda x: (x.id, x.name), df_product.collect()))
categor = dict(map(lambda x: (x.id, x.name), df_category.collect()))
prod_with_category = map(lambda x: (int(x.id_product), int(x.id_category)), df_product_with_category.collect())

print('-----------------------------------------------')


def ids_in_values(list_with_dict_ids, dick_for_key, dict_for_values):
    answer = dict()
    for i in list_with_dict_ids:
        if dick_for_key[i[0]] not in answer.keys():
            answer[dick_for_key[i[0]]] = dict_for_values[i[1]]
        else:
            answer[dick_for_key[i[0]]] = answer[dick_for_key[i[0]]], dict_for_values[i[1]]
    return answer


# answer = dict(map(lambda x: (prod[x[0]], categor[x[1]]) if(x[0] not in answer.keys()) else (
#     prod[x[0]], answer[prod[x[0]]] + f', {categor[x[1]]}'), prod_with_category))
print(ids_in_values(prod_with_category, prod, categor))


# answer = list()
# for i in df_product_with_category.collect():
#     answer.append(dict(map(lambda product, category: (product[i.id_product], category[i.id_category]))))
# for i in answer:
#     print(i)
# print(df_product.collect())

# print(df_product.select(df_product.name.count()).where(df_product.id == i.id_product))
# context = f"SELECT df_product.name FROM df_product WHERE df_product.id = {i.id_product}"
# print(SQLContext.sql(sqlQuery=context))

# sql_test = SQLContext.sql('select df_product.name from df_product where df_product.id =  ')
