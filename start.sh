#!/bin/bash

cd frontend
npm install
npm run build

cd ../backend
python app.py
