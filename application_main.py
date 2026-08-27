from lib.logger import Log4j
import sys  #python inbuilt module 
   #sys.argv=["main.py", "LOCAL"]
   #sys.argv[0] → main.py
   #sys.argv[1] → LOCAL
from lib import DataManipulation, DataReader, Utils
from pyspark.sql.functions import *

if __name__ == '__main__':   #Run the code below only when this file is executed directly.
    if len(sys.argv) < 2:
        print("Please specify the environment")
        sys.exit(-1)
        
    job_run_env = sys.argv[1]
    
    print("Creating Spark Session")
    
    spark = Utils.get_spark_session(job_run_env)

    logger = Log4j(spark)

    logger.warn("created Spark Session")
    
    
    orders_df = DataReader.read_orders(spark,job_run_env)
    
    orders_filtered = DataManipulation.filter_closed_orders(orders_df)
    
    customers_df = DataReader.read_customers(spark,job_run_env)
    
    joined_df =DataManipulation.join_orders_customers(orders_filtered,customers_df)
    
    aggregated_results = DataManipulation.count_orders_state(joined_df)
    
    aggregated_results.show()
    
    logger.info("end of main")