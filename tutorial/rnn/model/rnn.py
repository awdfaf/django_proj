# 패키지 정의
import numpy as np
# Tokenizer : 문장에서 단어 분류하기
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN

class Load_rnn:
    
    def __init__(self):
        # 훈련 모델 불러오기
        # self로 지정된 변수들은 모두 전역변수로 사용가능
        self.model = keras.models.load_model("C:/pknu_web/tutorial/rnn/model/django_rnn_model.h5")
        self.text = """경마장에 있는 말이 뛰고 있다\n
                그의 말이 법이다\n
                가는 말이 고와야 오는 말이 곱다\n
                """
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts([self.text])  
    
    # 예측할 단어로부터 다음 단어를 예측하기위한 함수
    # 매개변수 : 모델, 토큰나이저, 전달받은 단어, 반복할 횟수
    def sentence_generator(self, current_word, n):
        init_word = current_word
        sentence = ""
        
        # 전달받은 값 n번 반복시키기
        for _ in range(n):
            # 현재입력 받은 단어에 대한 정수 인코딩
            encoded = self.tokenizer.texts_to_sequences([current_word])[0]
            # 단어 자르기 : x값은 5개
            encoded = pad_sequences([encoded], maxlen=5, padding="pre")
            # 에측하기
            result = self.model.predict(encoded, verbose=0)
            # 예측결과 중 가장 빈도가 큰 값 결정
            result = np.argmax(result, axis=1)
            
            for word, index in self.tokenizer.word_index.items():
                # 만약 예측한 단어와 인덱스와 동일한 단어가 있다면 break
                if index == result:
                    break
                    
            # 현재 입력된 단어와 예측 단어 조합하기
            current_word = current_word + " " + word
            
            # 예측 단어 조합을 변수에 저장
            sentence = sentence + " " + word
        # 함수가 전달받은 단어에 대한 조합할 단어 합치기
        sentence = init_word + sentence
        
        return sentence