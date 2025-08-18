---
title: "CrewAI and AgentOps for beginners"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/lfUDYoYMhmY"
publish_date: "10-1-2024"
---

00:00:00.000 No text
00:00:00.240 in this video we will introduce two new tools coming out of the agent development world the first is crew aai
00:00:05.759 and the second is Agent Ops crew aai is a multi-agent framework and agent Ops is an agent observability tool crew AI is
00:00:12.599 one of the leaders in their space as is Agent Ops for reference here's a list showing the leading open- Source
00:00:18.640 multi-agent Frameworks ordered by GitHub stars as of October 2024 if you want to code along step by
00:00:25.599 step you'll need to install two tools onto your machine Docker desktop and s code both of these tools are free and
00:00:32.200 offer extremely easy to use installation processes with support for Mac windows and Linux I'll be using Mac in this
00:00:38.840 video but the general process of what we'll be doing will be the same for Windows or Linux let me now show you how
00:00:44.120 I installed these two tools on my Mac so you get a feel for how easy it was for me but if your experience is not as
00:00:49.640 straightforward please leave a comment so I'm aware or I suggest you put detailed descriptions of the issues you're running into into either Google
00:00:56.399 or chat GPT for help troubleshooting here's how to download and install Docker desktop on Mac go to the official
00:00:58.000 No text
00:01:03.000 download page download the appropriate version for me this is Apple
00:01:08.320 silicone open the downloaded DMG file and drag and drop the docker doapp
00:01:15.439 icon into your applications folder I've already done this so I'll click stop but
00:01:22.000 that's it it's that easy and here's how to download and install vs code on Mac
00:01:23.000 No text
00:01:27.920 go to the official download page download the appropriate version for me this is Apple silicone unzip the
00:01:35.399 downloaded zip file and drag the visual studio code. apppp icon into your
00:01:42.159 applications folder I've already done this so I'll click stop but that's it it's that easy
00:01:49.640 after installing VSS code you'll need to do one last thing open VSS code and come
00:01:55.159 over to the extensions Marketplace on the side menu and you'll need to install two two extensions a the docker
00:02:03.320 extension you can search for it in the search bar and once you find it in the panel and click on it and then you'll
00:02:11.160 see these buttons right here you can click to install it should only take one click it's that simple B you'll need the
00:02:18.840 dev containers extension you should see some buttons right here you can just click to install
00:02:25.680 it super simple and that should be all the setup you need all right here we go
00:02:29.000 No text
00:02:31.599 from scratch crew AI agent Ops let's do it here we have an empty folder
00:02:37.879 somewhere on our computer that we're going to use as our starting point first we're going to set ourselves up with a
00:02:43.360 very solid foundation to build this crew aai application on top of or I should say I find this Foundation to be very
00:02:50.640 solid but let me know what you think in the comments let's start by adding the following folder and files to this empty
00:02:57.280 project at the root let's create a folder calledd container inside of thisd
00:03:03.400 container folder let's create a file called devc container. Json and at the root of this project
00:03:10.799 let's also create a file called Docker file.
00:03:15.840 deev here is the content we will paste into the devc container. Json
00:03:22.000 file you'll understand what the content of this file does shortly
00:03:31.239 and here is the content we'll paste into the docker file. deev you understand what the content of
00:03:38.040 this file does shortly as well all righty now that we have these files set up we can launch our Dev container we
00:03:46.120 won't go into detail but when I say launch our Dev container what I mean is we will build a mini computer that will
00:03:52.360 run on top of our actual computer inside of this mini computer we'll play around with crew aai close or kill the min
00:03:59.799 computer when we're done and then our base machine AKA our laptop or desktop or whatever we're using will be left
00:04:06.799 clean as if nothing ever happened AKA this is a fantastic technique for
00:04:11.920 experimenting with new software without cluttering our base machine with potentially messy software
00:04:18.320 installations here's how we build our Dev container in vs code we type shift
00:04:23.800 command p and that opens this menu called the command pallet inside the
00:04:28.880 command pallet we look look for an option that says Dev containers reopening container I think this menu
00:04:36.639 option will only be available if you have the dev containers vs code extension installed when we select
00:04:42.560 it our Dev container will begin being built in my experience building a Dev
00:04:48.000 container takes about 1 to 3 minutes it depends on the number of factors like how fast my machine is or the details of
00:04:55.880 the dev container I'm building Etc but after the def container is right so that
00:05:01.639 took like what like a minute maybe even less but after a def container is built
00:05:07.080 we can shut it down turn it on shut it down turn it on shutting it down and turning it on only takes a few seconds
00:05:14.960 anyways it might take longer for you it might be shorter I don't know the details of your environment but
00:05:20.000 hopefully that gives you a feel for how this works let's quickly test out this development container to make sure it's
00:05:25.319 looking good as crew aai is a python based tool let's confirm we have python
00:05:31.280 installed and we do and let's try running some python
00:05:36.759 code to make sure that works too so here I've created a file called
00:05:42.520 main.py let's add some code into this file and pass this main.py file to the
00:05:50.160 python interpreter on the dev container and it looks like it works if
00:05:55.520 we look closer at the docker file. deev we can see we asked docker to build us a
00:06:00.840 mini machine with python 3.12 installed on it and we also asked for some
00:06:06.039 additional C++ libraries to be installed as well because these will be needed by crew aai the remaining lines of this
00:06:12.759 file outline where we want to work inside of this Dev container for example
00:06:18.960 if we enter the PWD command or present working directory on our Dev container we can see we are in a folder called
00:06:25.440 code at the root of the file system if we were to look at the root of the file Sy system on our base machine we would
00:06:31.599 not see any folder by the name of code the mental model to keep in mind is that
00:06:37.280 we have two separate systems running on our machine we have the dev container and we have our base machine each of
00:06:44.199 these two systems has its own file system and is capable of having completely different software installed
00:06:50.919 moving forward we're going to be working inside of the code folder at the root of the file system of the development
00:06:57.520 container or our mini machine that's running on top of our base machine hopefully that makes sense let's remove
00:07:04.120 this main.py file that we use for performing a quick hello world test and move along now that we have a solid
00:07:09.000 No text
00:07:10.840 foundation we can start building our crew AI project the way we're going to do this is not recommended at all but
00:07:16.800 for the purposes of learning how crei works it will be fantastic what we're going to do is build up a simple crei
00:07:23.400 project from scratch one file at a time here on cre ai's documentation they
00:07:28.720 provide an outline of what a crew AI application looks like we can see a crew AI project contains a source folder
00:07:35.000 inside of the source folder we have another folder here it's called my project inside of the my project folder we have a main.py file a crewp file a
00:07:42.000 tools folder a config folder inside of the config folder we have an agents. yo file and a task. yo file okay got it so
00:07:49.599 in the same way a chef can take a look at a recipe get the gist of it and improvise on it when cooking a dish we
00:07:55.360 are going to build an application that follows the general outline of what a crew AI application looks like let's add
00:08:01.319 the following folders and file to our Dev container at the root of our project let's create a folder called Source
00:08:07.240 inside of this Source folder let's create a folder called R crew of agents and inside of this R crew of Agents
00:08:12.560 folder let's create a file called main.py when a file ends inp it
00:08:18.479 indicates to us that it will hold python code when you're looking at python projects it's very common to see some
00:08:24.280 file called main.py for our purposes main.py will be the file we use to Launch our agents and give them tasks
00:08:31.919 for the beginners watching I find it important to tell you that when programming we can call files folders and many other aspects of the code we
00:08:38.399 write whatever we like for example we could have called main.py blah. py let me show you let's rename
00:08:46.200 main.py to be called blah. py and let's add simple instruction into
00:08:53.680 blah. py for example this is the instruction to print telling my agents
00:08:58.720 to do something to this screen and then let's pass this bl. py file to the python interpreter and then you can see
00:09:06.079 we get the text printed telling my agents to do something names are just labels and when programming there are an
00:09:12.320 infinite number of ways to organize your code in practice though so it's easier to collaborate and build with others we
00:09:18.360 follow conventions these conventions are learned through experience over time so be patient if you're feeling unfamiliar
00:09:24.760 with what you're looking at watch the whole video and come back to any confusing Parts later
00:09:30.079 let's rename this blah. py file back to main.py because that's more conventional
00:09:36.279 and quickly confirm that everything works and let's pass the main.py file to
00:09:44.360 the python interpreter and as we can see everything works just the same now
00:09:48.000 No text
00:09:49.839 instead of Simply printing out the text telling my agents to do something let's add some code provided to us by the team
00:09:55.640 at crew aai we could add all of the code of this product into a single file AKA
00:10:00.839 this main.py file but that is not advised as over time that would mean we would constantly be scrolling up and
00:10:06.399 down across the main.py file as we added more lines therefore let's add another file to our project called crepy let's
00:10:13.839 add this crew. py file inside of the r crew of Agents folder and here is the content that we
00:10:19.880 will paste into this crewp file and we can call the code in this
00:10:25.959 screw. py file from the main.py file like so
00:10:31.640 okay remember this Docker file. deev file and how it included this line that says python path equals SLC code this
00:10:39.959 line configures the python interpreter on the dev container to look for code we import at this specified path for
00:10:46.560 example if we look at the path of the crew. py file we can see the path is slode Source our crew of Agents crew. py
00:10:54.279 I know in the main.py file paths are specified with dots in our Imports
00:10:59.480 instead of slashes but in this context it means the same thing also note that
00:11:05.360 we don't have to write Pi at the end of python files we Import in our code quick
00:11:11.279 side note so in my vs code I was seeing a warning that said select interpreter the warning was showing right here vs
00:11:18.200 code should automatically detect The Interpreter path on the dev container right so hopefully you don't see this
00:11:23.320 issue but I've seen it happen from time to time and if this is happening for you this is how you fix it in vs code Type
00:11:29.720 shift command P that'll open up the command pallet and search for an option that says python select interpreter if you don't see this menu option you can
00:11:35.160 start typing python it'll start filtering out the menu options then you can select this one right this is the appropriate one python select
00:11:40.600 interpreter hit enter and that'll take you to a submenu as I mentioned vs code
00:11:46.079 should automatically detect The Interpreter path right hopefully you see a recommended option you can just select it and that'll make the warning go away
00:11:52.600 if for some reason you don't see a recommended option in the submenu you can manually enter the path to The
00:11:57.680 Interpreter on the dev container here right by selecting this option enter interpreter path the path to The
00:12:02.839 Interpreter is SL user SL local bin SL
00:12:08.880 python then you can click enter and that should make the warning go away as well if you recall you know I guess 30 60
00:12:16.600 seconds ago crew was colored white as was the r crew of Agents symbol right
00:12:22.560 and after I selected The Interpreter path everything became colored appropriately as I expected Etc so
00:12:29.480 like I said if everything's colored as you're seeing it or you know everything's working smoothly ignore the
00:12:35.320 section but if you have a warning showing somewhere in your vs code UI that says you know select interpreter
00:12:41.040 path I just showed you how to fix it so let's move forward let's try running our crew of agents for the first
00:12:43.000 No text
00:12:47.240 time module not found error no module named crei when we fed this main.py file to
00:12:53.600 the python interpreter the code or the instructions outline began being executed from top to bottom on line one
00:12:59.959 you can see we're doing an import we're importing source. our crew of agents. crew that popped the python interpreter
00:13:05.800 over to the crew. py file in this file you can see on line one we're also doing an import we're
00:13:11.320 importing this thing called CI and you can see as indicated by vs code has this
00:13:16.519 yellow squiggly line underneath it if we hover over we see the text import cre AI could
00:13:23.040 not be resolved so as indicated by the error in the console and as indicated by
00:13:28.800 VSS code this crei thing is nowhere to be found so what we're going to do is
00:13:33.959 add this crei thing to our Dev container and hopefully this error will go away python has a system in its ecosystem
00:13:40.560 called pipie which is short for python package index that allows us to easily download code published by other members
00:13:45.720 of the Python Community if we enter this command to our terminal code published to pii by the crei team will be
00:13:51.839 downloaded to our Dev container in a way that the python interpreter can access if we omit the version number and just
00:13:58.120 type pip install crei the latest version of the cre package will be downloaded
00:14:03.320 but to not confuse things especially for those following along let's just download this version which is the
00:14:08.720 latest version as of the time of recording it looked like the
00:14:13.800 installation worked and we can see that the warnings and vs code went away so let's now try running our crew again and
00:14:20.120 see what
00:14:26.759 happens okay we see a different error which is fantastic that means we fixed the crew aai import error but now we're
00:14:33.279 seeing an error that says file not found no such file directory code Source or
00:14:39.040 crew of Agents config agents. yaml I wonder what this could
00:14:44.970 [Music] mean the way crew AI is design requires
00:14:48.000 No text
00:14:50.600 us to add this agents. yo file at a very specific location so let's add this file like so inside of the r crew of Agents
00:14:58.040 folder let's create another folder called config and inside of this config folder
00:15:03.800 let's add a file called agents.
00:15:09.399 yo let's paste this content into the agents. yo file as of the time of recording in
00:15:16.160 October 2024 the content of this agents. emo file has to follow a very specific structure with no indentation we put the
00:15:23.120 name of each agent in our crew and then at one level of invitation below the name we specify the agent's role goal
00:15:29.279 and backstory in natural language there are other properties that we can specify for our agents but these are the
00:15:35.279 required ones all the other ones are optional FYI this way of outlining
00:15:40.440 configuration is extremely common in programming and is called yaml format yammo allows you to specify key value
00:15:46.560 pairs of information that can be nested at various levels in the context of a yo file this angled bracket character is
00:15:52.959 known as a folding block symbol this character allows you to write the value associated with a key or property on
00:15:58.519 multiple lines instead of one big long line the way we connect this agents. yo
00:16:04.000 config with the crew in our crew. py file is like so we reference the relevant key so that
00:16:10.759 it lines up with a method name that generates each agent and let's do this for the other agent real quick as
00:16:21.279 well and that's it and oops we never imported the agent class from crew AI
00:16:27.880 let's do that and now all of our warnings go away and
00:16:33.880 we're looking good taking a step back we can see that our crew class is coming together nicely for the beginners
00:16:40.120 watching in the context of programming a class is a blueprint for creating things to use another cooking analogy let's say
00:16:46.440 that we have the recipe for a dish the recipe is not the dish it's the instructions for how to make the dish
00:16:53.000 similarly in programming a class defines the ingredients or components of code when we pass a class The Interpreter of
00:16:59.680 a particular programming language for example the python interpreter we are left with runnable code that implements
00:17:05.000 the blueprint defined in the class we can see in this class we're defining a group of two agents with one of them
00:17:10.679 being George Washington and the other being Thomas Jefferson now that we've defined the details of our agents let's
00:17:16.280 try running our crew again okay we see a different error and
00:17:22.599 that's fantastic that means we fixed the error related to the missing agents. yo file but now we're seeing an error that
00:17:28.600 says says file not found no such file or directory code Source our crew of Agents
00:17:35.280 config tasks. yammo I wonder what this could [Music]
00:17:42.600 be in addition to configuring our agents the creai framework requires us to specify a file called task. yaml that
00:17:43.000 No text
00:17:49.760 outlines the task we want the agents in our crew to perform so let's create this task. yo file at the exact location
00:17:56.159 given to us by this last error inside of this file let's paste the following
00:18:02.080 content as of the time of recording in October 2024 the content of this file has to follow a very specific structure
00:18:09.280 at no level of indentation we specify the name of each task and then at one level of indentation below the task we
00:18:14.919 specify its description its expected output and the agent we want to assign the task to the way we let our crew
00:18:22.440 class or blueprint know about the tasks outlined in this tasks. yo file is like
00:18:28.240 so we come over to the copy file and add the following
00:18:34.559 code and we have to format this according to Python's rules one
00:18:42.919 sec and let looking good we just have to import the task class from the crew AI
00:18:52.200 package as well as the task decorator if you've never seen a
00:18:58.159 decorator before this is a decorator all a decorator is is a fancy
00:19:04.360 way of writing a function that takes a function as an input and returns another function don't stress out about it just
00:19:12.400 look at this stuff from a high level zooming out we can see we're designing our crew to consist of two agents who
00:19:18.360 will work together to accomplish two tasks by default crew aai executes the
00:19:23.880 tasks outlined in the task. yo file sequentially from top to bottom so here we can see we're assigning Thomas
00:19:29.880 Jefferson to write us a declaration of independence and the Declaration of Independence he spits out will be fed into George Washington who will then
00:19:36.280 generate a military strategy for us there are other patterns besides sequential execution when giving groups
00:19:42.799 of Agents tasks to accomplish your goals we'll leave those topics for another video as we're keeping this super simple
00:19:48.520 and beginner friendly all right let's try running our crew again and see what
00:19:56.840 happens all right well we get a different error so we fixed that missing task. yo file error that's great and now
00:20:04.799 we're getting an error that says something went wrong kickoff should return only one task output
00:20:11.559 so sometimes when you see errors it's very straightforward but other times
00:20:16.760 it's not so if we come to crew.
00:20:22.159 Pi okay so this should have been written like so
00:20:28.720 so excuse me so yeah I think that should
00:20:36.480 work and let's run our crew again and see what
00:20:42.919 happens okay cool yeah so we have to define the tasks inside of our class and
00:20:48.880 we also have to link them with the crew object here so hopefully that makes
00:20:55.760 sense and now we're getting a different error this error says open AI exception API
00:21:03.720 key client option must be set
00:21:08.799 right authentication error I wonder what this could [Music]
00:21:16.000 No text
00:21:16.440 be this error is happening because we haven't authenticated our project with open AI platform crew AI supports
00:21:23.760 various llms for powering the agents in a crew but by default it uses open AI
00:21:29.120 if you're unfamiliar with the term llm an llm is the part of an agent we would consider its brain the details of how an
00:21:36.039 llm Works can be explored outside of this video if interested but for our purposes we'll be calling an llm powered
00:21:42.240 by open AI via its API each time one of the agents in our crew is performing the task currently assigned to it connecting
00:21:49.159 our project with open AI is simple all we have to do is come to platform.
00:21:54.520 open.com in our browser and and if this is a new account
00:22:01.159 for you you will have to add a couple dollars open AI pricing model is usage
00:22:08.159 based it's like a gas station you will need some credits and after you have that set up you can browse around and
00:22:15.320 look for the API key
00:22:21.140 [Music] section API Keys have been replaced by
00:22:27.120 project API keys view project API keys so here we can create a new API key
00:22:35.000 so let's click this button and we can leave everything as default
00:22:41.279 and click create secret key and make sure you keep this private
00:22:47.760 but let's copy it and we'll be using it later so make sure that no one else
00:22:53.480 besides you gets access to this API key and here is how we securely add this API
00:22:59.320 key to our project for the beginners watching pay attention closely because this technique is very common at the
00:23:06.279 root of our project we're going to create aemv file inside of this EMV file
00:23:11.880 we will type on a single line in all caps open
00:23:17.080 aior aior key equals and then we will paste
00:23:23.080 in the API key that we provisioned on open ai's platform
00:23:28.600 we'll save this and the next thing we'll do is install this special package
00:23:34.120 called python. MV this is the version that we'll be
00:23:39.640 using and then we'll come over to the main.py file and add these
00:23:48.520 lines these lines will read in any secrets that we have in the M file and
00:23:53.600 make them available to our code so now if we run our crew let's see what
00:24:00.799 happens hopefully this should
00:24:06.159 work and yeah things look like they're working the console looks
00:24:11.960 [Music] beautiful
00:24:18.400 and interesting we only see George
00:24:23.559 Washington performing a task let's see what's going on
00:24:33.600 oh I see what happened so The Decorator was accidentally
00:24:39.440 deleted so if we run our crew [Music]
00:24:45.679 again yep now we see Thomas Jefferson writing the Declaration of Independence
00:24:50.919 and when he's finished George Washington will write us or I guess he'll come up with a military strategy
00:25:03.679 right there goes the Declaration of Independence [Music] and here is the military
00:25:10.960 strategy so that's fantastic we have a working crew remember the way we built up our
00:25:15.000 No text
00:25:17.039 crew of Agents up from scratch manually is not recommended at all but for the purpose of learning how crew AI works I
00:25:23.279 hope you found it useful let's do one final thing before we wrap this up let's show how we can track our agents using a
00:25:29.799 tool called Agent Ops agent Ops is compatible with many different multi-agent Frameworks and allows us to
00:25:35.520 track metrics such as the cost of the agents in our crew how long it's taking the agents in our crew to complete its
00:25:40.600 tasks and it'll also track any errors our agents run into as well the process of integrating agent Ops is extremely
00:25:46.880 easy and is very similar to how we integrated with open AI to integrate with agent Ops come over to app. agent
00:25:55.600 ops. if you haven't signed up already create an account account and come over to the API key section once you're
00:26:03.200 logged into your dashboard you should already have an API key provision for you by default and copy this API key and
00:26:11.840 come back to the creai project that we've been building and inside of the M
00:26:18.679 file or the EMV file let's add a new line and in all caps let's write agent
00:26:27.240 Ops _ API uncore key equals and then
00:26:32.600 paste in the API key that you copied from the agent Ops dashboard save and then let's come over
00:26:38.679 to the main.py file and let's add the following
00:26:49.120 lines make sure you add these lines after the load. M command so that the
00:26:54.279 agent Ops API key is available to be used and make sure you add this this agent Ops tracking code before you call
00:27:00.440 your agents so that they're ready to be tracked before doing tasks but hold up
00:27:06.679 notice how VSS code is giving this little warning indicator telling us that there's something up with this agent Ops
00:27:12.600 import and we've seen this before it's because we haven't installed this package yet so let's type this pip
00:27:19.720 command into our
00:27:24.840 terminal and after the installation completes we should see this warning go away in vs code and it does so now let's
00:27:33.240 run our crew again and see what
00:27:45.360 happens and when our crew is done we see some
00:27:50.600 analytics right see the cost and we see this link that we can click on and
00:27:57.000 inspect we can see it gives us a dashboard with an overview of this
00:28:04.640 session that we just had with our crew and this can be very useful for troubleshooting issues and getting an
00:28:10.880 overview of what's going on as you leverage agentic workflows more and more you're going to need a tool like agent
00:28:17.240 Ops for monitoring what's going on okay let's now wrap this up so I'm going to
00:28:18.000 No text
00:28:23.279 move these two lines to the top of the file just to be a bit
00:28:30.039 cleaner and that looks [Music] good and let's also record all of the
00:28:37.440 piie packages that we use throughout the building process so the conventional way of doing this is
00:28:46.039 to create a file at the root called requirements.txt
00:28:52.399 and inside of this requirements.txt file let's paste the following content to
00:28:59.039 record the various piie packages we used as well as their versions and now let's store a copy of
00:29:06.559 this code on GitHub add a file
00:29:12.480 called dogit ignore and inside of this dogit ignore
00:29:21.919 file let's add this entry git is no longer tracking the M
00:29:29.840 file which is great that's what we want never expose your API Keys let's create
00:29:35.840 a repo on GitHub then add a remote to our local git
00:29:43.440 configuration and then push our code to
00:29:54.640 GitHub and let me take a look at our code in GitHub we don't see the EMV file that's
00:30:02.640 what we want and we also need to upload all the tags because I've been tracking
00:30:07.760 each step along the way so we'll say get push D-
00:30:14.279 tags fantastic then when we reload yeah fantastic so you can easily
00:30:21.279 follow along so what we can do now is
00:30:30.240 close our Dev container and poof it's like nothing ever happened
