# Dr. ViKi DevOps Pipeline

A complete DevOps demonstration with CI/CD, monitoring, and security scanning.

## Quick Start

### Local Development
```bash
# Run locally
python app.py

# Test with Docker
./test_local.sh
```

### Monitoring Setup
```bash
# Start monitoring stack
docker-compose -f docker-compose.monitoring.yml up -d

# Access services:
# App: http://localhost:8080
# Prometheus: http://localhost:9090
# Grafana: http://localhost:3000 (admin/admin)
```

## Deployment Options

### Railway (Recommended)
1. Connect GitHub repo to Railway
2. Deploy automatically on push to main

### AWS EC2
```bash
# Install Docker on EC2
sudo yum update -y
sudo yum install docker -y
sudo service docker start

# Deploy
docker build -t drviki-app .
docker run -d -p 80:8080 drviki-app
```

## Security & Cost Optimization

### Cost Reduction Strategies
- Use auto-scaling to handle traffic spikes
- Implement container resource limits
- Use spot instances for non-critical workloads
- Monitor and optimize resource usage

### Security Best Practices
- Regular vulnerability scanning with Trivy
- Use non-root containers
- Implement proper secrets management
- Enable security monitoring and alerting

## Screenshots Required
1. GitHub Actions workflow success
2. Live deployed app URL
3. Grafana/CloudWatch dashboard
4. Docker container running
5. Security scan results