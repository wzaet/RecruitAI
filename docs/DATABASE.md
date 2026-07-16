# Database Design

**Status:** Draft

**Version:** 1.0

**Owner:** CTO

—

# Purpose

This document describes the logical database design for RecruitAI.

The database is designed around business domains rather than technical implementation.

—

# Design Principles

- Normalize data where appropriate.
- Avoid duplicate information.
- Keep business entities independent.
- Preserve historical records.
- Support future scalability.

—

# Core Entities

## User

Represents every authenticated person in the platform.

Relationships:

- Owns resumes
- Owns applications
- May belong to a company

—

## Company

Represents an organization using RecruitAI.

Relationships:

- Owns jobs
- Has recruiters
- Receives applications

—

## Resume

Represents a candidate’s professional profile.

Relationships:

- Belongs to one candidate
- Has many skills
- Has many experiences
- Has many education records
- Can be used in multiple applications

—

## Skill

Represents a standardized skill.

Examples:

- Python
- FastAPI
- SQL
- Docker

—

## ResumeSkill

Associates resumes with skills.

Additional information may include:

- Skill Level
- Years of Experience

—

## Job

Represents a published job opportunity.

Relationships:

- Belongs to a company
- Requires skills
- Receives applications

—

## JobSkill

Associates jobs with required skills.

Each skill may include:

- Required Level
- Importance
- Required or Preferred

—

## Application

Represents a candidate applying to a job.

Stores:

- Candidate
- Resume Version
- Job
- Status
- Match Score
- AI Recommendation
- Timeline

—

# Relationships

Candidate

↓

Resume

↓

Application

↓

Job

↓

Company

—

Resume

↓

ResumeSkill

↓

Skill

—

Job

↓

JobSkill

↓

Skill

—

# Future Entities

The following entities are planned for future releases:

- Interview
- Offer
- Notification
- Audit Log
- Subscription
- Payment
- Analytics

—

# Database Rules

- One candidate may own multiple resumes.
- One company may publish multiple jobs.
- One job may receive multiple applications.
- One application references exactly one resume.
- Historical application data must never be overwritten.

—

# Engineering Decision

The database is optimized for hiring workflows rather than simple CRUD operations.