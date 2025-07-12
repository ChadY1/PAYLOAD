# QR Tracker App

Une application Flask sécurisée permettant de scanner des QR codes chiffrés, suivre les utilisateurs, et journaliser chaque scan avec UID, IP, terminal, horodatage.

## Fonctionnalités
- 📷 Scan de QR via webcam
- 🔐 Déchiffrement Fernet sécurisé
- 🧠 Journalisation des scans (UID, IP, device, timestamp)
- 👤 Authentification sur le tableau de bord
- 📊 Tableau en ligne avec export CSV

## Installation

```bash
git clone https://github.com/votre-utilisateur/qr_tracker_app_final.git
cd qr_tracker_app_final
pip install -r requirements.txt
python app.py


---

## ✅ 2. `requirements.txt` — Dépendances Python

Fichier utilisé par `pip` pour installer tout ce qu’il faut :

### 📄 Contenu :


### ➕ Installation automatique :
```bash
pip install -r requirements.txt

echo "[contenu du README]" > README.md
echo "Flask\ncryptography\npandas" > requirements.txt

git add README.md requirements.txt
git commit -m "Ajout du README et du fichier de dépendances"
git push
