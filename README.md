# Dr. ViKi DevOps Pipeline

A complete DevOps demonstration with CI/CD, monitoring, and security scanning.

### 📁 Project Structure
```
doctor-viki-app/
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container configuration
├── docker-compose.monitoring.yml   # Monitoring stack
├── test_local.sh                   # Local testing script
├── .github/workflows/deploy.yml    # CI/CD pipeline
├── monitoring/prometheus.yml       # Prometheus config
├── .dockerignore                   # Docker ignore rules
├── .gitignore                      # Git ignore rules
└── README.md                       # Documentation
```

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

## 📸 Screenshots to Capture

### Screenshot 1: GitHub Actions Workflow ✅
- Push code to GitHub repository
- Navigate to Actions tab
- Show successful build → test → deploy pipeline

### Screenshot 2: Live Deployed App ✅
- Deploy to Railway/Render/AWS
- Show browser with "Hello from Dr. ViKi DevOps Pipeline!" message
- URL visible in address bar

### Screenshot 3: Monitoring Dashboard ✅
- Access Grafana at localhost:3000
- Show uptime/metrics dashboard
- Or use AWS CloudWatch if deployed to AWS

### Screenshot 4: Docker Container Running ✅
```bash
docker ps
# Show drviki-app container running
```

### Screenshot 5: Security Scan Results ✅
```bash
docker run --rm aquasec/trivy:latest image drviki-app
# Show vulnerability scan output
```

## 🔧 Deployment Options

### Option 1: Railway (Recommended)
1. Push to GitHub
2. Connect repo to Railway
3. Auto-deploy on main branch push

### Option 2: AWS EC2
```bash
# On EC2 instance
sudo yum update -y
sudo yum install docker -y
sudo service docker start
docker build -t drviki-app .
docker run -d -p 80:8080 drviki-app
```

### Option 3: Google Cloud Run
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/drviki-app
gcloud run deploy --image gcr.io/PROJECT-ID/drviki-app --platform managed
```

## 💰 Cost Optimization Strategies

1. **Auto-scaling**: Use horizontal pod autoscaling to handle traffic spikes
2. **Resource Limits**: Set CPU/memory limits in containers
3. **Spot Instances**: Use for non-critical workloads (60-90% cost savings)
4. **Monitoring**: Track resource usage and optimize accordingly
5. **Scheduled Scaling**: Scale down during off-hours

## 🔒 Security Best Practices

1. **Container Security**: Non-root user, minimal base image
2. **Vulnerability Scanning**: Regular Trivy scans in CI/CD
3. **Secrets Management**: Use environment variables, not hardcoded values
4. **Network Security**: Implement proper firewall rules
5. **Monitoring**: Set up security alerts and logging

## 📝 Submission Checklist

- ✅ Flask app with timestamp display
- ✅ Dockerfile with optimized build
- ✅ GitHub Actions CI/CD pipeline
- ✅ Monitoring setup (Prometheus + Grafana)
- ✅ Security scanning with Trivy
- ✅ Local testing scripts
- ✅ Documentation and README
- ✅ Cost & security optimization notes

## 🛠 Tools Used

- **Application**: Python Flask
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana
- **Security**: Trivy vulnerability scanner
- **Deployment**: Railway/AWS/GCP options
- **Version Control**: Git + GitHub

## 🎉 Next Steps

1. Push code to GitHub repository
2. Set up deployment platform account
3. Configure CI/CD secrets if needed
4. Take required screenshots
5. Submit with live URL and documentation