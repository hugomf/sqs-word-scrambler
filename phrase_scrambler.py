import boto3
import random
import uuid

# Define a function to receive messages from the SQS queue
def receive_message(sqs, queue_url):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )
    if "Messages" in response:
        message = response["Messages"][0]
        receipt_handle = message["ReceiptHandle"]
        word = message["Body"]
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        return word
    else:
        return None
    
def main():
    sqs = boto3.client("sqs")
    producer_queue_url = sqs.get_queue_url(QueueName="phrase-producer-queue")["QueueUrl"]
    scrambler_queue_url = sqs.get_queue_url(QueueName="phrase-scrambler-queue")["QueueUrl"]

    input_phrase = receive_message(sqs, producer_queue_url)
    if input_phrase is None:
        return
    #print (f"Received message: {input_phrase}")
    phrase_id = str(uuid.uuid4())
    words = list(input_phrase)
    size = len(input_phrase)
    word_positions = list(enumerate(words))
    # Shuffle the word positions
    random.shuffle(word_positions)
    # Send each scrambled word and its position as a message to the SQS queue
    for i, word in word_positions:
        message = f"{phrase_id}:{size}:{i}:{word}"
        print(f"message sent: {message}")
        response = sqs.send_message(
            QueueUrl=scrambler_queue_url,
            MessageBody=message
        )

    # if phrase is not None:
    #     print(phrase)
    # else:
    #     print("No message received")

if  __name__ == "__main__":
    while True:
        main()