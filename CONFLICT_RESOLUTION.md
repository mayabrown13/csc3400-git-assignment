# Conflict Resolution Process

This demonstrates the steps taken within the conflict resolution process throughout this assignment, with thorough explanation throughout.

## Creating a Merge Conflict

For this to occur, two things were present:
1. A change in the original repository
2. A slightly different change in the cloned repository

## Identifying a Conflict

1. Add your changes.

```git add .```

2. Commit your changes.

```git commit -m "Message"```

3. Push your changes to Github.

```git push -u origin main```

This error message like this will appear:

```To https://github.com/mayabrown13/csc3400-git-assignment.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/mayabrown13/csc3400-git-assignment.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```


## Steps to Fix It
1. Pull the latest changes from the remote repository.

```git pull origin main```

2. Edit the changes together to adding, deleting, or finding a compromise to incorporate both changes.
3. Save new file : 

Command + S

4. Add changes.

```git add .```

5. Commit changes.

```git commit -m "Resolved merge conflict"```

6. Complete the merge.

```git rebase --continue```

7. Push changes to Github.

```git push origin main```

## What Now?
The merge conflict has been resolved, and you can now continue with your project!