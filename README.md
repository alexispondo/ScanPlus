#Installation

**[+] Installer pip**

Si vous n'avez pas encore la dernière version de pip utiliser ceci:
```
sudo apt-get install python3-pip
```

**[+] Télécharger le projet**

Télécharger le projet sur git

```
git clone https://github.com/alexispondo/ScanPlus.git
```

Installer les modules necessaires
```
cd ScanPlus
cd ScanPlus
chmod +x installer.py
./installer.py
chmod +x index.py
./index.py
```

![](../Images/Screenshot_2022-01-27_11_26_58.png)

# Caractéristiques du programme
**Nom de programme: ScanPlus**

**Description:** ScanPLus est un programme de scan de vulnérabilité permettant de detecter les vulnérabilités d'une application web.

**Atouts:** Ce programme apporte un plus de par sa conception qui lui permet d'effectuer plusieurs types de scan differents dans une même application web.


# Les scans effectués


**1) Scan Global**

Scan Global est le type de scan qui permet de detecter les vulnérabilité lié à la presentation de l'application web qui peuvent être exploité par un attaquant.
Ce type de scan permet entre autre de:
* Obtenir le fichier robots.txt 
* Obtenir le fichier sitemap.xml
* Hyper Text Transfer Protocol (http/https) est sécurisé où non
* recuperer le language de programmation
* recuperer le nom et la version du serveur web

![](../Images/Screenshot_2022-01-27_11_27_20.png)

**2) Scan Is_BruteForce**

Le scan  is_BruteForce est un scan qui permet de detecter si un formulaire de connexion est BruteForçable.
En effet le programme test 10 connexion erronné consecutive et regarde la reaction du serveur.
Le formulaire de connexion est sécurité si à un 03moment du scan le serveur refuse les demandes de connexions à cause d’un certain nombre de tentative échoué, dans le cas contraire il est BruteForçable.

![](../Images/Screenshot_2022-01-27_11_28_25.png)

**3) Scan CommonUserPass**

Le Scan CommonUserPass est un Scan qui verifie si un formulaire de connexion est vulnerable aux noms d’utilisateur et mots de passe communs.
Le programme prend en paramètre l'URL de la page de connexion les names du username, password, submit et le message d'erreur qui est retourné lorsque les identifiants sont incorrectes.

![](../Images/Screenshot_2022-01-27_11_29_28.png)

**4) Scan d’injection SQL**

Ce Scan permet de detecter si un formulaire de connexion est vulnerable aux injections SQL.
Le programme prend en paramètre l'URL de la page de connexion les names du username, password, submit et le message d'erreur qui est retourné lorsque les identifiants sont incorrectes.
Le programme test ensuite une liste de commande d’injection SQL pour detecter celle qui arrive à bypasser le formulaire.
![](../Téléchargements/sql.png)

**5) Scan d’injection XSS**

Ce Scan permet de detecter si un formulaire de commentaire par exemple est vulnerable aux injections XSS.
Le programme prend en paramètre l'URL de la page de commentaire, le name du commentaire et du submit.
Le programme test ensuite une liste de commande d’injection XSS pour detecter celle qui arrive affecter l’appication.
Il faudra ensuite verifier les effets sur l’application pour voir leurs impacts.
![](../Téléchargements/xss.png)

**6) Scan d’injection de commande**

Ce Scan permet de detecter si un formulaire de recherche par exemple est vulnerable aux injections de commande.
Le programme prend en paramètre l'URL de la page de commentaire, les names du formulaire de recherche et du submit.
Le programme test ensuite une liste de commande d’injection de commande pour detecter celle qui arrive à executer des commande sur le système.
Il faudra ensuite verifier les effets sur l’application pour voir leurs impacts.
![](../Téléchargements/cmd_2.png)