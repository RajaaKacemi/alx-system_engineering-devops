```
░█████╗░██╗░░██╗░░███╗░░░░██╗██╗░░░
██╔══██╗╚██╗██╔╝░████║░░░██╔╝██║░░░
██║░░██║░╚███╔╝░██╔██║░░██╔╝░██║░░░
██║░░██║░██╔██╗░╚═╝██║░░███████║░░░
╚█████╔╝██╔╝╚██╗███████╗╚════██║██╗
░╚════╝░╚═╝░░╚═╝╚══════╝░░░░░╚═╝╚═╝

███╗░░░███╗██╗░░░██╗░██████╗░██████╗░██╗░░░░░
████╗░████║╚██╗░██╔╝██╔════╝██╔═══██╗██║░░░░░
██╔████╔██║░╚████╔╝░╚█████╗░██║██╗██║██║░░░░░
██║╚██╔╝██║░░╚██╔╝░░░╚═══██╗╚██████╔╝██║░░░░░
██║░╚═╝░██║░░░██║░░░██████╔╝░╚═██╔═╝░███████╗
╚═╝░░░░░╚═╝░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝
```



<br><br><br>

# Concepts



For this project, we expect you to look at these concepts:

* [Database administration](https://intranet.alxswe.com/concepts/49)
* [Web stack debugging](https://intranet.alxswe.com/concepts/68)
* [[How to] Install mysql 5.7](https://intranet.alxswe.com/concepts/100002)

<br>

![concept image](./images/concept.png)

<br><br>

# Resources

### Read or watch:

* [What is a primary-replica cluster](https://intranet.alxswe.com/rltoken/eojqG9FZbA6QVWN5P9cLzA)
* [MySQL primary replica setup](https://intranet.alxswe.com/rltoken/z2KVk2UKLMc0RvHMdJmYLg)
* [Build a robust database backup strategy](https://intranet.alxswe.com/rltoken/BharnxaLb-BDDYFywzME2Q)

### man or help:

* `mysqldump`

<br><br>


# Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/Lotf0yqq3mNeFHkrW67CZQ), <b>without the help of Google:</b>

### General

* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

### Copyright - Plagiarism

* You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
* You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
* You are not allowed to publish any content of this project.
* Any form of plagiarism is strictly forbidden and will result in removal from the program.


<br><br>


# Requirements


### General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.3.7-5~ubuntu16.04.1` via `apt-get`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing


<br><br>

# Tasks

░░░░░░░░░░░░ <b>Mandatory Tasks</b> ░░░░░░░░░░░░

<br><br>

## 0. Install MySQL


First things first, let’s get MySQL installed on <b>both</b> your web-01 and web-02 servers.

* MySQL distribution must be 5.7.x
* Make sure that [task #3](https://intranet.alxswe.com/rltoken/h8QknQcmmLf7oT8esoWgvg) of your [SSH project](https://intranet.alxswe.com/rltoken/Wx_BrR5Sk8s3Ywl44-33wg) is completed for `web-01` and `web-02`. The checker will connect to your servers to check MySQL status
* Please make sure you have your `README.md` pushed to GitHub.

Example:


```
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```



### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x14-mysql`






<br><br>

<br><br>

<br><br>

<br><br>

<br><br>

<br><br>




░░░░░░░░░░░░ <b>Advanced Tasks</b> ░░░░░░░░░░░░