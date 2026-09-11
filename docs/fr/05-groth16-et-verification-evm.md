# Groth16 et vérification EVM

La dernière étape peut convertir un reçu récursif en preuve Groth16 sur BN254, moins coûteuse à vérifier dans l'EVM.
Le passage identity_p254 prépare une preuve STARK avec un hachage adapté au champ BN254.
Le vérificateur Solidity doit contrôler le seal, l'identifiant de méthode et le digest du journal attendu.
Les clés et control IDs sont versionnés : mélanger des artefacts de versions différentes invalide la chaîne de confiance.
Cette enveloppe SNARK optimise la frontière on-chain sans remplacer les garanties STARK en amont.
Ce parcours est documentaire, sans audit ni certification cryptographique.
Aucune installation, compilation ou exécution n'a été réalisée ; les tests du dépôt restent la référence.
