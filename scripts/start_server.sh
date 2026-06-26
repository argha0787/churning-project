#!/bin/bash

# ============================================================
# CHANGE THESE TWO VALUES FOR EVERY NEW PROJECT
# ============================================================

IMAGE_NAME="churning-api"

CONTAINER_NAME="churning-api-container"

# ============================================================
# Go to the project directory
cd /home/ec2-user/churning-api

echo "Building Docker Image..."

docker build -t $IMAGE_NAME .

echo "Starting Docker Container..."

docker run -d \
--name $CONTAINER_NAME \
-p 8000:8000 \
--restart always \
$IMAGE_NAME

echo "Deployment Successful."