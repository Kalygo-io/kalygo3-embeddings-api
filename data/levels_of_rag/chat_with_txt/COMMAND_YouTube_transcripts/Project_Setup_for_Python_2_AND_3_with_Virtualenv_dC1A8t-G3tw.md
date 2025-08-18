---
title: "Project Setup for Python 2 AND 3 [with Virtualenv]"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/dC1A8t-G3tw"
publish_date: "12-28-2022"
---

00:00:02.460 here I have opened up a folder on my
00:00:05.220 computer with vs code
00:00:07.500 and we can see that inside of this
00:00:08.940 folder there exists one file called
00:00:11.360 readme.md when we're done with this
00:00:13.500 walkthrough you can take the final
00:00:15.000 boilerplate project and choose to use it
00:00:16.800 to build your own python applications
00:00:18.320 you will tweak this readme file to
00:00:20.939 contain information and documentation
00:00:22.380 that is relevant to the application that
00:00:23.880 you create
00:00:28.320 I prefer not to have one huge readme
00:00:31.380 file at the root of my project but
00:00:33.239 instead have smaller readme files for
00:00:36.719 organizational purposes
00:00:38.640 I put each readme file inside of the
00:00:40.980 readme's folder
00:00:42.840 right now the readme's folder has one
00:00:44.879 readme
00:00:45.899 with information that I will use to
00:00:47.820 guide me as I set up this first python
00:00:50.940 project
00:00:53.700 we already have python installed you
00:00:55.739 already have Pip installed
00:00:57.600 so let's install our first third-party
00:01:00.360 package virtual MV
00:01:07.439 I already have it installed
00:01:09.780 let's verify the version
00:01:15.000 the reason that we need virtual m is
00:01:17.040 that python by default installs packages
00:01:19.020 globally on our system
00:01:21.360 this means that if we have two projects
00:01:22.979 on our computer that use the same
00:01:24.180 third-party package but require
00:01:25.380 different versions of the third party
00:01:26.700 package we won't be able to run both
00:01:28.799 apps at the same time
00:01:31.140 for example let's say that we have
00:01:32.820 project and our computer that uses a
00:01:34.560 third-party package called awesome
00:01:35.640 package but uses version six
00:01:37.799 let's say that we also have Project B on
00:01:39.540 our computer but Project B uses awesome
00:01:41.159 package versus seven
00:01:43.799 when referencing packages from our
00:01:45.360 python code we can only specify the name
00:01:47.640 of the package not the version
00:01:49.500 so an issue will arise when running
00:01:51.119 either Project A or B because one of
00:01:53.280 them will not be referencing the version
00:01:54.479 of the package it needs
00:01:56.820 so what virtual M does is set up our
00:01:59.280 project to not install and use packages
00:02:00.899 globally but instead set us up to
00:02:02.579 install and use packages within our
00:02:03.899 project folder
00:02:05.159 this then allows each project on our
00:02:07.079 computer to use its preferred versions
00:02:08.399 of packages without affecting other
00:02:09.899 projects
00:02:10.979 here is how we can use VMV
00:02:15.780 this command
00:02:18.599 is how we can create a folder in our
00:02:21.480 project that will house all of the
00:02:24.360 Python packages we install
00:02:26.819 the final argument of this command is
00:02:28.860 the name of the folder that we want to
00:02:30.780 use
00:02:31.680 you can call it whatever you want but by
00:02:33.120 convention it is called the VM folder
00:02:36.540 the next thing to do is configure our
00:02:38.340 terminal or our shell
00:02:41.280 to configure pip to install whatever
00:02:45.660 packages we choose to install in our
00:02:47.459 project into this VM folder
00:02:51.120 and we do that with this command
00:02:53.099 if this command was successful you
00:02:55.260 should see that your terminal prompt has
00:02:56.879 changed to this before it was this
00:02:59.940 now it is this
00:03:02.040 let's smoke test everything to make sure
00:03:04.500 that
00:03:06.420 we're on the right track
00:03:09.660 we're creating a file called main.py
00:03:12.060 let's throw some code into that file
00:03:16.200 and let's execute
00:03:19.920 the main.py file
00:03:22.019 and we can see that hello world has been
00:03:24.239 printed
00:03:26.700 now let's run this command python
00:03:30.500 main.py without the three
00:03:33.239 and we can see it works
00:03:35.280 another thing that VM does is Alias the
00:03:38.519 python command to whatever version of
00:03:40.920 python you have installed in your
00:03:42.299 project
00:03:43.319 let's develop this main.py file to be a
00:03:46.140 little bit more intricate now
00:03:49.980 let's use
00:03:52.019 these
00:03:53.640 packages and
00:03:56.640 the app we are about to develop
00:04:00.599 pandas and
00:04:03.000 matplotlib
00:04:05.220 and we are going to graph
00:04:07.500 some temperature data
00:04:12.360 let's throw some temperature data into
00:04:15.180 this file
00:04:22.620 come back to our readme
00:04:24.840 and let's copy our new program into
00:04:28.680 main.py
00:04:32.639 save that let's run
00:04:36.960 main.py
00:04:40.560 voila
00:04:43.740 let's close that let me just show you
00:04:46.139 two more things the first of the last
00:04:48.360 two things being bookkeeping of the
00:04:51.300 third party packages we have installed
00:04:53.460 into our application
00:04:56.040 if you are familiar with node.js or Ruby
00:04:58.620 on Rails then you know about the
00:05:00.300 package.json or gem files these are
00:05:02.580 files that record all of the third-party
00:05:05.040 packages we have installed into our
00:05:06.540 application pip or python does not do
00:05:09.000 this by default we have to manually
00:05:11.900 execute this as another step
00:05:16.560 pip freeze will spit out all of the
00:05:19.800 third party packages as well as their
00:05:22.020 versions
00:05:23.039 and the second half of this command will
00:05:26.340 pipe this into a file
00:05:28.440 that is conventionally named
00:05:30.180 requirements.txt
00:05:32.580 the second of the last two things is
00:05:35.160 regarding the dot get ignore in node.js
00:05:38.520 development you do not store
00:05:41.160 the node modules folder into revision
00:05:44.639 control
00:05:45.660 and in Python development you do not
00:05:48.120 store the VM folder into revision
00:05:51.840 control
00:05:53.160 so let's add a DOT get ignore
00:05:56.460 and I will copy
00:05:59.580 this suggested dot get ignore file from
00:06:02.160 GitHub
00:06:03.120 and paste it into our project
00:06:07.560 actually let me show you one last thing
00:06:09.539 and that is what the reactivation
00:06:12.780 process would look like
00:06:14.580 so if we type deactivate
00:06:20.880 we see that we are now outside or have
00:06:24.360 exited our virtual environment
00:06:26.819 right so if you wanted to collaborate on
00:06:29.280 this project with a friend for example
00:06:33.780 they would not get the VM folder they
00:06:36.240 would get something like this right this
00:06:37.560 is what they would clone
00:06:39.539 and they would run the project like
00:06:43.800 so
00:06:45.000 they would
00:06:47.220 hopefully already have Python pipped and
00:06:50.819 virtual M installed
00:06:53.460 they would generate the VM folder
00:06:57.720 they would activate their shell
00:07:01.020 you can see that the terminal prompt has
00:07:02.520 changed and then they would reinstall
00:07:05.400 all of the packages listed in the
00:07:09.180 requirements.txt file
