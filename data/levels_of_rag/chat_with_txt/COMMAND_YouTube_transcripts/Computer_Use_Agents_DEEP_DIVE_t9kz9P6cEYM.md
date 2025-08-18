---
title: "Computer Use Agents DEEP DIVE"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/t9kz9P6cEYM"
publish_date: "11-19-2024"
---

00:00:00.160 in this two-part video we are going to
00:00:02.040 take a close look at the latest
00:00:03.439 developments in the realm of computer
00:00:05.640 use agents computer use agents are
00:00:08.440 exactly what you think they would be
00:00:10.120 they allow multimodal Transformers like
00:00:12.160 Cloud 3.5 Sonet or GPT 40 to execute
00:00:15.240 actions on your computer in the same
00:00:16.680 manner you would the multimodal aspect
00:00:19.080 is key as they rely on taking
00:00:20.840 screenshots to deduce context in
00:00:23.080 addition to deducing context from the
00:00:24.519 usual format of text my goal is to leave
00:00:27.240 you with a deep understanding of how
00:00:28.480 these agents work and highlight some of
00:00:30.480 the challenges they present in part one
00:00:33.160 we are going to show how to run a
00:00:34.440 computer use agent in a Docker container
00:00:37.360 part one's content should apply to
00:00:38.800 pretty much everybody as Docker
00:00:40.520 containers are supported on Mac windows
00:00:42.760 and Linux and in part two we're going to
00:00:45.440 show how to run a computer use agent
00:00:47.039 directly on a Mac general concepts
00:00:49.480 demoed in part two will apply to Windows
00:00:51.280 and Linux users but let's be real part
00:00:53.440 two's content is going to be of
00:00:54.559 particular interest to those who use Mac
00:00:55.960 based machines as I've not tested a
00:00:58.600 particular windows or Linux computer use
00:01:00.680 agent implementation I cannot safely
00:01:02.800 recommend one at this time along the way
00:01:05.400 we're also going to show how to set up
00:01:06.720 these agents for monitoring using a tool
00:01:08.520 called AG Ops the only prxs you'll need
00:01:11.560 to follow along are a a laptop or
00:01:13.680 desktop B Docker CVS code D familiarity
00:01:17.159 with Git e an anthropic API key and F an
00:01:20.000 agent Ops API key you can get Docker by
00:01:22.680 coming over to www.dr.com and then
00:01:25.479 downloading and installing the
00:01:26.640 appropriate version for your machine
00:01:28.320 this should be pretty painless leave a
00:01:29.960 comment if you have an issue installing
00:01:31.200 Docker you can get vs code by coming
00:01:33.560 over to code. visual studio.com and then
00:01:35.799 downloading and installing the
00:01:36.799 appropriate version for your machine
00:01:38.600 likewise this should be pretty painless
00:01:40.479 leave a comment if you have an issue
00:01:41.680 installing VSS code git is a free
00:01:44.240 software for sharing and editing code
00:01:45.960 with others on the internet and you can
00:01:47.320 install git a number of ways for example
00:01:49.759 you can come over to
00:01:58.840 g-.& Agents from GitHub the process for
00:02:02.320 getting an anthropic API key is very
00:02:04.000 similar to how you would provision an
00:02:05.240 open aai API key come over to console.
00:02:08.080 anthropic dcom and sign up purchase
00:02:10.919 credits and provision an API key just
00:02:14.120 like open aai anthropic pricing model is
00:02:16.040 usage based like a gas station so you
00:02:17.599 will need credits you can start with
00:02:19.319 whatever the minimum allowed amount is
00:02:20.800 and always purchase more credits later
00:02:22.120 if needed to get an agent Ops API key
00:02:24.760 come over to app. aent ops. and sign up
00:02:28.040 then come over to the API key section
00:02:30.400 and copy the default key or create a new
00:02:32.480 project to provision a non-default API
00:02:34.319 key for organizational purposes if you
00:02:35.840 like that takes care of all the PRX for
00:02:38.560 part one if you want to try out this
00:02:40.519 containerized computer use agent stuff
00:02:42.720 for yourself for the Mac users watching
00:02:45.080 I'm pretty sure you're excited to get to
00:02:46.480 part two but I highly recommend you
00:02:48.000 watch part one before watching part two
00:02:50.040 for additional context part two is going
00:02:52.319 to be simpler to set up than part one
00:02:54.440 but it comes with a tradeoff of
00:02:56.040 increased risk to your personal data
00:02:57.599 being either damaged or exposed
00:02:59.519 depending depending on what you ask the
00:03:00.720 agent to
00:03:01.400 [Music]
00:03:04.040 do here is a diagram showing how to set
00:03:06.920 up a containerized computer use agent
00:03:11.000 the benefit of running a computer use
00:03:12.560 agent inside of a container is that it
00:03:14.200 adds a layer of protection for the data
00:03:16.360 that sits on our base
00:03:18.319 machine yes this is not fullprof there
00:03:21.319 are crazy hacks that can cause the
00:03:23.519 software running in the container to
00:03:25.120 affect data on the base machine but the
00:03:27.280 whole premise and design of what a
00:03:29.159 container is does is intended to isolate
00:03:32.040 whatever software runs inside of the
00:03:33.319 container from the base machine itself
00:03:35.360 to make this a bit more practical if
00:03:37.599 there is some data that sits on our
00:03:39.400 machine that we'd like the computer use
00:03:41.840 agent that we run to access or work with
00:03:44.319 we'll need to explicitly copy that data
00:03:46.640 into the Container so that the agent can
00:03:49.040 work with and access it to give another
00:03:51.640 analogy running a computer use agent
00:03:54.120 inside of a container is sort of like
00:03:55.640 putting a dog inside of a pen yes the
00:03:58.519 dog can get over under around through
00:04:00.480 the pen the whole purpose of the pen
00:04:02.439 though is to confine the dog or to limit
00:04:04.159 the blast radius of how the dog can
00:04:05.560 affect its surrounding environment the
00:04:07.920 combined approach of being very
00:04:09.439 thoughtful about the tasks that you
00:04:10.879 assign to your computer use agents along
00:04:13.439 with running them in isolated or
00:04:15.519 containerized or virtualized
00:04:17.440 environments sums up the general
00:04:19.399 approach being presented here in part
00:04:20.839 one for how to run these types of Agents
00:04:23.120 with respect to data privacy and
00:04:24.800 protection okay let's give this
00:04:26.680 containerized computer use agent stuff a
00:04:29.360 spin
00:04:30.320 anthropics original computer use
00:04:32.240 implementation can be found at this
00:04:35.759 URL inside of this repo there's a number
00:04:38.919 of example projects this is the one that
00:04:41.560 we want let's click into it and let's
00:04:44.759 take a moment to read through this
00:04:47.320 cautionary message that welcomes US
00:04:50.759 computer use is a beta feature Please be
00:04:52.639 aware that computer use poses unique
00:04:54.280 risks that are distinct from standard
00:04:55.680 API features to minimize risks consider
00:04:58.680 one us using a dedicated virtual machine
00:05:00.800 or container two avoid giving the model
00:05:03.560 access to sensitive data three limit
00:05:06.199 internet access to a white list of
00:05:07.919 domains and for ask a human to confirm
00:05:10.639 decisions that may result in meaningful
00:05:12.000 real world consequences in some
00:05:14.199 circumstances Cloud will follow commands
00:05:16.000 found in content even if it conflicts
00:05:18.319 with the user's instructions for example
00:05:20.520 instructions on web pages may override
00:05:22.800 user instructions or cause claw to make
00:05:25.400 mistakes okay that was not reassuring at
00:05:28.000 all but let's move forward anyways
00:05:31.720 let's clone that
00:05:34.919 anthropic quick starts repo onto our
00:05:40.919 machine and let's enter the cloned or
00:05:46.479 copied project that we downloaded from
00:05:49.160 GitHub and here we see all of the
00:05:51.440 projects let's enter the computer use
00:05:53.479 demo
00:05:54.639 project and open it with vs code
00:06:03.160 in this project we see a
00:06:06.039 setup.sh script and let's run
00:06:10.800 that here you can see this
00:06:13.759 script is confirming we have Python and
00:06:19.000 cargo installed and it's going to set up
00:06:22.599 a virtual environment for us and
00:06:24.240 download all of the dependencies this
00:06:27.680 project needs Etc so let me be quiet and
00:06:31.240 let's just run
00:06:34.639 this all right so the setup script
00:06:39.440 finished and next up we have to
00:06:43.759 build the docker image that's going to
00:06:46.960 power our computer use
00:06:48.960 agent hopefully you're familiar with
00:06:50.840 Docker lingo so Docker file is to image
00:06:54.039 is to container as recipe is to frozen
00:06:58.599 food is to
00:07:00.080 meal as blueprint is to manufacture good
00:07:04.280 is to purchase good sort of abstract but
00:07:06.599 that's how it works Docker file image
00:07:09.919 container anyways next up we
00:07:13.840 will set our anthropic API key I
00:07:19.039 will censor
00:07:21.360 this so I don't
00:07:23.759 expose my key clear the terminal and now
00:07:28.000 we can run our Docker container that
00:07:29.840 will power our computer use
00:07:35.080 agent here we see the computer use agent
00:07:39.280 booting
00:07:40.479 up
00:07:42.120 and we see it's ready for us to load and
00:07:46.120 here we see the same image that we saw
00:07:49.440 on the architecture diagram of how to
00:07:51.919 set up a computer use agent in a Docker
00:07:55.440 container here is a simple web
00:07:58.840 application that consists of two panels
00:08:01.440 you see this left panel and this right
00:08:03.520 panel the left panel holds an iframe
00:08:06.560 powering a little chat application for
00:08:09.520 interacting with our computer use agent
00:08:12.599 and on the right is the desktop guey of
00:08:17.400 the computer that the agent is
00:08:21.280 controlling so if I say for example
00:08:25.599 hello right we see the agent taking
00:08:27.720 screenshots of the machine
00:08:31.279 and let's try this out now open the
00:08:36.360 calculator and add 2 +
00:08:45.399 2 right that's pretty incredible right
00:08:47.880 so next up let's show how to copy data
00:08:52.760 on our base machine into the Container
00:08:54.839 so that we can do some more practical
00:08:56.760 work okay here's the technique
00:09:00.279 so we are going to mount a folder in our
00:09:04.959 project into a folder in the container
00:09:08.560 and whatever files or data we add to
00:09:10.720 this folder will be visible to the agent
00:09:14.079 in the
00:09:14.959 container so for demonstration purposes
00:09:18.600 I am going
00:09:20.519 to add this service agreement
00:09:24.760 contract that I've used a few times over
00:09:27.800 the past year or two
00:09:30.279 it comes from Liam Atley I don't know if
00:09:32.160 you've ever heard of him he's a YouTuber
00:09:33.839 as well and what usually happens is a
00:09:37.360 perspective client will come into my
00:09:40.800 Pipeline and I'll need to draft a
00:09:43.560 proposal for them and customize a
00:09:46.240 template and let's see if the computer
00:09:50.120 use agent can do this work instead of me
00:09:52.480 doing it
00:09:53.720 so we've created the scratch folder and
00:09:58.680 this is how we
00:10:01.120 mount it to The
00:10:09.079 Container the computer use agent has
00:10:11.839 rebooted
00:10:14.360 and here's the
00:10:17.120 prompt that we're going to
00:10:19.839 send to have our
00:10:23.360 agent customize this service agreement
00:10:27.000 template for us
00:10:31.920 right and you can see the agent has
00:10:34.320 extracted the text from
00:10:36.639 this PDF
00:10:42.399 document all right so it extracted the
00:10:45.360 text and it
00:10:48.120 modified the service agreement with the
00:10:51.600 information I
00:10:53.160 provided and in the prompt I requested
00:10:55.959 the final document to be a PDF so
00:10:59.600 let's see if it does that part
00:11:08.959 two all right eventually it got pretty
00:11:12.480 much there it's not the best looking
00:11:17.440 agreement the original one is formatted
00:11:19.839 much more
00:11:22.040 nicely but you get a feel for how this
00:11:24.560 works now we're going to add in agent
00:11:26.600 Ops and rerun this PDF customization
00:11:28.720 request to confirm everything regarding
00:11:30.920 our agent's activity is being monitored
00:11:33.240 appropriately okay to do this first we
00:11:35.320 come over to the requirements.txt file
00:11:37.639 in the computer _ demo folder and add
00:11:42.200 another dependency that reads like
00:11:47.040 this agent Ops is still testing this
00:11:51.040 computer use agent tracking
00:11:53.279 feature that's why we have to import
00:11:56.120 this special unreleased version that was
00:11:57.839 authored by to NS AKA Romanian Raiden or
00:12:02.320 Romanian Ryden however you want to
00:12:03.839 pronounce it if and when this is
00:12:05.959 released you'll simply import it like
00:12:08.079 this but for now we have to go with this
00:12:10.519 the next thing that we have to do is
00:12:12.440 come over to the streamlit dopy file and
00:12:15.399 initialize agent Ops to track all of the
00:12:19.560 llm calls our application
00:12:23.120 makes and now we can
00:12:26.720 build our image again
00:12:32.440 and now we have to set our agent Ops API
00:12:36.680 key as a shell
00:12:42.120 variable this is the API key that you
00:12:44.560 copied from the agent Ops
00:12:50.120 console and now we can run our computer
00:12:54.959 use agent again with this command and
00:12:57.480 make sure you reference the agent Ops AP
00:13:02.560 key okay the computer use agent has
00:13:05.639 rebooted and we see agent Ops appears to
00:13:09.079 be
00:13:12.360 working and now if we send our agreement
00:13:17.320 customization prompt let's see if agent
00:13:21.399 Ops is indeed tracking all of the
00:13:24.920 agent's activity
00:13:39.000 okay so monitoring is set up and this is
00:13:43.120 an advisable way to use this system so
00:13:45.079 that you can audit what it does and you
00:13:49.000 know make sure you have a personal track
00:13:52.759 of everything that it's doing in case it
00:13:54.440 goes off the rails so to speak
00:14:00.040 we are now going to skirt cautiously on
00:14:02.079 the edge of Pandora's box-like territory
00:14:04.920 we are going to run a computer use agent
00:14:07.199 directly on a Mac while anthropics
00:14:09.600 original implementation was designed to
00:14:11.240 run the agent on an auntu machine within
00:14:13.560 a container a rather creative and
00:14:15.519 exceptional fellow by the name of DD
00:14:17.600 forked or customized this original
00:14:19.279 implementation so that the agent runs
00:14:21.360 directly in mac-based environments here
00:14:24.120 is a diagram outlining the design of
00:14:26.120 this Mac computer use agent and
00:14:28.079 immediately we can see that it's simpler
00:14:30.079 than the original containerized computer
00:14:32.560 use implementation that anthropic
00:14:34.399 published keep in mind that this Mac
00:14:36.720 computer use agent implementation will
00:14:38.639 periodically take screenshots of your
00:14:40.279 monitor and other snapshots of your
00:14:41.920 machine for upload to AWS and Google
00:14:44.639 Cloud as that's where I understand
00:14:45.880 anthropic models are currently
00:14:47.560 hosted after this data is uploaded to
00:14:49.959 these clouds it will be ran through
00:14:51.600 multiple layers of processing and
00:14:53.240 Analysis the exact details of which are
00:14:55.720 not publicly known secondly due to the
00:14:58.480 probabilistic nature of how multimodal
00:15:00.360 Transformers work they by their very
00:15:02.279 nature are capable of doing unexpected
00:15:04.199 things which in the realm of personal
00:15:05.600 data is not that reassuring let's say
00:15:08.120 for example that for maybe prompt
00:15:10.360 injection reasons one of the models
00:15:12.120 you're using were to edit or delete
00:15:14.079 sensitive data on your computer this
00:15:16.199 would be disastrous if backups were
00:15:17.920 never taken thirdly there is the
00:15:19.920 fundamental concern that we are
00:15:21.320 literally handing over control of our
00:15:23.079 computer to another entity yes there are
00:15:25.839 already many ways that big Tech players
00:15:27.920 and government actors are are monitoring
00:15:29.680 and restricting our personal computer
00:15:31.199 usage but this setup makes it explicit
00:15:33.839 you're literally handing over control to
00:15:35.480 another entity at the very least what
00:15:37.759 you should do is make sure that the
00:15:39.600 prompts you send to your computer use
00:15:41.399 agents include human in the loop steps
00:15:44.959 so that you stay involved at key points
00:15:47.319 in the tasks that you're assigning to
00:15:49.000 them that's the very least you can do in
00:15:51.199 order to make sure this doesn't have
00:15:52.440 unintended consequences you'll probably
00:15:54.000 need additional layers of protection
00:15:56.480 like virtualization you know fire walls
00:15:59.800 moving on now let's take this Mac
00:16:02.120 computer use agent for a spin DD's Mac
00:16:05.560 computer use implementation can be found
00:16:08.079 at this
00:16:10.360 URL and let's clone this project onto
00:16:14.800 our
00:16:18.399 computer and
00:16:20.319 enter the project and open it with vs
00:16:24.639 code and then there is this setup.sh
00:16:27.639 script that's going to inst install all
00:16:29.279 the requirements we need to run this
00:16:30.680 application on our computer for us so
00:16:33.560 let's run
00:16:39.120 it and
00:16:42.680 then let's create aemv file with these
00:16:49.199 variables
00:16:50.610 [Music]
00:16:51.880 and next up we want
00:16:56.440 to activate our virtual environment
00:17:03.000 and you can see our environment is
00:17:05.039 activated by this change in the
00:17:07.359 prompt I'm surprised it's not set up out
00:17:10.160 of the box for us but we have to rename
00:17:12.480 this streamlit dopy file to be called
00:17:14.919 streamlit app.py maybe try running it as
00:17:18.520 is see if it works for you but for me I
00:17:21.679 have to rename
00:17:23.280 it and then when I run this
00:17:27.839 application with this command it
00:17:30.799 hopefully should
00:17:34.600 work and it looks like it does let's run
00:17:38.679 a quick smoke test write the text Hello
00:17:41.520 to a new file called hello.txt on A's
00:17:43.559 desktop a is the Mac User running this
00:17:47.120 prompt
00:17:49.120 voila see
00:17:54.880 that
00:17:56.919 hello so that's immediately stop this
00:18:00.480 nonsense and shut this
00:18:03.760 down I'm pretty sure on this channel
00:18:06.000 that's as far as we're ever going to go
00:18:07.799 on this direct host-based computer use
00:18:10.320 agent setup stuff in conclusion computer
00:18:13.240 use agents are an amazing Innovation but
00:18:15.400 I'd highly advise against using them
00:18:17.840 without thoroughly assessing potential
00:18:19.880 consequences the trickiest thing about
00:18:21.840 them is that they can perform undesired
00:18:23.840 actions even after being explicitly
00:18:26.120 configured to not do so if you'd still
00:18:28.880 like to experiment with them however
00:18:30.720 here is the list of precautions to take
00:18:32.679 as a starting
00:18:35.360 point if you'd like to experiment with
00:18:37.480 developing the source code of a computer
00:18:38.880 use agent here is a fork of the original
00:18:40.919 anthropic implementation that I'm
00:18:42.280 particularly fond of it was authored by
00:18:44.520 tocns AKA Romanian Raiden and it
00:18:47.360 features outof the-box breakpoint
00:18:48.679 debugging and a more streamlined project
00:18:50.360 setup as a challenge to the community
00:18:52.640 one thing I'd love to see integrated
00:18:54.240 into this Fork would be the use of an
00:18:56.159 open-source multimodal model like for
00:18:58.400 example llama 3.2 multimodal 90b using a
00:19:02.480 locally hosted model for powering a
00:19:04.039 computer use agent is going to be a huge
00:19:06.120 step up from a data protection
00:19:07.520 standpoint finally in the description
00:19:09.720 for this video you should see a links
00:19:11.799 section I've included the links for
00:19:13.679 downloading git Docker and VSS code I've
00:19:16.880 also included the links for signing up
00:19:18.600 to anthropic and agent Ops plus I've
00:19:21.480 included a link for buying me a
00:19:23.039 metaphorical coffee and I've included an
00:19:26.080 affiliate link for buying this yoga ball
00:19:28.960 useful for stretching for bouncing for
00:19:33.720 exercise Etc wishing us all the highest
00:19:37.480 of blessings
