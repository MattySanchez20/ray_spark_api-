import time
import ray
from api_request import get_unbored_me_df
from spark_job import create_spark_dataframe_from_pandas_df, perform_summary_statistics
from pyspark.sql import SparkSession

def main():
    ray.init()

    df = get_unbored_me_df(1000)

    print("obtain df from api_request.py")

    ray.shutdown()

    spark = SparkSession.builder.appName("SummaryStats").getOrCreate()

    spark_df = create_spark_dataframe_from_pandas_df(df, spark)

    print("obtain spark_df from spark_job.py")

    summary_stats_df = perform_summary_statistics(spark_df)

    print("obtain summary_stats_df from spark_job.py")

    summary_stats_df.show()

    spark.stop()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    execution_time = end_time - start_time

    print("Execution time:", execution_time, "seconds")
