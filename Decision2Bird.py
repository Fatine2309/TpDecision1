import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Charger les données
data_Bird = pd.read_csv('Bird_strikes.csv', nrows=40)

# Remplacer les valeurs manquantes par 0
data_Bird = data_Bird.fillna(0)

# Afficher un aperçu des données
print(data_Bird.head())
print(data_Bird.info())

# Préparer les données pour l'arbre de décision
# Convertir en numérique si nécessaire
data_Bird["PeopleInjured"] = pd.to_numeric(data_Bird["PeopleInjured"], errors="coerce").fillna(0)
data_Bird["NumberStruckActual"] = pd.to_numeric(data_Bird["NumberStruckActual"], errors="coerce").fillna(0)
data_Bird["Damage"] = data_Bird["Damage"].map({'No damage': 0, 'Caused damage': 1}).fillna(0)  # Encodage
data_Bird["Engines"] = pd.to_numeric(data_Bird["Engines"], errors="coerce").fillna(0)

# Préparer les features et le label
X = data_Bird[['NumberStruckActual', 'Damage', 'PeopleInjured']]  # Sélectionner les colonnes pertinentes
y = data_Bird['Engines']  # Variable cible

print("Types de données dans X :\n", X.dtypes)

# Créer et entraîner l'arbre de décision
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X, y)

# Afficher l'arbre de décision
plt.figure(figsize=(20, 10))  # Ajuster la taille pour une meilleure lisibilité
plot_tree(
    clf,
    feature_names=X.columns,
    class_names=[str(c) for c in sorted(y.unique())],  # Utiliser les valeurs uniques de y comme noms de classes
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Arbre de décision pour les données des collisions avec des oiseaux")
plt.savefig('bird_decision_tree2.png', dpi=300)
plt.show()
