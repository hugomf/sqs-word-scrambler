from sqs_wrapper import SQSWrapper

def receive_words():

    sqs = SQSWrapper("phrase-scrambler-queue")

    #receive the first message
    proto_word = sqs.receive_message()
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
        proto_word = sqs.receive_message()
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