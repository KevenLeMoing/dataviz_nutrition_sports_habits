# Prerequistes

### Python
The entire project is running under Anaconda environnement with python 2.7
If you've not installed it yet, click HERE to install it

### Database

### Docker




########################################################### Reflexion

Il y a une marge d'erreur sur le calcul du nombre de calories dépensés par exercice si le user ne mets pas à jour son poids.
--> Expliquer l'utilité de chaque champs/relation dans le rapport.
--> Peut-t-on comparer l'assiduité des utilisateurs au sein d'une même timezone ou entre timezone ?
--> Représentation graphique de la performance / assiduité / nombre de calories brûlés / habitudes alimentaires / par timezone

Functions to re-use
##remove NaN values
data = data.fillna('')
## column concatenation
cpclight = pd.DataFrame(data['classification_cpc.0.symbol'].str.split(' ',1).tolist(),columns = ['cpc_1','cpc_2'])
data['cpc_1']=cpclight['cpc_1']

Créer la base donnée cool pour la visualisation
1) Scripts MYSQL
2) ORM

Pourquoi pas créer un petit outil d'alerte qui remonte les infos cruciales au success ?

# Open data

Import and compare with something outside ?




















# Project structure

### Notebooks

### Python Script

### MYSQL database

### Final Report





