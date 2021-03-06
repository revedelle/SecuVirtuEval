# Evaluation pour le module Sécurité des Infrastructures Virtualisées
***Pierre-Louis Palant / Landry Serin***

---

## Prelude

#### Les fichiers correspondants aux question 1 et 2 sont dans le dossier systemd
#### Les fichiers correspondants à la question 3 sont dans le dossier selinux
#### Les fichiers correspondants aux question 4 et 5 sont dans le dossier docker

## Question 1:

Préparons l'environnement pour l'execution du service:

```bash
#Création de l'utilisateur qui executera le service
useradd httptest
#Le script appartient au nouvel utilisateur créé
chown httptest httpserver.py 
#Le script est maintenant executable
chmod u+x httpserver.py
#Copie du script dans /usr/bin
sudo cp httpserver.py /usr/bin
```

Il faut placer httpserver.service dans /etc/systemd/system/

Pour lancer le service on execute les commandes suivante:

```bash
sudo systemctl daemon-reload
sudo systemctl start httpserver.service
```

## Question 2:

Le service est executé avec l'utilisateur httptest qui n'as pas de bash ni de privilèges

![non-root](./res/grepnonroot.png)

Le service à bien son propre dossier privé dans /tmp:

![tmp-grep](./res/tmpgrep.png)

## Question 3:

Policy module généré avec sepolgen, complété à l'aide de audit2allow

On peut acceder en lecture/ecriture à /var/www/html

![exemple-curl](./res/curlexmp.png)

On voit aussi qu'on ne peut pas accéder à /etc/ssl

Autre exemple, en lecture:

![exemple-curl-r](./res/curl_ex_r.png) 



## Question 4: 

Pour créer ce conteneur j'ai créer un dockerfile que vous pouvez trouver en pièce jointe
Ce dockerfile permet de respecter ces contraintes:
    - Image de fédora à jour
    - Variable d'environnement
    - Utilisateur non privilégié

Pour que le système soit en lecture seule et que l'on crée un point de montage il faudra le préciser dans la commande.

## Question 5: 

On construit ensuite l'image avec la commande: 

```bash
docker build -t imagehttp .
```

Puis on l'execute avec la commande suivante:

```bash
docker run --read-only -v volhttp:/tmp -d --name httpserver -p 8080:8080 imagehttp
```
Il faudra d'abord créer un volume

Afin de simplifier les choses j'ai utilisé docker-compose, il suffit ainsi d'executer: 

```bash
sudo docker-compose up -d  
```

Et docker-compose créer les volumes les montes et lance le conteneur





