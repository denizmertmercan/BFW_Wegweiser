# Temporary Branch Synchronization Strategy

## Context and Reasoning

- The secondary machine contains unpushed commits on the main branch (such as architectural decision records). Pushing new commits directly to origin/main from this machine would likely cause branch divergence.
- Isolating changes on a temporary feature branch (script-split) permits pushing intermediate progress to the remote repository without conflicting with unpushed commits.
- Rebasing script-split onto main on the secondary machine allows linear integration of new work without introducing merge commits.
- Deleting the branch locally and remotely after a fast-forward merge leaves a clean repository history.

## Workflow

### Phase 1: On this machine (now)

Create and switch to the temporary branch:

```powershell
git switch -c script-split
```

Stage and commit changes as work progresses:

```powershell
git add -A
git commit -m "Describe work completed here"
```

Push the branch to GitHub:

```powershell
git push -u origin script-split
```

### Phase 2: On the other machine (where main holds unpushed work)

Fetch the newly pushed branch from the remote:

```powershell
git fetch origin
```

Switch to the branch and rebase it onto local main:

```powershell
git switch script-split
git rebase main
```

Fast-forward main to include the rebased commits:

```powershell
git switch main
git merge --ff-only script-split
```

Push the updated main branch to GitHub:

```powershell
git push origin main
```

Delete the temporary branch locally and from the remote:

```powershell
git branch -d script-split
git push origin --delete script-split
```

### Phase 3: Back on this machine

Switch to main and pull the synchronized history:

```powershell
git switch main
git pull origin main
```

Remove the local branch reference:

```powershell
git branch -d script-split
```
