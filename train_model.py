import tensorflow as tf
from tensorflow import keras
import numpy as np
import mlflow
import mlflow.tensorflow

# Lancement d'une session de suivi MLflow
# autolog() s'occupe de tout enregistrer pour nous !
mlflow.tensorflow.autolog()

with mlflow.start_run():
    print("TensorFlow version:", tf.__version__)

    # --- 1. Chargement et préparation des données ---
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype("float32") / 255.0
    x_test = x_test.reshape(10000, 784).astype("float32") / 255.0
    print("Données chargées et préparées.")

    # --- 2. Construction du modèle ---
    model = keras.Sequential([
        keras.layers.Dense(512, activation='relu', input_shape=(784,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation='softmax')
    ])
    model.summary()

    # --- 3. Compilation du modèle ---
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    print("Modèle compilé.")

    # --- 4. Entraînement du modèle ---
    print("Début de l'entraînement...")
    model.fit(x_train, y_train,
              epochs=5,
              batch_size=128,
              validation_split=0.1)
    print("Entraînement terminé.")

    # --- 5. Évaluation du modèle ---
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"\nPrécision sur les données de test: {test_acc:.4f}")

    # --- 6. Sauvegarde du modèle ---
    model.save("mnist_model.h5")
    print("Modèle sauvegardé sous le nom 'mnist_model.h5'")