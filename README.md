# Quiz Flask — Version examen

Cette version utilise les images extraites visuellement du PDF
« أسئلة اختيار متعدد مع أجوبة مباشرة.pdf » afin de conserver le rendu
arabe, les nombres et les dates comme dans le document source.

## Fonctionnalités

- 20 questions aléatoires par tentative (modifiable).
- Une seule question affichée à la fois.
- Boutons السابق / التالي.
- Indicateur 1/20 et barre de progression.
- Numéros des questions permettant de revenir directement à une question.
- Compteur de temps (20 minutes par défaut).
- Envoi automatique lorsque le temps est terminé.
- Score automatique.
- Page de correction affichant l'image originale de chaque question.
- Affichage de la réponse correcte.
- Page Admin protégée par mot de passe.
- Export CSV.

## Installation Windows

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Puis ouvrir:

http://127.0.0.1:5000

Admin:

http://127.0.0.1:5000/admin

Mot de passe par défaut:

admin123

## Configuration

Variables d'environnement:

- QUESTIONS_PER_QUIZ : nombre de questions, par défaut 20
- QUIZ_TIME_MINUTES : durée en minutes, par défaut 20
- ADMIN_PASSWORD : mot de passe admin
- SECRET_KEY : clé Flask

Exemple Windows CMD:

```cmd
set QUESTIONS_PER_QUIZ=20
set QUIZ_TIME_MINUTES=20
set ADMIN_PASSWORD=VotreMotDePasse
python app.py
```

## Déploiement Render

Build Command:

```text
pip install -r requirements.txt
```

Start Command:

```text
gunicorn app:app
```

Pour un déploiement public réel, configurez obligatoirement une vraie
SECRET_KEY et un vrai ADMIN_PASSWORD dans les variables d'environnement.
