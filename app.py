from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Charger le modèle une seule fois au démarrage de l'app
model = tf.keras.models.load_model('mnist_model.h5')
print("Modèle chargé.")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    # Prétraitement de l'image
    image_data = np.array(data['image']).reshape(1, 784).astype("float32") / 255.0

    # Prédiction
    prediction = model.predict(image_data)
    predicted_class = np.argmax(prediction, axis=1)[0]

    return jsonify({
        'prediction': int(predicted_class),
        'probabilities': prediction.tolist()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)