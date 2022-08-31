# Analyse statistique & langage R

# Table of contents
- [Analyse statistique & langage R](#analyse-statistique--langage-r)
- [Table of contents](#table-of-contents)
- [Séance 1 - 10/02/21](#séance-1---100221)
- [Introduction & Objectif](#introduction--objectif)
- [R](#r)
- [Séance 2 - 02/03/21](#séance-2---020321)

# Séance 1 - 10/02/21  

Intro R & Manipulation de données

# Introduction & Objectif  

Nous allons utilier R comme outil statistique afin de traiter et d'organiser des volumes de données en masse.  
et en générer des informations et graphes.  

# R  

Interpréteur: renvoie des lignes avec des indices sous la forme de `[i]`. Il s'agit de l'indice du premier élément apparaissant sur la ligne qui est générée.     

- division euclidienne (entière): `%/%` = `13%/%3` = 4 
- modulo: `13%%3` = 1  
- affectation de variable: `<-` ou `=`  
- vecteur (ensemble de données de même nature/type): `vec <- c(14, 16, 18, 22)` (`c` pour `combine`)   
  - operations, se font termes à termes, si les vecteurs sont de tailles différents, la règle de recyclage s'applique (recycling rule) s'applique et le plus petit vecteur sera dupliqué afin de correspondre à la taille du plus grand vecteur. C'est ce qu'il se passe en réalité pour toute opération. R adapte les tailles des objets.   
- indexation en R: le premier élément est à l'indice 1 et non pas 0. 
- slicing `[i:j]`   
- `NA` : signifie une donnée manquante  
- conditionnement...
- R renvoie NA pour les jeux de données comportants des éléments valorisé à `NA`.  
- `na.rm= TRUE` permet d'omettre les NA avant d'effectuer les calculs... on sappelle cette syntaxe le __passage d'un argument nommé__.  
- `Factor` type de données R pouvant prendre un nombre limité de valeur (réponse à un questionnaire fermé avec choix). Sur certains éditeurs R ou version de R les `Factors` peuvent être affichés en `chr` pour `characters`.  

Si une ligne de code est à terminer, une nouvelle ligne avec un `+` apparaîtra.  

# Séance 2 - 02/03/21

R avec les statistiques bi-variées.  
__Statistiques bi-variée__ = __Etude de corrélation__ (régression).  