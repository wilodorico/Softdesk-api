# 🛠️ SoftDesk – API de gestion de projets et de tickets

**SoftDesk** est une API REST développée avec **Django REST Framework**. 

Elle permet à des utilisateurs authentifiés de gérer des projets collaboratifs, de suivre des tickets (issues) et d’interagir via des commentaires. 

Le projet respecte les exigences de sécurité (OWASP, RGPD) et vise une conception optimisée et durable.

---

## 🚀 Fonctionnalités principales

- Inscription
- Authentification par JWT (login, token)
- Création de projets par des utilisateurs authentifiés (Le créateur devient auteur et contributeur)
- Gestion des contributeurs par l'auteur du projet (ajout, suppression)
- Création d'issues + assignation à un contributeur (priorité, statut, tag)
- Ajout de Commentaires sur les issues par les contributeurs uniquement
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
| `POST` | `/api/users/` | Inscription utilisateur | Body : {username: str, password: str, password2: str, age: date, can_be_contacted: bool, can_data_be_shared: bool}|
| `PATCH` | `/api/users/<id>/` | Modifier utilisateur | Body : {username: str, password: str, age: date, can_be_contacted: bool, can_data_be_shared: bool}|
| `GET` | `/api/users/` | Liste utilisateurs |
| `GET` | `/api/users/<id>/` | Détails utilisateur |
| `DELETE` | `/api/users/<id>/` | Supprime utilisateur |
| `POST` | `/api/token/` | authentification utilisateur | Body : {username: str, password: str}
| `POST` | `/api/token/refresh/` | Refresh token utilisateur | Body : {refresh: str}
| `POST` | `/api/projects/` | Créer un projet | Body : {name: str, description: str, project_type: str (Choice : Backend, Front-end, iOS, ANDROID)}
| `GET` | `/api/projects/` | Liste projets |
| `GET` | `/api/projects/<id>/` | Détails projet |
| `PATCH` | `/api/projects/<id>/` | Modifier projet | Body : {name: str, description: str, project_type: str}
| `DELETE` | `/api/projects/<id>/` | Supprimer projet |
| `POST` | `/api/projects/<id>/contributors/` | Ajouter un contributeur | Body : {user: int}
| `GET` | `/api/projects/<id>/contributors/` | Liste contributeurs du projet |
| `DELETE` | `/api/projects/<id>/contributors/<id>/` | Supprime contributeur |
| `POST` | `/api/projects/<id>/issues/` | Créer une issue sur un projet | Body : {assigned_to: int user, name: str, description: str, status: str(choice: To Do, In Progress, Finished), tag: str(choice: Bug, Feature, Task), priority: str(choice: Low, Medium, High)}
| `PATCH` | `/api/projects/<id>/issues/</id>/` | Modifier issue | Body : {assigned_to: int user, name: str, description: str, status: str(choice: To Do, In Progress, Finished), tag: str(choice: Bug, Feature, Task), priority: str(choice: Low, Medium, High)}
| `GET` | `/api/projects/<id>/issues/` | Liste issues projet |
| `GET` | `/api/projects/<id>/issues/<id>/` | Détails issue |
| `DELETE` | `/api/projects/<id>/issues/<id>/` | Supprimer issue |
| `POST` | `/api/projects/<id>/issues/<id>/comments/` | Ajouter commentaire sur une issue | Body: {description: str}
| `PATCH` | `/api/projects/<id>/issues/<id>/comments/` | Modifier commentaire | Body: {description: str}
| `GET` | `/api/projects/<id>/issues/<id>/comments/` | Liste commentaires de l'issue |
| `DELETE` | `/api/projects/<id>/issues/<id>/comments/<id>/` | Supprimer commentaire |

> 🔒 Tous les endpoints nécessitent une authentification JWT.



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

Les endpoints peuvent être testés via Postman : http://localhost:8000/api/

Documentation : OpenAPI (Swagger / Redoc)
- Swagger : http://127.0.0.1:8000/api/schema/swagger-ui/
- Redoc : http://127.0.0.1:8000/api/schema/redoc/

## 👤 Auteurs

Projet réalisé dans le cadre de la formation développeur d'application Python chez OpenClassrooms.

Auteur principal : Wilfried.