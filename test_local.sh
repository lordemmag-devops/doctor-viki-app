#!/bin/bash

echo "Building Docker image..."
docker build -t drviki-app .

echo "Running container locally..."
docker run -d -p 8080:8080 --name drviki-test drviki-app

echo "Waiting for container to start..."
sleep 5

echo "Testing application..."
curl -f http://localhost:8080/
echo ""
curl -f http://localhost:8080/health

echo "Stopping container..."
docker stop drviki-test
docker rm drviki-test

echo "Running security scan..."
docker run --rm aquasec/trivy:latest image drviki-app