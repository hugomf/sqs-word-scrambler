import boto3
from sqs_wrapper import SQSWrapper

def main():
    
    sqs = SQSWrapper("phrase-producer-queue")

    phrases = [input("introduce la frase: ")]
    for i in range(len(phrases)):
        response = sqs.send_message(phrases[i])
            

if __name__ == "__main__":
    main()
