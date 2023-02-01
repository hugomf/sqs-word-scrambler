import boto3


def main():
    
    sqs = boto3.client("sqs")
    queue_url = sqs.get_queue_url(QueueName="phrase-producer-queue")["QueueUrl"]
    
    phrases = [input("introduce la frase: ")]
    for i in range(len(phrases)):
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=phrases[i]
        )
            

if __name__ == "__main__":
    main()
