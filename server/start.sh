#!/bin/bash

# Start the Node.js application
npm start &

# Start the Chainlit application
pwd
. .venv/bin/activate &
pip list &
pip show chainlit &

python --version

python -m chainlit run rag-chatbot/app.py

# Wait for all background processes to finish
wait