# Cours 1 10/02/2021

# vector
u <- c(-1, 0, 1, 2)
v <- c(4, 5, 6, 7)

# operations
u + 10

u^2

u + v

v - 2 * u

u * v

# recycling rule  
val <- c(1, 2)
val2 <- c(1,2,3,4)

val + val2

# vectors & co  
reponse <- c("Bac+2", "Bac+1", "Bac", "BacPro", "CAP", "Brevet")
reponse == "Bac"

tailles <- c(168, 192, 173, 174, 172, 167, 171, 185, 163, 170)
tailles > 180

# indexation par condition
tailles[tailles > 180]

##########
# Ex 1 Cours
##########
# a & b
u <- c(-54, 12, 0, 35)
u
v <- u > 0
v
v_only_pos <- u[u > 0]
v_only_pos

# logical operaotors  
u > 0 & u%%2 == 0
u > 0 | u%%2 == 0

# Functions
tailles <- c(168, 192, 173, 174, 172, 167, 171, 185, 163, 170)
length(tailles)

mean(tailles)

tailles <- c(168, NA, 173, 174, 172, 167, 171, 185, 163, 170)
mean(tailles, na.rm = FALSE)
mean(tailles, na.rm = TRUE)

a <- c(2, 4, 1, 6, 3, 13, 2)
min(a)
max(a)
mean(a)
var(a)
head(a, 3)
?sort()
sort(a)
order(a)
3 %in% a
unique(a)
unique(c('a','b','a','d'))

rep(a)
rep(a, times = 2)
rep(a, each = 3)
rep(a, times= 2, each = 2)

# generating integers as a vector  
-4:6
(-4:6)^2

#####################
# Suite Ex1 polycopié
#####################
# de c à g
# c
?rep()
rep_vec <- rep(c(54, 12, 35), times = 3)
rep_vec[-length(rep_vec)]

# correction
u <- c(54, 12, 35)
u
v <- rep(u, times= 3)[-length(u) * 3]  # [-length(u) * 3] = [-length(v)] car v n'est pas encore créé]
v

# d
?order
vec2 <- c(-54, 12, 0, 35)
vec2
ordered_pos_indices_vec <- which(vec_nat > 0)
ordered_pos_indices_vec

# correction
u <- c(-54, 12, 0, 35)
w <- (1:length(u))[u > 0]
# ou
w <- which(u > 0)
w


# e
vec_nat <- (0:20)
vec_nat[lapply(vec_nat, "%%", 2) != 0]

# correction
v <- (1:20) 
v
w <- v[v%%2==1]
w

# f
ht_prices <- c(54.99, 12.41, 35.14)
taxes <- 1.2
ht_prices
ttc_prices <- ht_prices * taxes
ttc_prices

# correction
u <- c(54.99, 12.41, 35.14)
v <- u * 1.20
v <- round(v, digits = 2)
v
# en une ligne
w <- round(u * 1.2, digits = 2)
w


# g
?seq
u_to_increment <- c(54, 12, 35)
u_to_increment
v_to_increment <- rep(u_to_increment, times = 3)*100
v_to_increment

# correction 1 
u <- c(54, 12, 35)
u
v <- c(u, u + 100, u + 200, u + 300)
v

# correction 2
v <- u + rep((0:3)*100, each = length(u))
v 

# Function applying to strings (cf polycopy)
# summary,: give infos depending on datatype inside vec
ch <- c("Lloyd", "Kratos", "Yos")
ch
summary(ch)

# n char
sentence <- "the computer"
sentence
nchar(sentence)

# grepl -> check for substrings as string vectors
grepl("com", sentence)  

#....
#############
# Ex 2 (travail sur les adresses mails)
#############
# a)
u <- c("Hello", "untel@gmail.com", "next", "comfortable", "me@mycompany.com")
u
v <- u[grepl('@', u)] 
v <- u[grep('@', u)] 
v

# b) 
u <- c("Hello", "untel@gmail.com", "next", "comfortable", "me@mycompany.com")
v <- u[nchar(u) > 10]
v


# c)
u <- c("Hello", "untel@gmail.com", "next", "comfortable", "me@mycompany.com")
v <- substr(u[nchar(u) > 10], start = 1, stop = 10)
w <- paste0(v, "...")
w

# en une ligne
x <- paste0(substr(u[nchar(u) > 10], start = 1, stop = 10), "...")
x

##############
# Ex 3
##############
u <- c("3.1", "-5", "6")
class(u)
u
v <- as.numeric(u)
v
sum_vec <- 0

for(i in 1:length(v)){
  sum_vec <- sum_vec + v[i]
}

print(sum_vec)

# alternative
x <- sum(as.numeric(v))
x

##############
# Ex 1 h)
##############

# Correction 1
u <- c(-54, 100, 35)
u
v <- grep(max(u), u)
z <- replace(u, v, max(u)*2)
z

# Correction 2  

t <- order(u)
t

ind <- order(u)[length(u)]

for(i in 1:length(u)){
 if(i == ind){
   v[i] = 2 * u[i]
 } else{
   v[i] = u[i]
 }
}

v

# Correction 3
v[which(v==max(v))] = u[which(u==max(u))]*2  

# imports and current working dir infos
wd = getwd()
wd

# setwd() to set another wd for the current R project  

# imports 
# read.table -> derives in read.csv, read.csv2...

# export when finished working out the data
# write.table -> derives in write.csv, write.csv2...  

data <- read.csv2("~/I2/analyse_statistique_et_langage_r/projets/bank2.csv")
nrow(data)
ncol(data)
dim(data)
names(data)
str(data)

head(data$age)
head(data$marital)
class(data$marital)

summary(data$marital)
summary(data$age)
summary(data$age)[4]
summary(data$age)[[4]]

# Generating histogram based on a vector/column 
hist(data$age)
                  
# accessing specific elements - indexation by name
data$age[2]

# direct indexation
# age - 3rd value
data[3, 1]

# using vectors 
data[1:4, 1:2]

# head for age column (since now row number specified, by default, take entire rows)
head(data[,1])

# same but with rows, taking all columns for one row, since no second index specified - first resource infos
data[1,]

# changing first three ages to 50 years old and reading dataset 
data[1:3,] <- 50
head(data[,1])

# table has 17 cols
# creating a col with items from the first col
data[,18] <- data[,1]
head(data[,18])


# INDEXATION + ASSIGNMENT to CREATE A NEW TABLE
data2 <- data[1:3, -c(2, 6, 8)] 

# conditionning over a vector of the dataset  
head(data$age > 40)

head(data[,1] > 40)

# indexation using conditionning and assigning
data$duration[data$duration < 100] <- 0 
head(data$duration)
data$duration[data$duration < 100] <- 0 

# creating new dataset, containing all rows where job is management and resources are at least 41
# i.e. selecting resource in data to create a sub-population (sample)
data3 <- data[data$age > 40 & data$job  == "management",]
dim(data3)
str(data3)
summary(data3$job)

# Same action but while avoiding NA values
data3 <- data[data$age > 40 & data$job  == "management" & !is.na(data$age > 40 & data$job  == "management"),]
str(data3)
summary(data3$job)

# Avoiding NA using a simpler syntax and subset() function
# SUBSET : best tool in R to create sub-population 
# subset : used to create sub-population, and automatically removes NA values 
# Here only conditioning on rows
data4 <- subset(data, age > 40 & job == "management")
str(data4)

# same with conditioning on cols as well
data5 <- subset(data, age > 40, select = c(age, job))
str(data5)

# keep all column except from cols from col 4 to 17 included
data6 <- subset(data, age > 40, select = -c(4:17))
str(data6)

# SORTING
# order() on a row/vector and returns indices
head(data)
head(order(data$age))

# creating a sub-pop with resource from youngest to oldest (ascending order) 
data_tri <- data[order(data$age), ]
str(data_tri)

# descending order (oldest to youngest)
data_tri_desc <- data[order(data$age, decreasing = TRUE), ]
str(data_tri_desc)  
