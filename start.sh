#!/bin/bash

npm install
npm i @vue/cli-service
npm run build

cd ../backend
python app.py
