---
title: "💎 Ruby On Rails For Node Developers 🟢"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/Dpszcu3Rq24"
publish_date: "8-27-2022"
---

00:00:00.399 the title of this video is ruby on rails
00:00:03.760 for node developers first i will give a
00:00:06.879 high level overview of ruby and ruby on
00:00:09.120 rails
00:00:10.160 then we will build a demo app using ruby
00:00:13.200 on rails to get a feel for what it's
00:00:14.639 like then finally i will show you how to
00:00:16.880 deploy this app that we are going to
00:00:18.720 build to a docker container
00:00:22.800 so what is ruby ruby is a programming
00:00:25.519 language that was created by a japanese
00:00:27.760 guy by the name of yukihiro matsumoto
00:00:31.519 i hope i am pronouncing his name
00:00:33.200 correctly
00:00:34.320 a few years after this language came on
00:00:35.840 the scene it became quite popular
00:00:39.120 and it got picked up by this danish
00:00:41.840 programmer
00:00:42.960 by the name of david heinemeyer-hanson
00:00:45.200 that's him right there
00:00:47.440 david heinemeyer-hanson used ruby to
00:00:50.160 build his own web application framework
00:00:53.039 that has since grown to become what we
00:00:54.879 know as ruby on rails ruby on rails is
00:00:58.160 quite popular it was used to build the
00:01:00.719 early versions of twitter the early
00:01:02.879 versions of github and the early
00:01:04.959 versions of airbnb if i'm not mistaken
00:01:07.040 so it definitely has made its impact
00:01:09.360 here are the tenants or the doctrine
00:01:11.920 that has guided david heinemeyer-hanson
00:01:14.240 in the development of this web
00:01:15.600 application framework i'm not going to
00:01:17.200 go over all of these but i will
00:01:18.880 highlight two or three of these that i
00:01:20.320 like most so
00:01:22.400 ruby on rails is a web application
00:01:24.000 framework that is optimized for
00:01:26.400 programmer happiness thing definitely
00:01:28.400 like that one
00:01:29.759 it is one that exalts beautiful code
00:01:34.400 definitely like that one
00:01:36.240 and it is one
00:01:37.680 that pushes up a big tent this means
00:01:39.759 that the culture surrounding ruby on
00:01:42.000 rails is one that welcomes people who
00:01:44.560 are interested in learning about it
00:01:46.960 now let's jump into building this app
00:01:52.320 we will be building an api for a very
00:01:55.040 simple mailing list
00:01:57.360 this api will expose crud routes for one
00:02:00.399 model
00:02:01.360 and the data for this model will be
00:02:02.719 stored in a postgresql table with two
00:02:05.360 columns one column for emails and
00:02:07.840 another column for whether or not each
00:02:09.840 email is subscribed to the mailing list
00:02:13.200 you should be able to get this up and
00:02:14.480 running regardless of what your
00:02:15.840 environment happens to be but just for
00:02:17.440 reference my environment is mac os
00:02:20.239 version 12.4 and i had to install xcode
00:02:23.480 13.4.1 along with the 13.4.1 command
00:02:27.040 line tools to get this working
00:02:29.040 as i understand it xcode not only
00:02:31.120 installs an ide for developing iphone
00:02:33.440 apps but also installs certain necessary
00:02:36.640 c and c plus plus libraries that are
00:02:38.560 used by ruby on rails and ruby to work
00:02:42.080 after you have all of the prerequisites
00:02:44.400 taken care of you should be able to type
00:02:46.080 this command and check out your ruby
00:02:47.599 version
00:02:49.200 i am using ruby version 3.1.2
00:02:53.360 for the node developers you should be
00:02:55.360 familiar with a tool called nvm that
00:02:57.840 allows you to easily switch between what
00:02:59.840 node version you are using in your
00:03:01.440 environment
00:03:02.879 and nvm has a corresponding tool in the
00:03:05.840 ruby community called rvm and it works
00:03:08.400 with the almost identical api as nvm
00:03:11.519 does
00:03:13.200 you can use rvm to easily switch between
00:03:15.680 what ruby version you are using
00:03:19.120 after you have that all set up you can
00:03:20.959 type this command to generate a fresh
00:03:24.239 ruby on rails application you do not
00:03:26.879 have to type all of the ruby on rails
00:03:28.879 code out from scratch
00:03:30.720 that is the benefit of using a framework
00:03:34.000 let's take a look at the generated ruby
00:03:36.080 on rails application
00:03:38.000 for the node developers you should be
00:03:39.519 familiar with the package.json file
00:03:41.440 where you specify the third-party
00:03:42.879 libraries that are used by your node
00:03:44.400 apps
00:03:45.760 the corresponding file in the rails
00:03:47.599 world is the gem file this is where you
00:03:49.599 specify the third-party ruby libraries
00:03:52.080 or
00:03:52.879 gems that your rails applications will
00:03:54.799 be using along with the versions of the
00:03:56.720 gems that you want to use
00:03:58.480 in a high-level manner a rails
00:04:00.400 application can be described as a
00:04:01.840 server-side rendered mvc framework
00:04:05.040 mvc meaning models views controllers
00:04:08.640 models are where you specify the data
00:04:10.560 that your application will be dealing
00:04:11.840 with views are where you specify the
00:04:13.760 user interfaces for your application and
00:04:16.000 controllers are where you specify the
00:04:17.600 logic for the api endpoints that are
00:04:19.519 exposed by your rails app
00:04:22.240 there are many other files and folders
00:04:24.000 in a generated rails application and
00:04:25.759 they all do very specific things this is
00:04:27.840 part of the convention over
00:04:29.360 configuration tenant in the rails
00:04:30.880 doctrine that i showed you at the
00:04:32.080 beginning of this video
00:04:33.600 the value of convention over
00:04:35.360 configuration is threefold
00:04:38.160 first it prevents you from redeveloping
00:04:40.240 features that have already been
00:04:41.280 developed by somebody else in the rails
00:04:42.960 community
00:04:44.240 second by you reusing existing code it
00:04:46.800 means that the existing code gets more
00:04:48.880 testing and more use
00:04:50.960 meaning that the quality of each gem
00:04:53.520 becomes higher and finally it allows
00:04:55.919 developers to easily collaborate on
00:04:57.759 other rails projects
00:04:59.919 the api for this simple mailing list
00:05:02.479 will feature persistent data so for that
00:05:05.199 we will need a database
00:05:07.360 and i will spin up a database via a
00:05:10.639 docker container running a postgresql
00:05:13.280 image
00:05:14.320 this is the command that you will need
00:05:18.000 i have already ran this command
00:05:21.280 and
00:05:23.759 you can see
00:05:25.199 the database running
00:05:27.120 in docker here
00:05:30.720 right
00:05:32.880 so now we can continue configuring the
00:05:35.759 rails app to plug into the database
00:05:40.720 we can
00:05:42.880 add this configuration file to the
00:05:45.919 config slash database.yaml file
00:05:50.080 in order to
00:05:52.720 finish plugging in
00:05:55.280 the rails app to the database we just
00:05:57.199 spun up
00:06:09.440 that should do it and now
00:06:11.540 [Music]
00:06:12.720 you should be able to run
00:06:17.039 rail setup
00:06:19.600 and
00:06:20.639 it will
00:06:24.880 create the databases for using the rails
00:06:27.520 app in development mode and test mode
00:06:31.039 and
00:06:33.120 now we can continue by generating our
00:06:37.600 model right i was mentioning that the
00:06:39.680 model is where you specify the data that
00:06:42.160 your application will be dealing with
00:06:44.319 we want a member model
00:06:46.479 that has two fields an email field and a
00:06:49.039 subscribed field a true or false value
00:06:51.840 saying whether or not this email is
00:06:53.759 subscribed to our mailing list
00:06:56.400 let's generate
00:06:59.120 the model right
00:07:01.680 now you start to see some of the nice
00:07:03.199 things about rails right it does a lot
00:07:04.880 of work for you if you know how to use
00:07:06.880 it correctly
00:07:09.680 and after you specify your model you now
00:07:13.280 want to mirror
00:07:15.360 this data type in the database
00:07:18.080 and you do that
00:07:19.840 by running this command
00:07:23.199 right so now our database is set up to
00:07:26.000 store
00:07:26.960 the data that we have specified
00:07:29.360 remember that i said the logic for your
00:07:32.160 controllers is what gets triggered when
00:07:34.560 an api endpoint is hit on your rail
00:07:37.520 server when someone on the internet hits
00:07:40.000 one of the api endpoints or routes on
00:07:42.000 your rails api or server it will trigger
00:07:44.720 the logic in your controllers
00:07:48.240 so first let's check which routes we
00:07:50.319 have specified on this rails api or
00:07:53.520 server
00:07:57.199 right we can type rails routes to see
00:07:59.039 what routes we have defined this is
00:08:01.199 rails magic right
00:08:03.520 we have no routes but we can add routes
00:08:05.759 in this file so look what happens when
00:08:07.520 we add
00:08:08.560 this line of code
00:08:10.639 to the routes dot rb file
00:08:15.440 save and we retype this rails routes
00:08:18.080 command
00:08:19.199 all of a sudden we have all of these
00:08:20.479 routes right but now we need to define
00:08:22.080 the controllers
00:08:24.479 we can scaffold out the controllers with
00:08:26.479 this command
00:08:32.958 rails will generate the controller files
00:08:37.599 take a quick look
00:08:38.880 all right looks great
00:08:40.958 now i have a snippet
00:08:43.679 of all of the controller logic that i
00:08:45.440 want to test
00:08:48.160 you can copy and paste this snippet
00:08:59.600 we can run
00:09:01.680 server
00:09:04.000 and we can test
00:09:06.080 this route which should return a json
00:09:08.800 object with a key of foo that has a
00:09:11.360 value of bar
00:09:14.320 fubar fubar right
00:09:16.720 fubar
00:09:18.800 fantastic
00:09:22.240 let me quickly show you how to debug
00:09:26.080 in rails right so if i put a
00:09:29.279 debug statement here
00:09:32.000 look what happens when i hit the
00:09:33.680 endpoint
00:09:34.839 right sorry
00:09:37.120 debugger my bad debugger
00:09:40.800 right we got a debugging console here
00:09:43.680 and we can click c to continue
00:09:46.080 and we get our value back right
00:09:48.800 so that's how easy it is to
00:09:51.360 use debugging
00:09:52.800 let me show you the rails console
00:09:55.440 so you can enter the rails console
00:09:58.160 like so
00:09:59.440 or you can just type c for short
00:10:02.880 and this will spin up
00:10:04.800 a development environment for
00:10:06.800 interacting
00:10:08.079 with your application in various ways
00:10:10.399 it's mostly useful for getting data
00:10:14.399 for example
00:10:16.079 if i
00:10:17.600 load this
00:10:20.480 and then run this command
00:10:23.519 i can see all of the models that i have
00:10:26.079 defined in my application right
00:10:28.720 and i can
00:10:30.160 query the class for all of the member
00:10:32.399 data in the system
00:10:34.480 you can see that i've created one two
00:10:36.079 three right
00:10:38.480 i can create another one
00:10:40.240 like so
00:10:46.079 and now
00:10:48.160 i can
00:10:50.000 find individual records
00:10:57.360 like
00:10:58.320 so
00:11:01.360 right
00:11:02.959 so that's the gist of the console you
00:11:04.320 can use it for other things but it's
00:11:05.519 mostly useful for getting data from your
00:11:07.920 database
00:11:10.160 now
00:11:11.200 let's continue
00:11:15.440 i will paste in
00:11:17.519 some more snippets
00:11:22.240 for example
00:11:25.440 this is a catch-all error handler
00:11:28.399 for the controller controller inherits
00:11:32.079 from this class
00:11:34.959 so
00:11:36.959 i can copy
00:11:38.480 paste that into the application
00:11:40.079 controller
00:11:41.680 and then
00:11:43.120 wrap up
00:11:44.399 the controller logic for the members
00:11:46.720 controller so that we have
00:11:50.160 full
00:11:50.959 crud capability
00:11:53.040 on
00:11:54.079 the members model
00:11:56.639 so now i can test this in postman
00:12:00.720 i can
00:12:02.800 create
00:12:05.760 new members
00:12:08.639 and i can
00:12:10.800 query
00:12:12.880 for
00:12:14.480 the data
00:12:16.160 i can delete data
00:12:21.760 all right
00:12:23.040 five
00:12:25.920 four
00:12:29.519 three
00:12:33.600 two
00:12:35.680 so i should have only one record left
00:12:39.360 right
00:12:41.920 so all of the crud routes are defined
00:12:46.399 and
00:12:49.920 now
00:12:54.720 we will move on to this
00:12:57.680 where we do some validation
00:13:00.079 so
00:13:01.839 you can see
00:13:04.560 that if i want to
00:13:06.880 create a record
00:13:08.560 let's say that i create a record
00:13:11.040 with an invalid email
00:13:13.600 see it still goes through
00:13:15.360 that's not what we want
00:13:18.000 so
00:13:19.120 we will add some validation to the model
00:13:22.079 that's the controller we want the model
00:13:26.079 so if i
00:13:28.959 paste in these validations inside of
00:13:33.200 the model
00:13:34.720 and then i try to add another
00:13:38.399 record with an invalid email we now get
00:13:40.480 an error
00:13:41.839 right that's what we want
00:13:46.839 so now i will wrap this up by adding
00:13:50.800 some rate limiting and then quickly
00:13:53.440 deploying this to a docker container and
00:13:55.600 then that will be it
00:13:57.040 we need this
00:14:00.399 gem
00:14:03.600 to be added to the project this is like
00:14:05.839 installing
00:14:07.680 a new npm package
00:14:09.839 for the node folks
00:14:12.000 we find the gem file
00:14:16.320 and we can add it anywhere
00:14:19.040 i will add it here
00:14:21.760 and leave a little comment
00:14:24.720 for rate
00:14:26.160 limiting
00:14:28.959 and then
00:14:31.680 type bundle install
00:14:37.519 sounds very familiar doesn't it node
00:14:39.199 folks
00:14:42.480 then we add this file
00:14:44.800 initializers
00:14:48.720 rack attack
00:14:57.680 and then we paste in this content
00:15:09.360 all right so
00:15:11.360 each ip address is limited to five hits
00:15:14.560 on the api every 20 seconds
00:15:18.480 let's call
00:15:19.760 the get members endpoint
00:15:25.519 twice
00:15:26.959 three times four times five times
00:15:31.279 too many requests rate limited
00:15:36.160 let's
00:15:38.480 deploy this into a docker container
00:15:42.320 so
00:15:45.680 we have our
00:15:47.630 [Music]
00:15:49.240 database.yaml looking good okay so
00:15:54.240 here is
00:15:57.600 where we need to add
00:16:00.240 the docker file
00:16:12.800 all right just copying this jazz
00:16:19.360 and then
00:16:23.600 add docker compose.yaml
00:16:35.279 with
00:16:40.720 this content
00:16:48.560 this will all be included in the code
00:16:52.560 and finally we need to
00:16:55.279 create this file
00:16:58.000 and make it executable
00:17:20.079 and now
00:17:22.720 this should work
00:17:25.359 compose up
00:17:27.520 oops we need to do one last thing which
00:17:29.679 is add
00:17:31.440 the environment variable
00:17:34.559 for
00:17:36.799 docker container that will house
00:17:39.600 the rails api
00:18:05.919 right
00:18:07.440 the rails api works
00:18:10.559 just as it did before meaning we can
00:18:12.559 deploy this to kubernetes
00:18:14.400 or
00:18:15.200 fargate etc
