# coding=utf-8
import tensorflow as tf

# This tutorial is about activation function
# 激励函数的作用是应对非线性问题
# y = AF(Wx)
# 一般激励函数要求是可微分的，这样才能在误差回传的时候回传误差

# 少量层中可以选择的