# coding=utf-8
import tensorflow as tf

# This tutorial is about placeholder

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.mul(input1, input2)

with tf.Session() as sess:
    # 注意这里placeholder变量自己来作为key
    print sess.run(output, feed_dict={input1: [7.], input2: [2.]})
