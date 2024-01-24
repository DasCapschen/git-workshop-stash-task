#!/bin/bash

# Local Helper Script only. Do not commit!

requested_env=$1

# create if not exists
touch .env

if [ $requested_env = "Production" ]; then
  echo "WORKSHOP_CORS=true" > .env
  echo "WORKSHOP_HTTPS=true" >> .env
  echo "WORKSHOP_ENV=Production" >> .env
  echo "Generated Production .env"
elif [ $requested_env = "Development" ]; then
  echo "WORKSHOP_CORS=false" > .env
  echo "WORKSHOP_HTTPS=false" >> .env
  echo "WORKSHOP_ENV=Development" >> .env
  echo "Generated Development .env"
else
  echo "Unknown Environment Requested"
  exit 1
fi

