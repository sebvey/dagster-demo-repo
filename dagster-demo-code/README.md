# ASSETS AND MATERIALIZATION

Développement autour du concept d'asset.  
asset = 'entité persistante' qui capture une compréhension du monde
eg: un fichier, un répertoire , une table, modèle ML ...


-> On ne développe pas des tasks (faire quelque chose) mais des assets
-> dans des modules pythons - un module python = une code location (eg. sous projet)

## ASSET
un ensemble de caractéristiques:
- nom, description, metadata, tags ...
- un ensemble de dépendances (assets)
- un partitionnement (une clé est un sous ensemble qui peut être matérialisé indépendamment)
- ... (pas mal d'autres choses qui vont structurer les interactions avec l'asset)

une fonction python qui permet la matérialisation de l'asset

@

## DAG
La définition des assets et de leurs dépendances permettent de définir un DAG

## MATERIALISATION

### Asset Jobs
- Manière 'historique'.
- Définition d'asset jobs. Ensemble d'assets comme cible.
- Un job run va matérialiser les assets dans l'ordre en fonction des dépendances
- Trigger: manual / schedules / sensors

### Declarative Automation
On défini des conditions sur l'asset. Quand celle-ci sont remplies, l'asset est matérialisé
Conditions fonction de : état de l'asset - état de ses dépendances - temporel

exemples:
- on_missing : déclenché quand l'asset n'est pas matérialisé mais que ses dépendances le sont
- eager : dès qu'une dépendance a été mise à jour, qu'il n'y a pas de dépendances en cours de maj ou manquantes
- cron : sur le CRON, si dépendances, après que celle-ci aient été mise à jour par ce même CRON
- custom

`basics.asset_automation -> eager automation`

https://docs.dagster.io/guides/automate/declarative-automation/#automation-conditions

### UI
- par asset
- upstream, downstream d'un asset
- en lançant des jobs
- on fait ce qu'on veut, on peut tout casser (demander des matérialisations alors que les deps sont pas matérialisées)

# INTERACTION AVEC L'EXTERIEUR

Les fonctions de matérialisations peuvent être utilisées avec plusieurs 'philosophies'.  


## IO MANAGERS

Se prête bien au pattern suivant:
- lecture des dépendances in-memory
- transformation in-memory
- écriture vers un datastore

PROS: la fonction de matérialisation porte la transformation. Facilement testable
https://docs.dagster.io/guides/test/unit-testing-assets-and-ops

## RESOURCES

Pour les autres cas de figures:
- You want to run SQL queries that create or update a table in a database
- Your pipeline manages I/O on its own by using other libraries/tools that write to storage
- Your assets won't fit in memory, such as a database table with billions of rows


## INTEGRATIONS
AWS:
Notre asset est interface pour lancer :
- lambda / glue / EMR / Athena / Redshift

Peux s'intégrer avec CloudWatch (logs / monitoring), Secrets Manager et autres

Equivalence GCP

Snowflake - execution de requete sur les warehouse
Databricks
Pleins d'autres


## METADATA

On peut attacher de la metadata à nos matérialisations. On retrouve cette donnée dans l'interface.  


## CHECKS
(io_manager)

Checks peuvent:
- définir des warning
- définir des failures

Checks simple :
- indédendant des assets
- sont joués par défaut à la fin de la matérialisation
- peuvent être bloquant

## Code Version

On peux définir une version de code à notre asset. Cette version de code sera associé au matérialisation.
Quand l'asset change de version, les matérialisations passent en async.

Si non défini, chaque run produit une version de code différente.

## Data version

Une version de donnée est associé à chaque matérialisation. Par défaut, c'est un hash de la version de code
et des versions des données dont il dépend.
On a la possibilité si nécessaire de calculer à la main la version de code


## Partitioning

Possibilité de partitionner les assets : l'asset est divisé en partitions. De base, un run matérialise une partition


## LOCAL vs DEPLOIEMENT

dagster dev :
- 

