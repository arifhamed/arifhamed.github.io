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
<hr>

## git clone 
To start of, let's find a public repository. In this demo, I will be using an old repo, <a href="https://github.com/arifhamed/minimalistpaint" target="_blank">https://github.com/arifhamed/minimalistpaint</a>. Now, in your terminal, it's best to change your current working directory to one where files would move frequently, like Downloads or Documents.
``` console
C:\WINDOWS\system32>cd /users/morph/downloads

C:\Users\morph\Downloads>D:

D:\>cd repos

D:\Repos>
```
The above example is just showing you can do this in Downloads or on a seperate disk. 
Next, your first git command is `git clone`, as shown below:
``` console
D:\Repos>git clone https://github.com/arifhamed/minimalistpaint
Cloning into 'minimalistpaint'...
remote: Enumerating objects: 20, done.
remote: Total 20 (delta 0), reused 0 (delta 0), pack-reused 20
Receiving objects: 100% (20/20), 19.87 KiB | 6.62 MiB/s, done.
Resolving deltas: 100% (8/8), done.

D:\Repos>
```
Now you have copied from the **remote** repository to your storage, in which that one is called the **local** repository. Git is where you can manage changes between **local & remote**, usually changes from local will update the remote. 
<hr>

## git add 
&lt;more details will come soon&gt;
