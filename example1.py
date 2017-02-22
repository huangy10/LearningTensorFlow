# coding=utf-8
# 下载示例数据集
# import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 下面的内容来自周莫烦的教程
import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# create tensorflow structure start ###
# 定义一个参数变量，指定初始值
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 上面的Weight和biases只是一个形式的占位，事实上在声明时并未被创建，下面的命令执行初始化
init = tf.initialize_all_variables()
# create tensorflow structure end ###

# 这里的session应该是类似数据库的session的概念，整个神经网络被做成了一个黑匣子，通过一个session
# 会话来获取里面的内容
# 或者说session其实是神经网络的一个interface
sess = tf.Session()
sess.run(init)  # 激活神经网络

for step in range(201):
    # 运行一步学习
    sess.run(train)
    if step % 20 == 0:
        print step, sess.run(Weights)[0], sess.run(biases)[0]

