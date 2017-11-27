# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:23:48 2017
@author: xuwh

"""
#对一个线性数据进行训练的demo
import tensorflow as tf
import numpy as np

#create 100 phony x, y data points in Numpy,y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32);
y_data = x_data * 0.1 + 0.3;

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# figure that out for us.)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
print(W)
b = tf.Variable(tf.zeros([1]))
print(b)
y = W * x_data + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.initialize_all_variables()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

# Learns best fit is W: [0.1], b: [0.3]