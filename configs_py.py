# -*- coding: utf-8 -*-
"""configs.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wXA1NoAytCW1jfDJLHVFYMlxE6rrqcwW
"""

# coding: utf-8

import tensorflow as tf

tf.app.flags.DEFINE_string('f', '', 'kernel') # 주피터에서 커널에 전달하기 위한 프래그 방법
tf.app.flags.DEFINE_integer('batch_size', 64, 'batch size') # 배치 크기
tf.app.flags.DEFINE_integer('train_steps', 10000, 'train steps') # 학습 횟수
tf.app.flags.DEFINE_float('dropout_width', 0.5, 'dropout width') # 드롭아웃 크기
tf.app.flags.DEFINE_integer('layer_size', 3, 'layer size') # 멀티 레이어의 크기 
tf.app.flags.DEFINE_integer('hidden_size', 128, 'weights size') # 가중치 크기
tf.app.flags.DEFINE_float('learning_rate', 1e-3, 'learing rate') # 학습률
tf.app.flags.DEFINE_string('data_path', './test_data.csv', 'data path') # 데이터 위치
tf.app.flags.DEFINE_string('vocabulary_path', './vocabularyData.voc', 'vocabulary path') # 사전 위치
tf.app.flags.DEFINE_string('check_point_path', './check_point', 'check point path') # 체크 포인트 위치
tf.app.flags.DEFINE_integer('shuffle_seek', 1000, 'shuffle random seek') # 셔플 시드값
tf.app.flags.DEFINE_integer('max_sequence_length', 25, 'max sequence length') # 시퀀스 길이
tf.app.flags.DEFINE_integer('embedding_size', 128, 'embedding size') # 임베딩 크기
tf.app.flags.DEFINE_boolean('tokenize_as_syllable', True, 'set syllable tokenize') # 음절에 따른 토크나이징 사용 여부
tf.app.flags.DEFINE_boolean('embedding', True, 'Use Embedding flag') # 임베딩 여부 설정
tf.app.flags.DEFINE_boolean('multilayer', True, 'Use Multi RNN Cell') # 멀티 RNN 여부

# Define Flags

DEFINES = tf.app.flags.FLAGS

## 불러올 경우 

## from configs import DEFINES

_