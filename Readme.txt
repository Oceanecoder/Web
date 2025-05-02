Objectif du Projet :
    Visualiser sur un site internet la constitution des arbres de la ville de Saint-Quentin.
    Pouvoir ajouter un arbre à la BDD de la ville
    Pouvoir déterminer et visualiser les différents clusters d'arbres de la BDD de la ville 
    Pouvoir prédire l'âge d'un arbre sélectionner sur la BDD de la ville 


Fonctionnalité 1 : page accueil
    Objectif : 
            Ajouter une page d'accueil pour le site internet de la ville

    Rendu : 
            Une page html et un style.css (fichier regroupant aussi les autres Fonctionnalités)

    Explications : 
            Cette page html à pour but de rediriger les utilisateurs vers les fonctions voulues.
            Il y a un bandeau comprenant les liens renvoyant vers les autres pages du site de la ville.
            Il n'y a pas d'autre connexion extérieur avec cette page.


Fonctionnalité 2 : Ajout d'un arbre
    Objectif : 
            Création de la page d'ajout d'arbre à la BDD de la ville

    Rendu : 
            Une page html et un style.css (fichier regroupant aussi les autres Fonctionnalités)
            Requêtes php pour faire la connexion avec la BDD. 

    Explications : 
            Cette page html à pour but d'ajouter des arbes à la BDD.
            L'utilisateurs rentres les caractéritiques de l'abre qu'il ajouter dans un formulaire dédié. 
            Les caractéritiques de l'arbres sont ensuite utilisées pour compléter la BDD avec ce nouvel arbre.
                


Fonctionnalité 3 : Visualisation du parc
    Objectif : 
            Création de la page permettant la Visualisation des arbres de la BDD

    Rendu : 
            Une page html et un style.css (fichier regroupant aussi les autres Fonctionnalités)
            Requêtes php pour faire la connexion avec la BDD.

    Explications : 
            Cette page html envoi une requête à la BDD, celle-ci lui renvoi sa composition, à savoir dans un tableau tous les arbres présents dans la BDD. Le tableau affiche aussi les caractéritiques de chaques arbres.
            A partir de cette parge, il y a deux boutons permettant de rediriger vers les pages "cluster" et "prédire âge", pour prédire l'âge, on doit utiliser l'encoche présente dans la première colonne.
            On a rajouté une carte intéractive permattant de visualiser l'emplacement des arbres de la ville de SAint-Quentin



Fonctionnalité 4 : Prédiction du cluster des arbres de la BDD
    Objectif : 
            Création de la page permettant la Prédiction des clusters des arbres de la BDD

    Rendu : 
            Une page html et un style.css (fichier regroupant aussi les autres Fonctionnalités)
            Requêtes php pour faire la connexion avec la BDD.

    Explications : 
            Cette page html récupère les info des la BDD, donc à savoir tous les arbres présents et leurs caractéritiques. 
            Via des requêtes php, on va déterminer les clusters des différents arbres.
            Ensuite, on va afficher sur une carte intéractive l'emplacementdes arbres avec différentes couleurs pour chaque cluster. 


Fonctionnalité 5 : prédire l'âge
    Objectif : 
            Création de la page permettant la Prédiction de l'âge des arbres de la BDD

    Rendu : 
            Une page html et un style.css (fichier regroupant aussi les autres Fonctionnalités)
            Requêtes php pour faire la connexion avec la BDD.

    Explications :
            Lorsque sur la page "Visualisation" on sélectionne un arbre du tableau, et que après on clique sur le bouton "prédire l'âge", on nous renvoi sur la page de prédiction de l'âge.
            Cette page va récupérer les info de l'arbre sélectionné et grâce au script python, va déterminer et afficher l'âge estimé de l'arbre.
