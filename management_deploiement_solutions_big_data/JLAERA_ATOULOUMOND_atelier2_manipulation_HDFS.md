# Atelier 2 - Implémentation et manipulation d'une arborescence HDFS

# Table des matières
- [Atelier 2 - Implémentation et manipulation d'une arborescence HDFS](#atelier-2---implémentation-et-manipulation-dune-arborescence-hdfs)
- [Table des matières](#table-des-matières)
- [Conception en amont (fondée sur notre rendu de TP1 et les retours de l'intervenant)](#conception-en-amont-fondée-sur-notre-rendu-de-tp1-et-les-retours-de-lintervenant)
- [Scripts de manipulation](#scripts-de-manipulation)

Nous proposons un rendu basé sur une conception en amont, conception obtenue suite à l'échange avec notre intervenant ainsi qu'à une adaptation/continuité de notre premier TP.  

La conception vise à montrer l'arborescence souhaitée, les scripts montrent notre implémentation.  

Pour lancer les scripts, il faut procéder comme suit:  
- rendre les scripts exécutables: `chmod +x script_to_make_executable.sh`  
- lancer le premier script `cluster_overall.sh`  
- lancer le second script `create_user_folder.sh` avec les arguments associés comme dans l'exemple suivant : `./create_user_folder.sh -e -u "username" -a "appname"`  

En amélioration, nous aurions souhaité implémenter un système de gestion de restriction d'accès en fonction des utilisateurs du serveur HDFS.    

# Conception en amont (fondée sur notre rendu de TP1 et les retours de l'intervenant)

```
/
	/users
		/client
			/client-001
				/appName
					/logs
						logs-date/
							logs-date.txt
				/save
					arborescence-date.txt
					/appName
						save-date/
							logs-date.zip
				/analytics
					/appName
				/alerts
					/appName
			/client-002
				[...]
				/appsettings
					/appName
						appsettings-env-version.*[json, xml ...]	
				/analytics
					/appName
				/alerts
					/appName
			/client-003
				[...]
				/vcs
					/path
						pathfile
					/file
				/analytics
					/appName
				/alerts
					/appName
		/admin

	/logs
		[date]/
			logs-date.txt
```  

# Scripts de manipulation  

```bash
#cluster_overall.sh

#!/bin/bash

sudo -u hdfs hdfs dfs -mkdir /logs
logs_creation=$(date)
dir_date_format=$(date +%F)
sudo _u hdfs hdfs dfs -mkdir /user/client
sudo _u hdfs hdfs dfs -ls /user/client
sudo -u hdfs hdfs dfs -mkdir /logs/$dir_date_format
sudo -u hdfs hdfs dfs -touch /logs/$dir_date_format/logs-$dir_date_format.tx
t
echo "Logs folder creation $logs_creation" | sudo -u hdfs hdfs dfs -appendToFile - /logs/$dir_date_format/logs-$dir_date_format.txt
```  

```bash
#create_user_folder.sh 

#!/bin/bash

usage() { echo "Usage: $0 [- 'express'|'standard'|'premium'] [-u <string>]" 1>&2; exit 1; }
account_type='';
while getopts "espu:a:" o; do
    case "${o}" in
        e)
            account_type='Express'
            ;;
        s)
            account_type='Standard'
            ;;
        p)
            account_type='Premium'
            ;;

        u)
            username=${OPTARG}
            ;;
        a)
            appname=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done

echo $account_type
echo $username
echo $appname

create_Express(){
      echo $1 "EXPRESS"
      count=$(hdfs dfs -ls /user/client | grep -E '^d' | wc -l)
      echo $count
      currentuser="$1"-"$count"
      echo $currentuser
      formatdate=$(date +%F)
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/$2
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/$2/logs
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/$2/logs/logs-$formatdate
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/save
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/save/$2
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/analytics
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/alerts
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/analytics/$2
      sudo -u hdfs hdfs dfs -ls -R /user/client/$currentuser/$2
      sudo -u hdfs hdfs dfs -ls -R /user/client/$currentuser
}
 create_Standard(){
      echo $1 "STANDARD"
      create_Express "$1" "$2";
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/appsettings
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/appsettings/$2
      sudo -u hdfs hdfs dfs -ls -R /user/client/$currentuser/appsettings
}
create_Premium(){
      echo $1 "PREMIUM"
      create_Standard "$1" "$2";
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/vcs
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/vcs/path
      sudo -u hdfs hdfs dfs -mkdir /user/client/$currentuser/vcs/file
      sudo -u hdfs hdfs dfs -ls -R /user/client/$currentuser/vcs
}


case $account_type in

        Express)
                create_Express "$username" "$appname"
                ;;
        Standard)
                create_Standard "$username" "$appname"
                ;;
        Premium)
                create_Premium "$username" "$appname"
                ;;
esac  
```  
