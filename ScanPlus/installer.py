import os

# Assurez vous d'utiliser la bonne version de pip: >> sudo apt-get install python3-pip
modules = ["requests==2.27.1", "termcolor==1.1.0"]

for mod in modules:
    try:
        commande = "pip install " + mod
        os.system(commande)
    except:
        print("")