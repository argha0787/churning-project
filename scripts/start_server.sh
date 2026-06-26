#!/bin/bash

# ============================================================
# CHANGE ONLY THE CONTAINER NAME FOR A NEW PROJECT
# ============================================================

CONTAINER_NAME="churning-api-container"

echo "Stopping old container..."

docker stop $CONTAINER_NAME || true

echo "Removing old container..."

docker rm $CONTAINER_NAME || true