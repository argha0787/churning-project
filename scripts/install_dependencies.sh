#!/bin/bash

# Update the EC2 instance
sudo yum update -y

# Install Docker
sudo yum install docker -y

# Start Docker service
sudo systemctl start docker

# Enable Docker to start automatically after reboot
sudo systemctl enable docker

# Give ec2-user permission to run Docker without sudo
sudo usermod -aG docker ec2-user

# Stop any running CodeDeploy deployment that may interfere (optional)
sudo systemctl restart codedeploy-agent