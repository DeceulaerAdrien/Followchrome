# Folochrome 🎨

**Folochrome** est une application backend (API) open source permettant de suivre et de lister les couleurs pour le maquettisme et le wargame à travers plusieurs marques (Vallejo, Citadel, Army Painter, etc.). 

L'idée est née du constat que l'application officielle de Games Workshop (*Citadel Colour*) limite son suivi à sa propre marque. **Folochrome** résout ce problème en centralisant l'ensemble des fabricants du marché au sein d'une même architecture de données.

## 🛠️ Stack Technique & Architecture Backend

Le cœur du projet est conçu pour valider des compétences clés en développement backend moderne :
- **Framework :** Python 3.13 + FastAPI / Uvicorn pour une API asynchrone rapide et documentée.
- **DevOps & Environnement :** Conteneurisation complète avec Docker et Docker Compose pour faciliter le déploiement.
- **Sécurité & Configuration :** Gestion rigoureuse des configurations et des secrets via des variables d'environnement (`.env`).

---

## 🚀 Prérequis & Instructions de démarrage

Avant de commencer, assurez-vous d'avoir **Python 3.13.3** installé sur votre machine.

### 1. Installation classique (Local)

**Installer les dépendances :**
Créez un environnement virtuel et installez les dépendances :
```bash
pip install -r requirements.txt
```

**Configurer l'environnement :**
Renommez le fichier `.env-sample` en `.env` et remplissez les variables nécessaires.

**Lancer l'application :**
Utilisez uvicorn pour démarrer le serveur de développement :
```bash
uvicorn app.main:app --reload
```

---

### 🐳 Utilisation avec Docker

Pour un déploiement rapide sans installer Python en local, tout est déjà configuré via Docker Compose.

1. **Variables d'environnement :** Renommez le fichier `.env-sample` en `.env` et ajustez vos variables.
2. **Démarrer les conteneurs :** Exécutez la commande suivante :
   ```bash
   docker-compose up --build
   ```
3. **Accéder à l'API :** Une fois les conteneurs démarrés, l'API sera pleinement accessible à l'adresse : `http://localhost:8000`

## 💡 Recommandation
Pour un environnement de développement optimal hors Docker, l'utilisation d'un environnement virtuel configuré en Python 3.13.3 est fortement recommandée.

## 📊 Statut du projet & Retours d'expérience

Le projet est actuellement en pause au stade de prototype (PoC) fonctionnel au niveau de son infrastructure (le conteneur Docker et le serveur FastAPI se lancent correctement). 

**Enseignements techniques tirés de ce projet :**
- **Problématique de la donnée :** La saisie manuelle des catalogues (plus de 3 000 lignes de JSON pour la gamme Vallejo) s'est avérée être un point de blocage majeur pour la viabilité du projet à long terme. 
- **Axe d'amélioration identifié :** Pour industrialiser l'application, l'étape suivante consisterait à remplacer la saisie manuelle par le développement d'un script de Web Scraping pour automatiser la récupération des nomenclatures des fabricants, ou à consommer une API tierce.
