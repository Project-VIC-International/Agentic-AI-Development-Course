# Exercise 0b: Git Basics

**Duration:** 20 minutes
**Goal:** Save a snapshot of your work with git, share it on GitHub, and type those steps yourself before asking an agent to help.

Work in the **private template repository** you created in Exercise 0. Keep this course guide open in a browser tab.

> **Observer mode?** Follow on the projector. After class, complete [GitHub: Hello World](https://docs.github.com/en/get-started/quickstart/hello-world) in a browser.

## Why this matters

Project VIC, CAC Ontology, CASE, and UCO all live in GitHub repositories. Development work is: copy the repo, make a small change, save a snapshot, share it, and ask for review. This exercise is that loop with a harmless practice file.

## Step 1: Two tools, two jobs

**Git** records snapshots of files on your computer. Each snapshot is a **commit**.

**GitHub** is the website that hosts those snapshots. You use it to search projects (Exercise 1), copy them (**clone**), discuss work (**issues**), and propose changes (**pull requests**).

You already installed git. You already copied a repository in Exercise 0. Now you will use both on purpose.

## Step 2: Confirm git knows who you are

In the Cursor terminal, inside your private project folder:

```bash
git config --global user.name
git config --global user.email
```

If either prints nothing, set them to the name and email you use on GitHub:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Step 3: Start from the latest `main`

```bash
git status
git pull
```

You should be on `main` (or `master`) in your private template repository. `pull` downloads commits that are already on GitHub.

If `pull` reports a conflict, stop and ask the instructor.

## Step 4: Make a branch and a tiny change

A **branch** is a named line of work. Use a new branch so `main` stays clean until someone reviews.

```bash
git switch -c practice-git
```

If that command is not found, use `git checkout -b practice-git`.

Create `scratch/git-practice.txt` with three lines of synthetic content:

```text
Name: Alex Rivera
Agency: training only
Note: synthetic practice file, no real case data
```

You may type those lines yourself or ask the agent to create the file. Creating the file is the only agent help in this step.

## Step 5: Review, then save

```bash
git status
git diff
git add scratch/git-practice.txt
git commit -m "Add git practice note"
```

- `status` lists files git is tracking or waiting to save
- `diff` shows the lines that changed
- `add` stages the file for the snapshot
- `commit` writes the snapshot with a short message

Read the `diff` before you commit. That habit matters more than memorizing flags.

## Step 6: Share the branch

```bash
git push -u origin practice-git
```

`push` uploads your branch to GitHub. `-u origin practice-git` sets the upstream once so later pushes can be `git push`.

If GitHub asks you to log in, run `gh auth login` from the [prerequisites](../../prerequisites.md), or follow the browser prompt.

## Step 7: Issue and pull request, by hand

Do this on github.com in your private repository, or with GitHub CLI if you installed it.

**Issue:** title `Practice: git lab note`. Body: `Training issue. Synthetic data only.`

**Pull request:** from `practice-git` into `main`. Title: `Practice: add git lab note`. In the body, mention the issue (`Closes #N`). Use a draft pull request if the UI offers that.

Leave it unmerged. In this course, and in Project VIC intern work, the maintainer merges unless they ask you to.

GitHub CLI equivalent:

```bash
gh issue create --title "Practice: git lab note" --body "Training issue. Synthetic data only."
gh pr create --base main --head practice-git --draft --title "Practice: add git lab note" --body "Training PR. Synthetic data only."
```

After `gh issue create`, copy the issue number into the PR body if you want `Closes #N`.

## Step 8: Agent help, after you can do it by hand

In Cursor, on the same branch, ask:

> Show git status and git diff. Do not commit, push, or merge.

Then:

> Draft a one-line commit message for the current diff. I will run the commit myself.

If there is no new diff, that is expected. You already committed. The agent may inspect and suggest. You run `git add`, `git commit`, and `git push`.

Later, on real tasks, you may ask an agent to open a **draft** pull request. Watch the command it runs. Approve it only when the branch is what you intend to share.

## Safety

Same rule as the rest of the course: no real case data, PII, victim information, or secrets in files, commits, issues, or pull requests. Use synthetic data only.

Do not run `git push --force` on shared branches. If `git pull` reports a conflict, stop and ask the instructor.

## Done When

- [ ] `user.name` and `user.email` are set
- [ ] You created branch `practice-git`
- [ ] You committed `scratch/git-practice.txt`
- [ ] You pushed the branch
- [ ] You opened a practice issue and a practice pull request
- [ ] You asked the agent to show status/diff without committing
- [ ] You left the pull request unmerged

## What You Just Did

You ran the loop used on CAC Ontology, CASE, UCO, and other Project VIC repositories:

1. Update `main`
2. Branch
3. Change
4. Review the diff
5. Commit
6. Push
7. Issue and pull request
8. Agent inspects; you still save and share

Keep the command table on the [cheat sheet](../../../resources/cheat-sheet.md) at your desk for the rest of the lab.
