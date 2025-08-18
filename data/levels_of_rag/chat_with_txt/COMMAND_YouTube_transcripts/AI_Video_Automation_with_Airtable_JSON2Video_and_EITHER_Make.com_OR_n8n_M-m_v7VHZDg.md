---
title: "AI Video Automation with Airtable, JSON2Video and EITHER Make.com OR n8n"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/M-m_v7VHZDg"
publish_date: "5-10-2025"
---

00:00:00.000 No text
00:00:01.760 we are now going to implement one simple AI automation but we are going to implement it two times first we're going
00:00:09.440 to implement it with make.com and then second we're going to implement it with N8N the AI automation we are going to
00:00:17.119 build will produce short form narrated videos that you can use for marketing orformational purposes you should be
00:00:24.160 able to follow along for free as all of the tools we'll be using are either premium or have some sort of free trial
00:00:31.039 but in the case that you've already experimented with some or all of these tools you might need to dish out some
00:00:36.320 money or get creative with using alternate emails here is the complete list of
00:00:41.440 platforms we will be combining in this walkthrough in part A we're going to be using make.com if you're following along
00:00:47.680 the free tier should work air Table if you're following along the free tier should work as well json to video json
00:00:54.480 to video comes with some free credits when you sign up but afterwards will be about 50 bucks for each subsequent batch of credits you'll need and we're also
00:01:00.879 going to be using ChatGBT and Pixels chatgbt has a free tier with limited messages so use your messages wisely and
00:01:08.400 Pixels is a website that we can use to download stock photography in part B we're going to be using NAN nad comes
00:01:15.680 with a twoe free trial when you sign up and afterwards will be 40 bucks per month air table which we've previously
00:01:21.520 explained and JSON to video which we've previously explained we're not going to need Chad GBT and pixels for part B
00:01:28.080 because we're going to reuse the outputs from part A and part B we're going to be starting from scratch so hopefully no
00:01:34.000 questions are left unanswered but if you have questions leave a comment and I've also linked a GitHub repo with all of
00:01:40.079 the automations pre-made or pre-built and you can use those to cut straight to the chase if you want to skip all the
00:01:46.040 fluff let's go honeys for step one of part A we are going to
00:01:47.000 No text
00:01:52.079 be creating an Air Table account if you've ever used Google Sheets or Microsoft Excel then you're going to pick up Air Table super quick at its
00:01:58.880 heart Air Table is nothing more than a fancy spreadsheet or I should say at least in the way that we're going to be using it today once you create an Air
00:02:05.600 Table account you should see something like this in your dashboard the way that data is organized in Air Table is like
00:02:11.200 so first you have your workspaces within your workspaces you have your bases or
00:02:16.800 databases within your bases you have your tables which are fancy spreadsheets
00:02:22.239 and then within your tables you have records each row of each table is a record that's where you store your data
00:02:28.640 let's create a new workspace in our Air Table account i'm going to call this workspace make or
00:02:36.760 n and then within this workspace let's create a base and when you're creating a
00:02:43.680 fresh base it gives you these two options which is a bit confusing but we'll click start from scratch and this
00:02:50.239 creates a base for us that we can rename here i'll call
00:02:55.480 this video automation let's rename the default
00:02:59.000 No text
00:03:03.120 table that was created for us we're going to rename this table we can do that by I think clicking this dropdown
00:03:10.959 then you see it has this option that says rename table and we're going to call
00:03:16.040 this script you can call this stuff whatever you want by the way i'm just choosing
00:03:22.159 names that are intuitive to me so let's save that and now that we have all that
00:03:28.159 set up let's populate this table with some records or some data and this table
00:03:33.280 has five columns and we don't want these five columns so these would be like the top
00:03:40.879 row of your Google sheet to give you some framework if you're familiar with
00:03:46.879 Google Sheets so here we can click this and edit this field and the first field
00:03:55.120 we're going to call order and in most spreadsheets you can
00:04:01.360 store whatever type of data you want in each cell of your spreadsheet or your
00:04:07.040 table and in Air Table you can restrict the type of value that's in each column
00:04:14.560 and depending on what you're trying to do that could be useful or annoying in our case for what we're doing here it's
00:04:21.680 going to be useful so let's go with a number for the order and we do not want
00:04:31.360 our numbers to have any decimal places and you can leave all this stuff as it
00:04:37.919 is you can always change it later great we're going to edit this
00:04:44.560 second column and this second column is going to be
00:04:49.880 line and we'll make this we'll make it a single line text
00:04:56.560 instead of a long text or multi-line text as mentioned we can always change this later and we'll save that and the
00:05:04.479 final column that we're going to go with for now is going to be
00:05:10.680 photo and this will be uh attachment or an
00:05:17.600 attachment excuse me and let's save that and we can edit all this stuff as
00:05:23.120 mentioned let's delete this fourth column
00:05:28.199 and we could have renamed this one and kept it but anyways let's delete this
00:05:33.360 column and this is going to be the table structure that we're going to go with so
00:05:37.000 No text
00:05:39.520 let's add each line of our script right
00:05:45.160 so let me close this out so you can type stuff in directly here and then if you
00:05:51.960 doubleclick on a row it might expand it or excuse me if you click this button
00:05:57.759 here it expands it so you can edit the row of data in this modal i'll keep it
00:06:04.319 simple we'll just edit it here there we go so this is going to be the first line
00:06:09.520 of our script and we'll say I am
00:06:15.960 healthy and we're going to find a photo that accompanies this line of this
00:06:21.600 script shortly and then the second line of our script
00:06:27.600 will be I am wealthy and we'll find a photo soon for
00:06:35.360 this line of our script and we'll say I am gay all right here's where Chad
00:06:42.000 No text
00:06:43.919 GPT comes in so if you have no sense of self-expression no sense of personality
00:06:49.039 absolutely zero creativity what you can do is come over to Chad
00:06:54.919 GPT and prompt it to write a short form video script for you
00:07:00.840 so write a three line script for a video
00:07:13.599 you can copy each line into each row of this table right
00:07:20.000 No text
00:07:21.360 now let's get some images to accompany each line of our script you can get your images from Google images from a hard
00:07:28.319 drive on your computer if you have some you can come over to chat GBT and prompt
00:07:33.759 to generate some images this
00:07:39.479 works and then you can download your images like that i however I'm going to
00:07:44.560 be using Pixels it's a royaltyfree stock photo site the nice thing about both the
00:07:52.080 OpenAI image generation feature and Pixels is that they have APIs that you can leverage for scaling your AI video
00:08:00.240 automation later if you want to produce a ton of videos we're not going to cover that today but just to give you some
00:08:05.560 ideas i've already found some photos that I'm going to use to accompany this
00:08:11.280 script and the way that we include them in our Air Table table is by dragging
00:08:17.599 each photo onto the corresponding cell of the row
00:08:25.319 this attachment cell has this handy feature where you can drag files onto it
00:08:34.399 this feature right here is why I like using Air Table over Google Sheets for doing this type of work now that we have
00:08:41.120 that set up we can jump into our automation platform and tie all of this
00:08:46.560 together to produce videos here we are in make.com and let's come over to the
00:08:49.000 No text
00:08:52.800 scenarios page and I've created a folder called make
00:08:58.360 ornat and here's where I've been mcking around let's create a new scenario and
00:09:04.800 start from scratch in make.com lingo uh scenario is an automation the first node
00:09:12.080 we're going to add is going to be an air tableable node so let's select the Air
00:09:18.080 Table app these are all of the modules within the Air Table app that we can choose and we want this one because we
00:09:25.440 want to pull in all of the records from that table that we created over here so
00:09:32.959 you're going to have to create a connection between make.com and Air Table it's actually quite simple you can
00:09:38.880 click create a connection and we're going to be doing this technique air tableable token or
00:09:46.760 key and the way that we get that is we come back to our Air Table account and
00:09:53.760 then in this little dropdown for our icon or profile we can
00:10:02.000 select builderhub and then we want to come over
00:10:07.120 to personal access tokens and then let's create a new token this one will be called
00:10:14.360 make or n call it whatever you want and then these are the permissions that this
00:10:21.120 token will grant to whoever is using it so we're going to need three scopes or
00:10:27.800 permissions this one this one and we
00:10:32.880 need this one data.records colon read is the first scope data.records colon write
00:10:39.279 is the second scope schema.basis bases colon read is the third scope after we
00:10:45.120 select the scopes that we're going to need we have to also specify what base
00:10:50.480 within our air table account this token will have access to and this is the one
00:10:55.760 that we've been working in now we can click create token let's copy this
00:11:01.800 into this field and if this works should be good to
00:11:07.959 go voila so you can see our base is available to be selected
00:11:15.640 and this table within our base is also available to be selected and this stuff
00:11:22.720 I think we can keep as it is for this initial test i'll click save then if I
00:11:28.079 run the automation you can see that we're getting our script into
00:11:35.480 our scenario fantastic the next node that we're going to add is a tools node and
00:11:44.480 to be specific a compose a string module we're going to be looping
00:11:52.880 over each row in our air table table and let me fix
00:11:59.240 this this is going to be
00:12:04.370 [Music] order and this is going to be line
00:12:12.279 right so this is a JSON to video scene i mentioned we were going to be using JSON
00:12:18.399 to video this is how you specify one scene of your video a scene is hopefully
00:12:26.720 self-explanatory how would you describe a scene a scene is a collection of
00:12:32.760 multi-dia assets stacked on top of each other anyways hopefully this makes sense
00:12:38.800 we're building a scene according to the JSON to video API if you have any questions about JSON to video leave a
00:12:44.959 comment and I also have an amazing video on JSON to video that you can check out on the channel if you want to learn the
00:12:51.279 fundamentals of JSON to video etc let's move along let's click save and the next node that we're going to add is going to
00:12:58.160 be a parse JSON module we're going to be doing here
00:13:06.600 is converting the string that's produced by this node into structure JSON or
00:13:14.320 parsing it into a JSON object that make.com can work with click save save
00:13:21.440 and then let's run this wait hold
00:13:26.839 up i'm leaving this in because this is actually very true to how make.com works
00:13:32.800 sometimes you have to provide placeholder values before you can run the application or the scenario rather
00:13:39.680 and then when you run the application you'll then have the values you need available to you so we built
00:13:46.079 the JSON string in the second node or module now we can select it we can click
00:13:52.639 save and now when we run this again it should work and it does and on the other
00:13:58.959 side of this parse JSON module we have for each
00:14:05.760 row of our air table table we have structure JSON you
00:14:11.560 see perfect the next node that we're going to add is going to be an array
00:14:22.920 aggregator and that's found in the flow control app array
00:14:29.399 aggregator and here you select the node that's
00:14:37.000 producing quote unquote bundles so each node in make.com has its particular
00:14:46.120 behaviors this one for example this search records node produces what are
00:14:51.839 called bundles and
00:14:57.240 the system behind make.com is going to trigger the subsequent nodes once for
00:15:05.360 each bundle by default and the way that we can close that feature or collapse it
00:15:13.519 back into one line of execution I don't know if that's the best way to describe it but anyways you can see by this icon
00:15:19.519 that we're taking multiple bundles and then collapsing them into one anyways when you're configuring the array
00:15:26.560 aggregator here you want to select the node that's producing these bundles
00:15:32.800 [Music] and here is what we'll select
00:15:38.120 and what we want to pick out for each
00:15:43.639 bundle is going to be the comment and
00:15:49.959 elements of the scene that's produced from the information from the air table table row in the bundle little bit of a
00:15:57.279 mouthful but anyways click save now when we run this hopefully it works you can see
00:16:05.040 these got executed three times in total so this first air table node produced
00:16:11.120 three bundles this got executed once for the first row of the table twice for the
00:16:18.160 second row three times for the third row and then all of these executions or
00:16:26.720 guess you could say bundles got collapsed into a single bundle on the other side of this array aggregator node
00:16:33.519 and here we have an array of our scenes scene
00:16:39.480 one scene three oh yeah this is expected because we're going to have to configure
00:16:45.639 this like so let me show you what I mean so we're going to
00:16:51.480 sort by the order in ascending order so if you
00:16:58.160 remember we added a column called order and this is why we added this column so that we can control the order of the
00:17:04.919 lines and now when we run this again we should have our scenes in the
00:17:10.959 expected order scene one scene two scene three
00:17:19.039 perfect we click save and then to wrap this up let's add
00:17:25.520 two more nodes we're going to add a JSON transform to JSON
00:17:32.679 module and this is going to be the output of the array
00:17:40.760 aggregator and now that we have that as a JSON
00:17:46.280 string we can send it to JSON to video using
00:17:47.000 No text
00:17:52.520 the create a movie from JSON module and in the same way that we had to connect
00:17:58.000 air tableable with make.com we now have to connect JSON to video with make.com so if we come over to JSON to
00:18:06.919 video then log in come over to our
00:18:12.360 dashboard here there's a page called API keys i will not show you this but on
00:18:17.679 this page it'll give you some API keys and then you can copy them
00:18:23.960 into this field right here and that
00:18:29.120 should allow.com to access your JSON video
00:18:35.160 account bingo and then what we're going to do is copy this string
00:18:44.360 template this is some more JSON to video stuff pretty much what we're doing here
00:18:50.600 is creating a movie a movie is comprised of scenes and we built our scenes in
00:18:58.679 the previous node right well we downloaded the rows
00:19:06.640 from Air Table we compiled each row into a valid JSON to video scene we put those
00:19:16.559 scenes into an array and then here's a string template for a
00:19:23.160 movie.json and we're replacing the value for the scenes key with the stringified
00:19:30.240 array that we built in the prior nodes hopefully that makes sense pretty much we have scenes and then if there's going
00:19:36.400 to be some elements like for example a backing track or maybe like a watermark or captions that you want to overlay
00:19:44.000 over the spoken audio or the narrated audio you can add a subtitles
00:19:50.120 element and here's where you customize the parameters of the subtitles element
00:19:56.320 i'm probably being a little bit too pedantic excuse me so anyways save and let's run
00:20:04.360 this that looked like it worked if we come over to the render logs in our JSON to video account we can see something is
00:20:12.360 rendering and
00:20:17.760 I am healthy i am wealthy i am gay we'll
00:20:21.000 No text
00:20:23.200 leave it there for now i just wanted to show you the basics of this air table plusmake.com plus JSON to video setup
00:20:29.520 you could take it to the next level by automating the script writing with for example the OpenAI API or the anthropic
00:20:35.360 API whatever you prefer and once you get the script back you can break that script up into lines and then automatically add each line to the air
00:20:42.679 table then you could generate an image prompt for example based on each line of the script and once you have the image
00:20:49.120 prompt you can send it to Midjourney or the OpenAI image generation API to automatically generate your images for
00:20:55.760 you you can also once you have the image for each line of the script send it to
00:21:01.280 Cling and Cling will generate a video for you based on that image so there's a
00:21:07.440 lot of creative direction you could go in i'll leave it there for now hopefully you enjoyed it and in part B we're going
00:21:15.039 to keep a lot of the same assets and setup but we're going to switch out
00:21:20.600 make.com for NADN see you in part B here is
00:21:24.000 No text
00:21:28.760 naden.io and let's sign in and enter one of our workspaces naden has workspaces just
00:21:36.240 like Air Table has workspaces for example and in our dashboard you can
00:21:42.159 organize your workflows into folders just like you can
00:21:48.559 on make.com i made a folder called make or n cuz this video is pretty much a
00:21:56.880 introduction to both of these platforms so you can see a quick overview of the differences and let's create a new
00:22:03.919 workflow so a workflow is an automation in naden the same way that a scenario is an automation in make.com so here we are
00:22:12.240 and the first node that we're going to add is going to be a manual trigger
00:22:18.400 running this node is the same thing as clicking the run button in make.com
00:22:23.840 right you click this button it triggers your automation and the second node that we're going to
00:22:31.159 add you can search for all of the nodes here we're going to add a air table node
00:22:38.159 and we're going to fetch the records from our script
00:22:46.280 table and let's create a new credential so you
00:22:51.679 understand the process it's very similar to make.com you have to provide an
00:22:57.200 access token and make sure that access token has these scopes or permissions
00:23:02.400 associated with it here in air table let's come over to the builder hub which
00:23:08.240 is accessible through this top right profile menu and let's create a new
00:23:13.799 token call this one make or
00:23:20.280 n alt the scopes that we're going to add are data.records records col read
00:23:27.240 data.records colon write and then we're going to need schema.basis read the base
00:23:34.080 that this token needs access to is the base where we have our script which is
00:23:39.679 the video automation base and now we can create this token copy it and come back
00:23:47.360 to Naden paste it in here
00:23:53.320 and we'll call this token make
00:23:58.919 or N just so we can easily identify it and
00:24:04.240 we can see the connection is successful and close this and we see that the air table node
00:24:12.080 is now using the token that we just created as its o credential and if we
00:24:20.240 click this dropdown we can see the base is available for us to select and if we
00:24:26.159 click this dropdown we see table within the base where we have our script is
00:24:31.440 available to be selected as well and to test it we can click this button right
00:24:36.960 here and you can see we get our script i am
00:24:42.279 healthy yeah three items so it's showing one at a time the same way that the
00:24:49.159 make.com air table search records node spits out one bundle at a time and it
00:24:54.240 ends air tableable search records node is doing the same thing here we see one of the bundles or outputs so that's
00:25:02.880 working next up we want to build a scene for each row that we receive from our
00:25:08.400 Air Table table and the way that we're going to do that is with the edit fields
00:25:14.720 node or the set node as it's sometimes referred to and we want to use this mode
00:25:21.919 for the edit fields node JSON mode this allows us to very specifically outline
00:25:27.600 whatever JSON we want and we want to put this field here into
00:25:36.480 expression mode and then click this button which gives us a little bit more room to work
00:25:43.080 with and we want to replace some of this
00:25:48.240 stuff well I'll just set it up so I can show you from scratch how this works so this
00:25:53.840 is the outline of a JSON object that is going to represent each scene in our
00:26:00.720 video we have to replace a few parts of this or I should
00:26:06.919 say we want to set up some variables to
00:26:12.159 replace certain parts of this JSON outline let me show you what I mean so
00:26:17.360 here we want to reference the image for each scene in our script
00:26:24.120 table or each row in our script table here we want to reference the line of the script in
00:26:34.880 the current scene or row and
00:26:40.360 here we'll put the order of the scene right and on the
00:26:47.919 right here you can see the values that fill in these variables for each output
00:26:55.520 generated by the Air Table search records node right make sense so that
00:27:01.919 looks good and then next up we're going to do something
00:27:08.480 identical to what we did with the make.com scenario we're going to use an aggregate
00:27:14.960 node which is going to collapse all of the bundles or outputs into a single
00:27:21.600 line of execution and the way that we do that is by selecting this option and
00:27:27.679 we'll rename this to be called scenes and that looks good let's test
00:27:34.279 this and here you can see we have an array called scenes that contains three
00:27:39.760 items each of the
00:27:45.039 rows of our table got transformed into a scene which is exactly what we wanted and we can take
00:27:51.880 this and send it to JSON to video but you can see here that there is no
00:27:58.080 dedicated node in NAN for JSON to video so what we have to do instead is build a
00:28:05.760 HTTP request ourselves for talking to the JSON to video API and this is the
00:28:14.080 node that we want the HTTP request node and now we build our HTTP request
00:28:23.480 and let me show you a little trick for quickly doing this what we can do is
00:28:28.880 come over to this specific page on the JSON to video docs that has an example
00:28:34.240 curl request for how to create a very simple movie using the JSON to video API so we can copy this curl request curl
00:28:42.080 for those who are unfamiliar with this is just a way of outlining the details of an HTTP request so most of the data
00:28:49.840 across the internet moves according to this protocol called HTTP sounds very
00:28:55.600 fancy all it is is a way of transferring data across the internet and it's pretty simple just have to provide the other
00:29:04.000 point on the internet you'd like to talk to that's your URL and they have a verb
00:29:10.640 here which can be either get post put delete there's a few values here but
00:29:16.640 typically you're just going to see get and post get implies that you're downloading data from this other point
00:29:24.159 on the internet that you specify with this URL and posting data usually means you're going to be sending data usually
00:29:31.200 that's how it works but there are some weird exceptions where people don't follow the convention and there's other
00:29:36.320 features where you can provide headers which are ways of specifying different
00:29:43.279 things depending on what you're trying to do that's very vague but for example you can pass a header that contains a
00:29:50.320 password or some sort of O token and that's what we're going to be doing here that's going to allow us to authenticate
00:29:55.919 with the JSON to video API from an ADM and you can send data right so excuse me
00:30:03.520 if I'm being a bit pedantic but for those who are brand new to this you now understand what's going on so let me
00:30:09.440 copy this example curl request come over to the HTTP request node and you see this button here that says import curl
00:30:16.559 so what we can do is delete whatever values in there and then we can paste in
00:30:21.679 this example curl click import and it's going to set up a lot of the fields in
00:30:28.640 this HTTP request node for us we will have to configure a few of them to get it working just right but it saves us
00:30:35.360 some time so that's a pretty handy feature and what I'm going to do first is set up the authentication header and
00:30:44.640 after that what we'll do is configure the movie.json and then we should be
00:30:50.240 able to test it out and hopefully have a video all right first let's set up the authentication header so it imported uh
00:30:58.960 header here when we imported the curl the reason why we don't want to put the header here is it's going to be public
00:31:07.440 for people to read if we were to ever share this automation with anybody so we can keep our headers private this way so
00:31:15.440 we can create a O credential and the authentication mechanism we'll use is a
00:31:22.559 plain old HTTP header which is simply a key value pair right and the key that
00:31:28.880 we're going to use is let's create a new credential here
00:31:35.360 those are the other ones I've already created all those are just key value pairs of API keys that I'm using for
00:31:42.399 other APIs so the name of this one that's relevant to JSON the video will
00:31:48.000 be X API key and then the value will be found in our dashboard on the API keys
00:31:54.799 page i will not show you this i will copy it and then paste it into that field in Naden paste save and then you
00:32:03.120 also should rename this so we know what this is in the future
00:32:09.720 save and that looks good and the next thing to do is configure the
00:32:17.159 movie.json aka the body of this HTTP request so let's switch this to
00:32:23.279 expression mode open this up so we have more space to work with and this is the
00:32:29.360 value that we're going to paste in here and we labeled the output of the aggregate node scenes so I think this is
00:32:36.559 ready to go this is almost identical
00:32:41.679 there might be something minor like comment might be different but this is pretty much the exact same movie.json
00:32:47.840 that we used in the last node of the make.com scenario
00:32:53.159 so let's test this and the request went through that's
00:32:58.960 good so if we come over to our dashboard and check out the render logs we see a
00:33:05.840 video being rendered but there's one thing that we missed i think we forgot
00:33:11.919 to sort the rows of the Air Table table
00:33:17.519 we need to sort by order ascending right and then now we can run the entire
00:33:25.960 workflow and then there should be another video
00:33:31.320 rendering right and let's reload this
00:33:36.480 this should be finished and the order should be as expected
00:33:41.679 i'm healthy i'm wealthy i am gay
00:33:47.000 No text
00:33:47.240 brazil brazil so hopefully you enjoyed
00:33:52.440 that you learned a technique or two that you can use for your personal brand your
00:33:59.279 company or your business or your clients businesses
00:34:05.320 and sending lots of love peace and blessings
