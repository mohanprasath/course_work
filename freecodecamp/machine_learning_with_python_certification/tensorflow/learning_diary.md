# Tensorflow

- Video Link <https://www.youtube.com/watch?v=tPYj3fFJGjk>

## Tensorflow - Introduction: Machine Learning Fundamentals

- Video Link <https://youtu.be/KwL1qTR5MT8>
- Artificial Intelligence (AI) - set of rules that computers follow to accomplish a task
- Machine Learning (ML) - figures out the rules to be followed to accomplish a task
- ML is a subset of AI
- Neural Networks (NN) - layered representation of the data (multiple layers)
- NN is a subset of ML
- features is the input data that we give it as an input to the model
- label/target/output is the data th model is supposed to predict
- _exercie solution - which statement is false:_
  - Neural networks are modeled after the way the human brain works

## TensorFlow - Introduction to TensorFlow

- colab Link <https://colab.research.google.com/drive/1F_EWVKa8rbMXi3_fG0w7AtcscFq7Hi7B#forceEdit=true&sandboxMode=true>
- refer materials folder for completed colab
- video link <https://youtu.be/r9hRyGGjOgQ>
- whats is a tensor?
  - a vector generalized to higher dimension
  - a vector is a point in a n dimensional system
  - data types: `int32`, `float32`, `string` and others
  - shape: represent the dimensions of the data
- **Creating Tensors:**
  - `string = tf.variable("this is a string", tf.string) # is a scalar`
- **Rank/Degree of Tensors:**
  - `rank1_tensor = tf.Variable(["Test"], tf.string)`
  - `rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)`
  - to find the rank of a tensor
  - `tf.rank(rank2_tensor)`
