import boto3
import random
import pprint
import time
import datetime
import numpy

client = boto3.client('kinesis')

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


response = client.get_shard_iterator(
    StreamName='sam-jin-test-kinesis-stream-1',
    ShardId="shardId-000000000004",
    ShardIteratorType="AT_TIMESTAMP",
    Timestamp=datetime.datetime.now() - datetime.timedelta(seconds=10)
)


iterator = response["ShardIterator"]

while(True):


    res = client.get_records(
        ShardIterator=iterator,
        Limit=20
    )
    tmp = []
    for e in res["Records"]:
        tmp.append(int(e["Data"]))
    mean_val = mean(tmp)
    print("Found {} records. mean is {}, {}".format(len(tmp), mean_val, tmp))
    iterator= res["NextShardIterator"]
    time.sleep(3)
