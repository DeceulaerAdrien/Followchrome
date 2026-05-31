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
