# coding=utf-8
import tensorflow as tf

# This tutorial is about Variable

state = tf.Variable(0, name="counter")
# print state.name

one = tf.constant(1)

new_val = tf.add(state, one)
update = tf.assign(state, new_val)

# 如果有变量的话，一定要运行这个来初始化变量
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print sess.run(state)
