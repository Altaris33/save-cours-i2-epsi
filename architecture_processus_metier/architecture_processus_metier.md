# Architecture Processus Métier (Business Process Management ou BPM)

# Table of contents
- [Architecture Processus Métier (Business Process Management ou BPM)](#architecture-processus-métier-business-process-management-ou-bpm)
- [Table of contents](#table-of-contents)
- [Introduction & Objectif](#introduction--objectif)
- [Evaluation](#evaluation)
- [Processus métier](#processus-métier)
	- [Catégorie de processus métier](#catégorie-de-processus-métier)
	- [Modélisation d'un processus métier](#modélisation-dun-processus-métier)
- [Exemple d'un processus métier (représentation linéaire)](#exemple-dun-processus-métier-représentation-linéaire)
- [Modèle CMMi (Capability Maturity Model + Intégration)](#modèle-cmmi-capability-maturity-model--intégration)
- [BPMN ( Business Processing Modeling Notation)](#bpmn--business-processing-modeling-notation)
	- [Symboles](#symboles)
- [Bonita](#bonita)
	- [Installation (Linux)](#installation-linux)
- [Cours 2 07/12/2020 - Installation de Bonita et TP](#cours-2-07122020---installation-de-bonita-et-tp)
- [Cours 3 08/12/2020 - Atelier Architecture processus métier](#cours-3-08122020---atelier-architecture-processus-métier)
- [Cours 4 14/12/2020](#cours-4-14122020)
- [Conclusion](#conclusion)
- [Glossaire](#glossaire)


# Introduction & Objectif

Matérialiser un processus dans le but de la comprendre et prendre des décisions efficaces et optimiser le système.  

Logiciel de modeliser d'architectures: __Bonita__.  

- Comprendre la place et le rôle du SOA (Service Orienté Architecture) et BPM.
- Identifier les apports mutuels
- Modeliser / exécuter des processus métier et identifier le services qui en découlent
- Connaître les enjeux de la gouvernance à travers une SOA et son BPM
- Etudier les relations entre BPM, SOA et intégration  

# Evaluation

- implication dans le cours
- réalisation des exos
- pertinence des réponses
- évaluation par groupe (oral + pptx)  


# Processus métier

Enchaînement d'activités réalisées de manière __chronologique__ par différents acteurs collaborants pour délivrer un résultat tangible et une __valeur ajoutée__ métier pour l'entreprise. Tout processus a une entrée/sortie, est composé de sous-processus, règle métiers (décisions) et d'activités. Des KPI (Key Performances Indicator) permettent de capturer les performances des processus.Le processus métier possède des groupements ou objets de groupements (utilisateur, vendeurs, acteurs...).       

C'est un flux d'information au sein d'une organisation, décrit le métier, et non le système informatique.  

Les Processus métiers peuvent être réalisés tout d'abord de façon linéaire, puis ensuite schématisés.  

## Catégorie de processus métier

- processus client
- processus support
- processus internes

## Modélisation d'un processus métier

- nommage (verbe d'action + objet) -> vendre un produit bancaire, évaluer une demande de prêt, identifier le client... Eviter les verbes d'actions comme gérer ou traiter. Eviter toutes références aux applications informatiques. Eviter les mots données, informations pour modélisater l'objet.  
- Identification d'événement déclencheur, de résultat attendu, objectifs poursuivis
- Diagramme d'activités ou diagramme BPMN  

# Exemple d'un processus métier (représentation linéaire)

<h2 style="	margin: 1em 0 0.5em 0;
	font-weight: 600;
	font-family: 'Titillium Web', sans-serif;
	position: relative;  
	font-size: 36px;
	line-height: 40px;
	padding: 15px 15px 15px 15%;
	color: #FFF;
	box-shadow: 
		inset 0 0 0 1px rgba(53,86,129, 0.4), 
		inset 0 0 5px rgba(53,86,129, 0.5),
		inset -285px 0 35px white;
	border-radius: 0 10px 0 10px;
	background: #FFF url(images/matrix_img.jpg) no-repeat center;"> Distribution de tee-shirt (ZEvent) </h2>

Constat: "Je veux un tee-shirt ZEvent pour soutenir l'organisme non-gouvernemental &laquo; Amnesty International &raquo;".  

__Côté viewer:__
- Sélectionner le tee-shirt sur la boutique en ligne
- Commander le tee-shirt
- Valider la commande
- Mail de réception de confirmation de la commande
- Attente de notification d'envoi
- Réception de la commande

Constat: "Jai bien reçu le tee-shirt et peux le porter"

__Côté expéditeur:__

- Réception de la commande
- Préparation de la commande
- Livraison de la commande
- Suivi de la commande
- Confirmation de livraison de la commande
- Réception du paiement

# Modèle CMMi (Capability Maturity Model + Intégration)

- Mesure le niveau de maturité d'une entreprise
- Echelle de mesure pour les processus  

# BPMN ( Business Processing Modeling Notation)

BPMN est un référentiel graphique pour réaliser des schémas tout comme SQK est un language commun à plusieurs SGBD. Il s'agit d'un standard OMG.  

Il faut gagner du temps et de l'argent, en formalisant, harmonisant, industrialisant les processus de l'entreprise.  
- améliorer la communication entre les mondes "métier" et "technique".  
- réseau d'objets graphiques représentant les activités qui interviennent dans le processus
- lien avec l'UML avec les diagrammes d'activité et simmilitude dans certains symboles.    

Le processus métier a une __granularité dans le temps__ et la notion de temps est donc importante (sauf tâche parallèle).  

## Symboles 

- objets de groupement: gros rectangle sur le schéma représentant toute une phase d'activités et tâches. 
  - Pool
  - Lane
- objets de flux:
- artefact connecteurs/ objets de liaison: flèches sous différentes formes.

  - activités: sous la forme de 2 catégories: atomique ou composée 
    - boucles, multi-instance, compensation(exemple: si un paiment par carte est refusé, alors choix d'un autre moyen de paiement)

  - tâches: modélisées par des pictographes, à l'intérieur d'un rectangle.  
  - enchainement d'activités: par points de jonction ou gateway (losanges). Il amène vers des choix et possibilités.

- Evènements de départ et fins: modélisés par des cercles pouvant contenir des éléments.  
- Artefact: annotation, objets de données ou autre.   

# Bonita 

__Bonita__ is an open-source and extensible platform for business process automation and optimization. Bonita Platform accelerates the development and production of business applications, with clear separation between capabilities for visual programming and for coding.  
BPMN (Business Process Modeling Notation), full extensibility, and reusable components allow smooth collaboration among the different profiles on the IT team, and with the business teams.
Bonita integrates with existing information systems, orchestrates heterogeneous systems, and provides deep visibility into processes across the organization.  

Bonita Platform has two components: the development environment, Bonita Studio, and the runtime environment, Bonita Runtime.  

## Installation (Linux)

- Download the `.run` file BonitaStudioCommunity-x.y.z-x86_64.run.
- Give permissions to execute the file in question: `chmod +x BonitaStudioCommunity-x.y.z-x86_64.run`.  
- Execute the file, that will launch a script to install it on the system: `./BonitaStudioCommunity-x.y.z-x86_64.run`.  
- Launch the file manually to start Bonita: `cd/<user>/BonitaStudioCommunity` -> `./BonitaStudioCommunity`  


# Cours 2 07/12/2020 - Installation de Bonita et TP

Bonita Studio: modélisation des processus
Bonita Portal: Exécution des processus


# Cours 3 08/12/2020 - Atelier Architecture processus métier

Trouver un sujet métier, avec un ou des processus métier à améliorer et le mettre en exergue avec la notation BPMN sous Bonita.  

Présentation de 10/15 mins via un powerpoint, peu axée sur la technique. Avec présentation du contexte initiale, puis la présentation BPMN. Suivie d'une présentation technique du bonita mis en oeuvre de 5 à 10 minutes (contexte non-optimisé, processus métier, présentation technique détaillée avec outils utilisé par Bonita).    

# Cours 4 14/12/2020

Exposés + Questions  

Extraction des images lors de l'extraction.  
Dossier afin de valoriser notre présentation.  

# Conclusion

Le processus métier est une priorité pour l'entreprise. Elle est pratique pour tout nouvel arrivant, afin de montrer le modèle suivi par l'entreprise. Elle effectue un contrôle et amélioration des échanges métiers.  

# Glossaire

__SOA__: Service Oriented Architecture - Architecture Orienté Service