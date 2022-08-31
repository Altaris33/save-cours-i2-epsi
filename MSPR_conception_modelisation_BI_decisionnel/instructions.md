# Solution BI  

Voir le doc MSPR Conception, Modélisation, Implémentation d'un solution BI.  

# MyLearningBox

[Allez vers MyLearningBox](https://mylearningbox.reseau-cd.fr/login/index.php)

# Groupes
De 4 à 5.  

# Powerpoint et présentation oral

en anglais

# Dossier de rendu

en français à l'écrit  

# Sujets & Définitions

L'entreprise SO-EMBALLAGE souhaite moderniser sa gestion de stocks.  

- informatique décisionnelles: informatique utilisant les données de l'entreprise exploitable afin de favoriser l'aide à la décision.  

# Indicateurs

Trouver des indicateurs pour l'entreprise, sous forme de graphique ou tableau de bord afin d'aider la prise de décision.  

> Mettre en place des outils décisionnels.  

Datawarehouse: entrepôt de données, en passant par une base de données classique, et l'orienter avec les données favorisant nos graphiques décisionnels. La DataWarehouse peut contenir plusieurs Datamarts.   
Datamart: magasin de données (entrepôt de données en plus simple).
Création d'un ETL: partir de la base de données fournies, et créer la base de données pour l'entrepôt.  

- partir des modèles de données (fichiers .sql sur mylearningbox)  
- conception d'une base de données qui nous aidera à obtenir les indicateurs, créer un entrepôt (dataware)    
- (plus dur mais moins prioritaire, chercher et intégrer des données externes)  
- maqueter le tableau de bord d'après toutes ces données

## Indicateurs & données à récupérer

- fluctuation des stocks
- quantité de stock par mois (nb de commandes)


Passer par des vues SQL. Parler de la préconisation des solutions de types scripts en Python, scripts en SQL, Microsoft Power BI, ELK.  



# Outils

- moteur de BDD (données)  
- tableau de bord => Google Data Studio, ou Power BIs  
- bonus data mining (faire parler les données via des graphes), difficile et optionnel  
- ELK: suite combinées de base de trois outils: Elastic Search(moteur de recherche, stocke des données pour analyse de données), LogStash(système de logs, pour faire des analyses) et Kibana(interface pour Elastic Search pour générer des graphes et informaitons). Il est possible d'ajouter d'autres plugins.  

- Récupérer une image docker:  
```
$ sudo docker pull sebp/elk
```

- Lancer un container Docker:
```
$ sudo docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk
```  

- Pour aller plus vite, le lancer avec Docker Compose en créant un fichier `docker-compose.yml` à l'endroit souhaité contenant les informations sur le nom de l'image et le port:
```yml
elk:
  image: sebp/elk
  ports:
    - "5601:5601"
    - "9200:9200"
    - "5044:5044"
```  

- lancer ensuite, depuis le même répertoire: 
```
sudo docker-compose up elk
```

- pour le couper faire:
```
sudo docker-composer down elk
```  
  
Le résultat sera le même mais avec un effort moindre.  

> Attention, il faut avoir un mémoire virtuelle (vm.max_map_count) au moins égale à celle du container en question. Sinon il y aura une erreur lors de l'exécution du container. Auquel cas, il faut setter avec la bonne quantité de mémoire virtuelle avec `sudo sysctl -w vm.max_map_count=262144`. `262144` étant la valeur choisie par le container.  

Se rendre sur l'interface Kibana via `localhost:5601`.  


# Diagramme

- Indiquer les données plus importantes en plus grand si possible.  
- progression chronologique: privilégier les histogrammes.
- répartition: diagrammes de surface, diagramme circulaire (avec modération voire à éviter).  
- qualitatif: diagramme polaire, à bulles...
- rapport statiques à dynamique, drills down/Zooms, infos sur des données... 


> Eviter les camembert, et diagramme en 3D, sauf si nous savons bien quoi démontrer.  