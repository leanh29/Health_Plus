import json
import numpy as np
import pandas as pd
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from gensim.models.keyedvectors import KeyedVectors
from keras.models import model_from_json
from keras_preprocessing.text import tokenizer_from_json

url_full_train_data = "C:\\Users\\HONGANH\\OneDrive\\Resources\\Corpus_Full_train.xls"
url_word2vec_full = "C:\\Users\\HONGANH\\OneDrive\\Resources\\model_word2vec_co_dau_21122020.model"
pad = ['post', 'pre']
epoch = 100
batch_size = 128
max_length = 300
NUM_WORDS = 50000
EMBEDDING_DIM = 300
test_num_full = 3004
L2 = 0.0004


def load_full_data():
    train_data = pd.read_excel(url_full_train_data, 'Sheet1')

    test_data = train_data[4415:4914]
    train_data = train_data.drop(test_data.index)

    texts = train_data.text

    tokenizer = Tokenizer(num_words=NUM_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n\'',
                          lower=True)
    tokenizer.fit_on_texts(texts)

    sequences_train = tokenizer.texts_to_sequences(texts)
    word_index = tokenizer.word_index

    X_train = pad_sequences(sequences_train, maxlen=max_length, padding=pad[0])

    word_vectors = KeyedVectors.load(url_word2vec_full, mmap='r')

    vocabulary_size = min(len(word_index) + 1, NUM_WORDS)
    embedding_matrix = np.zeros((vocabulary_size, EMBEDDING_DIM))

    for word, i in word_index.items():
        if i >= NUM_WORDS:
            continue
        try:
            embedding_vector = word_vectors[word]
            embedding_matrix[i] = embedding_vector
        except KeyError:
            embedding_matrix[i] = np.random.normal(0, np.sqrt(0.25), EMBEDDING_DIM)

    del (word_vectors)
    return tokenizer, sequences_train, X_train


def get_predict(text):
    tokenizer = Tokenizer(num_words=50000)
    labels = ['chưa xác định', 'bệnh hạ huyết áp', 'bệnh viêm đường ruột']

    with open('C:\\Users\\HONGANH\\OneDrive\\Resources\\vocab.json') as f:
        data = json.load(f)
    dictionary = tokenizer_from_json(data)




    json_file = open('C:\\Users\\HONGANH\\OneDrive\\Resources\\CNN_train_3c_relu.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    model = model_from_json(loaded_model_json)
    model.load_weights('C:\\Users\\HONGANH\\OneDrive\\Resources\\CNN_train_3c-035-0.0476-0.9940.h5')

    tok_sam, seq_sam, sample = load_full_data()

    sentence = []

    evalSentence = text
    if evalSentence:
        evalSentence = evalSentence.lower()

    sentence.append(evalSentence)
    eval_text = tok_sam.texts_to_sequences(sentence)
    text_test = pad_sequences(eval_text, maxlen=sample.shape[1], padding=pad[0])
    # pred = model.predict(testArr)
    pred = model.predict(text_test)
    print("%s; độ tin cậy %f%%" % (labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
    del evalSentence
    sentence = []

    return labels[np.argmax(pred)]


