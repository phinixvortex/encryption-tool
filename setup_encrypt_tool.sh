#!/bin/bash
echo "🔐 Setting up your Encryption Tool..."

ENV_DIR="$HOME/encrypt-env"

if [ ! -d "$ENV_DIR" ]; then
    echo "📦 Creating Python virtual environment at $ENV_DIR..."
    python3 -m venv "$ENV_DIR"
else
    echo "✅ Virtual environment already exists."
fi

echo "🚀 Activating virtual environment..."
source "$ENV_DIR/bin/activate"

echo "📥 Installing required Python packages..."
pip install --upgrade pip > /dev/null
pip install -r requirements.txt > /dev/null

echo "🧪 Launching the Encryption Tool..."
python encrypt_tool.py

deactivate
echo "🛑 Virtual environment deactivated. Goodbye!"
