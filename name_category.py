import findspark
findspark.init()

from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.shell import spark

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


def ids_in_values(list_with_dict_ids, dick_for_key, dict_for_values):
    answer = dict()
    for i in list_with_dict_ids:
        if dick_for_key[i[0]] not in answer.keys():
            answer[dick_for_key[i[0]]] = dict_for_values[i[1]]
        else:
            answer[dick_for_key[i[0]]] = f'{answer[dick_for_key[i[0]]]}, {dict_for_values[i[1]]}'
    return answer


def return_all_product_with_category(df_products, df_categories, df_relationships):
    product = dict(map(lambda x: (x.id, x.name), df_products.collect()))
    category = dict(map(lambda x: (x.id, x.name), df_categories.collect()))
    prod_with_category = map(lambda x: (int(x.id_products), int(x.id_categories)), df_relationships.collect())

    pre_answer = ids_in_values(prod_with_category, product, category)
    new_keys = set(product.values()) - set(pre_answer.keys())
    pre_answer = pre_answer | dict(map(lambda x: (x, ''), new_keys))
    answer = list(map(lambda x: (x, pre_answer[x]), pre_answer))

    columns = ['products', 'categories']
    df = spark.createDataFrame(answer, columns)
    return df


return_all_product_with_category(df_product, df_category, df_product_with_category).show()
