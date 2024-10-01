#Custom L1 Distance layer module

#Import dependencies
import tensorflow as tf
from tensorflow.keras.layers import Layer

#Custome L1 Distance Layer From Colab

class L1Dist(Layer):
    def __init__(self, **kwargs):
        super().__init__()

    def call(self, input_embedding, validation_embedding):
      return tf.math.abs(input_embedding[0] - validation_embedding[0])
    