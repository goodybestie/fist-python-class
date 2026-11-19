'''
. Git and GitHub

Key difference to state clearly:

Git is a tool on your computer that saves snapshots (versions) of your project.
GitHub is a website that stores your Git projects online, for backup, sharing and your portfolio.
Analogy: Git is like taking photos of your work; GitHub is the online album.

The three places your code lives (draw this on the board):

Working folder  →  git add  →  Staging area  →  git commit  →  History (local)  →  git push  →  GitHub
 (your edits)                 ("these go in the     (snapshot saved)                       (online backup)
                                next snapshot")

                                What each command does:

git init turns this folder into a Git project (creates a hidden .git folder).
git status shows what changed. Teach students to run it constantly. It’s their dashboard.
git add . stages every changed file (the . means “everything in this folder”).
git commit -m "..." saves the snapshot with a message describing what changed.
git push uploads commits to GitHub.
'''