# **Python Phrase Scrambler** ![GitHub python](https://img.shields.io/badge/python-v3.7-orange)


The inital service will br jumbling up a phrase, it is sent through the network to a separate service that unscrambles it and returns the original wording intact.

This program is intended to learn about *goroutines* and **AWS SQS** to handle multi-threads and communication between different processes.
There are three main programs:

- **phrase_producer.py:** Will producer a random phrase and push it into the AWS queue.

- **phrase_scrambler.py:** Will fetch the message from aws queue, it will then randomize the position of the word in the phrase and push it into other the AWS queue.

- **phrase_assembler.py:** Will fetch every word from AWS scrambled queue and it will assemble back to the original phrase

## **Prerequisites:**

- In order to persist the message, we need to provision two queues in AWS, **AWSCLIv2** Needs to be installed before using this feature, because we need to have your AWS credentials configured in order to acess **AWS SQS**:

```shell
	$ aws configure
```

- You need to install **CDKv2** in your system

```shell
$ npm install -g aws-cdk
$ cdk --version # Make sure the version (2+) is installed
```

- Follow the [CDKv2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) guide for more information

## **Usage:**

- Run the following commands to provision the **AWS SQS queues:**
```shell
	$ cd cdk-deploy 
	$ cdk synth 	# verify how the queue will be created
	$ cdk deploy	# to provision the queue
```

- After running the command these Queues will be created:
	* `phrase-producer-queue`
	* `phrase-scrambler-queue`

- Once the queue is provisioned successfully, run the following commands in separate windows to see how consumer and producer processes are running.

```shell
	$ python phrase_producer.py  # produce the phrase
  	$ python phrase_scrambler.py # scramble the Phrase
	$ python phrase_assember.py  # to rebuild the Phrase
```

