import random
import uuid
from sqs_wrapper import SQSWrapper

    
def main():
    sqsReceiver = SQSWrapper("phrase-producer-queue")
    sqsProducer = SQSWrapper("phrase-scrambler-queue")

    input_phrase = sqsReceiver.receive_message()
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
        sqsProducer.send_message(message)

if  __name__ == "__main__":
    while True:
        main()