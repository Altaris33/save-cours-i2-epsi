# Auteurs:
#          Jérémie LAERA
#          Thomas MAULON
#          Nicolas MAURIN
#          Arthur TOULOUMOND

# Prelude  
ventes <- read.csv("~/I2/analyse_statistique_et_langage_r/projets/ventes.csv")  
str(ventes)  
 
# Partie 1  
data_trunc <- subset(ventes, select = c(2:8))

data_trunc$Total <- rowSums(data_trunc[2:7])
data_trunc
str(data_trunc)
head(data_trunc$Total)

summary(data_trunc)
df$percentage <- df$Value/(sum(df$Value)/2)

data_trunc$per_produits_frais <- round((ventes_trunc[2]/ventes_trunc[8]) * 100) 

test_data <- aggregate(data_trunc$Total ~ data_trunc$Region, data=data_trunc, FUN=mean)
test_data




print(paste("CA moyen par region : ", test_data[[2]]))

# Partie 2
cor_test <- cor(ventes$ProduitsFrais, ventes$Lait, use = "complete.obs")  
cor_test <- cor(ventes[3], ventes[4], use = "complete.obs")  
cor_test


cor_test <- cor(ventes[3], ventes[4], use = "complete.obs")  
cor_ventes <- cor(ventes[3:8])
cor_ventes

log_ventes <- log(ventes[3:8])
log_ventes
cor_log_ventes <- log_ventes
cor_log_ventes

cor_best <- cor(ventes[,7], ventes[,5], use = "complete.obs")
cor_best


cor(ventes[3:8])
cor_ventes <- cor(ventes[3:8])
test <- which(cor_ventes == max(cor_ventes[cor_ventes<1]), arr.ind = TRUE)
test
rownames(test)
writeLines(paste("La meilleur corrélation est", test[[1]], ": ", test[[2]], cor_ventes[test[1],test[2]]))






# regression linéaire
# calcul de la corrélation linéaire
# ici phénomène décroissant, plus l'on fabrique de moteurs, moins il faudra de temps pour en fabriquer
# de plus, il ne sera pas très fiable 
cor12 <- cor(df_moteur$motfab, df_moteur$temps, use = "complete.obs")
cor12

plot(df_moteur$motfab, df_moteur$temps, xlab="Nombre de moteurs fabriqués", ylab="Temps moyen de fabrication")

# la droite n'ajustera pas correctement le nuage de points, elle sera peu représentative, d'où la question 2 de l'ex 4  
reg12 <- lm(temps ~ motfab, data=df_moteur)
abline(reg12)

plot(ventes$Epicerie, ventes$Detergents, xlab="Ventes en Epicerie", ylab="Ventes de détergents")
reg_epicerie_detergent <- lm(Epicerie ~ Detergents, data = ventes)
abline(reg_epicerie_detergent)  
reg_epicerie_detergent

plot(ventes$Detergents, ventes$Epicerie, xlab="Ventes en Epicerie", ylab="Ventes de détergents")
reg_detergent_epicerie <- lm(Detergents ~ Epicerie, data = ventes)
abline(reg_detergent_epicerie)  
reg_detergent_epicerie

# 3
# PREDICTIONS
# à la mano
# ax + b = 2640,773 (mean(Epicerie))*2 + 1.843
# x = epicerie * mean()
predict_vente_epicerie_detergent <- reg_epicerie_detergent$coefficients[[2]] * (mean(ventes$Epicerie) * 2) + reg_epicerie_detergent$coefficients[[1]]
predict_vente_epicerie_detergent
abline(predict_vente_epicerie_detergent)


reg_detergent_epicerie
predict_vente <- reg_epicerie_detergent$coefficients[[2]] * (mean(ventes$Detergents) * 2) + reg_epicerie_detergent$coefficients[[1]]
predict_vente_detergent_epicerie
abline(predict_vente_detergent_epicerie)

pred_with_predict <- predict(reg_epicerie_detergent, data.frame(Epicerie = mean(ventes$Epicerie)*2), Detergents=ventes$Detergents)
pred_with_predict

# avec predict
predict_var_encore_plus_complete <- predict(reg_epicerie_detergent, vente.frame(Depenses.pub = 17000), interval = "prediction")
predict_var_encore_plus_complete

# 4 
plot(ventes$Detergents, ventes$Epicerie, xlab="Ventes en Epicerie", ylab="Ventes de détergents")

