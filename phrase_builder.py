import boto3

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


def receive_words():

    sqs = boto3.client("sqs")
    queue_url = sqs.get_queue_url(QueueName="phrase-scrambler-queue")["QueueUrl"]


    #receive the first message
    proto_word = receive_message(sqs, queue_url)
    # create an array based on the information of the first message
    if proto_word is None:
        return None

    word_definition = proto_word.split(":")
    if (len(word_definition) != 4):
        raise Exception(f"Invalid Token, expected 4 tokens, got {proto_word}")
    
    phrase_id = word_definition[0]
    size = int(word_definition[1])
    pos = int(word_definition[2])
    word = word_definition[3]

    phrase = [None] * size
    phrase[pos] = word
    while None in phrase:
        proto_word = receive_message(sqs, queue_url)
        word_definition = proto_word.split(":")
        if (len(word_definition) != 4):
            raise Exception(f"Invalid Token, expected 4 tokens, got {proto_word}")
        elif (phrase_id == word_definition[0]):
             phrase[int(word_definition[2])] = word_definition[3]
    
    return phrase


def main():
    while True:
        phrase = receive_words()
        if not phrase is None:
            print (''.join(phrase))


if __name__ == "__main__":
        main()