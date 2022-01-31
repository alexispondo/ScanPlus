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
python installer.py
```

Demarrer le programme
```
python index.py
```
![Screenshot_2022-01-27_11_26_58](https://user-images.githubusercontent.com/47490330/151662328-5b9b486e-b3ee-44f6-9867-e26473fa76ee.png)

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

![Screenshot_2022-01-27_11_27_20](https://user-images.githubusercontent.com/47490330/151662369-f42457a1-a197-4668-a694-f1abd8df3277.png)

**2) Scan Is_BruteForce**

Le scan  is_BruteForce est un scan qui permet de detecter si un formulaire de connexion est BruteForçable.
En effet le programme test 10 connexion erronné consecutive et regarde la reaction du serveur.
Le formulaire de connexion est sécurité si à un 03moment du scan le serveur refuse les demandes de connexions à cause d’un certain nombre de tentative échoué, dans le cas contraire il est BruteForçable.
![Screenshot_2022-01-27_11_28_25](https://user-images.githubusercontent.com/47490330/151662412-043ddd5c-5c11-4f3d-b9ec-9e769a473368.png)

**3) Scan CommonUserPass**

Le Scan CommonUserPass est un Scan qui verifie si un formulaire de connexion est vulnerable aux noms d’utilisateur et mots de passe communs.
Le programme prend en paramètre l'URL de la page de connexion les names du username, password, submit et le message d'erreur qui est retourné lorsque les identifiants sont incorrectes.
![Screenshot_2022-01-27_11_29_28](https://user-images.githubusercontent.com/47490330/151662438-c60cd0c3-3529-4843-9db7-fc171113dce3.png)


**4) Scan d’injection SQL**

Ce Scan permet de detecter si un formulaire de connexion est vulnerable aux injections SQL.
Le programme prend en paramètre l'URL de la page de connexion les names du username, password, submit et le message d'erreur qui est retourné lorsque les identifiants sont incorrectes.
Le programme test ensuite une liste de commande d’injection SQL pour detecter celle qui arrive à bypasser le formulaire.
![sql](https://user-images.githubusercontent.com/47490330/151662458-375ba7dd-cb9d-4532-a33b-ccfb1acf0578.png)

**5) Scan d’injection XSS**

Ce Scan permet de detecter si un formulaire de commentaire par exemple est vulnerable aux injections XSS.
Le programme prend en paramètre l'URL de la page de commentaire, le name du commentaire et du submit.
Le programme test ensuite une liste de commande d’injection XSS pour detecter celle qui arrive affecter l’appication.
Il faudra ensuite verifier les effets sur l’application pour voir leurs impacts.
![xss](https://user-images.githubusercontent.com/47490330/151662481-82e8437e-7e9f-4db3-91f6-528896400684.png)

**6) Scan d’injection de commande**

Ce Scan permet de detecter si un formulaire de recherche par exemple est vulnerable aux injections de commande.
Le programme prend en paramètre l'URL de la page de commentaire, les names du formulaire de recherche et du submit.
Le programme test ensuite une liste de commande d’injection de commande pour detecter celle qui arrive à executer des commande sur le système.
Il faudra ensuite verifier les effets sur l’application pour voir leurs impacts.
![cmd_2](https://user-images.githubusercontent.com/47490330/151662495-29335d77-9eb9-4113-93c6-486f301e6b96.png)
