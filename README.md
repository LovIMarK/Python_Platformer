# Python Platformer Game

Un **jeu de plateforme en Python**, développé avec **Pygame**, inspiré du tutoriel YouTube de [freeCodeCamp.org](https://www.youtube.com/watch?v=6gLeplbqtqg).

Ce projet personnel a pour objectif de renforcer mes compétences en Python, Pygame et développement de jeux vidéo.  
Il inclut plusieurs niveaux, des pièges variés, des animations dynamiques, des particules, et un système de progression par niveaux.

📅 **Date de création** : mai 2023

---

## 🎮 Description

Ce jeu est un platformer classique avec :  
- Sauts, double sauts  
- Plateformes mouvantes  
- Pics, pièges, ventilateurs, projectiles  
- Checkpoints, chrono, score  
- Animations fluides pour le joueur et les pièges  

### ✅ Améliorations déjà apportées :
- Intégration de sprites personnalisés
- Double saut
- Fruits collectables comme système de score
- Attaque au corps-à-corps (slash)

---

## 🧭 Prochaines améliorations

- 🔁 **Refactorisation en POO complète** :  
  Transformer les entités du jeu en véritables objets orientés objets, pour améliorer la clarté, la modularité et la maintenabilité du code.

- 🧩 **Séparation des responsabilités** :  
  - Créer un module dédié à la gestion des **interactions entre objets** (collisions, effets, déclenchements).  
  - Séparer un fichier spécifique pour la **gestion des entrées clavier** (touche saut, déplacement, attaque, etc.).

- 📊 Ajout futur d’un système de statistiques ou d’XP (expérience).

---

## 📷 Captures d’écran

| Image | Description |
|-------|-------------|
| ![Gameplay](ScreenShots/level1.png) | Un aperçu du premier niveau avec des plateformes simples et des pièges basiques. |
| ![Gameplay](ScreenShots/levels.png) | La sélection des niveaux disponibles dans le jeu, avec plus de 50 niveaux débloquables. |
| ![Gameplay](ScreenShots/level2.png) | Un aperçu du second niveau. |
| ![Gameplay](ScreenShots/fire.png) | Le joueur saute au-dessus de pièges de feu : attention à bien calculer son saut ! |
| ![Gameplay](ScreenShots/trampoline.png) | Le joueur utilise un trampoline pour rebondir plus haut et atteindre des plateformes. |
| ![Gameplay](ScreenShots/checkpoint.png) | Le joueur atteint un point de contrôle (checkpoint) qui enregistre sa progression. |

---

## 🚀 Lancer le jeu

Assurez-vous d’avoir installé Python (>= 3.9) et Pygame.

```bash
# Cloner le repo
git clone https://github.com/ton-github/ton-projet.git
cd ton-projet

# Installer les dépendances
pip install pygame

# Lancer le jeu
python game.py
