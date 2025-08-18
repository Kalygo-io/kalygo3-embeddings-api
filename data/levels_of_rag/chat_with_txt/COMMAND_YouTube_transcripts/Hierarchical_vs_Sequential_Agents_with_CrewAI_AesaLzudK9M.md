---
title: "Hierarchical Agents vs. Sequential Agents with CrewAI"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/AesaLzudK9M"
publish_date: "11-8-2024"
---

00:00:00.280 now we're going to add in some AI let's
00:00:03.199 update the requirements.txt to contain
00:00:05.480 the following thirdparty
00:00:09.120 packages and let's update the main.py
00:00:11.679 file to contain the following
00:00:15.640 contents and you can see a number of
00:00:17.640 import errors at the top so let's sort
00:00:20.240 those out by creating the following
00:00:23.279 files let's create another helper
00:00:27.720 file let's add
00:00:30.640 folder for
00:00:32.360 storing the schema for this application
00:00:35.160 we'll be
00:00:37.760 building
00:00:41.480 and let's add a config
00:00:44.320 folder with a tasks. yo
00:00:48.920 file
00:00:50.520 and an agents. yo
00:00:54.000 file and let's
00:00:57.039 populate the helper
00:01:01.120 and schema
00:01:06.640 folder and the agents.
00:01:12.280 file and the
00:01:14.560 tasks.
00:01:18.520 file and of course let's pip
00:01:26.640 install if we look closely at this
00:01:28.840 config folder we can see we're creating
00:01:30.600 a team of agents who are reporting the
00:01:32.520 latest news regarding
00:01:35.200 Haiti this is what we're going to roll
00:01:37.040 with for demonstration purposes and you
00:01:39.520 can easily tweak these prompts according
00:01:43.000 to the niche you're interested in let's
00:01:45.320 now run this updated application and see
00:01:47.920 what
00:01:49.880 happens all right we get an error that
00:01:53.240 says missing open AI API Key by default
00:01:58.280 crew AI the multi-agent framework we're
00:02:00.399 using uses open AI for powering llms it
00:02:03.759 supports other llms but as I mentioned
00:02:06.520 open AI is the one that it supports by
00:02:08.038 default if you're new to all this agent
00:02:10.080 stuff here's a diagram that shows what I
00:02:12.040 mean and in the context of this video an
00:02:15.480 agent is a virtual person and the llm
00:02:19.800 acts as this virtual person's brain we
00:02:22.640 can get an open AI API Key by coming
00:02:25.040 over to platform. open.com and signing
00:02:28.200 up after you're signed up make sure to
00:02:30.640 add some credits to your account open
00:02:33.120 AIS platform is payer use it's like a
00:02:36.920 gas
00:02:37.720 station and I suggest adding whatever
00:02:41.280 the minimum allowed amount is because
00:02:44.080 the cost of what we'll be doing here is
00:02:45.680 only going to be in the pennies after
00:02:48.200 you have credits added to your account
00:02:50.319 come over to the
00:02:52.120 dashboard API key section and create a
00:02:56.319 new API key call that whatever you want
00:03:00.920 you can leave every option default by
00:03:02.360 the
00:03:03.840 way and then copy the provisioned API
00:03:07.080 key into your project by coming over to
00:03:10.040 the EMV file and adding a new entry that
00:03:14.080 reads open
00:03:15.959 AI API key equals then paste in the API
00:03:22.400 key and when that's all set up let's try
00:03:24.760 running our application again and see
00:03:26.680 what happens
00:03:33.159 it looks like it's
00:03:34.799 working if we take a closer look at this
00:03:37.319 config code we can see we're creating
00:03:39.080 two agents a manager agent and a
00:03:42.280 reporter
00:03:43.519 agent and this is the task that we're
00:03:46.560 assigning to these agents we would like
00:03:49.000 them to perform research across this
00:03:51.080 list of websites and if we come to the
00:03:53.519 main.py file online
00:03:57.720 56 the configuration gets tied together
00:04:01.480 as of the time of recording crei lets
00:04:03.480 you run your agents in two modes
00:04:05.760 sequential mode and hierarchical mode
00:04:08.879 sequential mode means that the agents
00:04:10.760 are going to perform the tasks outlined
00:04:12.599 in the tasks. yo file sequentially from
00:04:15.120 top to bottom one by one with sequential
00:04:17.839 mode you have to map each task to the
00:04:20.478 agent you want to perform it in
00:04:23.120 hierarchical mode which is what we're
00:04:24.600 using we assign one of the agents in our
00:04:26.960 crew as the manager and we assign tasks
00:04:29.400 to the the manager the manager will
00:04:31.680 automatically break up the task to be
00:04:33.240 assigned into subtasks and will
00:04:35.360 automatically assign each subtask to the
00:04:37.800 appropriate agents in the crew if you're
00:04:40.360 familiar with this agent stuff one way
00:04:41.840 of thinking about it is the worker
00:04:43.600 agents become tools of the manager
00:04:45.759 agents depending on the llm and other
00:04:48.280 implementation details the reliability
00:04:50.440 and reproducibility of running
00:04:51.720 hierarchical mode agents can sometimes
00:04:53.680 be impressive and can sometimes be
00:04:55.160 atrocious but for the job of
00:04:56.960 synthesizing information across a number
00:04:58.440 of websites I find hierarchical mode to
00:05:00.440 be a worthy match let's run this crew of
00:05:03.240 Agents a few times to get a better feel
00:05:04.880 for what it's
00:05:06.199 doing let's come over to the tasks. yo
00:05:08.880 file and let's edit this list of
00:05:11.680 links to only have
00:05:14.600 one and then let's run our crew if we
00:05:20.039 come back to the main.py file we can see
00:05:22.479 that the crew will be spitting out its
00:05:26.120 results into a file called report. MD
00:05:29.880 this file right here so let's wait till
00:05:32.800 the crew has finished running and let's
00:05:34.240 see what it spits out into this report.
00:05:36.360 MD
00:05:37.600 file all right it finished running and
00:05:40.639 let's open this up and we can see that
00:05:42.880 we're getting
00:05:44.680 news from the one website that we have
00:05:48.280 listed in the
00:05:49.720 prompt all of these are coming from the
00:05:51.759 same Source
00:05:54.680 now let's
00:05:57.240 add the second website in this list so
00:06:00.479 if this is working as expected we should
00:06:02.600 see news results from two
00:06:09.680 websites all right it finish running and
00:06:13.520 you can see now we're getting news
00:06:15.520 results from two different websites
00:06:18.960 right you can see in the
00:06:20.440 sources The Source link
00:06:23.479 is coming from the two websites we have
00:06:26.039 listed in the prompt all
00:06:28.280 right just to make sure this is working
00:06:31.400 as expected let's add a
00:06:34.599 third website to this list and have our
00:06:38.039 agents perform research on these three
00:06:39.960 news outlets and when I say research
00:06:43.479 what's happening is the agents are
00:06:45.639 instructed to load all of the text on
00:06:48.560 each web page and they're prompted to
00:06:52.000 extract the most meaningful or the most
00:06:54.680 relevant information given the current
00:06:57.160 date so here we are if this works we
00:07:00.919 should see news results from three
00:07:04.080 separate
00:07:05.720 sources all right so our crew finish
00:07:09.120 running
00:07:14.479 and yeah so this
00:07:18.000 first result is coming from hai. Loop
00:07:21.879 news.com this second result is coming
00:07:24.160 from
00:07:25.080 l.com and this third result is coming
00:07:27.319 from Haitian times.com
00:07:29.960 so things appear to be working and I
00:07:33.199 hope that gives you a good feel for what
00:07:36.120 this little multiagent application is
00:07:38.759 doing okay so using this report. MD file
00:07:41.879 is useful for debugging but we don't
00:07:43.800 need to track it in git so let's add
00:07:48.560 another entry to the git
00:07:51.759 ignore
00:07:54.000 and now we're ready to move on to part
00:07:56.360 six in part six we're going to send this
00:07:58.960 AI generated news report via email to a
00:08:02.240 list of subscribers
