# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > * `mkdir` - make a directory
* `grep` - searches text in files
* `cat` - read file
* `pwd` - shows your current file path
* `chmod` - change permissions for file
* `pushd` / `popd` - push/pop directory
* `touch` - create empty file
* `rmdir` - remove directory
* `mv` - move directory
* `man` - read manual page
* `apropos` - find appropriate manual page

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > * `ls`: list files and folders in directory, except hidden ones (i.e. ones starting with . or ..)
* `ls -a`: list files and folders in directory, including hidden ones 
* `ls -l`: shows long list format of files and folders in directory, including details for file permissions, size, owner, date modified, etc.
* `ls -lh`: combination of -l and -h, which shows long list of format of files and folders in directory in “human readable” format
* `ls -lah`: combination of -l, -a, and -h, which shows long list of format of all files and folders in directory, including hidden ones, in “human readable” format
* `ls -t`: list files and folders in directory, sorted by time modified
* `ls -Glp`: shows long list format of files and folders in directory with colorized file names and a forward slash displayed after directories (rather than files)

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * `ls -m`: shows an easy-to-read list of contents in directory, separated by commas
* `ls -R`: shows contents of directory and all subdirectories
* `ls -u`: shows contents of directory sorted by access time
* `ls -l` : shows long list format of contents in directory
* `ls -S` : shows contents of directory sorted by file size
* `ls -G` : shows colorized file names

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` executes a command on a number of provided arguments. For example, `find . -name "temp*" | xargs rm` would take in the list of files output by `find` (i.e. any file starting with a name starting with "temp") and remove each one. 

 
