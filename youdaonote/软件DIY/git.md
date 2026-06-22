

```javascript
git init
git config --global user.name "redstoneleo"
git config --global user.email "redstone-cold@163.com"
```

To get Git to track them, you need to stage them, or add them to the staging environment.

whenever you hit a milestone or finish a part of the work, you should add the files to a Staging Environment.





“fatal: refusing to merge unrelated histories”

git pull origin master --allow-unrelated-histories







A repository is usually used to organize a single project. Repositories can contain folders and files, images, videos, spreadsheets, and data sets -- anything your project needs.



You can use branches to experiment and make edits before committing them to main.



Have you ever saved different versions of a file? Something like:





story.txt


story-edit.txt


story-edit-reviewed.txt


Branches accomplish similar goals in GitHub repositories.





Here at GitHub, our developers, writers, and designers use branches for keeping bug fixes and feature work separate from our main (production) branch. When a change is ready, they merge their branch into main.



You can make and save changes to the files in your repository. On GitHub, saved changes are called commits. Each commit has an associated commit message, which is a description explaining why a particular change was made. Commit messages capture the history of your changes so that other contributors can understand what you’ve done and why.



When you open a pull request, you're proposing your changes and requesting that someone review and pull in your contribution and merge them into their branch. Pull requests show diffs, or differences, of the content from both branches. 







A remote repository is generally a bare repository — a Git repository that has no working directory. Because the repository is only used as a collaboration point, there is no reason to have a snapshot checked out on disk; it’s just the Git data. In the simplest terms, a bare repository is the contents of your project’s .git directory and nothing else.





sudo apt-get install -y git-core



git clone --bare mysite  mysite.git























