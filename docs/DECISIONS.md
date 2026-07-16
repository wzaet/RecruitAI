# RecruitAI Engineering Decisions

Status: Active

Version: 1.0

Owner: CTO

—

# Purpose

This document records the major engineering and architectural decisions made during the development of RecruitAI.

Every important decision must include:

- The decision
- The reason
- The expected impact

—

# Decision 001

## Title

Resume-Centric Architecture

### Decision

A Resume is the primary entity for candidate evaluation.

Users may own multiple resumes.

### Reason

Candidates often maintain different resumes for different industries or job roles.

### Impact

- Supports multiple resume versions.
- Better scalability.
- More flexible AI analysis.

—

# Decision 002

## Title

Application is a Historical Record

### Decision

Applications store historical hiring information.

Applications must preserve:

- Resume Version
- Match Score
- Status
- Timeline

### Reason

Candidate resumes evolve over time.

Hiring decisions should remain reproducible.

### Impact

Historical consistency.

—

# Decision 003

## Title

Analyze Once

### Decision

Resume analysis happens only once after upload.

RecruitAI stores:

- Original Resume
- Extracted Text
- Structured AI Data

### Reason

Avoid repeated AI processing.

Reduce cost.

Improve performance.

### Impact

Faster searches.

Lower AI costs.

—

# Decision 004

## Title

AI Assists, Humans Decide

### Decision

Artificial Intelligence provides recommendations only.

Final hiring decisions always belong to humans.

### Reason

Transparency.

Trust.

Explainability.

### Impact

Better adoption by companies.

Reduced legal and ethical risks.

—

# Decision 005

## Title

Business Domains

### Decision

RecruitAI is organized around business domains instead of technical layers.

Domains include:

- Identity
- Company
- Recruitment
- Candidate
- Decision Engine
- Platform

### Reason

Improves scalability and maintainability.

### Impact

Cleaner architecture.

Independent development.

—

# Future Decisions

Future architectural decisions must be documented here before implementation.