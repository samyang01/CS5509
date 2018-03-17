import tensorflow as tf

a=tf.constant([[1,1,1],[2,2,2],[3,3,3]])  # generate 3, 3x3 matrices
b=tf.constant([[1,1,1],[2,2,2],[3,3,3]])
c=tf.constant([[1,1,1],[2,2,2],[3,3,3]])

x=tf.matmul(a,a)    # define function x as matrix multiplication of matrices a*a
y=tf.add(x,b)       # define function y as element wise addition of matrices y and b
z=tf.matmul(y,c)    # define function z as matrix multiplication of y and c

with tf.Session() as sess:
    eval=sess.run(z)
    print(eval)
