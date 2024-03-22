import pandas as pd
from pyspark import sql
from pyspark.sql.functions import count, avg, min, max

def create_spark_dataframe_from_pandas_df(pandas_df: pd.DataFrame, spark: sql.SparkSession) -> sql.DataFrame:
    
    df = spark.createDataFrame(pandas_df)
    
    return df


def perform_summary_statistics(df: sql.DataFrame) -> sql.DataFrame:
    # Partition the DataFrame by the "type" column
    partitioned_df = df.groupBy("type")
    
    # Perform summary statistics on each partition
    summary_stats_df = partitioned_df.agg(
        count("*").alias("count"),
        avg("price").alias("avg_price"),
        min("price").alias("min_price"),
        max("price").alias("max_price"),
        avg("participants").alias("avg_participants"),
        min("participants").alias("min_participants"),
        max("participants").alias("max_participants")
        # Add more summary statistics as needed
    )
    
    return summary_stats_df