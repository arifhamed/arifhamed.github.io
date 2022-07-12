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
* Any terminal/console/bash window (preferably with administrator rights)
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

## git config
Before we even begin anything at all, this step is essential to let the repository know that it is you who are changing it. tbh, idk why it doesn't require a password, because if someone knows your username and email, then they can just modify anything you have.
``` bash
~$ git config --global user.name "<your username>"
~$ git config --global user.email "<your email>"
~$ git config --list
```

Something that helps is using `gh auth login`, though more or less, the GitHub CLI is used for managing issues, branches, releases, release assets, and other GitHub-specific details. `git` here is also used for other repository types, like mercurial, and, um, other ones. Is mercurial counted as one anymore? eh, whatever.

<hr>

## git clone 
To start of, let's use a repository that you own. In this demo, I will be using an old repo, <a href="https://github.com/arifhamed/files-000" target="_blank">https://github.com/arifhamed/files-000</a>. Now, in your terminal, it's best to change your current working directory to one where files would move frequently, like Downloads or Documents. Next, your first git command is `git clone`, as shown below:
``` bash
~$ git clone https://github.com/arifhamed/files-000
Cloning into 'files-000'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

~$ cd files-000
```
Now you have copied from the **remote** repository to your storage, in which that one is called the **local** repository. Git is where you can manage changes between **local & remote**, usually changes from local will update the remote. 

<hr>

## git add, git rm
`git add` will not update your remote repository so fast, but it will just record your change. I am a simple man, and so is this command too, for after making a lot of changes to your files, you can just put in the following command:
``` bash
~$ git add .

~$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

```
The `.` there represents everything, basically. In here, I used `git status` to check if `git add .` worked, as it did, after I opened, edited & saved the README.md. 

Now, your edit/addition/removal is recorded!

<hr>

## git commit 
Commit is basically putting all the changes into the envelope, but not sending it yet. `git commit` will put all your changes into a commit. You can have multiple commits at a time.

``` bash
~$ git commit -m "edit for the blog"
[main 81af249] edit for the blog
 1 file changed, 2 insertions(+)

~$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

```

Every commit requires a message to come with it, as shown above, after the command and option `-m`, i left a string there, `"edit for the blog"`. Now, I have one commit, and also shown in `git status`, there is nothing new for me to commit, as all the edits, additions & removals (with `git add` & `git rm`). 

Now, you can push it!

<hr>

## git push
With your commit, it is important to push it so that you can update your remote repository. 

``` bash
~$ git push -u origin head
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 312 bytes | 156.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/arifhamed/files-000
   57e8612..1c5c92d  head -> main
branch 'main' set up to track 'origin/main'.

```

Now if you check your remote repository, it would show the latest commit pushed, as shown below in the screenshot:

<img src="/static/images/git-pushed.jpg" class="w-100">

_&lt;more details will come later&gt;_