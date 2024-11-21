#!/bin/bash

# Start the Node.js application
npm start &

# Start the Chainlit application
python --version

# Wait for all background processes to finish
wait