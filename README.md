# demo1-mlflow (partie 1)
Pour mettre en place ce projet de Machine Learning avec Streamlit, FastAPI et MLflow sur GitHub, voici une liste de fichiers essentiels :

1. **`app.py`** (pour Streamlit) : Ce fichier contiendra votre code Streamlit pour l'interface utilisateur. Voici un exemple de contenu :
    ```python
    import streamlit as st

    st.title("Application de Machine Learning")
    st.write("Ceci est une application Streamlit pour visualiser des modèles de Machine Learning.")
    ```

2. **`main.py`** (pour FastAPI) : Ce fichier définira vos API FastAPI. Exemple :
    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Hello World"}
    ```

3. **`train.py`** (pour MLflow) : Fichier pour le script d'entraînement et le suivi MLflow. Exemple :
    ```python
    import mlflow
    import mlflow.sklearn

    with mlflow.start_run():
        mlflow.log_param("param1", value1)
        mlflow.log_metric("metric1", value1)
        mlflow.sklearn.log_model(model, "model")
    ```

4. **`requirements.txt`** : Liste de toutes les dépendances nécessaires. Exemple :
    ```
    streamlit
    fastapi
    uvicorn
    mlflow
    scikit-learn
    ```

5. **`README.md`** : Documentation de votre projet (le texte que vous avez fourni peut être utilisé ici).

6. **`.gitignore`** : Pour ignorer les fichiers inutiles (p. ex., fichiers de cache ou dossiers `__pycache__`). Exemple de contenu :
    ```
    __pycache__/
    *.pyc
    .DS_Store
    ```

7. **`Dockerfile`** et **`docker-compose.yml`** (optionnels) : Si vous souhaitez dockeriser votre application, ces fichiers configureraient l'environnement.

Voici comment structurer votre dépôt GitHub :
```
/projet-ml
│
├── app.py
├── main.py
├── train.py
├── requirements.txt
├── README.md
├── .gitignore
├── Dockerfile (optionnel)
└── docker-compose.yml (optionnel)
```

Pour initialiser un dépôt git et pousser ces fichiers sur GitHub, vous pouvez suivre ces commandes :
```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/votre-username/projet-ml.git
git push -u origin main
```

# demo1-mlflow (partie 2)


L'architecture du projet pour intégrer Streamlit, FastAPI, et MLflow dans une application de Machine Learning se compose généralement des trois principales composantes suivantes :

1. **Frontend (Streamlit)** :
   - **Rôle** : Interface utilisateur pour interagir avec le modèle de Machine Learning.
   - **Technologies** : Streamlit pour créer des interfaces utilisateur interactives et intuitives rapidement.
   - **Fonctionnement** : L'utilisateur interagit avec l'application via une interface web construite avec Streamlit. Cette interface permet de visualiser des données, de lancer des prédictions, et de contrôler les paramètres du modèle en temps réel.

2. **Backend (FastAPI)** :
   - **Rôle** : Serveur pour gérer les requêtes HTTP et servir de point de contact entre l'interface utilisateur et les modèles de Machine Learning.
   - **Technologies** : FastAPI pour construire des APIs robustes et performantes, uvicorn comme serveur ASGI pour exécuter l'API.
   - **Fonctionnement** : FastAPI reçoit les demandes de l'interface utilisateur (par exemple, des demandes de prédiction ou des requêtes de données), traite ces demandes en interagissant avec les modèles de Machine Learning ou la base de données, et renvoie les résultats à l'interface utilisateur.

3. **MLOps (MLflow)** :
   - **Rôle** : Gestion et suivi des expérimentations, modèles et déploiements.
   - **Technologies** : MLflow pour gérer le cycle de vie des modèles de Machine Learning, y compris le suivi des expérimentations, la reproductibilité, le déploiement des modèles, et la gestion des registres de modèles.
   - **Fonctionnement** : MLflow est utilisé pour enregistrer des métriques, des paramètres et des artefacts des modèles pendant l'entraînement. Il fournit une interface web pour visualiser les expérimentations et gérer les versions des modèles.

### Diagramme de l'architecture du projet

```
┌────────────────┐           ┌────────────────┐           ┌────────────────┐
│                │           │                │           │                │
│   Frontend     │           │   Backend      │           │   MLOps        │
│ (Streamlit UI) ├──────────►│   (FastAPI)    ├──────────►│   (MLflow)     │
│                │   HTTP    │                │   API     │                │
│                │  Requests │                │  Calls    │                │
└────────────────┘           └────────────────┘           └────────────────┘
```

### Installation et configuration

- **Streamlit** est installé via pip et lancé localement pour développer l'interface.
- **FastAPI** nécessite également une installation via pip et est exécuté via uvicorn, qui peut être configuré pour recharger automatiquement lors du développement.
- **MLflow** est configuré pour enregistrer des données localement ou sur un serveur distant, et son interface utilisateur est accessible via un navigateur web.

Cette architecture vous permet de développer une application de Machine Learning complète et intégrée, avec un frontend interactif, un backend performant et une plateforme robuste pour le suivi et la gestion des modèles.
