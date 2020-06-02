import tensorflow.compat.v1 as tf
import tf_slim as slim
tf.disable_v2_behavior()

def head(endpoints, embedding_dim, is_training):
    endpoints['emb_raw'] = slim.fully_connected(
        endpoints['model_output'], embedding_dim, activation_fn=None,
        weights_initializer=tf.orthogonal_initializer(), scope='emb')
    endpoints['emb'] = tf.nn.l2_normalize(endpoints['emb_raw'], -1)

    return endpoints
