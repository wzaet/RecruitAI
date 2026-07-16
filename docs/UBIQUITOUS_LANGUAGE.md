# Ubiquitous Language

**Status:** Draft

**Version:** 1.0

**Owner:** CTO

—

# Purpose

This document defines the official business language used across RecruitAI.

Every developer, designer, product owner, and AI module must use the same terminology.

This ensures consistency across the codebase, documentation, APIs, database, and user interface.

—

# Core Terms

## User

A person with an account in the system.

A user may have one of the following roles:

- Candidate
- Recruiter
- Company Admin
- Platform Admin

—

## Candidate

A user looking for job opportunities.

Candidates can:

- Create resumes
- Apply for jobs
- Track applications
- Receive AI recommendations

—

## Company

An organization that recruits candidates.

Companies publish jobs and manage the hiring process.

—

## Recruiter

A company member responsible for hiring candidates.

Recruiters review applications and manage hiring workflows.

—

## Resume

A structured representation of a candidate’s qualifications.

A resume may include:

- Skills
- Education
- Experience
- Projects
- Certificates
- Languages

A candidate may own multiple resumes.

—

## Job

A published employment opportunity created by a company.

A job defines:

- Requirements
- Responsibilities
- Skills
- Experience
- Location
- Employment Type

—

## Application

A candidate’s submission to a specific job.

An application records the complete hiring history for that job.

—

## Match

The result of comparing a resume against a job.

A match includes:

- Match Score
- Strengths
- Weaknesses
- AI Explanation
- Confidence Level

—

## Decision Engine

The AI-powered system responsible for analyzing resumes and generating hiring recommendations.

It does not make hiring decisions.

It supports human decision-making.

—

## Hiring Pipeline

The complete hiring workflow from job publication to hiring.

Typical stages include:

- Applied
- Screening
- Interview
- Offer
- Hired
- Rejected

—

# Naming Rules

Always use these terms consistently.

Preferred:

- Candidate
- Resume
- Application
- Company
- Recruiter
- Match
- Decision Engine

Avoid:

- Applicant
- CV Record
- Employee Candidate
- AI Score Only

—

# Engineering Rule

Every new feature, API endpoint, model, service, and database table must use the terminology defined in this document.