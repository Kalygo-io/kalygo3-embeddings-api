---
title: "How to build a Fastify API in 4 minutes ; )"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/rtx3EVLLnn8"
publish_date: "11-26-2022"
---

00:00:03.780 let's build this API from scratch
00:00:08.220 we are starting with a folder with a
00:00:10.500 readme in it
00:00:12.599 we add a DOT get ignore
00:00:16.199 we make this a node project by adding a
00:00:18.600 package.json file
00:00:22.740 we add a readme's folder for housing
00:00:24.600 information about each step of this
00:00:26.160 process
00:00:27.840 we install packages for the first time
00:00:29.580 that's why we see a package.log.json
00:00:31.740 file now we are installing typescript
00:00:33.600 packages we will be installing many more
00:00:35.460 packages as this proceeds
00:00:38.760 we configure the typescript compiler via
00:00:41.219 the tsconfig.json file
00:00:45.540 we add a source folder for housing all
00:00:48.239 of the application code
00:00:51.539 we add a vs code folder right now it has
00:00:54.180 a settings.json file in it this is how
00:00:56.340 we set up prettier to Auto format our
00:00:59.219 code
00:01:02.160 we add a nodemon.json file this is how
00:01:04.979 we set up our project to be compatible
00:01:07.320 with nodemon and the vs code debugger
00:01:12.000 we add a launch.json file this is also
00:01:15.000 for setting up our project to work with
00:01:17.159 the vs code debugger
00:01:20.640 we add all of the code for our
00:01:23.100 authentication API
00:01:28.320 we next add a underscore underscore
00:01:30.659 tests underscore underscore folder this
00:01:33.119 is where all of the Just tests will sit
00:01:35.220 we will not focus on just in this video
00:01:39.119 but just is cool too it depends on what
00:01:41.880 you're trying to do just might be more
00:01:43.979 appropriate but I think for most people
00:01:45.740 Postman is going to be more intuitive
00:01:48.000 and easier to pick up which is why I
00:01:50.280 have focused on it
00:01:55.320 we next add a DB module this is where
00:01:57.899 the DB connector will sit for storing
00:02:00.299 data into mongodb
00:02:04.439 The Next Step it doesn't look like
00:02:05.939 anything happened but if we go into the
00:02:07.979 package.json file we see that we have
00:02:09.780 installed
00:02:10.860 fastify cookie and fast defy JWT these
00:02:14.400 will power the authentication logic
00:02:17.879 we next add eslint this is a code linter
00:02:22.680 or code cleaner
00:02:24.420 this will remove unused variables remove
00:02:28.160 unused Imports Etc
00:02:34.860 we next add support for DOT EMV files
00:02:43.019 we then add the emails module we will
00:02:47.040 need to send emails for our
00:02:48.959 authentication API for example
00:02:50.580 verification emails or password reset
00:02:52.739 emails
00:02:54.060 I am using Amazon SES for this
00:02:59.580 next we do some refactoring
00:03:03.840 then we add the postman folder inside of
00:03:06.780 here we will put the tests that we will
00:03:09.720 build with the postman GUI in the
00:03:12.180 following section for The Following part
00:03:14.340 part two
00:03:17.640 next we add some utility scripts for
00:03:20.099 being able to run our Postman tests
00:03:22.140 either in parallel or in sequence
00:03:28.500 and finally in Step 20 we add some
00:03:31.680 documentation for how to do performance
00:03:34.500 or Benchmark testing
00:03:36.959 so hopefully that gives you a good feel
00:03:39.300 of what you're looking at and what the
00:03:42.060 code does and is
