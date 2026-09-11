# Architecture hôte–invité

RISC Zero sépare le programme hôte, chargé des entrées et des preuves, du programme invité exécuté dans la zkVM.
L'invité est compilé vers RV32IM et son image produit un identifiant qui engage le code autorisé.
Le journal contient les sorties que la preuve rend publiques ; le reste de l'état d'exécution peut rester privé.
Vérifier un reçu sans vérifier l'identifiant de méthode reviendrait à accepter la preuve d'un autre programme.
La frontière d'entrée/sortie doit donc être conçue comme une API de sécurité, avec encodage et version explicites.
Les crates zkvm et build montrent où ces engagements sont construits.

Suite : [02 — Exécution segmentée](02-execution-segmentee.md).
