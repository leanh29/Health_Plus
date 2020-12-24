import json
import numpy as np
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import model_from_json
from keras_preprocessing.text import tokenizer_from_json


# this utility makes sure that all the words in your input
# are registered in the dictionary
# before trying to turn them into a matrix.
def convert_text_to_index_array(text):
    # cnn_lstm_model()
    # we're still going to use a Tokenizer here, but we don't need to fit it
    # for human-friendly printing
    # labels = ['positive', 'neutral', 'negative']

    # read in our saved dictionary
    '''
    with open('D:\\app\\DL_models\\Aspect\\vocab.json', 'r') as dictionary_file:
        dictionary = json.load(dictionary_file)
    '''
    with open('D:\\Final IT\\GRADUATE THESIS\\Projects\\CNN\\word2vec\\vocab.json') as f:
        data = json.load(f)
    dictionary = tokenizer_from_json(data)

    words = kpt.text_to_word_sequence(text,filters='!"#$%&()*+,-./:;<=>?@[\\]^`{|}~\t\n\'')
    wordIndices = []
    for word in words:
        if word in dictionary.word_docs:
            wordIndices.append(dictionary.word_docs[word])
        else:
            print("'%s' not in training corpus; ignoring." %(word))
    return wordIndices


def get_predict(text):
    labels = ['bệnh viêm đường ruột', 'bệnh hạ huyết áp', 'chưa xác định']
    # read in your saved model structure
    # json_file = open('model.json', 'r')
    json_file = open('D:\\Final IT\\GRADUATE THESIS\\models\\CNN_doc_raw_train_2c_relu.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    # and create a model from that
    model = model_from_json(loaded_model_json)
    model.load_weights('D:\\Final IT\\GRADUATE THESIS\\models\\CNN_doc_raw_train_2c-062-0.0284-0.9760.h5')

    # okay here's the interactive part
    sentence = []

    evalSentence = text
    if evalSentence:
        evalSentence = evalSentence.lower()

    testArr = convert_text_to_index_array(evalSentence)

    # print(testArr)
    sentence.append(testArr)
    sentence = pad_sequences(sentence, maxlen=300, padding='post')
    pred = model.predict(sentence)
    print("%s sentiment; %f%% confidence" % (labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
    del evalSentence
    sentence = []
    return labels[np.argmax(pred)]
