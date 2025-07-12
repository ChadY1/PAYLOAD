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
