# ASSET / DEPENDANCE
Les dépendances sont déduites de deux manières complémentaires:
-  les dépendances explicites données dans la def de l'asset
- les dépendances de la fonction de matérialisation (si nom d'un arg = nom d'un asset -> dépendance)



# Declarative Automation

asset_basics -> asset_silver --> asset_gold_* -> en eager  
- asset_bronze_1: code versionné -> changement data version uniquement lors changement de code
- asset_bronze_2: pas de versionnement -> changement data version à chaque matérialisation
