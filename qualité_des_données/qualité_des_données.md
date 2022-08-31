# Qualité des données

__MyLearningBox__ = [Plateforme de cours en ligne MyLearningBox](https://mylearningbox.reseau-cd.fr/enrol/index.php?id=22888)
__TPs__ = ébauche d'un référentiel de données de SI

# Table of content

- [Qualité des données](#qualité-des-données)
- [Table of content](#table-of-content)
- [Introduction](#introduction)
  - [Outils](#outils)
- [Evaluation](#evaluation)
- [Enjeu](#enjeu)
- [Gestion des données de référence ou Master Data Management](#gestion-des-données-de-référence-ou-master-data-management)
- [Cours 2 - 27/10/2020](#cours-2---27102020)
  - [Qualité des données personnelles](#qualité-des-données-personnelles)
  - [Les cadres légaux](#les-cadres-légaux)
  - [Privacy by](#privacy-by)
  - [Droit des personnes (Article 15 et 21 du droit Français)](#droit-des-personnes-article-15-et-21-du-droit-français)
  - [Document à produire](#document-à-produire)
  - [Impact du RGPD sur le référentiel](#impact-du-rgpd-sur-le-référentiel)
- [Atelier 2 - Ajout d'information de données personnelles en conformité au RGPD à un référentiel](#atelier-2---ajout-dinformation-de-données-personnelles-en-conformité-au-rgpd-à-un-référentiel)
- [Cours 3 - 30/10/2020](#cours-3---30102020)
  - [Audit de données](#audit-de-données)
- [Atelier 3 - Réalisation d'un audit avec l'outil Talend MQ](#atelier-3---réalisation-dun-audit-avec-loutil-talend-mq)
- [Glossaire](#glossaire)

# Introduction

Aborder la qualité des données au sein de l'entreprise.
- lister les défauts possibles d'un jeu de données
- rédiger un référentiel de données (modèle commun à toutes les applications de l'entreprise)
- utiliser ce référentiel dans une démarche RGPD
- auditer des données grâce à certains indicateurs

## Outils

__Talend MDM/DQ Studio__  

# Evaluation

- ateliers (en groupe)
- QCM (indivivuel)


# Enjeu

Quel cadre légal gouverne les entreprises, comment est-ce appliqué aux entreprises.

- __importance des données__: la donnée est un actif. L'entreprise veut intégrer les données comme actifs.
- __difficulté de la qualité__: critères (actualité, cohérence, complétude, unicité, validité, véracité, utilisabilité, confiance, valeur...)  
- __nécessité de gouvernance__: __gouvernance de données__: mise en oeuvre de dispositifs (règles, normes, protocoles, conventions, contrat...) pour une meilleure coordination des acteurs en vue de décisions et d'actions concertées.  

- comment aller de "données" à "valeur": valoriser et exploiter les données.  

# Gestion des données de référence ou Master Data Management

L'objectif pour les entreprises est de le mettre en place.  

- acteurs et processus
- répertoire des informations sur les données
- contrôle des accès et préservation
- impacts sur le SI  

La gouvernance des données, définira les responsabilités et règles(manipulation des données) concernant les données. Des personnes seront responsable (réferrant) de telle ou telle donnée.   

Deux référentiels: __DM-BOK__ & __COBIT5__.  

1. Responsabilités: Globale -> chief data officer (CDO), doit connaître les processus et avoir des capacités de management.  
Par donnée clé -> data owner (métier), data steward (méthodo gestion de la donnée)  

2. Référentiel: document de référence -> énnumération des données clés(données métiers) + métadonnées(données sur nos données: nom de table de BDD, champs des tables, droits d'accès). On y ajoute les descriptions, utilité, point d'acquisition et point de vérité.

3. Métadonnées: données structurées -> modèle de données, qualité, niveau de partage. Données non-structurées -> document, page web, image, tag, titre, description. Qui a accès à ces données? Etablir une taxonomie des métadonnées.   

4. Sécurité: définir des catégories de données en fonction de leur gravité, caractère, niveau de confidentialité. Attribution de droits pour chacune.   

5. Architecture: comment modéliser et placer les données dans le SI de l'entreprise. 
   1. Modèle de données d'entreprise (MCD ou Entité relation à l'étrangers, UML...)
   2. Cartographies
   3. Propagation, définir un point de vérité et rendre les données disponibles pour tout acteur souhaitant accéder aux données( via un mode de mise à disposition) par API, export CSV...

# Cours 2 - 27/10/2020

Le cours se focalisera sur deux notions:
- les cadres légaux
- les privacy by  

## Qualité des données personnelles

Comment respecter les normes RGPD et cadre légal.

Le but est pour une entreprise, ou toute ressource d'une entreprise est respecter les lois, et voir l'impact sur les référentiels de données.  
Pour toute information, voir les article du RGPD. 

## Les cadres légaux

Les cadres légaux sont:  

En France: 
- 1978, Loi Informatique et Liberté.
- 2016, Loi République Numérique
- 2018, RGPD, maintenu par la CNIL

La CNIL est l'organisme qui fait appliquer les lois concernant le RGPD en France en tout cas.  

Au USA:
- 4ème ammendement (vie privée par rapport à l'Etat)
- En Californie: loi Shine The Light (2005) sur la vie privée.  
- Loi Disparates, chaque état a son propre modèle

En Asie:
- APEC: Asia Pacific Economic Corporation (cadre économique Privacy Framework). Document énumérant le cadre légale pour les pays d'Asie

__Les droits des citoyens__:
- consentement, accès, rectification (demande), effacement (droit à l'oubli), portabilité (une personne peut demander à récupérer ses données sous forme: export des données via CSV, API...), limitiation(limiter le périmètre des traitements concernant les personnes), information en cas de violation (perte des données, vols, piratage, détérioration...).  

Les traitements sur ces données sont également concernés. Il faut informer les personnes des traitements faits sur les données. Une personne a un droit d'opposition quant à certains traitements.   

__Les documents__:
- __Analyse d'impact__ : __PIA__ document du Périmètre de données sensibles.
- __Registre des traitements__: quel traitement fait-on sur la donnée, de manière à avoir un inventaire exhaustif.
- __Accountability__ (devoir que nous avons de garder une trace de tout ce qui est fait sur les données, de tout ce qui est fait pour les protéger). (tracabilité de tout action effectué et rendu de compte pour tout responsable de donnée d'une entreprise, mise en oeuvre des actions pour protéger et conserver les données);

Cela s'inscrit dans le but de respecter conformément le RGPD.  

__Les sanctions:__ 
- Niveau 1 -> dysfonctionnement (pas bien tenu le registre ou pas d'analyse d'impact) (pénalité allant jusqu'à 2% du CA, ou 10M)
- Niveau 2 -> droit des personnes (refus, ou sciemment passé le consentement ou injonction de la CNIL non respecté) (// 4% du CA, ou 20M)
- Code Pénal (Hors RGPD, spécifique à la France) -> code pénal (condammable personnellement si détournement de données personnelles) (Jusqu'à 300K ou 5 ans de prison)

## Privacy by

Tout ces textes de lois plus le RGPD font beaucoup allusion au __Privacy By__.  

Articles de lois définis dans une loi Canadienne datant d'avant le RGPD.

__Privacy by default__: par défaut, il faut protéger les données personnelles. Si, les données n'ont pas besoin d'être traitées, on ne les stocke pas dans l'entreprise, et on ne les met pas à disposition, sauf pour telle ou telle personne de l'entreprise. Certaines personnes n'ayant pas besoin de certaines donnée, ne doivent pas avoir d'accès à ces données. Il faudra ces données du MDM.  
__Privacy by design__: dès la conception, prise en compte de la protection des données personnelles. Nous pouvons __anonymiser__ ou __pseudonymiser__ les données afin d'éviter de voir directement qui est affecté à ces données personnelles. Exemple d'anonymisation: Perdre un lien entre un ID et un achat afin de perdre l'identité de la personne. Exemple de pseudonymisation: Décoreller les deux données, avoir juste un id qui ne permet de ne pas voir directement dans la donnée qui est associé, mais au besoin permettra de retrouver qui. Ainsi, nous respectons le RGPD dès la conception. Ce __privation Privacy By Design__ est soumis à une __Obligation de moyens__: Montrer que l'on a tout mis en oeuvre dans les processus du Privacy by design. Car nous ne sommes pas à l'abri de perdre l'anonymisation.   


## Droit des personnes (Article 15 et 21 du droit Français)

- Droit du consentement (majorité numérique en France 15ans et 16 en UE, elle précède la majorité) La personne peut donner ou retirer son consentement. Ceci est valable pour tous les droits.
- Requêtes : toute requête d'une personne majeure numériquement, droit être traitée au plus vite, l'entreprise doit tout mettre en oeuvre afin de montrer qu'elle aura fait les traitements nécessaire dans les meilleurs délais (accountability). Si, l'entreprise n'a pas pu le démontrer, l'entreprise serait condamnable par les lois RGPD. 
- MDM (collaboration entre les responsables des données afin de respecter les droits des personnes au mieux et aller au plus vite, traitement consigné dans le référentiel, il peut y avoir une communication entre le responsable des données personnels et les responsables des données de références).  

## Document à produire

Il y a plusieurs documents à produire:  

- Acountability (document de traçage de toute activité), prouve le respect du RGPD et l'adaptation de l'entreprise (gestion des nouveaux fichiers) Cela sera facile avec le référentiel car il y a un dialogue entre le DPO Data Privacy Owner (responsable des données personnelles) et le responsable des données de référence.
- Analyse d'impact de traitement (Pour données sensible, liée à la religion ou santé, aussi donnée lié à un contrat de vente ou de travail(augmentation...)) => faire une analyse des risques, si risque faire une déclaration auprès de la CNIL (gestion des risques et contact éventuel auprès de la CNIL, nature et finalité des traitements). Il est possible de faire un PIA, outil téléchargeable en ligne. La démarche provient de la CNIL. 
  - Démarche ISO 27001 (démarche de sécurité): Nous pourrons montrer les mesures de sécurité à mettre en oeuvre dans l'analyse d'impact.  
  - Etude de risque, si il y a eu une attaque par organisation criminelle ou autre impact... Prévenir la CNIL si des risques résiduels sont présents sur des données sensibles ou liées au contrat de travail.

Il se peut qu'il y ait pas de données sensibles et donc, d'analyse de risque à faire. UN registre des activités pourra être obligatoire en fonction de certains critères de l'entreprise.  

- Registre des activités et traitements (Article 30 RGPD) (pour toute entreprise ayant plus de 250 collaborateurs ou si le traitement des données est non-occasionnel) Il faudra définir un responsable du registre. Il faudra tenir ce registre à jour. Avec l'aide du MDM nous avons la nature, finalité des données collectées ainsi que le contact du responsable afin de nous aider à remplir le registre.  


## Impact du RGPD sur le référentiel

Le référentiel nous aide à gérer le RGPD. Mais comment préparer le référentiel afin de faciliter les démarches de gestion RGPD.  

- Identifier dans le ref, tous les points d'acquisitions de données personnelles, données clés et de références
- Indexer en début de document les données personnelles trouvées, pas mal en début de document.
- Préciser ensuite Nature et finalité des traitements
- Préciser aussi Mode d'acquisition et de stockage des traitements.  
- Préciser Délai d'effacement/conservation des données personnelles.  
- Préciser éventuellement les détails sur les sous-traitants (il est possible que nous éligions des responsables non-internes) Dépendant des services (commercial, financier) on pourra préciser les temps de conservation de certaines données. 
- Sécurité: Pour chaque donnée personnelle, réaliser une etude de risque (ISO 31000 norme liée aux traitement des données), procédure de gestion de validation (comment prévenir les utilisateur de tout changement ou violation de données personnelles), pseudonymisation/anonymisation (précision les mesures pouvant être mises en oeuvre).  

Dans ce cadre légal du RGPD, il y a beaucoup d'élément à étudier afin d'être en conformité. Le référentiel nous aide à être en conformité et inversement le RGPD fait que le référentiel doit s'adapter.   

# Atelier 2 - Ajout d'information de données personnelles en conformité au RGPD à un référentiel

- énumérer les données personnelles (ex: table personne...) sur la page d'index
- voir les tables concernées
- choisir quels traitements, impacts,
- Recopier les zones en jaunes pour toute table concernées par le traitement de données personnelles.  

- sur la page d'index, pointer vers les différentes pages que nous aurons renseignées.  

# Cours 3 - 30/10/2020  

## Audit de données

__Outils:__ Talend Open Studio for Data Quality, en version communautaire. Il est en Java, sur une base Eclipse.  

- Requis: JRE installé
- Télécharger le zip pour Windows 
- Dézipper dans un répertoire utilisateur, plutôt que système, car il nous faudra des droits utilisateur pour lancer certaines commandes.  
- Double-cliquer sur l'exécutable. Si message d'erreur, lancer le programme en admin. Si demande de télécharger des libraires supplémentaire, ne pas le faire, elles ne seront pas nécessaires pour nos ateliers. Si un message d'erreur persiste, vérifier notre version de Java ou regarder la stack trace générée.    

Depuis la perspective Talend:
- Bibliothèque : toutes nos données d'audit conservées
- Modèles: toutes nos connexions
  - Connexions au bases de données, clique droit et nouvelle connexion pour ajouter une BDDà auditer (indiquer, l'hôte, le port et autre donnée nécessaire) 
  - Fichier délimité, clique droit et nouveau fichier délimité, pour le TD, indiquer un nom, objectif, description, et faire de l'audit sur un fichier csv par exemple.


# Atelier 3 - Réalisation d'un audit avec l'outil Talend MQ

Basé sur l'exercice 3 sur MyLearningBox, réaliser un audit avec l'outil Talend MQ et faire un petit rapport d'audit contenant les captures d'écrans des indicateurs et résultats obtenus.
L'audit se fera sur un fichier CSV contenant les données.

Un audit est un constat fait sur la donnée.  


__Faire une fréquence de valeurs__: voir fin de vidéo, faire des indicateurs. Aller dans les indicateurs, chercher dans statistiques avancées et sélectionner fréquence de la valeur. Fréquence d'apparition d'une valeur.  

# Glossaire

__SIRH__ = logiciel permettant de gérer les ressources RH  
__Sage__ = Logiciel de compta
__LDAP__ = Annuaire d'entreprise (contient la liste des employés et services)  
__Magento__ = CMS de vente en ligne.
__CRM__ = logiciel de relation client, CRM hébergé en ligne (via HubSpot). Ces logiciels permettent de suivre les traces de suivi client, rdv retour etc... Le leader est salesforce mais des entreprises peut le personnaliser en fonction de leur méthode de travail.  
__Aras__ = PLM (Product Life Cycle Management). Gestion du cycle de vie d'un produit. Outil logiciel permettant la documentation sur l'élaboration et commercialisation d'un produit.  
__Odoo__ = Outil de SCM open source (Supply Chain Management). Gestion des flux et stocks.  

