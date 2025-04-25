# 🛠️ SoftDesk – API de gestion de projets et de tickets
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoRESTFramework](https://img.shields.io/badge/DJANGO-DRF-990000?style=for-the-badge&logo=django&logoColor=white&color=990000&labelColor=gray)
![PIPENV](https://img.shields.io/badge/PIPENV-eeeeee?style=for-the-badge&logo=)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

**SoftDesk** est une API REST développée avec **Django REST Framework**. 

Elle permet à des utilisateurs authentifiés de gérer des projets collaboratifs, de suivre des tickets (issues) et d’interagir via des commentaires. 

Le projet respecte les exigences de sécurité (OWASP, RGPD) et vise une conception optimisée et durable.

---

## 🚀 Fonctionnalités principales

- Inscription
- Authentification par JWT (obtention et rafraîchissement de token)
- Création de projets par des utilisateurs authentifiés (L'utilisateur créateur devient automatiquement auteur et contributeur)
- Gestion des contributeurs par l'auteur du projet (ajout, suppression)
- Création d'issues + assignation à un contributeur (priorité, statut, tag) (Réservé aux contributeurs du projet)
- Ajout de Commentaires sur les issues (Réservé aux contributeurs du projet)
- Permissions granulaires :
  - Seul l’auteur peut modifier/supprimer un projet ou une ressource
  - Seuls les contributeurs peuvent accéder aux ressources d’un projet
- Pagination sur les ressources listables

---

## 🔐 Sécurité et conformité

L’API est conçue pour respecter :
- **RGPD** :
  - Vérification de l’âge minimal (15 ans)
  - Consentement pour la collecte et le partage de données
  - Accès, rectification et suppression du compte
- **OWASP** :
  - Authentification sécurisée (JWT)
  - Autorisation par permissions personnalisées
  - Contrôle d’accès strict à chaque ressource
- **Green Code** :
  - Pagination des listes
  - Optimisation des requêtes

---

## 🔗 Endpoints de l'API

| Méthode | Endpoint | Description | Body |
|--------|----------|-------------|-------|
| `POST` | `/api/users/` | Inscription d'un utilisateur | Body : {username: str, password: str, password2: str, age: date, can_be_contacted: bool, can_data_be_shared: bool}|
| `PATCH` | `/api/users/<user_id>/` | Modifier l'utilisateur | Body : {username: str, password: str, age: date, can_be_contacted: bool, can_data_be_shared: bool}|
| `GET` | `/api/users/` | Liste des utilisateurs |
| `GET` | `/api/users/<user_id>/` | Détails de l'utilisateur |
| `DELETE` | `/api/users/<user_id>/` | Supprime l'utilisateur |
| `POST` | `/api/token/` | authentification de l'utilisateur | Body : {username: str, password: str}
| `POST` | `/api/token/refresh/` | Refresh token utilisateur | Body : {refresh: str}
| `POST` | `/api/projects/` | Créer un projet | Body : {name: str, description: str, project_type: str (Choice : Backend, Front-end, iOS, ANDROID)}
| `GET` | `/api/projects/` | Liste des projets |
| `GET` | `/api/projects/<project_id>/` | Détails du projet |
| `PATCH` | `/api/projects/<project_id>/` | Modifier le projet | Body : {name: str, description: str, project_type: str}
| `DELETE` | `/api/projects/<project_id>/` | Supprimer le projet |
| `POST` | `/api/projects/<project_id>/contributors/` | Ajouter un contributeur | Body : {user: int}
| `GET` | `/api/projects/<project_id>/contributors/` | Liste des contributeurs du projet |
| `DELETE` | `/api/projects/<project_id>/contributors/<contributor_id>/` | Supprime le contributeur |
| `POST` | `/api/projects/<project_id>/issues/` | Créer une issue sur le projet | Body : {assigned_to: int user, name: str, description: str, status: str(choice: To Do, In Progress, Finished), tag: str(choice: Bug, Feature, Task), priority: str(choice: Low, Medium, High)}
| `PATCH` | `/api/projects/<project_id>/issues/<issue_id>/` | Modifier l'issue du projet | Body : {assigned_to: int user, name: str, description: str, status: str(choice: To Do, In Progress, Finished), tag: str(choice: Bug, Feature, Task), priority: str(choice: Low, Medium, High)}
| `GET` | `/api/projects/<project_id>/issues/` | Liste les issues du projet |
| `GET` | `/api/projects/<project_id>/issues/<issue_id>/` | Détails de l'issue |
| `DELETE` | `/api/projects/<project_id>/issues/<issue_id>/` | Supprimer l'issue |
| `POST` | `/api/projects/<project_id>/issues/<issue_id>/comments/` | Ajouter un commentaire sur l'issue | Body: {description: str}
| `PATCH` | `/api/projects/<project_id>/issues/<issue_id>/comments/<comment_id>/` | Modifier le commentaire | Body: {description: str}
| `GET` | `/api/projects/<project_id>/issues/<issue_id>/comments/` | Liste les commentaires de l'issue |
| `DELETE` | `/api/projects/<project_id>/issues/<issue_id>/comments/<comment_id>/` | Supprimer le commentaire |

> 🔒 Tous les endpoints nécessitent une authentification JWT sauf la route d'inscription.

---

## 📦 Installation
1. **Cloner le dépôt GitHub**
```bash
git clone https://github.com/wilodorico/Softdesk-api.git
cd Softdesk-api
```

2. **Créer et activer l'environnement virtuel**
- Ce projet utilise pipenv pour gérer les dépendances (avoir pipenv installé)
- Faire un python --version version minimale (3.11)
- Ajuster la commade pipenv avec votre version de python
```bash
pipenv --python 3.12
```
- Activer l'environnement virtuel :
```bash
pipenv shell
```
- Installer les packages :
```bash
pipenv install
```

---

## 🧪 Tests et documentation

Les endpoints peuvent être testés via Postman :
- Télécharger la collection json dans le dossier postman_collection
- Importer la collection dans postman
- Postman a été configuré pour utiliser le bearer token dans l'environnement
- Générer un token via la route /api/token/ et il sera partagé sur toutes les routes qui le demande 😉

Documentation : OpenAPI (Swagger / Redoc)
- Swagger : http://127.0.0.1:8000/api/schema/swagger-ui/
- Redoc : http://127.0.0.1:8000/api/schema/redoc/

## 👤 Auteurs

Projet réalisé dans le cadre de la formation développeur d'application Python chez OpenClassrooms.

Auteur principal : Wilfried.