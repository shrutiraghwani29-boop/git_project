GitHub Project: Selective Branch Creation Using Cherry-Pick
1. Project Overview

Consider a software development project in which three developers are working together on the same GitHub repository.

Each developer is assigned a different task and works on a separate part of the project.

The three developers are:

Developer	Assigned Task	File Name
Developer A	Develop a calculator program	cal.py
Developer B	Develop a vowels-finding program	vowels.py
Developer C	Develop a demo program	demo.py

After completing their assigned tasks, all three developers commit their changes and push their commits to the same main branch of the GitHub repository.

2. Current Situation

The main branch contains the work completed by all three developers.

The commit history looks like this:

text
main
 |
 * Commit C - Developer C
 |
 * Commit B - Developer B
 |
 * Commit A - Developer A
 |
 * Initial Commit


At this stage, all three developers' changes are available in the main branch.

3. New Requirement

After reviewing the project, the development team receives a new requirement.

The team needs to create a separate branch that contains only the work completed by Developer A and Developer B.

Developer C's changes must not be included in the newly created branch.

The original main branch must remain unchanged.

4. Expected Result

The development team must create a new branch named:

AB_development

This branch should contain:

Developer A's work.
Developer B's work.
The initial project files required by both developers.

It must exclude Developer C's work.

5. Main Objectives

The objectives of this project are:

Understand Git branches and commits.
Learn how to identify commits using commit IDs.
Create a new branch from a specific commit.
Use Git cherry-pick to select individual commits.
Exclude unwanted commits from the new branch.
Push the newly created branch to GitHub.
Verify that the new branch contains only the required changes.
6. Git Concept Used

Git Cherry-Pick

Git cherry-pick allows developers to select a specific commit from one branch and apply its changes to another branch.

Instead of merging the entire main branch, we can selectively bring only the required developers' commits into a new branch.

7. Expected Final Repository Structure
Main Branch

Contains all three developers' work.

text
main
 |
 * Developer C
 |
 * Developer B
 |
 * Developer A
 |
 * Initial Commit

AB_development Branch

Contains only Developer A's and Developer B's work.

text
AB_development
 |
 * Developer B
 |
 * Developer A
 |
 * Initial Commit

8. Expected Outcome

At the end of this project:

The original main branch will remain unchanged.
A new branch named AB_development will be created.
Developer A's changes will be included.
Developer B's changes will be included.
Developer C's changes will be excluded.
The new branch will be pushed to GitHub.

For the complete implementation, refer to SOLUTION.md.