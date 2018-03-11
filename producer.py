import boto3
import random
import pprint
import time

client = boto3.client('kinesis')



while(True):
	random_int = random.randint(0, 10)
	print("Putting random int {}".format(random_int))
	response = client.put_record(
    	StreamName='sam-jin-test-kinesis-stream-1',
    	Data=str(random_int),
    	PartitionKey="producer-1"
	)
	# pprint.pprint(response)
	time.sleep(0.1)


