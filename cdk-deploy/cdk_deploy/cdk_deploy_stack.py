from constructs import Construct
from aws_cdk import (
    Duration,
    CfnOutput,
    aws_sqs as sqs,
    Stack,
)

class CdkDeployStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create an SQS queue
        queue = sqs.Queue(
            self, "PhraseProducerQueue",
            queue_name="phrase-producer-queue",
            visibility_timeout=Duration.seconds(300)
        )
        
        # Output the URL of the queue
        CfnOutput(
            self, "PhraseProducerQueueUrl",
            value=queue.queue_url
        )

        queue = sqs.Queue(
            self, "PhraseScramblerQueue",
            queue_name="phrase-scrambler-queue",
            visibility_timeout=Duration.seconds(300)
        )
        
        # Output the URL of the queue
        CfnOutput(
            self, "PhraseScramblerQueueUrl",
            value=queue.queue_url
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkDeployQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
