# Git Workflow

## Branching Strategy

* **main**: main source of code
* **feature/error-handling**: deals with any input errors
* **feature/user-interface**: utilizes calculator function
* **hotfix/readme-update**: detailed instructions file

## 2. Commit Message Conventions

* Format: `type(scope): short description`

  * Example: `feat(auth): add login validation`

## 3. Code Review Process

1. Create a **pull request** from your branch.
2. Check code quality and accuracy.
3. Address comments.
4. Merge pull request.

## 4. Release Workflow

1. Create a **release branch** from main.
2. Test and fix bugs.
3. Merge release branch into main and tag version (`v1.0.0`).
4. Production!

## 5. Common Git Commands

| Command                 | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| `git clone <repo>`      | Copy repo locally                        |
| `git status`            | See changes and branch info              |
| `git add <file>`        | Stage changes                            |
| `git commit -m "Message"`| Commit changes                           |
| `git pull`              | Get latest changes from remote           |
| `git push`              | Send commits to remote                   |
| `git checkout <branch>` | Switch branches                          |
| `git merge <branch>`    | Merge branch into current                |
| `git rebase <branch>`   | Reapply commits on top of another branch |
| `git log --oneline`     | See commit history                       |
