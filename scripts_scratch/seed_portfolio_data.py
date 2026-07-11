import os
import sys
import django
from datetime import date

# Setup Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from apps.core.models import HeroIdentity, ProfessionalSummary, SocialLink, Resume
from apps.skills.models import SkillCategory, Skill
from apps.certifications.models import Certification
from apps.experience.models import Experience
from apps.projects.models import Project
from apps.showcases.models import Showcase

def seed_core():
    print("Seeding high-impact core models...")
    HeroIdentity.objects.all().delete()
    ProfessionalSummary.objects.all().delete()
    SocialLink.objects.all().delete()
    Resume.objects.all().delete()

    # 1. HeroIdentity
    hero = HeroIdentity(
        name="Sanket Prajapati",
        title="DevOps & Cloud Infrastructure Engineer",
        tagline="4x AWS Certified | Automating High-Availability 3-Tier Architectures & GitOps Pipelines",
        availability_status="available",
        location="Remote / India",
        years_experience=2, # Representing comprehensive practical full-stack & DevOps experience
        avatar="avatars/IMG_20230928_114821_4_mGp0tYD.jpg"
    )
    hero.save()
    print("Created HeroIdentity.")

    # 2. ProfessionalSummary (Compelling, recruiter-focused narrative)
    summary_text = (
        "4x AWS Certified DevOps and Cloud Infrastructure Engineer with a proven track record of designing, "
        "securing, and automating production-grade 3-tier AWS architectures. Specialized in containerization "
        "(Docker, Kubernetes), Infrastructure as Code (Terraform), and high-availability setups that eliminate "
        "single points of failure. Passionate about GitOps and continuous delivery—bridging Django/React full-stack "
        "development with enterprise-grade cloud automation, secrets management, and robust monitoring stacks."
    )
    ProfessionalSummary.objects.create(content=summary_text)
    print("Created ProfessionalSummary.")

    # 3. SocialLink
    SocialLink.objects.create(platform="github", url="https://github.com/MrSanketPrajapatissp", icon_class="github", order=1)
    SocialLink.objects.create(platform="linkedin", url="https://linkedin.com/in/sanket-prajapati", icon_class="linkedin", order=2)
    SocialLink.objects.create(platform="twitter", url="https://x.com/SanketP33817397", icon_class="twitter", order=3)
    SocialLink.objects.create(platform="email", url="mailto:prajapatisanketssp321@gmail.com", icon_class="mail", order=4)
    SocialLink.objects.create(platform="phone", url="tel:+918421927904", icon_class="phone", order=5)
    print("Created SocialLinks.")

    # 4. Resume
    Resume.objects.create(
        file="resumes/Sanket_Prajapati_DevOps_Resume.pdf",
        is_active=True
    )
    print("Created Resume link.")

def seed_skills():
    print("Seeding high-impact skills...")
    SkillCategory.objects.all().delete() # cascades to Skill

    skills_data = {
        "Cloud Engineering (AWS)": {
            "icon": "cloud",
            "skills": [
                ("AWS Core (VPC, EC2, S3, IAM, Route 53)", 95),
                ("AWS Serverless & Compute (Lambda, ECS Fargate)", 92),
                ("Database Scaling (RDS Multi-AZ, Aurora Serverless)", 90),
                ("Cloud Cost Optimization & FinOps", 85)
            ]
        },
        "Infrastructure as Code & GitOps": {
            "icon": "code",
            "skills": [
                ("Terraform (IaC Automation)", 94),
                ("GitHub Actions (CI/CD GitOps)", 92),
                ("AWS Systems Manager & SSM Run Command", 90),
                ("AWS CodePipeline & CodeBuild", 88),
                ("Ansible (Configuration Management)", 85)
            ]
        },
        "Containers & Orchestration": {
            "icon": "box",
            "skills": [
                ("Docker (Multi-stage builds, Optimization)", 93),
                ("Kubernetes (EKS, Deployment Patterns)", 88)
            ]
        },
        "Full-Stack Development": {
            "icon": "terminal",
            "skills": [
                ("Python (Django REST Framework)", 90),
                ("JavaScript (React, Vite, Next.js)", 86),
                ("WSGI Servers (Gunicorn, Nginx Reverse Proxy)", 88),
                ("Shell Scripting (Bash Automation)", 90),
                ("Java / OOP Design Patterns", 80)
            ]
        },
        "Databases & Observability": {
            "icon": "activity",
            "skills": [
                ("PostgreSQL (RDS Tuning, Schemas)", 90),
                ("MySQL / SQLite", 85),
                ("Prometheus & Grafana (System Monitoring)", 86),
                ("SonarQube (Static Application Security)", 82)
            ]
        },
        "Collaboration & Professional Tools": {
            "icon": "shield",
            "skills": [
                ("Git & GitHub Advanced Workflows", 95),
                ("Agile Project Management (Trello, Slack)", 90),
                ("Enterprise AI Tools (Claude, GLM-5.2)", 92)
            ]
        }
    }

    for idx, (cat_name, cat_info) in enumerate(skills_data.items(), 1):
        cat = SkillCategory.objects.create(
            name=cat_name,
            icon=cat_info["icon"],
            order=idx
        )
        for s_idx, (s_name, s_prof) in enumerate(cat_info["skills"], 1):
            Skill.objects.create(
                category=cat,
                name=s_name,
                proficiency=s_prof,
                order=s_idx
            )
    print("Created SkillCategories and Skills.")

def seed_certifications():
    print("Seeding premium certifications...")
    Certification.objects.all().delete()

    certs = [
        {
            "name": "AWS Certified Machine Learning Engineer – Associate",
            "issuer": "Amazon Web Services (AWS)",
            "credential_id": "HC-TFA-003-AC",
            "credential_url": "https://www.credly.com/badges/f1a45883-ea4a-4a6d-9d00-335665340a8c/public_url",
            "badge_image": "certifications/aws-certified-machine-learning-engineer-associate.png",
            "date_obtained": date(2026, 4, 28),
            "expiry_date": date(2029, 4, 28),
            "status": "obtained",
            "order": 1
        },
        {
            "name": "AWS Certified Data Engineer – Associate",
            "issuer": "Amazon Web Services (AWS)",
            "credential_id": "",
            "credential_url": "https://www.credly.com/badges/09aaf95d-d017-41a4-9a3c-846b07b8f9e7/public_url",
            "badge_image": "",
            "date_obtained": date(2026, 3, 29),
            "expiry_date": date(2029, 3, 29),
            "status": "obtained",
            "order": 2
        },
        {
            "name": "AWS Certified Solutions Architect – Associate",
            "issuer": "Amazon Web Services (AWS)",
            "credential_id": "AWS-SAA-2026-AC",
            "credential_url": "https://www.credly.com/badges/d3ff44a3-1e6d-47f6-b02b-feb0054b3755/public_url",
            "badge_image": "certifications/aws-certified-solutions-architect-associate.png",
            "date_obtained": date(2026, 2, 20),
            "expiry_date": date(2029, 2, 20),
            "status": "obtained",
            "order": 3
        },
        {
            "name": "AWS Certified Cloud Practitioner",
            "issuer": "Amazon Web Services (AWS)",
            "credential_id": "",
            "credential_url": "https://www.credly.com/badges/d3ff44a3-1e6d-47f6-b02b-feb0054b3755/public_url",
            "badge_image": "",
            "date_obtained": date(2026, 2, 15),
            "expiry_date": date(2029, 4, 15),
            "status": "obtained",
            "order": 4
        },
        {
            "name": "Python Full Stack Development Certificate",
            "issuer": "Kiran Academy",
            "credential_id": "",
            "credential_url": "",
            "badge_image": "",
            "date_obtained": date(2026, 4, 1),
            "status": "obtained",
            "order": 5
        }
    ]

    for cert in certs:
        Certification.objects.create(**cert)
    print("Created Certifications.")

def seed_experience():
    print("Seeding high-impact experience...")
    Experience.objects.all().delete()

    exp1 = Experience(
        role="Trainee Developer | Python Full Stack & DevOps Engineer",
        company="Kiran Academy",
        company_url="https://www.kiranacademy.com",
        start_date=date(2025, 11, 1),
        end_date=date(2026, 4, 30),
        is_current=False,
        description=(
            "Designed and built production-ready Python/Django full-stack applications "
            "coupled with secure, automated, and highly available AWS cloud architectures."
        ),
        achievements=[
            "Architected and provisioned an AWS 3-Tier Production Architecture (VPC CIDR '192.168.0.0/16') spanning 2 Availability Zones, enforcing isolation via 2 public and 4 private subnets.",
            "Deployed Nginx/React frontends and Django/Gunicorn backend task nodes on EC2 instances behind dual-tier Application Load Balancers (ALB) and Auto Scaling Groups (ASG) to dynamically absorb sudden traffic spikes.",
            "Automated Docker builds and seamless continuous deployment flows by engineering a GitHub Actions CI/CD pipeline integrated with AWS Systems Manager (SSM) Agent, eliminating SSH exposures.",
            "Configured a Multi-AZ Amazon RDS PostgreSQL database in isolated subnets with strict security group parameters (ingress restricted to App-SG on port 5432) and externalized configurations to SSM Parameter Store."
        ],
        technologies=["AWS", "Terraform", "Docker", "GitHub Actions", "Amazon ECR", "AWS SSM", "PostgreSQL", "Nginx", "Django", "React"],
        order=1
    )
    exp1.save()

    exp2 = Experience(
        role="Web Development Intern | PrimaDelhiPoint Developer",
        company="Primathink Technologies Pvt. Ltd.",
        company_url="https://www.primathink.com",
        start_date=date(2022, 5, 1),
        end_date=date(2022, 7, 31),
        is_current=False,
        description=(
            "Developed interactive and highly responsive web pages and implemented optimized "
            "search/navigation interfaces using Agile methodologies."
        ),
        achievements=[
            "Developed and launched PrimaDelhiPoint, a responsive tourist information portal utilizing HTML5, CSS3, and vanilla JavaScript to provide an optimized mobile layout.",
            "Engineered client-side search filtering and dynamic UI interactive components using optimized JavaScript DOM manipulation, reducing page load latency.",
            "Collaborated closely with senior developers in an Agile framework, managing code versions and project sprints via Git and GitHub."
        ],
        technologies=["HTML5", "CSS3", "JavaScript", "DOM Manipulation", "GitHub", "Git", "Agile"],
        order=2
    )
    exp2.save()
    print("Created Experience.")

def seed_projects():
    print("Seeding recruiter-impressing projects...")
    Project.objects.all().delete()

    # Load Portfolio README dynamically
    portfolio_readme = ""
    try:
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path, 'r', encoding='utf-8') as f:
            portfolio_readme = f.read()
    except Exception as e:
        print(f"Warning: Could not read portfolio README: {e}")

    foodbridge_readme = """# FoodBridge — Production-Grade 3-Tier AWS Architecture & Platform

> **A High-Availability, Secure, and Automated Food Waste Reduction Platform Connecting Donors with Verified NGOs.**
> 
> **Production Live URL**: [https://foodbridge.sanketdevs.online](https://foodbridge.sanketdevs.online)
> 
> **Stack**: Django 5 (REST API Backend) + React 18 & Vite (Nginx Frontend) + Amazon RDS PostgreSQL (Database) + AWS ECR (Container Registry) + GitHub Actions (CI/CD)

---

## 🏗️ Production Architecture Overview

This project is deployed using a production-ready **3-Tier AWS Architecture** to ensure security, scalability, high availability, and zero single-points-of-failure. 

### Key Architectural Pillars

*   **Multi-AZ High Availability**: Deployed across two Availability Zones (`ap-south-1a` and `ap-south-1b`) in the ap-south-1 region.
*   **Isolated Subnet Security**: 
    *   **Public Web Tier**: Hosts the Internet-facing Application Load Balancer (ALB) and Nginx/React Web servers.
    *   **Private Application Tier**: Django REST API servers run in private subnets, shielded from direct internet access.
    *   **Private Database Tier**: Amazon RDS PostgreSQL instance runs in isolated database subnets, accessible only from the App Tier.
*   **Outbound Internet Gateway Protection**: Private App EC2 instances communicate with the outer internet (e.g., ECR login, SMTP mailers) through a **NAT Gateway** in the public subnet.
*   **Auto Scaling Groups (ASG)**: Both the Web (Nginx) and App (Django) tiers are managed by independent Auto Scaling Groups, configured to scale between 1 and 2 instances based on demand.
*   **Dual Load Balancing**: 
    *   **External ALB**: Terminates public SSL/TLS (HTTPS) traffic on port 443 via an AWS Certificate Manager (ACM) SSL certificate and forwards it to the Web Tier.
    *   **Internal ALB**: Acts as a private proxy, forwarding API requests securely from Nginx to Gunicorn/Django on port 8000.

---

## 🛠️ Infrastructure Configuration (VPC Spec)

| Component | Resource Name | Details |
|-----------|---------------|---------|
| **Region** | `ap-south-1` | Asia Pacific (Mumbai) |
| **VPC** | `foodbridge-vpc-vpc` | CIDR: `192.168.0.0/16` |
| **Public Subnets** | `foodbridge-public-a`, `foodbridge-public-b` | `192.168.0.0/24`, `192.168.16.0/24` (Hosts Web ALB & Frontend) |
| **Private App Subnets** | `foodbridge-app-a`, `foodbridge-app-b` | `192.168.128.0/24`, `192.168.176.0/24` (Hosts Django API Backend) |
| **Private DB Subnets** | `foodbridge-db-a`, `foodbridge-db-b` | `192.168.160.0/24`, `192.168.144.0/24` (Hosts RDS PostgreSQL) |
| **NAT Gateway** | `foodbridge-vpc-nat...` | Associated with Elastic IP, deployed in `ap-south-1a` |
| **RDS Instance** | `foodbridge-db` | Engine: `PostgreSQL 16`, Instance: `db.t4g.micro` |

---

## 🚀 CI/CD GitOps Pipeline & Automation

The application uses an automated **GitHub Actions** deployment pipeline that executes on every push to the `main` branch:

1.  **Build & Containerize**: Compiles Docker images for both frontend (`frontend/Dockerfile`) and backend (`backend/Dockerfile`).
2.  **ECR Registry Push**: Authenticates with AWS and pushes compiled images to private **Amazon Elastic Container Registry (ECR)** repositories tagged with the specific git commit SHA and `latest`.
3.  **SSM Auto-Deploy**: Triggers deployment commands securely using the **AWS Systems Manager (SSM) Agent** on the target EC2 instances. It pulls the latest ECR images, stops old containers, loads environment configurations from the SSM Parameter Store, and launches the updated containers dynamically without exposing SSH keys to GitHub.
"""

    karvion_readme = """# Karvion — FinTech & Tax Compliance Portal

> **A Production-Grade, Secure, and Highly Compliant Financial & Tax Management Portal.**
> 
> **Stack**: Django 5.1 (Gunicorn Backend) + React 19 & Vite (Frontend) + Render & Cloudflare Pages (Hosting) + Google Drive API (Serverless Uploads) + AES-256-GCM (Security) + JWT Authentication (Session Management)

---

## 🚀 Core Features & Security Implementations

*   **Secure Document Management**: Implemented a serverless-style document upload flow using the **Google Drive API** to stream user files directly from requests. Achieved strict zero-local-storage data compliance with automated 15-day purge audit logging.
*   **Cryptographic Security**: Engineered secure credential storage using **AES-256-GCM encryption** to protect sensitive user tax parameters and documents.
*   **Robust Session Authentication**: Set up JWT session validation with token blacklisting to secure API endpoints, preventing unauthorized access.
*   **Optimized Deployment & Delivery**: Deployed the Gunicorn backend on **Render (Docker)** and static frontend assets on **Cloudflare Pages** for global caching and high performance.
"""

    p1 = Project(
        title="FoodBridge — Production-Grade 3-Tier AWS Architecture & Platform",
        description=(
            "A High-Availability, Secure, and Automated Food Waste Reduction Platform. "
            "Engineered with a Multi-AZ 3-Tier AWS Architecture including isolated subnets, "
            "dual Application Load Balancers, Auto Scaling Groups, and full GitOps automation."
        ),
        tech_stack=["Django 5", "React 18", "Vite", "Nginx", "Amazon RDS PostgreSQL", "AWS ECR", "GitHub Actions", "AWS Systems Manager (SSM)"],
        github_url="https://github.com/MrSanketPrajapatissp/FoodBridge",
        live_url="https://foodbridge.sanketdevs.online",
        readme_content=foodbridge_readme,
        image="projects/AWS_cloud_architecture_diagram__p0qCwx4.jpeg",
        is_github_synced=True,
        github_repo_name="MrSanketPrajapatissp/FoodBridge",
        status="deployed",
        order=1
    )
    p1.save()

    p2 = Project(
        title="Control Plane — Next-Gen AWS DevOps Portfolio Platform",
        description=(
            "An enterprise-grade, high-availability monitoring and control dashboard portfolio platform. "
            "Deployed on serverless AWS ECS Fargate, featuring automated CodePipeline CI/CD rolling deployments, "
            "centralized CloudWatch logging, and secure SSM secrets injection."
        ),
        tech_stack=["Next.js 14", "Django REST Framework 4.2", "Gunicorn", "AWS ECS Fargate", "AWS CodePipeline", "CodeBuild", "AWS RDS Aurora", "Amazon S3", "SSM Parameter Store", "Route 53", "ACM", "CloudWatch"],
        github_url="https://github.com/MrSanketPrajapatissp/DevOps-Portfolio",
        live_url="https://portfolio.sanketdevs.online",
        readme_content=portfolio_readme,
        image="projects/AWS_Architecture_Diagram_animated_2K_202607111534.jpeg",
        is_github_synced=True,
        github_repo_name="MrSanketPrajapatissp/DevOps-Portfolio",
        status="deployed",
        order=2
    )
    p2.save()

    p3 = Project(
        title="Karvion — FinTech & Tax Compliance Portal",
        description=(
            "A production-grade secure tax compliance portal. Engineered secure credential storage with "
            "AES-256-GCM encryption, JWT sessions, and a serverless document upload stream straight to "
            "Google Drive API to ensure zero-local-storage client data compliance."
        ),
        tech_stack=["Django 5.1", "React 19", "Docker", "Render", "Cloudflare Pages", "AES-256-GCM", "JWT", "Google Drive API"],
        github_url="https://github.com/MrSanketPrajapatissp/Karvion",
        live_url="",
        readme_content=karvion_readme,
        image="",
        is_github_synced=False,
        github_repo_name="MrSanketPrajapatissp/Karvion",
        status="deployed",
        order=3
    )
    p3.save()
    print("Created Projects.")

def seed_showcases():
    print("Seeding showcases...")
    Showcase.objects.all().delete()

    s1 = Showcase(
        title="FoodBridge 3-Tier AWS Architecture",
        slug="foodbridge-3-tier-aws",
        description="Designed and deployed a highly available, secure, and automated 3-tier AWS architecture for the FoodBridge platform.",
        diagram_image="projects/AWS_cloud_architecture_diagram__p0qCwx4.jpeg",
        technologies=["AWS VPC", "EC2", "ALB", "ASG", "RDS PostgreSQL", "NAT Gateway", "Route 53", "ACM", "GitHub Actions"],
        challenge="Deploying a full-stack Django and React application with high availability, isolated subnet security, auto-scaling, and secure deployment pipelines without exposing credentials.",
        solution="Implemented a custom VPC with 2 public subnets for external ALBs and frontend, 2 private app subnets for backend, and 2 private DB subnets for RDS. Configured outbound-only NAT Gateway routing. Set up Autoscaling Groups and Load Balancers. Built a GitOps pipeline using GitHub Actions and AWS Systems Manager (SSM) Agent to pull and deploy container images from ECR.",
        impact="Achieved zero single point of failure, isolated private app tier from direct internet, enabled automated container builds and zero-downtime SSM deployments, and secured database with restricted Security Group access.",
        order=1
    )
    s1.save()

    s2 = Showcase(
        title="Control Plane — AWS ECS Fargate Architecture",
        slug="control-plane-ecs-fargate",
        description="An enterprise-grade, high-availability containerized platform hosting the portfolio using ECS Fargate, ALB, and RDS Aurora PostgreSQL, automated via AWS CodePipeline.",
        diagram_image="projects/AWS_Architecture_Diagram_animated_2K_202607111534.jpeg",
        technologies=["AWS ECS Fargate", "AWS CodePipeline", "CodeBuild", "AWS RDS Aurora", "Amazon S3", "SSM Parameter Store", "Route 53", "ACM", "Docker"],
        challenge="Setting up a secure, zero-downtime rolling update deployment for a containerized full-stack application on AWS, ensuring database credentials and secret variables are managed securely.",
        solution="Configured a custom VPC with public, private, and isolated DB subnets. Packaged the app into optimized Docker containers and pushed to ECR. Deployed tasks onto serverless AWS ECS Fargate with path-based routing via ALB. Managed secrets in AWS SSM Parameter Store. Set up a 3-stage AWS CodePipeline triggered by GitHub webhooks to automate docker builds (CodeBuild) and roll out updates (ECS rolling deployment with 100-200% tasks).",
        impact="Achieved 100% automated GitOps CD pipeline, zero-downtime rolling updates, securely isolated backend from public networks, and centralized logging via CloudWatch.",
        order=2
    )
    s2.save()

    s3 = Showcase(
        title="Karvion FinTech & Tax Compliance Architecture",
        slug="karvion-fintech-architecture",
        description="Designed a secure cloud-native architecture for a FinTech and Tax compliance portal using Gunicorn/Django on Render and Cloudflare Pages.",
        diagram_image="",
        technologies=["Django 5.1", "React 19", "Docker", "Render", "Cloudflare Pages", "AES-256-GCM", "JWT", "Google Drive API"],
        challenge="Securing sensitive financial documents and user credentials, ensuring zero local storage of tax documents, and establishing robust session authentication.",
        solution="Developed a streaming file upload system to Google Drive API directly from request stream to achieve zero local storage compliance. Encrypted user credentials using AES-256-GCM. Implemented secure JWT session authentication with token blacklisting.",
        impact="Achieved strict compliance with financial data storage policies, reduced local storage footprint to zero, secured endpoints with robust token authentication, and optimized static asset delivery via Cloudflare CDN.",
        order=3
    )
    s3.save()
    print("Created Showcases.")

def main():
    seed_core()
    seed_skills()
    seed_certifications()
    seed_experience()
    seed_projects()
    seed_showcases()
    print("\nDatabase seeded successfully with recruiter-ready profiles!")

if __name__ == '__main__':
    main()
