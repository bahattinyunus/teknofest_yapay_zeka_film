#!/bin/bash
echo "🎬 Setting up AI Cinematic Universe Environment..."

# Create necessary directories
mkdir -p logs outputs assets

# Check for Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 could not be found. Please install it."
    exit
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Initial environment setup
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📁 Created .env file from template. Please update your API keys."
fi

echo "✅ Setup complete. Use 'source venv/bin/activate' and 'python main.py --help' to get started."
