Solution: Creating a Separate Branch Using Git Cherry-Pick

This document explains the complete implementation of the problem described in README.md.

The solution uses Git cherry-pick to create a new branch containing only Developer A's and Developer B's work.

Step 1: Understand the Existing Repository

Assume the GitHub repository is named:

git_project

The developers have completed their work and pushed their commits to the main branch.

Example commit history:

text
* bf6dd58  Developer C
* ddebaa8  Developer B
* 6a2c813  Developer A
* 028045d  Initial Commit

Commit Details
Commit ID	Developer	File
bf6dd58	Developer C	demo.py
ddebaa8	Developer B	hello.py
6a2c813	Developer A	cal.py
028045d	Initial Commit	vowels.py

Step 2: Check the Commit History

Open PowerShell or the terminal in your project directory.

Execute:

bash
git log --oneline --graph --decorate


This command displays the commit history of the repository.

Identify the commit IDs belonging to Developer A and Developer B.

Step 3: Check the Working Directory

Before creating a new branch, check whether there are any uncommitted changes.

bash
git status


Make sure the working directory is clean.

If there are important uncommitted changes, save or stash them before proceeding.

Step 4: Switch to the Main Branch

Execute:

bash
git switch main


This switches your working branch to main.

Step 5: Create a New Branch from the Initial Commit

Execute:

bash
git switch -c developer_demo 028045d

Explanation
git switch switches branches.
-c creates a new branch.
developedemo is the new branch name.
028045d is the initial commit.

We create the branch from the initial commit because we want to selectively add only Developer A's and Developer B's changes.

To verify the branch:

bash
git branch


Expected output:

text
* developer_demo
  main


The asterisk indicates the currently active branch.

Step 6: Cherry-Pick Developer A's Commit

Developer A's commit ID is:

6a2c813

Execute:

bash
git cherry-pick 6a2c813

Explanation

This command applies Developer A's changes to the current branch.

After successful execution, Developer A's file cal.py will be available in the new branch.

Example output:

text
[developer_demo new-commit-id] Developer A
1 file changed


The new commit ID will be different from the original commit ID.

Step 7: Cherry-Pick Developer B's Commit

Developer B's commit ID is:

ddebaa8

Execute:

bash
git cherry-pick ddebaa8

Explanation

This command applies Developer B's changes to the current branch.

Now the new branch contains both Developer A's and Developer B's work.

This is the main reason we use cherry-pick instead of merging the entire main branch.

Step 8: Verify the Files

Execute:

bash
dir


Expected files:

text
cal.py
vowels.py


The demo.py file should not be present.

This confirms that Developer C's changes have been excluded.

Step 10: Verify the Commit History

Execute:

bash
git log --oneline --graph --decorate


Expected structure:

text
* new-B-commit (HEAD -> developedemo) Developer B
* new-A-commit Developer A
* 028045d Initial Commit


This confirms that the new branch contains the initial commit and the selected changes.

Step 11: Push the New Branch to GitHub

Until now, the branch has been created locally.

To make it available on GitHub, execute:

bash
git push -u origin developedemo

Explanation
git push uploads commits to GitHub.
origin represents the remote repository.
developedemo is the branch being uploaded.
-u sets the upstream tracking relationship.

After successful execution, open your GitHub repository and select the branch dropdown.

You should see the newly created AB_development branch.

Step 12: Final Verification

Execute:

bash
git branch -a


Expected output:

text
* AB_development
  main
  remotes/origin/developedemo
  remotes/origin/main


This confirms that the new branch exists locally and remotely.

Final Result
Main Branch

The original main branch remains unchanged.

text
main
 |
 * Developer B - vowels.py
 |
 * Developer A - cal.py
 |
 * Initial Commit

developedemo Branch

The new branch contains only the initial project and the selected work.

text
AB_development
 |
 * Developer B - vowels.py
 |
 * Developer A - cal.py
 |
 * Initial Commit

All Commands at One Place
bash
# Check commit history
git log --oneline --graph --decorate

# Check working directory
git status

# Switch to main
git switch main

# Create a new branch from initial commit
git switch -c AB_development 028045d

# Cherry-pick Developer A's commit
git cherry-pick 6a2c813

# Cherry-pick Developer B's commit
git cherry-pick ddebaa8

# Verify files
dir

# Verify commit history
git log --oneline --graph --decorate

# Push new branch to GitHub
git push -u origin AB_development

# Verify local and remote branches
git branch -a

Important Git Commands
Command	Purpose
git log	Displays commit history
git status	Checks working directory status
git switch main	Switches to main
git switch -c	Creates a new branch
git cherry-pick	Applies a selected commit
git branch -a	Displays local and remote branches
git push	Uploads changes to GitHub
Conclusion

The development team successfully created a separate branch named AB_development containing only Developer A's and Developer B's changes.

The original main branch remains unchanged.
