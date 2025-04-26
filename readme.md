# Bienvenue sur mon projet Folochrome

Folochrome est une application permettant de suivre et de lister les couleurs pour le maquettisme et le wargame des marques connues comme Vallejo ou Citadel.
L'idée m'est venue en voyant l'application de Games Workshop, qui propose un suivi uniquement pour les couleurs Citadel. Folochrome contiendra toutes les marques qui me viendront à l'esprit.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- **Python 3.13.3** : La version recommandée pour exécuter ce projet.
- **Dépendances** : Installez les dépendances listées dans le fichier `requirements.txt`.

## Instructions de démarrage

1. **Installer les dépendances**  
   Créez un environnement virtuel et installez les dépendances avec la commande suivante :

   ```bash
   pip install -r requirements.txt
   ```

2. **Configurer l'environnement**  
   Renommez le fichier `.env-sample` en `.env` et remplissez les variables nécessaires.

3. **Lancer l'application**  
   Utilisez `uvicorn` pour démarrer le serveur :

   ```bash
   uvicorn app.main:app --reload
   ```

## Utilisation avec Docker

Pour ceux qui préfèrent Docker, tout est déjà configuré dans le fichier `docker-compose.yml`. Voici les étapes :

1. **Mettre en place les variables d'environnement**
   Renommez le fichier `.env-sample` en `.env` et écrivez vos variables d'environnement.

2. **Construire et démarrer les conteneurs**
   Exécutez la commande suivante :

   ```bash
   docker-compose up --build
   ```

3. **Accéder à l'API**
   Une fois les conteneurs démarrés, l'API sera accessible à l'adresse suivante :
   [http://localhost:8000](http://localhost:8000)

## Recommandation

Pour un environnement de développement optimal, utilisez un environnement virtuel Python 3.13.3
