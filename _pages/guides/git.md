---
title: "Git"
permalink: /guides/git
redirect_from:
 - /guides/git/
layout: default
---

# Git
<a href="https://git-scm.com/" target="_blank">Git</a> is a version control system  is basically a version control system and here is where I can show the basics of using Git to control both your remote and local repositories. In this guide, I will go through a step-by-step demo to showcase the basics and essentials of Git (most of the ones that I use frequently anyway).

What is required for this:
* A GitHub account (you can create <a href="https://github.com/signup" target="_blank">here</a>, awesome ui by github btw)
* Any terminal/console window (preferably with administrator rights)
* <a href="https://git-scm.com/downloads" target="_blank">Git</a> installed to your computer
* A repository you own (requires GitHub account). If you don't have one, you can create one <a href="https://github.com/new" target="_blank">here</a>

<hr>

Now this is how git version control works (or at least to my own interpretation):
1. Copy from remote to local ([git clone](#git-clone))
1. Make change in local
1. Record change ([git add, git rm](#git-add-git-rm))
1. Put changes in envelope ([git commit](#git-commit))
1. Send envelope to remote ([git push](#git-push))
1. Remote will change according to what was recorded in envelope

This can happen on any local repo that links to the same remote repo, but what if a local repo updated the remote repo, making yours different?
1. Get the latest details from remote (can run anytime) (git fetch)
1. Read for any changes (can run anytime) (git status)
1. Sync it (git pull)

<hr>

## git clone 
To start of, let's use a repository that you own. In this demo, I will be using an old repo, <a href="https://github.com/arifhamed/files-000" target="_blank">https://github.com/arifhamed/files-000</a>. Now, in your terminal, it's best to change your current working directory to one where files would move frequently, like Downloads or Documents.
``` console
C:\WINDOWS\system32>cd /users/morph/downloads

C:\Users\morph\Downloads>D:

D:\>cd repos

D:\Repos>
```
The above example is just showing you can do this in Downloads or on a seperate disk. 
Next, your first git command is `git clone`, as shown below:
``` console
D:\Repos>git clone https://github.com/arifhamed/files-000
Cloning into 'files-000'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

D:\Repos>cd files-000

D:\Repos\files-000>
```
Now you have copied from the **remote** repository to your storage, in which that one is called the **local** repository. Git is where you can manage changes between **local & remote**, usually changes from local will update the remote. 

<hr>

## git add, git rm
`git add` will not update your remote repository so fast, but it will just record your change. I am a simple man, and so is this command too, for after making a lot of changes to your files, you can just put in the following command:
``` console
D:\Repos\files-000>git add .

D:\Repos\files-000>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md


D:\Repos\files-000>
```
The `.` there represents everything, basically. In here, I used `git status` to check if `git add .` worked, as it did, after I opened, edited & saved the README.md. 

Now, your edit/addition/removal is recorded!

<hr>

## git commit 
Commit is basically putting all the changes into the envelope, but not sending it yet. `git commit` will put all your changes into a commit. You can have multiple commits at a time.

``` console
D:\Repos\files-000>git commit -m "edit for the blog"
[main 81af249] edit for the blog
 1 file changed, 2 insertions(+)

D:\Repos\files-000>git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

D:\Repos\files-000>
```

Every commit requires a message to come with it, as shown above, after the command and option `-m`, i left a string there, `"edit for the blog"`. Now, I have one commit, and also shown in `git status`, there is nothing new for me to commit, as all the edits, additions & removals (with `git add` & `git rm`). 

 Now, you can push it!

 <hr>

 ## git push
 _&lt;more details will come later&gt;_