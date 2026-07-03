#!/bin/bash

echo "🚀 Starting AI Travel Planner..."

# Activate virtual environment (if you have one later)
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "🐍 Virtual environment activated"
fi

# Start Ollama in background (if not already running)
echo "🧠 Checking Ollama..."
if ! pgrep -x "ollama" > /dev/null
then
    echo "Starting Ollama..."
    ollama serve &
    sleep 2
else
    echo "Ollama already running"
fi

# Start Streamlit
echo "🌐 Starting Streamlit app..."
streamlit run app.py
