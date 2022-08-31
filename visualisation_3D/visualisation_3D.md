# Visualisation 3D

# Table of contents
- [Visualisation 3D](#visualisation-3d)
- [Table of contents](#table-of-contents)
- [Introduction & Outils](#introduction--outils)
- [Three JS](#three-js)
- [Object & Scènes](#object--scènes)
- [Animation](#animation)
- [Hiérarchie d'objets](#hiérarchie-dobjets)
- [Convetions Axes](#convetions-axes)
- [Cours 2 13/01/21](#cours-2-130121)
  - [Les matériaux](#les-matériaux)
  - [Textures](#textures)
  - [Maps](#maps)
- [Cours du 01/02/21](#cours-du-010221)
- [Données Astres](#données-astres)
  - [Soleil](#soleil)

# Introduction & Outils

Logiciel modélisation 3D: Blender.  

Objectifs: réaliser la Terre.  
- Voir les notions de la programmation 3D.  

- Ensuite travailler à plusieurs sur un sujet choisis.  

- Bibliothèque utilisée: Threee.js.  
- notion de plus bas niveau: mathématique avec calcul matricielle, vectorielle.  

- lien du cours: https://gayerie.dev/epsi-i2-3d/  
- solution: placées dans le répertoire `/solution`.  

- prérequis: avoir un hardware suffisant pour lancer de la 3D sur le web.  
> Les téléphones portables supportent bien la visualisation 3D car ils sont bien équippés. 

> 2D = 3D à laquelle on a retiré un axe (z).

# Three JS

Librairie open-source & gestionnaire de scènes basée sur l'API WebGL, portage de OpenGL ES (Embedded System).  

Il y aura peut-être besoin d'un serveur qui nous chargera les pages HTML pour permettre un chargement asynchrone de composant Three.js. Nous pouvons lancer n'importe quel type de serveur.  
Three chargera des composants en asynchrone.  

Three est un rendered d'objets & gestionnaire de scènes, représentant virtuellement les éléments de nos environnement, référence au cinéma. Un scène est un arbre mathématique. Pour ce faire, il utilise les objects canvas. Three js créera un object canvas et s'en servira pour créer des objets 3D. Nous y aurons accès avec l'attribut `docElement`.  

- voir un monde 3D: ajouter une camera (notion inventée sur les ordinateur pour répliquer la réalité), qui est une matrice de projection de dimensions 4x4 (4 dimensions).  
  - Caméra orhtographique (pratique, mais sans ligne de fuite et non réel) vs caméra de perspective (vrai perspective mimée). Derrière c'est que des maths via des matrices de projection. La caméra génèrera un cône de vision de la caméra appelé __Frustum__ tronqué par un __near plan__ et __far plan__. La caméra ne voit que ce qu'il y a dans le frustrum. Ceci n'est pas réel mais favorise l'optimisation, notamment dans les jeu vidéos lorsqu'un objet se charge lorsque nous avançons dans une scène. Donc le frustum représente ce que l'on peut voir. Axe z de la camera, sort de la caméra d'un point de vue cordoonées main droite(va vers notre oeil). Donc si nous augmentons la valeur de la position z cela signifie que la camera va reculer. 
  - Un Object de type Caméra Perspective comprtera 4 paramètres : un field of view (fov), le ratio largeur/longuer, le near plan et far plan.            

- scène: environnement, arbre mathématique
  - couleur, unité réglable entre 0 et 1, 1 étant la valeur la plus élevée dans le monde du graphisme. Ex: (1, 1, 1) = fond blanc.  

- rendre la scène en créant une image avec la méthode `render()` en passant en parallèle la scène et la caméra créées.   

Si nous changeons notre image, il faudra ajouter le code pour rendre la nouvelle image modifiée.   

# Object & Scènes  

Vulgairement, une scène est un ensemble d'objet 3D. Il faut se repérer dans l'espace d'un monde virtuel. Repère de coordonner à main droite basé sur la technologie OpenGL. Le camera est par défaut positionné à (0, 0, 0) et regarde vers -z (centre de la camera).    

Il s'agit en réalité d'un objet 3D contenant tout un ensemble d'autres objets 3D.  

Deux objets:  Mesh & Geometry

- `Mesh` = maillage/ensemble de points(vertices) permettant de représenter une forme en 3D. (plusieurs vertices, singulier vertex). Un vertex est un point ayant des informations dans l'espace, ex = (0, 0, 0). `Mesh` est un objet héritant d'un object appelé `Object3D`. Nous pourrons créer des faces. Les meshs contiendront des geometry. Donc si nous passons plusieurs vertices, nous créerons des triangles. Ces ensemble de triangles permettront de créer d'autres objets.   
- `Geometry` = figure géometrique, prenant des vecteurs en coordonnées, définissant des points.  

C'est la mémoire de la carte graphique qui travaillera avec les données concernant les points et géométries ce qui peut donc avoir un impact de performance. Pour des grosses scènes, la même geometry est utilisée pour des meshs différents.

> Le Mesh s'ajoute dans la scène et l'objet Geometry gère des points et espaces.  

Three JS propose un tas de geometry prédéfinies et utilisables.  

Un mesh ont 3 état: coordonnées, axe de rotation (radians / rotation d'Euler autour d'un des 3 axes), et scale (mise à l'échelle).  

Tous les objets 3D possèdent la méthode `lookA()`. Il faudra ajouter le shading afin de donner une impression 3D. Par défaut, il n'y a pas de shading: on parle de __flat shading__ dans ce cas de figure.  

Des méthodes(actions) s'ajoutent pour changer les états des objets: rotate et translate. L'ordre dans lequel les transformations sont faites sont importantes. De plus, Three Js appliquera les opérations dans l'ordre inverse qu'indiqué, car les opérations matricielles (multiplication de matrices) sont appliquées. Par exemple, une rotation de fera par rapport à un point.  

# Animation

Nombre d'images par secondes. 
Nous essairons d'afficher 60 images par seconde soit 1/60 d'images par secondes pour créer une animation continue. 
- `requestAnimationFrame` est une fonction standard JavaScript.  

Les méthodes d'actions sont utilisées pour créer des animations.  

# Hiérarchie d'objets 

Les objets peuvent fils d'autres objets. Les espaces de coordonnées changeront.  
Il est possible d'utiliser des objets `Group` de Three JS afin de place d'autres objets en son sein. Un objet ne peut avoir qu'un seul parent.    

# Convetions Axes

Les axes en 3D sont représentés comme suit:
x (1, 0, 0) rouge
y (0, 1, 0) vert
z (0, 0, 1) bleu  

# Cours 2 13/01/21  

## Les matériaux  

Avoir au moins une sphère pour la session qui va suivre.  

Matériaux en 3D: rendu d'une image sur la façon dont les objets doivent rendre la lumière (virtuellement). Représenter le monde réel au travers de matériaux.  
Ajout d'ombrage, en anglais shaders, programmes compilés dans la carte graphique.  

Un matériau c'est l'ensemble des paramètres utilisé par Three.js pour créer un shadeer. Ce sont des petites programmes qui tourneront dans la carte graphique, de base représenté par des pixels blancs. Pour faire de la 3D, nous allons imiter le réel en apportant de la notion de lumière (point, emplacement dans l'espace).  

Rappel: 3 vertex(points) = triangle.  

Ce sont des vecteurs qui donnent l'impression d'avoir des rendus de couleurs.  

- `MeshBasicMaterial`: matériau de base sans ombrage. Très intéressant pour la 2D, sans l'axe z. 
- `MeshLambert`: en lien au mathématiques de Gouraud
- `MeshPhong`: algo utilisé dans les anciens cartes graphiques
- `MeshStandard`: algo actuellement utilisés dans les jeux vidéos, ou film d'animations
- `MeshPhysical`: idem  
- ...  

Le PBR(Physical Based Rendering), modèle de génération d'image le plus réaliste qu'on a actuellement, utilisé par les jeux, films Disney ou Pixar...  

Tous les autres matériau auront besoin de paramètre de lumière et auront un rendu de couleurs variés.  

- `wireframe` transforme les objets en fils de fer.  

Le shader est un programme qui calculera les couleurs à apporter sur chaque côté des triangles. On parle de vecteurs d'incidence des lumières.  

Il y a 6 types de lumières (xxLight).  

Tous ceux-ci sont des objets héritant de 3DObject et donc positionnables sur l'objet Scene.  

> C'est donc l'ombrage et le shading qui créent les effets de 3D.  

## Textures

Prendre un pixel d'une image au lieu d'une couleur. Mais les images sont en 2D, les vertex ont donc besoin de coordonnées en 2D, coordonnées textures. On parle de convention u, v, u étant x et v étant y.  

Le fait de placer l'ensemble des triangles sur un object 3D depuis une image 2D est appelé processus de __dépliage UV__, qui créera les points et les mappera. Three.js le fera automatiquement pour nous avec les algorithmes gérés en arrière-plan.  
Donc les coordonnées 2D pour une image sont appelées UV.  

Three.js propose les objects `TextureLoader` via des requête XHR. Le navigateur web ne sera pas d'accord faute de sécurité, et il faudra donc placer nos fichier *.html* dans un serveur web.  

Si un update est fait, il faudra update à la main, en accédant au matériau de notre Mesh et utiliser la propriété `neddsUpdate` pour la basculer à `true` afin de recompiler le programme de shading.  
Il faudra les changer de manière asynchrone.  

`CubicTexture` objets permettent d'enfermer la scène dans un cube, donc sous la forme de 6 images pour chaque face du cube. Il faudra utiliser un loader particulier pour charger les textures.    

## Maps

Associées aux textures, ce sont des couches de couleurs qui feront surface sur les triangles de base.  

__Vecteur normal__: vecteur partant perpendiculairement de la surface plate de la base d'un plan. Ces vecteurs permettent de créer des __normal maps__.    

# Cours du 01/02/21  

Rappel Mini-projet: trouver des données à représenter en 3D et interagir avec l'utilisateur.  
Tout seul ou à deux.  

Scale = mettre à l'échelle les objets sans toucher à leur géométrie. Le scale mettra juste à l'échelle et noe changera la géométrie mais changera seulement l'objet.  
Une seule geo sphère qu'on passe en param de nos mesh, et appliquer un scale sur chaque planète pour adapter en proportion.  

Les points se déplaceront sur l'espace et les points seront multipliés par une matrice de transformation.   

__MVP__: trois matrices, 

Le Carte Graphique est bien câblée et adaptée pour faire des milliards de calculs de matrices.  

Un géométrie dans Three JS représentent les points de la géométrie. s

# Données Astres

## Soleil

Température surface: 5778 deg Celsius
Diameter: 1 392 684 km

