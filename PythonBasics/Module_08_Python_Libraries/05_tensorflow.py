"""
Module 8 — PYTHON LIBRARIES
Feature: Tensorflow

TensorFlow is for numerical tensors and neural networks.
This demo trains a tiny model: y ≈ 2x - 1  (fast CPU example).

Install if needed:
  pip install tensorflow
"""

try:
    import tensorflow as tf
    import numpy as np
except ImportError:
    print("Install first: pip install tensorflow")
    print("If that is heavy, study the comments and skip running.")
    raise SystemExit(1)

print("TensorFlow version:", tf.__version__)

# y = 2x - 1
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(optimizer="sgd", loss="mean_squared_error")
model.fit(xs, ys, epochs=200, verbose=0)

pred = float(model.predict(np.array([10.0]), verbose=0)[0][0])
print("predict x=10 (expect ~19):", round(pred, 2))
print("weights:", [w.numpy() for w in model.weights])


if __name__ == "__main__":
    print("\nTensorFlow demo complete.")
