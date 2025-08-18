---
title: "Production-Grade A.I. Agents MASTERCLASS"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/upTlhKQbnsE"
publish_date: "11-11-2024"
---

00:00:00.000 No text
00:00:03.719 we will now take a close look at a production application involving the use of llms AI agents Python gcp and Docker
00:00:12.559 that's right I said production application this is the real deal wake up if you're new to these Technologies
00:00:19.000 I'll do my best to make them approachable but you will need some familiarity with python cloud computing
00:00:24.160 and clis to follow along easily if you're familiar with these Technologies I'd love your feedback on the overall
00:00:29.599 design being presented in this walkthrough we will build a team of personalized AI agents who will send us
00:00:35.800 daily bullet points highlighting news updates happening across multiple websites here's a diagram showing what
00:00:41.840 we'll be building for clarity this design can be used as the foundation for building many applications but to get your creative
00:00:48.239 juices flowing here are two that come to mind one you can use this as a productivity hack for staying up to date
00:00:54.120 on a niche that matters to you and two you can use this as a foundation for building your own AI powered newsletter
00:01:00.359 we'll be building our agents with a python framework called crew aai and we'll be designing our application to run on an easy to use platform managed
00:01:06.240 by Google called Cloud run jobs so our agents run for us 24/7 here's an overview of the sections
00:01:12.000 that follow so you know what's ahead and I 100% guarantee this is going to be incredible
00:01:18.439 you will still get a ton of value if you want to Simply watch but if you want to code along here's what you'll need a
00:01:25.000 you'll need a PC AKA a laptop or desktop this is going to cost you some money B
00:01:30.479 you'll need Docker installed on your PC Docker is free C you'll need a code editor I suggest vs code or cursor vs
00:01:38.159 code is free cursor has a free trial FYI cursor is an altered version of vs code so even though I'll be using VSS code
00:01:44.759 you should be able to follow along D after vs code or cursor is installed install two VSS code extensions namely
00:01:51.719 the docker extension and the dev containers extension both of these extensions are free E you'll need a
00:01:57.159 GitHub account github's free tier will work F you need a gcp account gcp will
00:02:02.880 practically be free G you need an open AI account open AI will cost you between
00:02:08.038 a few pennies and a few dollars depending on circumstances H you'll need a mail gun account mail gun as a free
00:02:13.720 trial I you'll need an agent Ops account agent opsis free tier will work and optionally J You'll need a domain I know
00:02:20.920 this sounds like a lot but it's not that bad let me break it down in regards to Docker the code editor and the two BS
00:02:27.080 code extensions I'll be playing a clip shortly that shows how I install them onto my M1 MacBook Pro in under a minute
00:02:33.480 and even though my machine is Mac based the broad Strokes of what you'll see In that clip will apply to both Linux and
00:02:38.519 windows machines in regards to GitHub you can get an account by coming over to github.com and signing up in regards to
00:02:44.920 gcp you can come over to cloud.google.com and sign up gcp usually offers free credits upon sign up or
00:02:51.599 activation plus the cost of what we're doing in this video will be in the pennies so the gcp side of things should
00:02:58.159 be practically free assuming you tear on the gcp project within a couple days of building it we'll be showing how to tear
00:03:03.920 down gcp projects at the end of the video so what I'm saying is setting up
00:03:09.360 Docker a code editor two vs code extensions a GitHub account and a gcp
00:03:14.599 account is enough to get started the remaining items can wait till part five those being the open AI account powering
00:03:21.480 our agents the mail gun account for delivering our AI generated emails the agent Ops account for monitoring our
00:03:28.200 agents and optionally the domain if you don't mind the AI generated emails we
00:03:33.319 create being sent to spam which I think is okay for learning purposes don't worry about setting up a domain but if
00:03:39.280 you do want the AI generated emails we create to be properly sent to the recipient's inbox you will need a verified domain I suggest using whatever
00:03:46.720 domain regist you're most familiar with for example I'll be using Route 53 later in part six so let's take a deep
00:03:54.439 breath let it all out
00:04:00.079 if you have any setup or installation issues leave a comment or I suggest pasting detailed descriptions of the
00:04:05.519 errors you run into into either Google or chat GPT for assistance FYI if you're
00:04:11.400 laser focused you can complete all of the setup in under 15 minutes but if you
00:04:16.478 find it to be overwhelming just do Parts a through F and worry about the rest for
00:04:21.000 No text
00:04:21.490 [Music] later here's how to download and install Docker desktop on Mac go to the official
00:04:28.880 download page download the appropriate version for me this is Apple
00:04:34.240 silicone open the downloaded DMG file and drag and drop the docker doapp
00:04:41.320 icon into your applications folder I've already done this so I'll click stop but
00:04:47.919 that's it it's that easy and here's how to download and install vs code on Mac
00:04:53.880 go to the official download page download the appropriate version for me this is Apple silic cone unzip the
00:05:01.320 downloaded zip file and drag the visual studio code. apppp icon into your
00:05:08.039 applications folder I've already done this so I'll click stop but that's it it's that easy
00:05:15.479 after installing VSS code you'll need to do one last thing open VSS code and come
00:05:21.039 over to the extensions Marketplace on the side menu and you'll need to install two extensions a the docker extension
00:05:30.240 you can search for it in the search bar and once you find it in the panel click
00:05:35.280 on it and then you'll see these buttons right here you can click to install it
00:05:40.680 should only take one click it's that simple B you'll need the dev containers
00:05:47.120 extension you should see some buttons right here and you can just click to install it super simple and that should
00:05:54.120 be all the setup you [Music] need welcome
00:05:56.000 No text
00:06:00.360 so I'm assuming you have at least these prerequisites installed on your computer let's get started by creating a
00:06:07.599 folder somewhere on our computer perhaps in your home folder I'm going to create a folder
00:06:15.599 called how to host things on Google Cloud run
00:06:21.880 jobs and let's open this folder BS
00:06:28.400 code and and if I pop open the terminal built into vs code and take a look at where we are on
00:06:36.560 the file system you can see we are in this folder that we just created now let's create our Dev container if you're
00:06:43.840 unfamiliar with the term Dev container hold tight it's going to make sense in a few minutes in our empty folder let's
00:06:50.199 create the following folder in files let's create a folder called dodev container inside of this dodev container
00:06:56.319 folder let's create a file called Dev container Json and at the root of our
00:07:02.240 project folder let's create another file called dockerfile
00:07:07.520 dodev and let's populate the dev container. Json file with this content
00:07:13.280 and let's populate the docker file. deev with this content this code looks a bit hectic but
00:07:21.039 it's actually useful this code will build a little mini computer called a container that runs on top of our base
00:07:28.280 machine AKA our laptop or desktop or whatever we're using when we're done with this walkthrough we can simply kill
00:07:35.440 or delete this container and our base machine will be left clean from all of the software that we installed into the
00:07:42.280 Container in addition to helping us stay organized the use of containers is highly compatible with Cloud platforms
00:07:48.520 like AWS gcp and Azure so when we get to the point where we're deploying this
00:07:54.479 application to the cloud it'll make that process super easy to shed some light on what the files are doing the docker
00:08:01.080 file. deev configures our container and the dev container. Json file tells VSS code how to attach to our container when
00:08:07.240 we'd like to edit the files inside of it take a closer look at the docker file. deev and we can see we're installing
00:08:14.159 python we're installing git we're installing
00:08:20.240 gcloud this is going to allow us to speak to gcp from inside our container and we're also installing a Docker
00:08:27.080 client this is going to allow us to speak to the docker server running on our base machine from inside our
00:08:32.479 container FYI when you use a container for the purposes of developing software inside of it we call it a Dev container
00:08:40.719 later in this video when we ship our application to gcp we're going to make a second container we're going to refer to
00:08:46.440 that second container as our production container because our Dev container and our production container are going to be
00:08:52.160 so similar there's a high likelihood that our code will work exactly as it does in our development environment when
00:08:57.200 we run it in gcp in a nutshell using this approach is going to make shipping our code to the cloud very easy if none
00:09:03.600 of this makes sense don't worry about it let's move on we can interact with Docker completely from the command line
00:09:09.480 but Docker also comes with this tool called Docker desktop Docker desktop is a UI for interacting with
00:09:16.480 Docker and on my local Docker instance you can see at the moment I have no
00:09:21.519 containers and I have no images let's come back to our editor AKA vs Cod or
00:09:27.720 cursor whatever we're using and let's type these keystrokes shift command P
00:09:32.959 this will open up the command pallet as it's so-called and in the command pallet you should see an option if you've
00:09:39.160 installed the dev containers extension that says Dev containers reopen in container you can also search for it
00:09:45.519 let's select this option and see what
00:09:50.680 happens when you build a container from your Docker files the process will usually take a few seconds maybe a few
00:09:57.440 minutes it depends on how much software you're packing into the Container so it looks like the build process has
00:10:02.560 completed and let's come back to Docker desktop and see what things look like
00:10:08.680 you can see we now have a few images and we also have a container this is our Dev
00:10:18.200 container let's come back to vs code or whatever we're using and let's pop open the built-in terminal
00:10:25.880 and look at where we are on the file system and you can see now now we are in a folder at the root called code we are
00:10:33.959 no longer in the original folder we created moving forward we will be developing our application inside of
00:10:40.160 this Dev container let's quickly confirm all the software we'll need is installed in this Dev
00:10:46.880 container we have python we have git we have
00:10:53.959 gcloud and we have our Docker client so
00:11:00.040 everything's looking good let's save our progress in a remote repository on GitHub if I come over to my GitHub
00:11:09.959 account I will create a new repository
00:11:15.519 called how to host things on Google Cloud run jobs and click create
00:11:22.440 repository and there are times for creativity and this is not one of them so let's just follow these commands
00:11:29.040 right here let's initialize our local repository to be tracked with
00:11:36.519 Git let's create a commit so I'll save all of these
00:11:45.040 changes and I'm using get shortcuts that were outlined in the docker file. deev
00:11:51.839 and let's rename our Branch to be called main let's add our git remote OTE as
00:11:59.800 it's socalled this lets our local git project know where to push code to and then
00:12:08.040 let's push our code we can see our project has been
00:12:16.279 backed up if you have a Keen Eye you're thinking what just happened so long story short is whatever credentials were
00:12:22.079 authenticated to GitHub with on our base machine get forwarded to the dev container when it's launched here we are
00:12:27.880 in the dev container if I type git push we can see we're authenticated with
00:12:33.240 GitHub that's our remote in this scenario and if I run this same
00:12:39.440 command in this project folder on the host we can see we're authenticated as
00:12:46.040 well so on Mac there's this application called keychain access that stores
00:12:51.160 credentials for us when we authenticate with different systems I think the corresponding application on Windows would be credential manager on Linux it
00:12:58.000 would be lib Secret but anyways so here in the keychain access app we can see a
00:13:04.040 store credential for GitHub so if I delete this and try to authenticate with GitHub
00:13:15.440 again we can see we're prompted for our credentials again and then let's try it in the dev container so if I say get
00:13:23.680 push we're prompted for our credentials again here is how I suggest we authenticate with GitHub so here we are
00:13:30.760 on the page for our newly created repository if we come to our profile
00:13:36.079 settings there's an option that says developer settings you can see this
00:13:41.519 personal access tokens drop down get up has this newish feature called fine
00:13:47.560 grain tokens let's click on that and let's generate a new token we'll call
00:13:54.000 this token how to hostings on Google Cloud R jobs and let's restrict this
00:14:01.800 token to only be able to access the repository we just
00:14:08.079 created this [Music] one and if we open this repository permissions
00:14:13.880 dropdown let's add contents read and write
00:14:20.440 permissions and the only other permission will'll need is metadata
00:14:25.600 permission but I think this is always enabled by default and let's generate the token and we can use this token let's
00:14:33.519 copy it to authenticate with GitHub in a very controlled manner so if I perform
00:14:42.399 this git push command again it'll prompt for my username and if I provide that access
00:14:49.800 credential or that token rather now we're authenticated
00:14:55.199 again and if I come to the def container and try pushing
00:15:00.880 [Music] again we're authenticating the dev container as well so long story short is
00:15:07.880 your host machine or base machine credentials or authentication with Git
00:15:13.600 gets shared with a Dev container so we're probably not going to need this personal access token again from GitHub
00:15:20.880 but let's store it just in case we do need it so what I'll do is create a
00:15:26.600 another file at the root of our project call.
00:15:32.399 EMV and let's store this GitHub personal access token as it's called so I'll say
00:15:39.680 GitHub personal access token and then I'll paste it in here and let's also add a dog
00:15:49.440 ignore and make sure that we ignore this
00:15:54.839 EMV come over to this link and when you develop python
00:16:02.480 projects there's a whole host of files that you do not need to add to GitHub or git for that matter so let's add them
00:16:08.759 all at once right now and I think that does it
00:16:14.839 so let me save this so if you have any issues
00:16:20.959 authenticating with GitHub from the dev container as a backup you can just use a
00:16:26.800 terminal on your host machine so I will we'll see you in part [Music]
00:16:31.000 No text
00:16:32.600 two in part two we'll learn how to deploy a simple job to Google Cloud run
00:16:37.680 as we're starting from scratch let's create a new project in our gcp account
00:16:43.040 by coming over to console. cloud.google.com welcome it's going to load one of the
00:16:50.079 products in your account and if we click this drop down right here it'll open up a model that includes a button saying
00:16:57.360 new project let's click on that and create a project called how to host
00:17:04.039 teams on Google cloudon jobs let's click
00:17:11.119 create and all of the gcp related work that we will be doing will be done
00:17:16.839 inside of this project for organizational purposes after our project is created in gcp let's select
00:17:23.359 it and search for cloud run in this top search bar and select the op
00:17:29.400 that says Cloud run Cloud run is a managed service for running containers
00:17:34.880 on the cloud run page you'll see two tabs one that says services and one that says jobs services in this context are
00:17:42.039 long running applications like HTTP apis that need to be listening to the internet for requests jobs on the other
00:17:48.799 hand are for triggering scripts these scripts will release the resources needed to run them immediately upon
00:17:53.919 script completion or failure as this video covers Cloud run jobs let's run a simple job to get our feet wet first
00:18:00.600 let's authenticate with gcp in our Dev container by typing the gcloud init
00:18:08.919 command and this will take us through an offlow and I'll say yes I would like to
00:18:15.640 sign in and if I command click this link and copy it come over to
00:18:24.320 whichever browser tab or browser instance
00:18:29.520 I'm logged into gcp with and paste it into the URL bar I'll be able to select
00:18:36.640 my account and I have to give
00:18:44.280 consent and my password more consent and then I'm
00:18:50.159 presented with a oth code that I can copy and paste into the terminal that
00:18:57.919 kicked this whole off flow off and I'll be asked to select my project which is
00:19:05.840 three for me and now the dev container is authenticated with
00:19:12.080 gcp okay many g-cloud commands are going to ask us to reference our project ID so
00:19:17.640 let's create a variable for it so we don't have to constantly type it right and some g-cloud commands require us to
00:19:27.159 specify another ID identifier for our product which is called its product number you can find the product number
00:19:34.280 by coming over to the dashboard of our selected project
00:19:41.360 and you should see the product number displayed here let's copy
00:19:48.679 it and yeah trust me you're going to be very happy that you just did this so now
00:19:54.000 let's set up our project so that we can run Cloud run
00:19:59.200 jobs inside of it so by default this is the list of gcp apis that are enabled in
00:20:06.880 uh fresh out of the box project gcp has hundreds of apis and now let's
00:20:13.799 enable two more of them and the apis that we will enable will be
00:20:21.520 the cloud run API and the cloud build API and after that completes let's
00:20:29.919 list the enabled apis on our project and we can see that this list has grown by
00:20:35.880 two entries this next command will give the cloud run API in our project permissions
00:20:42.840 to talk to a number of other apis in our gcp account okay that takes care of all of
00:20:48.840 the permissions and apis we need to enable in order to run a simple Cloud run job so the high level overview of
00:20:55.280 what we're going to do for the remainder of part two is first first we're going to build a little application a very
00:21:01.280 simple application then second we're going to ship it to Cloud run jobs so our little application is going to
00:21:07.760 require six more files to be added to our
00:21:13.679 project these five and then we're going to have a
00:21:20.279 helpers folder that will hold one file and let's populate the main Pi file
00:21:30.279 with this content and the requirements.txt file with this content
00:21:38.919 and the proc file with this content the
00:21:44.919 docker file. prod with this content the
00:21:50.120 cloud bill. with this content and say hello.py
00:21:58.120 helper with this content as we can see a python Cloud run job project is really not that
00:22:03.760 different from other python projects so as usual let's install our
00:22:11.000 dependencies and that should make this import error go away if it doesn't go away try opening up the command pallet
00:22:19.360 and restarting the Python language server but that did fix this import
00:22:24.760 error and now let's run our
00:22:30.799 script and it works so we built a little application we tested it out now let's
00:22:36.679 ship it to Cloud run the left half of this diagram shows what we have done up till this point and the right half of it
00:22:44.200 shows what we're about to do deployment step number one will be to create a repository in Google artifact registry a
00:22:51.240 repository in this context is a place where we can store images when we build a Docker file we are left with what is
00:22:57.320 called an image an image in the context of Docker is a collection of files that defines all of the code and operating
00:23:03.440 system requirements needed to run a particular application if we recall to when we built the dev container we
00:23:10.000 remember seeing a few images and a container inside of the docker desktop
00:23:15.200 UI when this image holding all of the configuration of our Dev container was ran it left us with this container when
00:23:22.880 we build a Docker file it leaves us with an image and when we run an image holding all of the code and operating
00:23:29.159 system requirements of a particular application it leaves us with a container we are now going to build our
00:23:35.440 second container AKA our production container by building the docker file. PR into an image holding all of the code
00:23:41.720 and operating system requirements needed to run our application in Google Cloud run because our development container
00:23:47.039 and our production container are going to be so similar there's an extremely high likelihood that our little application will work exactly as it did
00:23:52.919 in our development container when we run it in Google Cloud run if we take a closer look at our Docker file. PR and
00:23:58.440 in our Docker file. deev we see the only difference between the two is the removal of a handful of tools in the
00:24:04.320 docker file. prod we don't need git we don't need g-cloud we don't need Docker these tools are not necessary when
00:24:10.600 running our application in production so now you understand why Docker is so useful when you take code that's written
00:24:16.120 on your computer and ship it to other computers without defining all of the operating system requirements it needs it increases the likelihood that it's
00:24:22.120 not going to work so what Docker does is package your code with all of its OS requirements so that when it's Shi to
00:24:28.760 other computers there's a higher likelihood that it will work finally now let's create an image repository in
00:24:34.679 Google artifact registry by entering this command but before we enter this command let's come over to the gcp
00:24:41.840 console and come over to the artifact registry page so we can compare the before and
00:24:48.320 after and now let's enter this command and when that completes let's come back
00:24:53.960 to the artifact registry page and reload it and now you can see we have an image
00:25:00.279 repo so for clarity an image repo is not the same thing as a git repo an image
00:25:06.000 repo is a place where we can store images and a git repo is a place where we can store code changes made to a
00:25:11.080 particular code base so now that we have this set up let's build our production image and store it in this repo called
00:25:18.440 repo for job one first we'll do this using Cloud build if we pop open the
00:25:23.840 cloud build. file we'll see a script with Two Steps step one one is building
00:25:29.200 the docker file. prod and step two is pushing the resulting image to the
00:25:34.480 repository we just created in artifact registry and the URLs of repositories in
00:25:40.200 Google artifact registry have to follow this specific format if they don't follow this format things will not work
00:25:47.200 and the last thing I'll mention is we can see that there is a colon at the end of the repository URL followed by a
00:25:54.279 string this is the tag of a particular image this is a way that we
00:25:59.799 can give a custom ID to each image that we store in a
00:26:07.600 particular repository the default tag is latest this hints to us that this
00:26:12.799 version of the image is the latest one and we're not going to be using this tag feature pretty much at all but it's
00:26:19.880 useful to know about and it's useful for QA and sometimes you'll use the gith has
00:26:26.120 to identify each version of a particular image this is useful for storing a history of all the versions of an
00:26:31.360 application Etc so anyways let me stop rambling and let's build our production
00:26:37.799 image and store it in the repository we just created by sending it to Cloud build with this
00:26:43.320 command while that's building I'll come back to the gcp console and you can see that inside of
00:26:51.240 our repository we currently have no images and when this script is
00:26:56.880 finished we should see an image inside of our repository okay the script finished in
00:27:03.640 Cloud build let me reload this page and now you can see we
00:27:09.240 have an image inside of our repository and second we'll do this with a Docker client inside of the dev container all
00:27:16.240 right this is what this looks like we have to build the docker file. prod and tag it with the appropriate image URL
00:27:21.840 format or repository URL format and notice how we're also including this
00:27:27.679 platform flag that reads Linux amd64 I'm guessing the hardware that powers Cloud run is provided by
00:27:34.399 AMD and we have to retrieve an access token from
00:27:41.480 gcp and then we log into artifact registry like
00:27:48.200 so so we provide this access token as
00:27:53.399 the password
00:28:02.960 and that worked and then we have to enter this command and when we push our
00:28:12.000 [Music] image should
00:28:17.440 work and it does now that we have our production image stored in a repository in Google
00:28:23.279 artifact registry let's run our first job ever
00:28:28.679 we finally made it back to Cloud run so let's come over to the cloud run
00:28:34.679 page and come over to the jobs Tab and what we're going to do is
00:28:40.720 register a job with Cloud run that uses the image that we stored in our repository as the application that will
00:28:47.640 get triggered when we trigger the job so here's what that looks like this is the command that will register a job in
00:28:54.039 Cloud run jobs here we specify the job's name first CL run job
00:28:59.679 ever and here is where we reference the image in artifact registry that we would
00:29:05.000 like to use as the application that gets triggered when we trigger the job so if
00:29:10.559 I enter this command and come back to the cloud run
00:29:15.720 page and that command finishes executing we can see we now have a job registered in Cloud run
00:29:22.399 jobs and here is how we trigger the job so we execute this command and
00:29:29.279 provide the job's name
00:29:34.840 and if we come over to the cloud run dashboard again and select the job we
00:29:42.440 can see the job's logs here and we should see the same exact output that we were seeing when we were running this
00:29:48.720 application in our Dev container and there we go we see the same logs that we
00:29:53.880 were seeing in the dev container so that's great we now know how to manually deploy containerized scripts to Cloud
00:29:59.640 run jobs next up we'll automate this deployment process using GitHub
00:30:05.490 [Music] actions we are now going to automate the deployment of our simple job using
00:30:06.000 No text
00:30:11.279 GitHub actions the way that we do this is by creating a folder at the root of our project called. GitHub and inside of
00:30:17.919 this. GitHub folder we're going to create another folder called workflows and inside of this workflows folder we're going to create a file called cicd
00:30:25.679 doyl here is the content that we will paste
00:30:31.600 into this cico file and by placing this emo file at this specific location of our project whenever we push to the main
00:30:38.840 branch of our GitHub repository this code inside of it will automatically get triggered if we look closely at the
00:30:44.880 cicdl script we can see it's requiring us to specify some GitHub
00:30:50.120 variables as well as a GitHub secret the way that we provide these
00:30:55.320 values is by coming over to our G repository and should see a tab that
00:31:03.360 says settings in the settings tab there is a option that says secrets and
00:31:09.320 variables and it has a sub option that says
00:31:15.200 actions on these two tabs is where we can provide our secrets and our
00:31:21.159 variables first I'll provide all of the variables one of the variables of our cicd script is going to be our project
00:31:29.480 ID and the next one will be our project
00:31:34.600 number and the next one will be the name of our job in Cloud
00:31:44.200 run and second let me show you how to generate the secret that we'll need so
00:31:50.000 if we come over to console. cloud.google.com
00:31:56.080 and make sure our product is selected if we come over to the IM am and admin
00:32:05.120 option and select the service accounts sub option
00:32:11.919 here is where we can create a service account which is a fancy way of saying a username and password that we give to an
00:32:18.240 application so that it has the permission to do what we want it to do so let's create a service
00:32:25.480 account and I'm going to call the service account how to hosting on Google
00:32:33.480 Cloud run jobs cicd service account
00:32:39.480 sa and we'll add a description so that we know what this is for we come back to
00:32:46.919 this a while from now done to the key now you might have
00:32:52.760 noticed that there was already a service account sitting in this list before we ever created a service account so by
00:32:58.639 default gcp creates this default compute service account as it's so-called and gives this service account to a number
00:33:04.720 of apis so that they have permissions to do what they need to do so now if we select the service account from this
00:33:11.559 list that we just created and come over to the Keys tab we'll see this drop-
00:33:17.320 down button that says add key let's create a new key we'll use the Json key
00:33:22.559 type c create and a file will be downlo to our
00:33:28.200 computer and the contents of this file will be our secret so let's copy the contents of
00:33:34.240 this downloaded Json file and come back to our GitHub repository and create a new secret I'll call it
00:33:42.440 gcp cicd SAA key then we'll paste
00:33:48.679 in our service account key add our
00:33:55.639 secret and then that takes care of setting all of the secrets and variables for our cicd script now we're ready to
00:34:01.880 test out our cicd automation with GitHub actions let's come over to the actions tab on
00:34:07.960 GitHub and we have nothing here at the moment
00:34:13.199 and let's come back to our project and let's push our latest
00:34:19.480 changes to GitHub and see what happens
00:34:41.918 okay so we need more permissions added to our
00:34:47.520 personal access token so let's come back to GitHub and come over to the settings
00:34:54.520 section and let's come over to the developer settings
00:35:00.680 option find the personal access tokens drop down come over to F grain tokens
00:35:07.040 and here's our personal access token and we need to add more
00:35:16.599 permissions okay so we need workflow
00:35:22.720 permissions and let's try to push again
00:35:28.200 all right that worked come over to the actions page and reload so as we can see
00:35:33.920 it failed and if we click on the
00:35:40.800 automation we can see that we're failing
00:35:46.200 because we're not able to upload images to artifact registry this is the command
00:35:53.839 that will grant our service account those permissions so
00:35:59.480 now we can re-trigger our cicd
00:36:08.440 Automation and it failed and it's more permission stuff
00:36:13.960 this is the command that will grant the next slew of permissions we need to give
00:36:20.640 to our service account and it looks like it worked
00:36:32.520 and there more permission stuff so this is the command that will give our service account the next FLW of
00:36:38.119 permissions it needs and that looked like it
00:36:47.440 worked our automation completed successfully so we're definitely moving in the right direction now what we're
00:36:52.760 going to do is check out the logs of the cloud run
00:36:58.440 job and we're going to make an update to our application and confirm in the logs
00:37:04.880 that our update gets propagated to the cloud run job hosted on Google so let's
00:37:10.960 test this out here is the command that will trigger our
00:37:17.720 job we can see that it got triggered again
00:37:24.079 right and we get more logs so so now what we're going to do is Let's Make a
00:37:30.680 update to our application instead of saying hello
00:37:38.400 let's you know say hello
00:37:44.960 daddies and let's save this
00:37:55.839 change push it and in GitHub on the actions tab of our
00:38:03.200 repository we see that another run of our automation is in
00:38:13.680 flight and after this has completed we're going to trigger our job again and we should
00:38:19.680 see this line in the application logs say hello
00:38:25.960 daddies all right so completed and now let's trigger our job
00:38:42.040 again and we see our job got triggered for a third time
00:38:47.760 and it just completed so we should have some more logs and indeed this log line got updated so have
00:38:57.240 te is working in part four we're going to learn how to automatically trigger our job on a regular schedule using
00:39:04.280 another gcp product called Cloud [Music]
00:39:08.000 No text
00:39:09.920 Schuler in order to use cloud Schuler we need to enable the cloud scheduler API
00:39:15.359 so let's do so by entering this
00:39:22.560 command and when that completes if we list out all of the enabled apis in our
00:39:28.920 project we should see an additional entry here we are Cloud schedule API is now enabled now we can create a Cron job
00:39:37.520 a Cron job for those who have never heard the term is a scheduled task that runs on a regular interval the way that
00:39:43.079 we Define the interval for a Cron job is with this expression format for example
00:39:48.359 this would be the expression for once a minute this will be the expression for every Monday at 9:00
00:39:53.880 a.m. this will be the expression for the first and 15th of each month at 2 p.m. and this would be the expression for
00:40:00.040 every 5 minutes between 8:00 a.m. and 10: a.m. here is the g-cloud command template for creating Crown jobs in gcp
00:40:06.560 with Cloud Schuler the only variable whose value we don't yet have is the service account so let's create a new
00:40:12.400 service account with a minimum needed permissions to trigger jobs in Cloud run and this time let's create the service account using the command line all right
00:40:19.839 here's how we create service accounts from the command line and now we need to add invoker
00:40:28.319 permissions for cloud run to this service account and this is how we do
00:40:35.440 so and if we list out all of the service accounts in our
00:40:43.000 project we see we have three now so in the gcloud command template for creating
00:40:48.280 cron jobs with Cloud Schuler let's replace the variables with the following values before we enter this command
00:40:54.880 though let's come back to the console and come over to the cloud Schuler
00:41:02.200 page and we currently see no Cloud Schuler jobs displayed so if we enter this command
00:41:12.560 now when it completes we should see a crown job registered in the
00:41:20.119 console and we do and if everything's working as
00:41:25.920 expected if we come to Cloud
00:41:30.960 run and take a look at the page for our
00:41:36.119 job we should see it getting triggered once a
00:41:41.640 minute yep you see
00:41:53.079 that so yeah as we can see everything's working
00:42:00.040 we see our Cron job listed as a trigger here on cloud run and our application
00:42:07.680 logs are also getting printed out each time the job gets triggered so this is fabulous we now know how to set up cron
00:42:15.720 jobs on Google Cloud run [Music]
00:42:20.000 No text
00:42:21.319 jobs now we're going to add in some AI let's update the requirements.txt to
00:42:27.240 contain the following thirdparty packages and let's update the main.py
00:42:33.720 file to contain the following contents and you can see a number of
00:42:39.680 import errors at the top so let's sort those out by creating the following
00:42:45.280 files let's create another helper file let's add folder for
00:42:54.400 storing the schema for this application we'll be
00:42:59.839 building and let's add a config
00:43:06.400 folder with a tasks. yo file
00:43:12.599 and an agents. file and let's
00:43:19.119 populate the helper and schema folder
00:43:29.680 and the agents. file and the tasks. emo
00:43:40.599 file and of course let's pip
00:43:48.720 install if we look closely at this config folder we can see we're creating a team of agents who are reporting the
00:43:54.559 latest news regarding Haiti this is what we're going to roll with for demonstration purposes and you can
00:44:01.839 easily tweak these prompts according to the niche you're interested in let's now
00:44:07.640 run this updated application and see what happens all right we get an error that
00:44:15.280 says missing open AI API Key by default
00:44:20.319 crew aai the multi-agent framework we're using uses open AI for powering llms it
00:44:25.839 supports other llms but as I mentioned openi is the one that it supports by default if you're new to all this agent
00:44:32.160 stuff here's a diagram that shows what I mean and in the context of this video an
00:44:37.599 agent is a virtual person and the llm acts as this virtual person's brain we
00:44:44.720 can get an openai API Key by coming over to platform. open.com and signing up
00:44:51.000 after you're signed up make sure to add some credits to your account open platform is pay per use it's like a gas
00:44:59.800 station and I suggest adding whatever the minimum allowed amount is because
00:45:06.119 the cost of what we'll be doing here is only going to be in the pennies after you have credits added to your account
00:45:12.400 come over to the dashboard API key section and create a
00:45:18.400 new API key call it whatever you want you can leave every option default
00:45:24.319 by the way and then copy provisioned API key
00:45:29.359 into your project by coming over to the EMV file and adding a new entry that
00:45:36.119 reads open AI API key equals then paste in the API
00:45:44.480 key and when that's all set up let's try running our application again and see what
00:45:54.200 happens it looks like it's working if we take a closer look at this config
00:45:59.800 code we can see we're creating two agents a manager agent and a reporter
00:46:05.599 agent and this is the task that we're assigning to these agents we would like
00:46:11.079 them to perform research across this list of websites and if we come to the main.py file online
00:46:19.760 56 the configuration gets tied together as of the time of recording creai lets
00:46:25.520 you run your agents in two mod modes sequential mode and hierarchical mode
00:46:30.920 sequential mode means that the agents are going to perform the tasks outlined in the task. yo file sequentially from
00:46:37.200 top to bottom one by one with sequential mode you have to map each task to the
00:46:42.520 agent you want to perform it in hierarchical mode which is what we're using we assign one of the agents in our
00:46:49.000 crew as the manager and we assign tasks to the manager the manager will automatically break up the task to be
00:46:55.319 assign it into subtasks and will automatically assign each subtask to the appropriate agents in the crew if you're
00:47:02.440 familiar with this agent stuff one way of thinking about it is the worker agents become tools of the manager agent
00:47:08.839 depending on the llm and other implementation details the reliability and reproducibility of running hierarchical mode agents can sometimes
00:47:15.680 be impressive and can sometimes be atrocious but for the job of synthesizing information across a number of websites I find hierarchical mode to
00:47:22.520 be a worthy match let's run this crew of Agents a few times to get a better for what it's
00:47:28.280 doing let's come over to the tasks. yo file and let's edit this list of
00:47:33.880 links to only have one and then let's run our crew if we
00:47:42.119 come back to the main.py file we can see that the crew will be spitting out its
00:47:48.200 results into a file called report. MD this file right here so let's wait till
00:47:54.880 the crew is finished running and let's see what what it spits out into this report. MD file all right it finished running and
00:48:02.720 let's open this up and we can see that we're getting news from the one website that we have
00:48:10.359 listed in the prompt all of these are coming from the same Source
00:48:16.760 now let's add the second website in this list so
00:48:22.559 if this is working as expected we should see news results from two
00:48:31.720 websites all right it finish running and you can see now we're getting news
00:48:37.559 results from two different websites right you can see in the sources The Source link
00:48:45.520 is coming from the two websites we have listed in the prompt all right just to make sure this is working
00:48:53.480 as expected let's add a third website to this list and have our agents
00:49:00.440 perform research on these three news outlets and when I say research what's
00:49:05.799 happening is the agents are instructed to load all of the text on each web page
00:49:12.520 and they're prompted to extract the most meaningful or the most relevant information given the current
00:49:19.240 date so here we are if this works we should see news results from three
00:49:26.079 separate sources all right so our crew finish
00:49:31.160 running
00:49:36.680 and yeah so this first result is coming from ha. Loop
00:49:43.960 news.com this second result is coming from the.com and this third result is coming
00:49:49.359 from Haitian times.com so things appear to be working
00:49:54.720 and I hope that gives you a good feel for what this little multi-agent
00:50:00.000 application is doing okay so using this report. MD file is useful for debugging
00:50:05.280 but we don't need to track it in git so let's add another entry to the git
00:50:13.839 ignore and now we're ready to move on to part six in part six we're going to send this
00:50:21.079 AI generated news report via email to a list of subscribers
00:50:26.490 [Music] next up we will integrate email into our
00:50:27.000 No text
00:50:32.720 application there are many email providers we could use but for demonstration purposes we will go with
00:50:38.240 mail gun I'm suggesting mail gun as I found their integration process to be straight forward but feel free to use
00:50:44.000 another email provider if you prefer anyways come over to sign up. Mail
00:50:49.359 gun.com sign up after you sign up you have to verify your account via an authorization code that you receive
00:50:55.640 either in your email inbox or on your phone after you complete the account verification process you can provision
00:51:01.240 an API key this API key is What will authenticate our application with mail gun's email API next let's come over to
00:51:09.079 the domains page and we can see that mail gun gives
00:51:14.559 us a free domain for testing we can send emails from this test domain to any
00:51:21.760 email address we list as an authorized recipient here to authorize a recipient
00:51:28.200 we enter the email here and save it and then the owner of the email will receive
00:51:33.920 a consent email that they'll have to agree to if they want to receive emails
00:51:39.200 from our test mail gun account after we authorize some email let's add some code
00:51:45.400 to our application to test out our mail gun integration so let's create a
00:51:52.640 file in the helpers folder called send email
00:51:57.960 and here is the code that we will populate this file
00:52:05.920 with and let's call this code
00:52:12.599 from the main.py file
00:52:18.200 here and we have to import this
00:52:24.319 Helper and for testing purposes is let's comment out all of the code except the send
00:52:32.079 email call and run
00:52:37.680 our application to see what
00:52:44.240 happens okay if we come to our inbox and refresh our inbox we see
00:52:50.839 nothing but if we come over to our spam folder
00:52:58.040 look at that we just received an email 12:08 a.m. 1208
00:53:04.280 a.m. in regards to this video if you don't mind emails being sent to spam skip ahead to part seven but if you'd
00:53:11.400 like the emails we sent to arrive in the inbox as expected here are the steps you'll need to take come over to the
00:53:18.240 mail gun domains page and add a particular subdomain of a domain you own
00:53:25.920 for example I used mail. wish bliss. link wish bliss. link is the domain
00:53:31.559 mail. wish bliss. link is the subdomain after you add a domain you'll
00:53:36.960 be presented with some DNS records that you need to add to your DNS settings here are what these mail gun
00:53:43.680 records look like in my Route 53 account for reference after you have your DNS
00:53:48.839 settings updated you can click this verify button to have mail gun verify
00:53:53.880 that we are indeed the owner of this domain and now when we send emails from our
00:53:59.880 verified domain they should arrive in our inbox as
00:54:18.960 expected voila if you have issues purchasing a domain or setting up DNS leave a comment
00:54:25.880 or I suggest just pasting detailed descriptions of the issues you run into into either Google or chat GPT setting
00:54:31.839 up a custom email domain is not too difficult but if you never done it before it can be a bit tricky if anyone
00:54:37.559 in the community knows of an easier way to set up emails for the purposes of this walkthr please leave a comment and
00:54:43.240 I'll pin it to the top of the comments let's move on to part [Music]
00:54:48.000 No text
00:54:49.640 seven we are now going to make most of the remaining changes that will move us towards the final form of our
00:54:54.760 application so pay attention closely first of all we do not want this AI
00:54:59.880 generated research report to be written to a file but instead would like it delivered to us via email so to do that
00:55:05.520 let's make this little change to this task
00:55:12.920 object Let's test this out so you see what it's
00:55:24.640 doing we can see that our crew has now generated a Json structured output of
00:55:30.280 the news report so what we can now do is combine the flexibility of llms with the
00:55:36.720 predictability of traditional programming to transform this Json structured output into the body of an
00:55:42.680 email to do that let's add a few more helper
00:55:53.680 functions and let's add this code to the format news for email helper function
00:56:01.799 and let's add this code to the is valid email heler
00:56:08.920 function and let's update the main.py file
00:56:14.839 onlines 71-74 and then let's import these
00:56:23.200 helpers finally let's update the send email
00:56:40.319 Helper and now if we test our application let's see what happens if it
00:56:46.720 works as expected we should receive an email with our AI generated news reports
00:56:57.319 all right our application just finished running and if we come over to our inbox we see our AI generated news
00:57:06.079 report and the links are working
00:57:15.200 too great we are now going to use another product in the gcp suite called
00:57:20.359 secret manager secret manager is a product specially designed for storing API keys secr and any other sensitive
00:57:27.559 data here is how we enable this API in our gcp
00:57:33.119 project and after that command completes if we list the enabled services in our gcp account we can see that this list
00:57:39.480 has been extended by one entry so this is how we would add the open AI API key
00:57:46.599 to secret manager you can see we're piping in the
00:57:51.839 API key into this g-cloud Secrets create command and this is the name of the secret in secret
00:57:59.000 manager and this is how we would pipe in the mail gun API key so that it's stored
00:58:04.880 in secret manager as well FYI here's how you update secret
00:58:12.520 values anyways the last thing that we need to do before we test this is make
00:58:19.400 sure that our default compute service account has the permissions to access
00:58:26.119 these secrets in secret manager so let's first run this command and then this
00:58:35.599 command once again for clarity what these commands are doing are giving Cloud run the ability to retrieve these
00:58:43.160 secrets from Secret manager when we run our application all right now we're ready to test this so let's come over to
00:58:49.520 the cd. yo file and come to the deploy step and let's add another
00:58:57.319 flag called set secrets and you can see that this flag is passing
00:59:03.640 in the environment variables for our API keys by referencing them in secret
00:59:10.480 manager so it's doing that for the open AI API key as well as the mail gun API
00:59:16.359 key so let's quickly come over to the get ignore same way that we ignored the
00:59:22.200 report. markdown file let's also ignore the report. Json
00:59:27.599 file this is only useful to us for debugging purposes
00:59:33.240 so that looks good so we
00:59:38.280 go say nearly
00:59:45.960 finished okay I'm actually glad this happened so the build
00:59:51.440 failed because we need to add some additional software into the Container
00:59:57.000 so we're using a multi-agent framework called creai creai has what are called
01:00:02.599 tools which are add-ons that you give to your agents that allow them to do things for example there's tools for browsing
01:00:08.760 the internet there's tools for accessing the files on your computer there's tools
01:00:14.039 for generating images these all come to you with crew AI so some of the tools
01:00:20.160 require some C++ libraries to be installed and we need to add these C++
01:00:26.200 libraries into our production container so we
01:00:31.319 will put this here build the central is going to
01:00:36.400 add some extra C++ libraries into the Container so let's
01:00:42.480 test this out and woo that worked let's trigger
01:00:49.480 our job in Cloud run to confirm we still get AI generated news delivered to us via email
01:00:57.760 okay our job got triggered
01:01:03.559 and now it's running and it was able to complete if we come to our inbox we do
01:01:11.799 indeed get our AI generated news report so that's great this application works
01:01:19.319 in our Dev container and it works in Cloud run so we're looking really good
01:01:25.200 before we wrap up part seven let's discuss a few of the flags available to us when running jobs in Cloud run so we
01:01:33.039 can see in the yaml config for our job that we have the ability to specify the
01:01:39.599 amount of memory allocated to each container when it runs a job the amount of retries the container is allowed to
01:01:46.359 make before the job is reported as failed to us the timeout seconds so this looks like 10 minutes timeout so what
01:01:54.279 we're going to do is twe twe the memory and tweak the max retries because agents are probabilistic
01:02:01.720 by Design they're always going to work differently every time I've seen them sometimes generate so much text to where
01:02:07.599 they consume all the memory allocated to them when they're ran in Cloud run jobs
01:02:12.720 so what we're going to do is double the amount of memory that is given to a cloud job container by default and we're
01:02:19.960 also going to increase the Max retries from 3 to 5 and here's how we'll tweak them we will come over to the deploy
01:02:27.119 command in our cicd script and add two more
01:02:36.760 flags all right that worked so let's quickly confirm that our configuration
01:02:43.599 got updated and yeah you can see we now are
01:02:48.720 at five Max retries and we have double the memory that we had before so moving
01:02:55.559 on next we are going to add in an amazing tool called Agent Ops agent Ops will
01:03:02.279 allow us to monitor our agents in a much more intuitive and simpler fashion than
01:03:08.240 digging through gcp you're going to need a tool like agent Ops when you have dozens or even hundreds of Agents
01:03:14.359 working for you so you get an overview of what they're all doing how much each of them is costing you Etc so I'll see
01:03:20.680 you in part [Music] eight the process for integrating with
01:03:22.000 No text
01:03:26.200 agent Ops is very similar to how we integrated with open AI first let's come over to the agent
01:03:31.680 Ops web app come over to app. aent ops. a and find the API Keys page I found it
01:03:39.880 in this drop down and let's create a new one let's
01:03:47.279 create a project called agents Master
01:03:52.880 Class and then let's copy the API key that was
01:04:00.319 created for us and we add it to our project by adding a new entry in the EMV
01:04:09.960 file that reads agent opscore aior key and we paste in the API
01:04:18.520 key that we copied from the agent Ops dashboard and then let's come over to the requirements.txt file and we need to
01:04:26.559 add the package for installing agent Ops and let's save this file and then pip
01:04:32.240 install as
01:04:38.760 usual and the final step of integrating agent Ops involves coming over to the
01:04:43.880 main.py file and towards the top of this file before you initialize your agents
01:04:51.000 add this bit of code and we also need
01:04:56.599 need import the OS package so if we run our
01:05:05.440 application we should see some information showing up
01:05:11.920 in the agent Ops dashboard and agent Ops offers this
01:05:19.319 overview dashboard as well as this drill down and
01:05:27.160 there we go so we're starting to see some data
01:05:32.680 come in all right we see our product manager agent our researcher
01:05:39.680 agent and our agents are still at work so let's see what the agent Ops
01:05:45.440 dashboard looks like when our agents are finished
01:05:52.359 and if we reload right we see some beautiful charts
01:05:57.559 giving us an overview of what happened when our agents were at
01:06:03.279 work on the right here we can see the details of what the llms produced and
01:06:11.680 ingested for each step of the overall session and we also see the
01:06:19.839 costs involved as well as all the versions of the libraries that were used
01:06:25.799 under the hood and this is fantastic
01:06:31.960 and this page gives us an overview of what just happened as well to set up our
01:06:37.720 agents in gcp AKA our production environment we must add the agent Ops
01:06:44.039 API key into secret manager and then give our default
01:06:50.079 compute service account permissions to access this agent Ops API
01:06:58.039 key and then we reference the agent Ops API key in secret
01:07:04.160 manager in our cicdl
01:07:15.599 script let's push these changes to GitHub
01:07:37.119 okay that worked and now let's trigger our agents in Cloud run and confirm that
01:07:47.000 they still work and that they are being tracked by agent Ops so here is the
01:07:53.440 command all right so our job got
01:08:04.000 triggered and it's running and let's come back to agent Ops
01:08:09.520 and here we are we see our
01:08:15.120 gcp agent session being tracked by agent Ops as well taking a look at what our
01:08:20.479 agents are doing via this dashboard is a lot more intuitive and straightforward
01:08:26.158 than digging through the gcp console we have now arrived at the end of this
01:08:31.198 incredible journey we are masters of agents and we are masters of Our
01:08:37.520 Fate to wrap things up let's do a few final
01:08:42.000 No text
01:08:43.120 things let's update our prompts to focus on a different Niche so Insurance
01:08:52.640 technology and instead of focusing our task on
01:09:00.560 Haiti insurance techology and instead of focusing on
01:09:07.198 these new sources let's focus on these
01:09:13.120 ones and let's also make the subscriber list a secret
01:09:22.080 so we don't dox whoever is receiving news reports from this application so
01:09:30.679 let's define the subscriber list via an environment variable for now you'll
01:09:36.600 probably want to do this with some sort of database but that's outside of the scope of this video
01:09:44.399 and let's turn that into an array like
01:09:51.520 so and let's create environment variable in secret
01:09:59.600 manager I'm just going to put one email for now but you would put a comma separated list of
01:10:05.760 emails and then of course we have to
01:10:11.280 give the default compute service account permissions to access this secret and
01:10:22.280 then we reference this Secret in our cicdl
01:10:33.239 script this is the final batch of
01:10:39.080 changes we now have our production grade
01:10:44.000 No text
01:10:45.000 application as promised here's how to tear down the gcp project and avoid
01:10:51.840 incurring charges so my suggested approach
01:10:59.320 is to delete all of the resources that were provisioned so here I'm deleting the
01:11:05.920 Cron job next I'm going to delete the cloud
01:11:11.520 run job then we'll delete the repository in artifact
01:11:17.880 registry then we'll delete the service
01:11:22.920 accounts then we'll delete the secrets in secret
01:11:28.320 manager and then we come to the gcp
01:11:34.430 [Music] console dashboard project
01:11:40.520 settings and shut down our project the reason why we have to
01:11:46.280 manually delete all of these resources is because with this shutdown policy
01:11:52.080 there'll be a 30-day grace period or billing period that's still in effect until all of the resources get shut down
01:11:59.159 I guess a good side of that is that if you accidentally shut down a project you have 30 days to change your mind and you
01:12:06.280 know disable the shutdown but from a billing standpoint if you have anything
01:12:11.400 that's costing you money you'll be build for you know another month after you
01:12:16.840 select the project for shutdown so I think that's everything namaste

