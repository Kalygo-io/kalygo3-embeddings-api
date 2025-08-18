---
title: "How to leverage LLMs for writing technical documentation and unit tests"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/VtJKQHoyb2A"
publish_date: "9-17-2024"
---

00:00:00.399 and in this demo we will show how we can
00:00:03.080 use groups of llm Agents or swarms for
00:00:06.000 code generation we'll showcase some
00:00:08.679 amazing techniques that we can use for a
00:00:11.320 documentation writing and B automated
00:00:13.879 testing we will feature the use of
00:00:16.119 python and a little bit of node.js you
00:00:18.560 can adapt these techniques to other
00:00:20.080 programming languages and Frameworks
00:00:22.240 assuming the llm you're using was
00:00:23.800 trained on sufficient amounts of data
00:00:26.599 these examples were inspired by two
00:00:28.359 scripts found in the Kyo as swarms REO
00:00:31.160 on GitHub the first being the autod docs
00:00:34.239 script and the second being the auto
00:00:36.640 tests script first let's take a look at
00:00:39.320 how we can use adapted versions of this
00:00:41.840 autod doc
00:00:44.160 [Music]
00:00:45.920 script here we have the code for some
00:00:48.480 API powering some web application let's
00:00:51.960 now show how we can easily document this
00:00:53.960 code by leveraging
00:00:55.960 llms at the root of this project you can
00:00:58.440 see we've included an empty scripts
00:01:00.480 folder let's now add this amazing script
00:01:04.080 that is going to allow us to easily
00:01:05.840 document this codebase this script
00:01:08.680 allows us to list all of the files in
00:01:10.720 our project that we would like to
00:01:12.360 generate documentation for we have to
00:01:14.640 define the path for each file as well as
00:01:17.439 the name of the final generated
00:01:18.920 documentation file that will explain how
00:01:21.000 the code in the file works the type of
00:01:23.560 documentation we will be generating is
00:01:25.159 called markdown documentation markdown
00:01:28.200 documentation is compatible with many
00:01:30.360 popular documentation Site Builders like
00:01:32.880 for example docusaurus or make
00:01:36.439 docs here we can see that for each file
00:01:40.520 we are sending it in parallel to an llm
00:01:43.280 agent for
00:01:45.680 processing this is the prompt that we
00:01:48.040 use to define how each agent in our
00:01:52.280 swarm works you can see that we are
00:01:55.520 giving each agent the Persona of a
00:01:57.320 technical writer with Decades of
00:01:58.840 experience and that we're also including
00:02:00.960 our code as well as some contextual
00:02:03.360 information about the application in
00:02:05.360 which the code sits like for example the
00:02:07.560 overall application schema as well as
00:02:10.000 all of the routes on our API after each
00:02:12.959 agent has finished processing its file
00:02:15.640 we will write the final generated
00:02:17.040 markdown into a scratch folder at the
00:02:19.000 root of our project we can then copy
00:02:21.440 this Final Markdown into popular
00:02:23.200 documentation site systems like for
00:02:24.879 example docusaurus or make docs let's
00:02:28.080 see how this works first we run the
00:02:35.959 script second we generate a
00:02:38.840 documentation website using a
00:02:41.239 documentation website builder like for
00:02:43.159 example
00:02:45.159 docusaurus typescript all
00:02:50.040 day third we copy the generated markdown
00:02:53.120 files into the relevant areas of our
00:02:55.120 documentation website for docusaurus
00:02:57.519 this is the docs folder
00:03:01.159 and fourth we run the documentation
00:03:04.879 website and make sure it
00:03:10.640 works and here we see our
00:03:14.599 documentation and honestly for no effort
00:03:17.599 this looks amazing of course you're
00:03:20.239 going to have to refine this generated
00:03:22.040 content and massage how it looks on your
00:03:25.080 documentation site but as I said I think
00:03:28.400 this is an amazing technique for
00:03:29.840 generating
00:03:31.960 [Music]
00:03:33.599 documentation we will now show how you
00:03:35.599 can leverage multiple llm agents AKA
00:03:38.000 swarms for performing unit testing on
00:03:40.400 your applications in my experience
00:03:43.120 leveraging llms for this use case rarely
00:03:45.480 goes smoothly but I still find it worthy
00:03:47.680 of sharing with you as a huge
00:03:49.400 productivity boost we will be using this
00:03:52.360 fast API product for this demo and at
00:03:54.680 the root of this project we have a
00:03:56.720 scripts folder in which we can place
00:03:58.720 utility Scripts
00:04:00.799 let's add this gen tests script that was
00:04:04.519 adapted from the auto test script found
00:04:07.879 in the kyom Swarms repo on GitHub we can
00:04:12.400 see this script allows us to list
00:04:14.280 classes in our project for which we
00:04:15.959 would like to generate
00:04:17.478 tests each listed class will be sent in
00:04:21.040 parallel to an llm agent who will read
00:04:24.440 its source code and generate tests for
00:04:27.199 it that are compatible with the pi test
00:04:29.759 testing framework here is the prompt
00:04:32.199 that we're using to define the persona
00:04:34.280 for each agent in our swarm and you can
00:04:36.880 see we're giving each agent in our swarm
00:04:39.080 the Persona of an expert software
00:04:40.840 engineer specialized in writing tests
00:04:42.639 for python
00:04:43.840 codebases you can easily tweak this
00:04:46.080 prompt if python is not your preferred
00:04:48.720 language let's now run this gen test
00:04:51.320 script on the most core class of this
00:04:53.479 API that being the agent class wink
00:04:58.639 wink we can see that the llm has
00:05:01.919 generated some code that appears to be
00:05:04.280 compatible with the pest testing
00:05:06.240 framework let's flow through the process
00:05:08.720 of how an engineer would use this
00:05:10.520 generated testing file so you understand
00:05:12.960 the overall process being presented in
00:05:15.520 this video first you would copy this
00:05:18.080 testing file to the tests
00:05:21.639 folder at the root of the project this
00:05:24.960 has to do with how py test works next we
00:05:29.880 would take a look at this code before
00:05:31.680 running it to make sure it's not doing
00:05:33.639 anything dangerous quote unquote for
00:05:36.560 example it's not going to delete any
00:05:39.319 files on our computer or do something
00:05:41.520 weird and after auditing it we can run
00:05:45.199 it at this point we have two options of
00:05:47.800 what we can do option one we can go
00:05:51.000 through and delete all of the failing
00:05:53.039 tests and call it a day
00:06:01.479 or two we can go down the rabbit hole of
00:06:03.680 fixing all of the broken tests until
00:06:05.759 this test Suite works exactly how we
00:06:07.919 would like it to depending on the
00:06:09.960 nuances of your application I could see
00:06:12.120 how both approaches could be valid
