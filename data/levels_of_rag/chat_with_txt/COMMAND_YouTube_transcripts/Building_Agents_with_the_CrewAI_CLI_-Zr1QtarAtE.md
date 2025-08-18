---
title: "Building Agents with the CrewAI CLI"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/-Zr1QtarAtE"
publish_date: "10-7-2024"
---

00:00:00.000 No text
00:00:03.360 in this video we are going to build a crew of Agents using the crew AI command line interface or CLI after we build our
00:00:10.880 crew we're going to layer on a tool Called Agent Ops for monitoring them if you want to follow along you only need
00:00:16.440 two things installed on your computer Docker desktop and vs code Docker
00:00:21.480 desktop allows us to run these little mini computers on top of our actual computer AKA our laptop or desktop and
00:00:28.640 inside of these little mini computers called Dev containers we can experiment with new
00:00:33.760 software as you'll soon see using Dev containers for doing software development is a great way to stay
00:00:40.280 organized vs code on the other hand is a code editor think of VSS code AS
00:00:46.079 Microsoft Word but for viewing and editing code instead of documents after installing vs code
00:00:52.559 you'll also need to install two VSS code plugins or extensions namely the docker
00:00:58.600 extension and the def containers extension both Docker desktop and vs
00:01:04.040 code are free and offer support for Mac windows and Linux let me show you how I
00:01:09.600 installed them onto my Mac so you get a feel for how easy it was for me but if you run into issues I suggest leaving a
00:01:16.240 comment or pasting detailed descriptions of what you're running into into either Google or chat GPT here's how to
00:01:21.000 No text
00:01:22.799 download and install Docker desktop on Mac go to the official download page
00:01:28.520 download the appropriate version for me this is Apple silicone open the downloaded DMG
00:01:35.399 file and drag and drop the docker doapp icon into your applications folder I've
00:01:42.479 already done this so I'll click stop but that's it it's that easy and here's how
00:01:47.000 No text
00:01:48.399 to download and install vs code on Mac go to the official download page
00:01:54.479 download the appropriate version for me this is Apple silicone unzip the downloaded zip file and drag the visual
00:02:03.079 studio code. apppp icon into your applications folder I've already done this so I'll
00:02:09.878 click stop but that's it it's that easy after installing VSS code you'll need to
00:02:15.120 do one last thing open vs code and come over to the extensions Marketplace on
00:02:20.920 the side menu and you'll need to install two extensions a the docker extension you
00:02:28.200 can search for it in the search bar and once you find it in the panel you click on it and then you'll see these
00:02:35.360 buttons right here you can click to install it should only take one click it's that simple B you'll need the dev
00:02:43.159 containers extension you should see some buttons right here and you can just click to
00:02:49.040 install it super simple and that should be all the setup you need here we go
00:02:53.000 No text
00:02:55.040 from scratch AKA and empty project this is the first set of file files that we're going to add to this
00:03:01.360 empty project first we're going to add a folder by the name ofev
00:03:08.280 container inside of this folder we're going to place a file called Dev container.
00:03:15.560 Json and at the root of the project we're also going to create a file called
00:03:21.000 Docker file. deev these files are related to Docker
00:03:26.519 and we'll configure a little mini machine or Dev container that runs on top of our base machine this is the
00:03:33.080 content that we're going to use to populate these files this is what we'll paste into the dev container. Json
00:03:43.159 file let me expand this and here is the content we will
00:03:50.280 paste into the docker file.
00:03:57.519 deev these files will make sense shortly now that we have these files added let's
00:04:04.040 build or launch our mini computer or Dev container before we do that though let's
00:04:10.439 take a quick look at the docker desktop UI and we can notice there's no containers
00:04:15.440 running and let's also set up a timer so that we can time how long it takes to
00:04:21.478 build this Dev container so if we come back to vs code
00:04:27.400 here's how we launch the dev containers so we'll type shift command P that'll
00:04:33.199 open up this command pallet as it's soall and you'll find an option in the
00:04:38.800 menu called Dev containers reopen in container this menu option will only be
00:04:45.080 available if you have the dev containers extension installed we'll click enter then quickly
00:04:52.960 start the timer and let's see how long it takes
00:05:01.440 is that it took less than 10 seconds for me but
00:05:06.520 yeah I would say on average building a Dev container usually takes about like 1 minute maybe 3 minutes it depends on the
00:05:14.280 details of your machine and how much software you're packing into the dev container the next thing to notice
00:05:22.280 is in the docker desktop UI remember before we had no containers showing but
00:05:28.240 now you can see we do have a container showing let's run a little smoke test on this Dev container to make sure it
00:05:34.000 behaves as we expect so because crew AI is a python based tool let's make sure we have
00:05:40.880 python installed and we do python 3.12 this aligns with line one of the
00:05:48.600 docker file. deev this is configuring the mini machine to come installed with python
00:05:56.520 3.12 and let's make sure that we can execute python python code on this Dev
00:06:02.280 container let's create a little hello world script and see what happens when we pass
00:06:10.039 it to the python [Music] interpreter and that
00:06:15.919 works let's delete this main.py script because we won't need it moving
00:06:21.599 forward and the last little smoke test that we'll do is confirm the
00:06:27.759 location that we're in on the dev container and we can see that we're at the root of the file system in a folder
00:06:35.440 called code if we were to look at the root of the file system on our base machine we would see no folder called
00:06:43.240 code the mental model to keep in mind is that we have two machines running on our
00:06:48.360 computer we have the dev container and we have the base machine both of these
00:06:53.800 machines have independent file systems and are capable of having completely different software installed
00:07:00.080 moving forward we're going to be working in the dev container and once we're done with this
00:07:06.280 walkth through we're going to kill the dev container along with all the software that we install on it and our
00:07:12.479 base machine will be left clean now that we have a solid foundation let's install crew from the python package index AKA
00:07:14.000 No text
00:07:21.800 piie let's type this command pip install crew AI equals equals
00:07:27.759 0.671 this is the latest version as of the time of
00:07:36.360 recording after installing the crew AI package we can use the crew AI CLI like
00:07:46.759 so I don't know what's going on here but here is the crew AI CLI menu
00:07:56.520 and you can see the crew AI CLI offers command fans for doing
00:08:02.759 training for replaying sessions that you've had
00:08:08.080 with your crew and of particular note or importance to us there is this create
00:08:15.199 command for creating Crews so because we're going to be creating
00:08:21.280 a a claimed group of musicians to help us write a hit song Let's enter the
00:08:28.840 following command crew AI create crew hit music
00:08:34.320 only hit music only is the name of our project or crew this is customizable you
00:08:39.880 can put whatever you want here in the console we can see all of these generated files and folders and this is
00:08:47.440 great because using the CLI saves us time from having to create
00:08:52.880 all these files and folders manually ourselves and also note how all these
00:08:58.120 files and folders were created within this folder in our project these files that were
00:09:05.279 generated adhere to the guidelines of python poetry python poetry is a popular
00:09:13.440 python framework that has gained a lot of traction over the past few years the other thing to note is that if
00:09:21.800 we dig a Little Deeper we can see that we actually have a working crew called
00:09:28.640 the hit music only crew in this code and at the moment this crew
00:09:35.160 consists of a researcher agent and a reporting analyst
00:09:40.839 agent because all of these generated files were added in a subfolder of our
00:09:46.800 project route and not the project route itself we have a very minor technical
00:09:52.320 tweak that we have to perform and the way that we do this little tweak is by coming over to the
00:09:57.839 devc container. json5 and adjusting the workspace folder key
00:10:03.959 here is the updated value that we will specify we'll put the name of our
00:10:13.320 generated crew AI project and because this is an update to
00:10:20.600 the configuration of the dev container we actually have to rebuild the dev container as a reminder the specs of the
00:10:28.160 dev container are determined by the content we put inside of the dev container. Json and dockerfile dodev
00:10:34.920 files from step one there are a couple of ways that we can perform this rebuild
00:10:40.880 but for Simplicity we're going to do it like this let's come over to the docker
00:10:46.320 desktop UI stop our Dev
00:10:52.680 container and then delete it we might have been able to just delete it right away but anyways I chose
00:11:00.120 to shut it down first and then delete it so here we are deleting it right so if
00:11:05.160 you come back to vs code vs codes like what happened Dev container is no longer here
00:11:14.320 you know it's like an error right so anyways let's cancel this and close vs
00:11:20.600 code and the way we're going to reopen It Is by opening the project folder just
00:11:26.160 like we would open any other coding project with s code
00:11:31.959 so I'll open it on the command line but you can do this via the guey as
00:11:38.760 well but I'm going to navigate
00:11:44.279 to the project folder we've been working in then open this project folder with vs
00:11:50.839 code like [Music] so and because we placed this Dev
00:11:57.360 container. Json file in the appropriate Loc location vs code picks up that we
00:12:03.000 would like to open a Dev container and this is courtesy of the dev containers
00:12:08.160 vs code extension so that probably went away but there's a button on it you can click to
00:12:14.920 trigger the rebuild of the dev container but we can also trigger the rebuild by
00:12:20.600 going to the command pallet and selecting this option Dev containers reopen in container so we'll select that
00:12:31.560 and we should be directly in the Poetry project right and that is the case if we
00:12:39.760 come to the terminal on the dev container and check out where we are on the file system you can see we're no
00:12:47.040 longer in the code folder but we're in the code SL hitmusic only folder so the
00:12:52.560 reason why we did this is because we want VSS code to play nicely with our poetry project if we code opens at the
00:13:00.600 product route our POI product is nested one folder down so vs code has a process
00:13:06.440 when it launches where it tries to detect the type of project being opened and now it can detect that our product
00:13:13.040 is a python poetry product and it'll give us some extra nice to have features that will enhance our developer experience that's why we did this but
00:13:20.560 check this out let's open the crew AI CLI menu
00:13:25.680 again but what happened it's saying crew AI command not found but we installed it
00:13:32.480 right so what happened was when we rebuilt the dev container it lost some
00:13:39.680 of its state or it lost its state I should say so you can shut down and turn
00:13:45.079 on and shut down and turn on a Dev container and that will preserve its state but if you rebuild a Dev container
00:13:51.160 it will lose its state so now what we have to do is reinstall crew aai
00:14:02.040 FYI if we want to avoid reinstalling the QI package each time we rebuild the dev
00:14:09.199 container we can edit the docker file dodev but let's not worry about that for
00:14:16.120 now and move forward okay we're back in the hit music only subfolder right so
00:14:21.279 the present working directory is slode hitmusic only we're almost ready to run
00:14:26.600 the crew but we have to do one one last thing before we do so because this code
00:14:34.320 is based on the python poetry framework we have to run the standard poetry setup
00:14:40.720 or install process so let's time this just for
00:14:45.759 reference and the First Command we got to type or we got to enter rather is
00:14:54.320 this one then the second one is
00:15:00.120 poetry install let's see how long this
00:15:15.720 takes I think why this poetry setup process took so long was because this
00:15:22.279 generated cre AI project comes with tools and cre AI seems to have many
00:15:28.519 tools I looked on their website and they have tools for connecting to databases for scraping websites for searching
00:15:35.639 YouTube Etc if you're not familiar with the term tools in the context of agent
00:15:40.800 development tools are the Integrations made between our agents and the outside
00:15:45.920 world now let's run our
00:15:52.680 crew and then it looks like the crew started to run but then
00:15:59.040 error was thrown and we can see here the error is related to a missing API
00:16:04.160 key and to be exact a missing open AI
00:16:09.480 API key so believe it or not we're actually in really good shape so crew
00:16:15.319 aai by default uses open aai for powering the agents in a
00:16:21.240 crew crew AI supports other llms as well but like I said by default it uses open
00:16:27.440 AI before we we add our open AI API key to the project and fix this error though
00:16:33.519 let's recap what's happened up till this point first we started from scratch AKA
00:16:38.680 an empty folder we then set up a Dev container which is like a little mini computer that runs on top of our laptop
00:16:44.399 or desktop whatever we're using then we installed the crew aai package from piie
00:16:49.800 in order to use the crew AI CLI then we generated a crew aai project called hit
00:16:55.440 music only then we noticed how the generated project was placed into a subfolder and because we wanted our VSS
00:17:02.279 code Editor to play well with this generated poetry based project we had to adjust the configuration of our Dev
00:17:07.919 container to open the generated subfolder when launching so we edited the dev container. Json config and
00:17:13.640 rebuilt our Dev container after the new Dev container finished launching we were placed directly into the generated poetry
00:17:20.240 project which allowed VSS code to give us some extra nice to have development features like import inspection and
00:17:25.799 syntax highlighting then because our Dev container lock it state after being killed we had to reinstall the crew aai
00:17:32.320 package we then ran the standard poetry setup process AKA pip install poetry followed by poetry install and after the
00:17:39.320 Poetry setup process completed we ran our crew AI project and successfully launched our default crew of Agents
00:17:45.520 before they aired out due to missing access credentials when trying to connect to open AI I hope this makes
00:17:52.120 sense let's now move forward by adding an open AI API key to our project
00:17:58.000 No text
00:17:58.360 connecting a crew aai project with open aai is simple all we have to do is come over to platform.
00:18:05.000 open.com and sign up if this is a new account for you you will need to add some credits to your account open aai
00:18:12.080 system is usage based it's like a gas station so you will need some credits to use it you can always add more later so
00:18:19.039 I recommend adding the minimum amount and after you have that set up look for
00:18:25.280 the section that reads API keys I found it in the dashboard section right on the
00:18:31.159 sidebar there's this API Keys option and we can click this button here to open up
00:18:37.080 a little model for configuring some aspects of this API key let's just leave it default then click create secret key
00:18:44.640 and then we'll be given an API key that we can use to connect our crew aai project with the open AI platform the
00:18:51.000 way we add it to our project is like so inside of the Poetry project at the root
00:18:56.320 there is this EMV file let's make sure that this file includes a line that
00:19:01.440 reads in all caps open aior aior key
00:19:06.840 equals then we will paste in the value that we copied from open AI after we
00:19:12.320 have that set up let's run our crew again and hopefully everything works so
00:19:18.679 we'll type crew AI run and there goes the
00:19:26.600 researcher and this is the output generated by the
00:19:31.640 researcher and that output got fed into the analyst
00:19:37.320 and this is the final report generated by the analyst so no we were able to run our crew successfully so that's great
00:19:43.000 No text
00:19:44.039 let's now customize our crew by replacing the default agents and the default tasks that were given to us when
00:19:49.640 we generated the project we can do that by coming over to the source hit music
00:19:55.440 only or whatever your product's name is config folder and inside of the config folder we should see a file called
00:20:01.280 agents. yaml you can see by default we were given a researcher agent and a reporting
00:20:07.720 analyst agent let's replace these agents with
00:20:12.799 the following agents A songwriter agent and a producer
00:20:20.080 agent you can see for each of these agents we're outlining its role goal and
00:20:25.760 backstory in natural language and there are other properties that we can supply but if you want to learn about those go
00:20:32.440 to qi's documentation let's now update the tasks that will be assigned to our agents by coming over to the tasks. emo
00:20:39.400 file and you can see this is the list of tasks that was provided to us by the qai
00:20:46.919 CLI here we have a research task followed by a reporting task by default
00:20:53.480 kui will execute the tasks listed in this task. yo file sequentially from top to bottom
00:20:59.480 bottom so let's replace this content
00:21:04.919 with these tasks here you can see we're first going
00:21:10.440 to assign a songwriting task to the songwriter agent and after the output is generated
00:21:17.240 by this songwriter we will pass it and have a producing task executed by
00:21:24.520 the producer so what we're doing here is having a songwriter write lyrics and
00:21:30.080 beautiful Melodies and those raw ideas are getting passed to a producer who will compose it into a full song after
00:21:37.000 No text
00:21:37.760 saving these updates to our crew config we have to link it with the crew class in the crew. py file so let's come over
00:21:45.120 to the crew class and make the following updates our researcher agent has now
00:21:53.039 become a songwriter
00:22:00.400 and the reporting analyst agent has now become a
00:22:09.000 producer and let's also update the tasks that we're assigning to
00:22:24.039 them and the producer is also going to
00:22:29.360 Output a file so we can check out the final result the final song and let's update the name of this
00:22:37.760 file that it'll spit out results to to be called song. MD so zooming out what
00:22:44.799 we've done here is create a internationally acclaimed songwriting
00:22:51.440 Duo and task them with writing us a number one hit
00:22:57.240 song and and we're almost ready to run this crew and have a hit on our hands but before we do that let's do one more
00:23:03.840 thing that being adding in agent Ops so that in addition to having our song
00:23:09.120 written to a file on our local computer we have a backup in the cloud as well as
00:23:14.520 you know can see some metrics about how this crew generated the song Here's how
00:23:19.000 No text
00:23:20.640 easy it is to add agent Ops from monitoring our crew first come over to
00:23:25.840 app. aent ops. a and sign up if you haven't already they do have a free tier
00:23:32.159 and that should be enough for what we're doing here and after you're signed up come
00:23:37.520 over to the API key section and you should see a default API
00:23:45.720 key that you can copy and the way that we add this API key to our project is by
00:23:53.039 coming over to the EMV file at the root of the Poetry project and on a new line
00:23:59.559 let's add a entry that reads in all caps
00:24:04.919 agent opscore API uncore key equals then we'll paste in the API key that we
00:24:11.640 copied from the agent Ops dashboard after we have that set up let's come over to the main.py file and add a few
00:24:20.919 lines these are the lines that we're going to add make sure to add them at the top of the file
00:24:29.360 so that by the time you run your crew tracking is set up by agent Ops but
00:24:37.159 observe how VSS code is telling us there's an issue with this agent Ops import and we can read the warning that
00:24:43.640 says import agent Ops could not be resolved this is because we haven't yet installed the agent Ops package from
00:24:51.360 piie so let's do that now by entering this
00:24:56.880 command I should say before we enter this that because this project is a
00:25:02.240 poetry project we have to use the Poetry ad command if this was a plain old
00:25:07.520 python project we would type something or enter something along the lines of pip install agent
00:25:14.600 Ops right but because this is a poetry project we have to use the Poetry ad
00:25:19.640 command so let's enter this and see what
00:25:25.919 happens okay that looks good it looked like it worked and notice that even though we installed the Hops package
00:25:31.880 with the Poetry ad command correctly we still have this warning this is because by default VSS
00:25:39.120 code does not know where poetry installs packages and we can easily fix this
00:25:44.679 minor issue like so first we have to find out the location where poetry is
00:25:50.279 installing packages and we can do that by typing or entering poetry EMV info
00:25:58.799 and you can see this path is where packages are being
00:26:05.600 installed by poetry so let's copy this path value and once we have it copied we'll
00:26:14.000 enter the following keystrokes into vs code shift command P to open up the command pallet and let's look for an
00:26:21.360 option that reads python select interpreter let's select this option and
00:26:26.399 then you'll see a recommended option I think this might work but just to make sure it's the same
00:26:32.960 exact one that we just copied there's also an option that says enter interpreter path so we can select that
00:26:40.120 paste in the path value that we just copied click enter and that should fix the import
00:26:47.600 error and it does in summary we're using one tool AKA pip for installing the crew AI CLI and
00:26:55.000 we're using another tool AKA poetry for adding packages to the project generated by the crei CLI I know it's confusing
00:27:03.039 but welcome to python development finally let's run this crew and generate a hit song to review everything we've
00:27:04.000 No text
00:27:10.159 done up till this point the agents. yo file looks great the tasks. yo file looks
00:27:18.840 great the crew. py class looks
00:27:24.039 great and the main.py file looks
00:27:29.120 great as well but notice this this wouldn't affect us if we ran
00:27:34.360 it now but we like to be clean so crew AI allows you to pass in values
00:27:39.720 dynamically when running or kicking off your crew so if we wanted to use this
00:27:45.840 feature we would use it like so let's say for example we wanted to
00:27:50.880 customize the genre that our hit making Duo is specialized in so we could put
00:27:56.840 curly braces then specify some variable like this right and we would
00:28:04.640 also put this template variable over
00:28:11.799 here and we would pass in a dictionary that includes the value we
00:28:17.960 would like to replace that template variable with for example hip hop
00:28:23.799 right maybe country pop you get the point but we're not going to
00:28:30.399 use this feature for now we're going to keep it simple you can explore the more advanced features offered by crew AI
00:28:35.440 outside of this video and let's
00:28:40.559 delete all this inputs stuff we're not going to do any
00:28:47.159 training but let's just delete that right let's delete these template
00:28:53.840 variables from the agents. file and
00:28:59.120 now let's cook up this number one hit by
00:29:04.320 entering the crew AI run
00:29:15.480 command Okay agent Ops looks like it's tracking our crew and we can see that our songwriter is writing a song about
00:29:22.440 total accountability and here are the lyrics generated by the songwriter
00:29:28.960 and these lyrics are then going to be passed to the music producer who will
00:29:35.279 you know compose a song around them and that'll leave us with our number one
00:29:41.720 hit this looks very
00:29:46.840 usable and we have a copy of this hit in this song. MD file for
00:29:55.880 reference and if we click on on this link provided by agent
00:30:01.159 Ops we can see we also have a copy of this hit recorded to the agent Ops console
00:30:08.559 and we get some additional metrics too for example you can see that the songwriter
00:30:15.760 went first in this session and after the
00:30:22.080 songwriter was finished producer got to work here we can see the cost of
00:30:27.200 generating this song and yeah this is fantastic
00:30:32.559 so now let's actually make this song and see what it sounds [Music]
00:30:33.000 No text
00:30:44.240 like in the mirror I see the
00:30:52.279 truth every scar every bruise
00:31:01.159 all the choices that I've
00:31:07.840 made they shape the man that I've
00:31:15.320 become come on no more running no more games standing T I'll take the blame no
00:31:25.519 more running no more game Standing Tall I'll take the
00:31:32.399 BL I'm going to own it on my past every
00:31:38.000 moment every blast through the storm I'll stand so
00:31:44.480 proud accountability shout it loud I'll take the way I'll bear the
00:31:52.200 cost in this life I'm never lost to Freedom it starts within when
00:32:00.919 you own [Music] it okay so I did adapt the raw output
00:32:04.000 No text
00:32:09.240 let's take a look at the original version of the song so I did use the
00:32:15.080 name or I guess I will use the name I like the name right own it I did use the
00:32:20.919 same recommended BPM beats per minute that's like the tempo of the song how fast it is this core progression I did
00:32:29.519 use and the chorus I switched it up a
00:32:35.399 little bit so I adapted what was spit out here so here it had four chords and
00:32:43.080 what I did was similar but I did something a little different and I did use for the most
00:32:51.559 part the lyrics provided for the verse the melody to me didn't make much
00:32:57.360 sense I didn't like the way it fit with the chords so I just came up with a
00:33:03.000 Melody that sounded good to me and I didn't use these and I did use the
00:33:10.159 lyrics for the chorus I did adapt them a bit but yeah these Melodies that were
00:33:15.919 suggested for each line of the chorus I did not use those either and I only did the first verse
00:33:24.080 and one of the choruses to do the whole song would be a little bit you know a little bit much I think let's
00:33:29.000 No text
00:33:30.519 wrap this video up by doing one final thing let's copy this adapted version of
00:33:36.039 the output generated by our crew and send it to a service called sunno sunno
00:33:42.120 allows you to put in a prompt and it'll generate a song for you and you can see sunno generated two songs and let's see
00:33:50.120 what the first one sounds like
00:33:55.519 up get it right near it shows a face I'm know not afraid to fight dreams are
00:34:02.360 calling out my name I won't be the same stepping out to start my day time for
00:34:08.359 any shame running through the city streets Ry in my feet voes whisper my
00:34:15.159 name making me stars are shining my eyes is lighting up the feel the heartbe my
00:34:23.000 chest watch me as I Rise I will only it own it
00:34:28.440 Never Let It Fade breaking all the walls that life is there me I it itar me when
00:34:37.040 I say this is my life and I'll take it all the way
