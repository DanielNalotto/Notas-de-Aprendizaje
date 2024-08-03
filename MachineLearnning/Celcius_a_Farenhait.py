import tensorflow as tf
tf.VERSION

"""from calendar import EPOCH
import tensorflow as tf
import numpy as np


celsius = np.array([-40,-10,0,8,15,22,38], datatype=float)
fahrenheit = np.array([-40,14,32,46,59,72], datatype=float)

capa = tf.keras.layers.Dense(units=1,input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizer.Adam(0.1),
    loss = 'mean_squared_error'
)

print("Comienza entrenamiento")
historial = modelo.fit(celsius, fahrenheit, epoch = 1000, verbose=False)
print("Termina entrenamiento")
"""