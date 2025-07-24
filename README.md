# ML-MAZE

Ce projet propose une activité pédagogique pour apprendre aux élèves (11–14 ans) comment un algorithme peut naviguer un labyrinthe.

## Objectif

* Expérimenter la différence entre une programmation statique par règles et un apprentissage automatique (Q-learning) pour résoudre un labyrinthe.

## Utilisation

1. Lancez `maze_ml_activity.py` pour générer un labyrinthe aléatoire.
2. Observez la solution par règles (recherche de chemin) puis par un agent à apprentissage.

```bash
python maze_ml_activity.py
```

Ou ouvrez `maze_activity.html` dans votre navigateur pour la version Blockly interactive.

Dans cette interface web, vous disposez de plusieurs boutons de contrôle :

- **Start** : lance l'exécution automatique de l'agent dans le labyrinthe.
- **Stop** : arrête l'exécution en cours.
- **Step** : avance d'une étape pour observer le comportement au ralenti.
- **Reset** : régénère un labyrinthe et replace l'agent au départ.
- **Show path** : affiche le chemin calculé par l'algorithme de recherche (BFS).
- **Train AI** : entraîne l'agent par apprentissage automatique.
- **Mode** : alterne entre l'exécution par règles et par IA entraînée.

## Notes pédagogiques

Au début, l'élève peut essayer de définir lui-même une séquence d'actions adaptée à un labyrinthe fixe. Ensuite, le labyrinthe change à chaque exécution et l'élève constate que sa solution doit généraliser. C'est l'occasion d'introduire l'apprentissage automatique.
