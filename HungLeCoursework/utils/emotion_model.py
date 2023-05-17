import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_addons as tfa

from datetime import datetime
from HungLeCoursework.utils.constance_data import emotion_track_list, decode_cut_list
from HungLeCoursework.utils.pre_processing_data import preprocessing_data, pre_processing_data_2, text_transform


def emotion_predict(sentence: str):
    lr = 1e-3
    wd = 1e-4 * lr
    model = tf.keras.models.load_model("HungLeCoursework/model/nlp_surrey_coursework_hunglenhat")
    # model.compile(loss='sparse_categorical_crossentropy',
    #               optimizer=tfa.optimizers.AdamW(learning_rate=lr, weight_decay=wd), metrics=['accuracy'])
    sentence = pre_processing_data_2(sentence)
    if not sentence:
        sentence = preprocessing_data(sentence)

    sentence = text_transform(sentence)
    try:
        sentence = model.predict(sentence)
    except Exception as E:
        print(E)
    index_max = np.argmax(sentence)
    result = emotion_track_list[decode_cut_list[index_max]]
    return result


def user_capture(user_input, emotion_prd):
    dataframe_capture = pd.read_csv('request_notebook/user_logs.csv')
    user_input_logs = pd.DataFrame({
        "user_input": [user_input],
        "emotion_predict": [emotion_prd],
        "time_logs": [datetime.now()],
    })
    dataframe_capture = pd.concat([dataframe_capture, user_input_logs], ignore_index=True)
    dataframe_capture.to_csv("request_notebook/user_logs.csv", index=False)
    print("Done")
