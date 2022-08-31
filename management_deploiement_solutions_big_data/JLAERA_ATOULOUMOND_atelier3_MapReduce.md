# Management & Déploiement de solution Big Data - Atelier 3 - MapReduce: Statistiques de location de films  

# Table of contents  
- [Livrables](#livrables)  
- [Commandes HDFS](#commandes-hdfs)  
- [Script (PJ)](#script-pj)  

# Livrables

- commandes HDFS utilisées pour l'atelier  
- scripts de mappers et reducers

# Commandes HDFS

- création du répertoire de stockage des fichiers csv: `hdfs dfs -mkdir -p /user/root/rental/in`
- ajout du fichier dans le répertoire de stockage des données d'entrée: `hdfs dfs -put sakita_rental.csv /user/root/rental/in`
- vérification de la présence du fichier dans le nouveau répertoire: `hdfs dfs -ls /user/root/rental/in`  
- test des mappers en local: `cat sakital_rental.csv | mapper_location_per_client.py`
- test des reducers en local: `cat sakital_rental.csv | mapper_location_per_client.py | reducer1.py`  
- exécution du MapReduce via Hadoop Streaming: `hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapred.reduce/tasks=2 -files src/mapper_location_per_cilent.py,src/reducer1.py -mapper mapper_location_per_client.py -reducer reducer1.py -input /user/root/rental/in -output /user/root/rental/out`    

# Script (PJ)

- cf script en PJ du zip.  
  - `mapper_location_per_client.py`