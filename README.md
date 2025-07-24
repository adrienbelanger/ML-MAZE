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

## Notes pédagogiques

Au début, l'élève peut essayer de définir lui-même une séquence d'actions adaptée à un labyrinthe fixe. Ensuite, le labyrinthe change à chaque exécution et l'élève constate que sa solution doit généraliser. C'est l'occasion d'introduire l'apprentissage automatique.
