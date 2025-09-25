# Classification d'Images MNIST : De la Conception au Déploiement

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Frameworks](https://img.shields.io/badge/Frameworks-TensorFlow%20%7C%20Flask-orange.svg)
![Outils MLOps](https://img.shields.io/badge/MLOps-MLflow%20%7C%20Docker-blueviolet.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Ce projet a été réalisé dans le cadre du cours "Machine Learning II : Deep Learning". Il met en œuvre un pipeline MLOps complet pour la classification de chiffres manuscrits à partir du célèbre jeu de données MNIST. L'objectif est de démontrer la maîtrise de l'ensemble du cycle de vie d'un modèle, de l'entraînement initial à la mise en production via une API conteneurisée.

---

## ✨ Fonctionnalités

*   **Modèle de Deep Learning** : Un réseau de neurones (MLP) construit avec Keras et TensorFlow pour la classification d'images.
*   **Suivi d'expérimentations** : Intégration de **MLflow** pour logger les paramètres, les métriques et les modèles de chaque entraînement, garantissant la reproductibilité.
*   **API RESTful** : Une API légère créée avec **Flask** pour servir le modèle et exposer un point de terminaison de prédiction.
*   **Conteneurisation** : Utilisation de **Docker** pour empaqueter l'application et ses dépendances dans une image portable et isolée, prête pour le déploiement.
*   **Workflow CI/CD** : Conception d'un pipeline d'intégration et de déploiement continus (avec GitHub Actions) pour automatiser la construction et le déploiement.

---

## 📂 Structure du Projet