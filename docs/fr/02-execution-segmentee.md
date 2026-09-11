# Exécution segmentée et reçus

Une longue exécution est découpée en segments afin de borner la mémoire nécessaire au prouveur.
Chaque SegmentReceipt engage un état initial, un état final et la partie de calcul correspondante.
La continuité entre segments empêche de raccorder deux exécutions incompatibles.
Les hypothèses différées permettent de référencer une preuve qui sera résolue plus tard par la récursion.
Le reçu final ne signifie que ce que son claim encode : méthode, journal et conditions de terminaison doivent être contrôlés.
Cette structure rend la preuve composable sans masquer les obligations de liaison.

Suite : [03 — STARK et FRI](03-stark-et-fri.md).
