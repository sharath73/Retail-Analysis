import pytest
import pytest
from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    "Creates spark Session"
    spark_session =  get_spark_session("LOCAL")
    yield spark_session    # yiled is used to retrive the user once the test is done
    spark_session.stop()

@pytest.fixture
def expected_results(spark):
    "gives the expected results"
    results_schema = 'state string,count integer'
    return spark.read \
    .format("csv") \
    .schema(results_schema) \
    .load("data/test_results/state_aggregate.csv")