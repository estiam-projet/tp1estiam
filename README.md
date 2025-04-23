# TP1ESTIAM - Interface CLI Python

Une interface en ligne de commande simple développée avec Python et Click.

## 📦 Installation

Pour installer et exécuter ce projet, suivez ces étapes :

### 1. Clonez le dépôt :

```bash
git clone https://github.com/estiam-projet/tp1estiam.git
cd tp1estiam
```

### 2. Créez et activez un environnement virtuel :

```bash
# Création de l'environnement virtuel
python -m venv venv

# Activation sur Windows
venv\Scripts\activate

# Activation sur Linux/macOS
source venv/bin/activate
```

### 3. Installez les dépendances :

```bash
pip install click
```

---

## 🚀 Utilisation

### Commande `hello`

Affiche un message de bienvenue :

```bash
python cli.py hello
# Affiche : Bonjour monde !

python cli.py hello "Jean"
# Affiche : Bonjour Jean !
```

### Commande `repeat`

Répète un message plusieurs fois :

```bash
python cli.py repeat "Message à répéter"
# Affiche le message une fois

python cli.py repeat --count 3 "Message à répéter"
# Affiche le message 3 fois
```

---

## ❓ Aide

### Afficher l’aide générale :

```bash
python cli.py --help
```

### Afficher l’aide d’une commande spécifique :

```bash
python cli.py hello --help
python cli.py repeat --help
```

---

## 📁 Structure du projet

```text
tp1estiam/
├── venv/             # Environnement virtuel Python (à créer lors de l'installation)
├── .gitattributes    # Configuration Git
└── cli.py            # Script principal de l'interface en ligne de commande
```

---

## 🛠️ Technologies utilisées

- Python 3  
- Click (pour l'interface en ligne de commande)
