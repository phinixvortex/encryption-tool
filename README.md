cat > README.md <<'EOF'
# 🔐 Encryption Tool

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A small Python CLI for encrypting/decrypting text:
- Base64, Hex, ROT13, Caesar Cipher
- Fernet (AES, password-based demo)

---

## Features
- Encrypt/decrypt text from terminal
- Read input from file or text entry
- Save output to file

## Quick start

```bash
git clone git@github.com:phinixvortex/encryption-tool.git
cd encryption-tool
pip install -r requirements.txt
chmod +x setup_encrypt_tool.sh
./setup_encrypt_tool.sh
# or run directly
python encrypt_tool.py
