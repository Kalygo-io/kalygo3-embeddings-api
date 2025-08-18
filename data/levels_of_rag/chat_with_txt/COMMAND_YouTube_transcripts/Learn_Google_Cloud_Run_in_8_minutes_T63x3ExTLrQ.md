---
title: "Learn Google Cloud Run in 8 minutes"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/T63x3ExTLrQ"
publish_date: "5-4-2024"
---

00:00:00.000 No text
00:00:02.040 now we are going to build a simple fast
00:00:04.759 API remember the focus is not building
00:00:08.160 some crazy API here but rather learning
00:00:10.719 the overall process of how to deploy
00:00:12.759 dockerized containers to GCR let's
00:00:15.000 No text
00:00:16.239 install gcp CLI into our development
00:00:19.080 container here is the new version of the
00:00:22.359 development Docker file you can look
00:00:24.640 through it and see that it will install
00:00:27.240 gcloud which is gcps CLI this is a
00:00:30.439 change to the docker file so we will
00:00:32.159 need to rebuild our development
00:00:35.040 container how do we do that we type
00:00:38.520 shift command
00:00:40.120 p and reload
00:00:47.039 window after doing that you should see
00:00:49.399 the dev containers extension pick up
00:00:52.039 that there was a change to the docker
00:00:53.719 file you can click this rebuild button
00:00:58.830 [Music]
00:01:15.479 after our Dev container has been rebuilt
00:01:18.400 we can run this smoke test to confirm
00:01:20.400 that g-cloud has been
00:01:23.759 installed and indeed it has when you're
00:01:27.000 No text
00:01:27.159 working with gcp or any cloud provider
00:01:29.640 for that that part you want to stay
00:01:31.600 organized and the suggested technique
00:01:33.479 for doing this is to organize the
00:01:35.600 resources you provision into
00:01:38.680 projects so let's create a project and
00:01:43.280 we'll call it how to deploy a fast API
00:01:49.240 to GCR we'll click create and we'll be
00:01:53.119 able to easily delete all of the
00:01:54.719 resources we provision by simply
00:01:56.640 deleting this project so we'll select
00:01:59.479 this Pro project the next thing to do is
00:02:02.000 No text
00:02:03.039 authenticate our Dev container with our
00:02:07.320 gcp account so the way we do that is by
00:02:11.360 typing gcloud
00:02:16.840 init yes I would like to log
00:02:19.580 [Music]
00:02:22.080 in it'll spit out a URL that you can go
00:02:26.760 to in your browser
00:02:32.800 I will choose my
00:02:38.400 account
00:02:39.959 type my
00:02:43.640 password accept and then I will
00:02:46.120 eventually be given
00:02:49.440 a verification code that I can use to
00:02:53.440 authenticate my Dev container with gcp
00:02:56.720 then I will select the project that we
00:03:00.480 just
00:03:01.159 created and now our Dev container is set
00:03:05.599 up to provision resources so what we'll
00:03:09.400 do now is prepare our application to be
00:03:10.000 No text
00:03:11.319 deployed starting by first creating
00:03:13.280 what's called a repository in our gcp
00:03:16.080 account our repository is a place where
00:03:18.959 we can store our images to give you an
00:03:21.319 analogy if you're confused by this
00:03:22.640 Docker lingo the docker file is sort of
00:03:25.200 like a blueprint we will read the
00:03:27.159 instructions in our Docker file and that
00:03:28.720 will leave us with what's called an
00:03:30.159 image an image will be a Deployable
00:03:32.879 version or runnable version of our
00:03:34.760 application and all of the dependencies
00:03:36.519 it requires including its OS
00:03:38.360 requirements let's check out
00:03:41.640 our Google Cloud console and go over to
00:03:45.040 the artifact registry enable it for our
00:03:49.760 project this is where we will be storing
00:03:52.200 our images now let's create a repository
00:03:55.319 that will store all of the images for
00:03:57.599 the production versions of our
00:03:59.120 application here's how we do
00:04:03.840 this great and now if we reload the
00:04:07.799 console we see we have a repository
00:04:11.120 created in our artifact registry let's
00:04:14.400 now create another Docker file in our
00:04:16.000 No text
00:04:17.839 project this one will house the
00:04:20.079 instructions for how to build our
00:04:22.560 application for deployment purposes this
00:04:25.560 one is called Docker
00:04:27.639 file. and this is the content that we
00:04:31.360 will populate this file with now that we
00:04:34.520 have our production Docker file we will
00:04:35.000 No text
00:04:36.479 add one more file called Cloud build.
00:04:41.650 [Music]
00:04:45.600 yaml now we can issue a command to gcp
00:04:50.600 through the g-cloud CLI that will read
00:04:54.280 these instructions and build our Docker
00:04:57.440 file in a way that's compatible with the
00:05:00.160 GCR platform let's give this a spin what
00:05:04.680 you're seeing here is something you'll
00:05:06.639 see often when interacting with the gcp
00:05:09.800 platform they do their best to ask for
00:05:12.520 your consent before using new features
00:05:16.039 on their platform I will say yes so
00:05:20.160 let's pop over to our repository once
00:05:24.240 again I reload
00:05:27.479 this eventually we should see our image
00:05:31.080 stored here and there it is so once
00:05:33.639 again what we did was create another
00:05:36.479 Docker file that includes the
00:05:37.840 instructions for how to build our
00:05:39.600 application in a way that we can deploy
00:05:41.360 to GCR we also included a file called
00:05:44.600 Cloud Buu we ran the command to perform
00:05:48.000 our build on gcloud and when that
00:05:50.759 succeeded we now have an image in our
00:05:53.400 repository now that we have our
00:05:55.199 production image stored in a repository
00:05:57.000 No text
00:05:57.639 in Google artifact registry we can we
00:05:59.680 can issue a command to GCR to pull our
00:06:02.800 image from our repository and run it
00:06:06.039 let's see what that looks like first
00:06:07.800 what we'll do is create another file in
00:06:09.840 our project called service. yo and we
00:06:13.360 will populate this file with the
00:06:15.599 following
00:06:19.319 content and now let's run our
00:06:23.280 application in
00:06:25.880 GCR here is some more permission stuff
00:06:30.840 yes I would like to enable GCR on this
00:06:34.720 project and look at that we've been
00:06:36.960 given a URL that will allow us to
00:06:39.960 interact with the deployed version of
00:06:41.759 our application so if I command click
00:06:44.360 let's see what we
00:06:48.280 find this is expected because by default
00:06:52.280 GCR services are not publicly accessible
00:06:56.599 so we have to do one last thing update
00:06:57.000 No text
00:07:01.840 our service policy and the way we do
00:07:04.560 that is by creating another file in our
00:07:07.960 project and we will populate this
00:07:11.479 file with the following
00:07:14.400 content this is a policy that allows
00:07:17.680 anybody to invoke our service so let's
00:07:22.120 apply this policy to our
00:07:24.520 service and now when we load our
00:07:26.800 endpoint let's see what we find
00:07:33.080 we've come a long way you now know how
00:07:35.840 to take containers that run on your
00:07:37.560 local machine and deploy them to an
00:07:39.759 amazing managed service like GCR
