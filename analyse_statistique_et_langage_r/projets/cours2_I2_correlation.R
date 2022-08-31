# cours 2 - Stats bi-variées & études de corrélations  
getwd()

# pendant chaque des dépenses en matière de dépenses publicitaires.
# etudier la relation entre les dépenses publicitaire et les ventes de l'entreprise (2 variables) 

budg <- read.csv2("~/I2/analyse_statistique_et_langage_r/projets/budget_pub.csv")
budg

str(budg)

# on affiche un nuage de point afin d'avoir un premier aperçu d'une éventuelle relation  
# chaque point a un abscisse les dépenses pub et en ordonnée les ventes correspondantes
plot(budg$Depenses.pub, budg$Ventes, xlab = "Depenses publicitaires", ylab = "Ventes")

# points relativement alignés: suggestion d'une forte corrélation engtre dépenses_pub et ventes, courbe
# plutôt sous la forme d'une droite, donc corrélation linéaire
# une nombre appelé corrélation linéaire peut mesurer à quel point les points sont alignés, il faut le calculer entre les 2 variables
# plus le coefficient linéaire(sa valeur absolue) est proche de 1, plus la corrélation sera forte  
# ici il s'agit d'une étude de phénomène croissante visible depuis le graphe  
# il se peut que le nombre soit négative (étude de phénomène décroissant) donc c'est pour cela que nous prenons la valeur absolue
# du coefficient de corrélation linéaire

# cor() = corrélation linéaire, use = prendre la totalité des observations 
cor(budg$Depenses.pub, budg$Ventes, use = "complete.obs")

# on peut ensuite trouver une droite qui ajustera au mieux le nuage de points (ajustement affine, équation d'une droite),
# si l'on une corrélation bonne
# on appelle cela régression linéaire
# expression des ventes(y) en fonction des dépensesPub(x) (l'ordre est important dans l'instruction)
reg <- lm(Ventes ~ Depenses.pub, data = budg)
reg

# intercept: ordonnée à l'origine
# depenses.pub: coefficient directeur
# y = 10,62x + 1383.47

# on trace ensuite la droite à partir de la régression calculée (droite qui passe au plus près du nuage de points)
abline(reg)

# à quoi cela sert-il? De faire des extrapolation/prévisions vu que la droit et la coef de corrélation sont fiables  
# Ex: Quel dépenses faudrait-il afin d'atteindre des ventes de 17000? (cf polycopié)  
# La fiabilité de la prévision dépendra de la force du coef de corrélation linéaire(noté r) et donc de l'ajustement de la droite affine
# plus l'on s'éloignera de la plage de valeuer, moins les prédictions seront fiables  
# calcul de prédiction avec R  

# on récupère les deux nombres de la variable reg
reg$coefficients[[1]]
reg$coefficients[[2]]

predict_vente <- reg$coefficients[[2]] * 17000 + reg$coefficients[[1]]
predict_vente

# lorsque l'on ne peut pas travailler avec les noms des variables, on peut utiliser l'indexation
str(budg)
plot(budg[,2], budg[,3], xlab = names(budg[2]), ylab = names(budg[2]))
cor(budg[,2], budg[,3], use = "complete.obs")
reg <- lm(budg[,3] ~ budg[,2], data = budg)
reg

# R possède une fonction pour faire les prédictions plus rapidement (ne marche que si la regression a été faite à partir des noms 
# des variables)
predict_var <- predict(reg, data.frame(Depenses.pub = 17000))
predict_var[[1]]

# prediction plus fine, avec un intervalle de prédiction, avec un fit qui est la moyenne d'un lower et upper
# plus lower et upper sont proche l'un de l'autre, plus la fiabilité de la prédiction est forte  
predict_var_encore_plus_complete <- predict(reg, data.frame(Depenses.pub = 17000), interval = "prediction")
predict_var_encore_plus_complete  


# Jusqu'à présent nous avons: 
# - fait de l'ajustement affine (droite)

# ajustement non-linéaire possible avec des changements de variables est possible

#-----------------------------------------------
# Exercice 4  
#-----------------------------------------------
# 1)
df_moteur <- read.csv2("~/I2/analyse_statistique_et_langage_r/projets/moteurs.csv")
df_moteur
str(df_moteur)  

names(df_moteur)

# changement du nom des variables avec une assignation vectorielle
names(df_moteur) <- c("motfab", "temps")
names(df_moteur)
str(df_moteur)

# calcul de la corrélation linéaire
# ici phénomène décroissant, plus l'on fabrique de moteurs, moins il faudra de temps pour en fabriquer
# de plus, il ne sera pas très fiable 
cor12 <- cor(df_moteur$motfab, df_moteur$temps, use = "complete.obs")
cor12

plot(df_moteur$motfab, df_moteur$temps, xlab="Nombre de moteurs fabriqués", ylab="Temps moyen de fabrication")

# la droite n'ajustera pas correctement le nuage de points, elle sera peu représentative, d'où la question 2 de l'ex 4  
reg12 <- lm(temps ~ motfab, data=df_moteur)
abline(reg12)

# 2) Ajustement du nuage de points par une courbe 
# Nous aurons besoin des logarithmes népérien des colonnes motfab et temps
df_moteur$lnmotfab <- log(df_moteur$motfab)
df_moteur$lntemps <- log(df_moteur$temps)
str(df_moteur)  

# calculer les 3 autres coef de correlation linéaire et voir lequel est le plus fiable
# meilleur coefficient mais pas top
cor1 <- cor(df_moteur$motfab, df_moteur$lntemps, use = "complete.obs")  

# encore meilleur coefficient
cor2 <- cor(df_moteur$lnmotfab, df_moteur$temps, use = "complete.obs")  

# dernière combinaison possible  
cor3 <- cor(df_moteur$lnmotfab, df_moteur$lntemps, use = "complete.obs")  

# on préférera donc la plus fiable et alors une régression entre lnmotfab et lntemps
plot(df_moteur$lnmotfab, df_moteur$lntemps, xlab="Nombre de moteur fabriqués(exprimé en log nep)", ylab="Temps moyen exprimé en log nep")

# on a bien une courbe affine qui se dégage, grâce au changement de variable  
reg_mot <- lm(lntemps ~ lnmotfab, data = df_moteur)
reg_mot
abline(reg_mot)

# prédiction pour 200 moteurs à fabriquer  
# on a donc y = ax + b
# soit y = -0.5481x + 4.0415
# soit y = 4.0415 * 200 - 0.5481
lntemps = reg_mot$coefficient[[2]] * log(200) + reg_mot$coefficient[[1]]  
lntemps
temps = exp(lntemps)
temps

predict(reg_mot, data.frame(lnmotfab = log(200)))

# effectuer la même prédiction en une seule ligne  
temps <- exp(predict(reg_mot, data.frame(lnmotfab = log(200)))[[1]])
temps

print(paste("Lorsque 200 moteurs seront fabriqués, on prévoit un temps moyen de: ",
            round(temps, digits = 1), "heures."),  quote = FALSE)

# TP final: dataset, il faudra sélectionner les bonnes variables, avec un programme qui ne doit pas nécessiter une intervention
# humaine, faire des corrélations et régression  
# Groupe constitué de 4 personnes  