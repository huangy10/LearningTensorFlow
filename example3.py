import tensorflow as tf

# This tutorial is about Variable

state = tf.Variable(0, name="counter")
# print state.name

one = tf.constant(1)

new_val = tf.add(state, one)
update = tf.assign(state, new_val)

init = tf.initialize_all_variables()


