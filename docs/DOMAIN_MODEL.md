# RecruitAI Domain Model

## Vision

RecruitAI is an AI-powered recruitment platform that helps companies hire faster and helps candidates find the right opportunities.

The system is divided into independent business domains.

—

# Domain 1: Identity

Purpose:
Manage users, authentication, authorization and security.

Entities:

- User
- Role
- Permission
- Session

—

# Domain 2: Company

Purpose:
Manage companies and HR teams.

Entities:

- Company
- CompanyMember
- Department
- Branch

—

# Domain 3: Recruitment

Purpose:
Manage the hiring workflow.

Entities:

- Job
- Application
- Interview
- Offer
- HiringStage

—

# Domain 4: Candidate Intelligence

Purpose:
Build an AI-powered candidate profile.

Entities:

- Resume
- ResumeAnalysis
- Education
- Experience
- Certificate
- Project
- CandidateSkill

—

# Domain 5: AI Engine

Purpose:
Analyze resumes and match candidates.

Modules:

- Resume Parser
- Resume Cleaner
- Resume Extractor
- Skill Engine
- AI Provider
- Embedding Engine
- Matching Engine
- Recommendation Engine

—

# Domain 6: Platform

Purpose:
Provide platform-wide services.

Modules:

- Notification
- Subscription
- Billing
- Analytics
- Audit Log

—

## Engineering Principles

- Architecture before implementation.
- AI where it adds value.
- Scalability first.
- Security by design.
- Clean Architecture.
- Every feature must solve a real business problem.