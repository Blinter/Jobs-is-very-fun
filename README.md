# Jobs.blinter.link

# Refactor Outline

This document outlines the plan for refactoring the Jobs Tracker application. The goal of this refactor is to improve code quality, maintainability, and performance.

## Table of Contents

- [Jobs.blinter.link](#jobsblinterlink)
- [Refactor Outline](#refactor-outline)
  - [Table of Contents](#table-of-contents)
  - [Refactor Task List](#refactor-task-list)
    - [Phase 1: Planning and Analysis](#phase-1-planning-and-analysis)
    - [Phase 2: Backend Refactor](#phase-2-backend-refactor)
    - [Phase 3: Frontend Refactor](#phase-3-frontend-refactor)
    - [Phase 4: Testing and QA](#phase-4-testing-and-qa)
    - [Phase 5: Documentation](#phase-5-documentation)

---

## Refactor Task List

### Phase 1: Planning and Analysis

*   [ ] **Task 1.1:** Reconfigure and deploy staging/production and testing environment.
*   [ ] **Task 1.2:** Identify current pain points and areas for improvement.
*   [ ] **Task 1.3:** Look over current codebase and observe for further changes needed for refactoring.

### Phase 2: Backend Refactor

*   [ ] **Task 2.1:** Refactor API endpoints and clean up job database for maintainability
    *   *Details:* Consolidate old APIs while maintaining data for old versions for historical integrity.
*   [ ] **Task 2.2:** Optimize database queries through DRY (Don't repeat yourself) principles. Improve maintainability by building libraries for common string queries.
*   [ ] **Task 2.3:** Improve debugging and error logging messages for bug-fix mitigation.
*   [ ] **Task 2.4:** Implement asynchronous scraping processes for improved scraping speed.
*   [ ] **Task 2.5:** Rework duplicate data detection logic and track results.
*   [ ] **Task 2.6:** Enhance text handling mechanisms (e.g., parsing, sanitization).
*   [ ] **Task 2.7:** Develop additional API tools/endpoints for the admin dashboard.
*   [ ] **Task 2.8:** Implement a subscription system for users to receive job data feeds based on location and job title.
*   [ ] **Task 2.9:** Implement a job expiration system for users to search for jobs that have been past their specified expiration date.
*   [ ] **Task 2.10:** Reconfigure email server and mail settings.
*   [ ] **Task 2.11:** Implement latest Google ReCaptcha for user verification.
*   [ ] **Task 2.12:** Implement latest Google SSO for user authentication.
*   [ ] **Task 2.13:** Implement task manager to perform tasks and save routine logs efficiently.
*   [ ] **Task 2.14:** Implement a swagger UI for users to query the database with proper authentication.

### Phase 3: Frontend Refactor

*   [ ] **Task 3.1:** Update UI components.
*   [ ] **Task 3.2:** Improve state management.
*   [ ] **Task 3.3:** Enhance user experience (UX).
*   [ ] **Task 3.4:** Rework Admin UI to implement a stale website filtering system management control panel.
*   [ ] **Task 3.5:** Integrate new API tools into the Admin Dashboard UI.
*   [ ] **Task 3.6:** Improve overall user interface and site responsiveness.

### Phase 4: Testing and QA

*   [ ] **Task 4.1:** Prepare testing scripts/CI-CD pipeline.
*   [ ] **Task 4.2:** Execute pre-deployment testing suite.
    *   *Details:* Run automated Python unit tests (main logic), Selenium website functionality tests, and smoke tests as part of the CI/CD pipeline before final deployment.
*   [ ] **Task 4.3:** Deploy to staging environment.
*   [ ] **Task 4.4:** Deploy to production environment.
*   [ ] **Task 4.5:** Perform post-deployment testing.
*   
### Phase 5: Documentation
* [] Reproduce Demonstration content and reading material, development notes and deployment steps.
* [] Allow for extra feed-back on additional user improvements and tidy up diagrams to understand complex processes.