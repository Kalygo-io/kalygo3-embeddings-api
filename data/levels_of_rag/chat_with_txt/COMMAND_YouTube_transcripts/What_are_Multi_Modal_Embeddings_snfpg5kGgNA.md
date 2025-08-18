---
title: "What are Multi-Modal Embeddings?"
description: "Transcript for a video on the COMMAND YouTube channel"
video_url: "https://youtu.be/snfpg5kGgNA"
publish_date: "8-22-2024"
---

00:00:03.520 in this demo we will showcase the power
00:00:05.600 of multimodel embeddings multimodel
00:00:08.039 embeddings enable us to connect data
00:00:10.000 across sensory mediums let's take a look
00:00:12.880 here is an application for locating
00:00:14.360 multimedia assets related to a search
00:00:16.199 query let's search for media assets
00:00:17.880 related to the term
00:00:21.160 Outdoors you can see we get outdoorsy
00:00:23.599 images let's search for media assets
00:00:25.519 related to the term
00:00:28.000 drugs our top result isn't in fact an
00:00:30.359 image of Aderall let's now search for
00:00:32.759 media assets related to the term
00:00:36.040 speed I guess somebody who has ADHD
00:00:38.719 might take speed and notice how we're
00:00:40.879 also getting an audio
00:00:46.000 result this audio result sounds to me
00:00:48.320 like a Speed Racer note that we are not
00:00:50.440 doing string comparison against the
00:00:51.800 metadata of these media assets when
00:00:53.280 searching but instead are comparing the
00:00:54.879 vector representing the search query
00:00:56.680 against the vectors representing the
00:00:57.879 media assets themselves the embedding
00:01:00.320 model we are using to power this
00:01:01.760 functionality is called image bind image
00:01:04.280 bind was released by meta in May 2023
00:01:07.200 image bind lets you search for audio
00:01:08.840 using
00:01:11.759 images images using
00:01:15.880 audio and much more you can access image
00:01:19.040 bind embeddings via a platform called
00:01:20.920 replicate dcom shout out to Alex
00:01:23.439 Comerford for putting me on to this here
00:01:25.960 is the script that I use to upload a few
00:01:27.960 of my media assets to image bind forver
00:01:29.920 conversion into vectors after each media
00:01:32.119 asset is converted into a vector you can
00:01:34.079 see we are storing the resulting Vector
00:01:35.759 into a database index hosted by pine
00:01:37.759 cone after the vectors representing our
00:01:40.040 media are stored into pine cone or any
00:01:42.280 other Vector database for that matter we
00:01:44.079 can perform searches if you want to try
00:01:45.759 this yourself using pine cone you'll
00:01:47.280 need to make sure you create an index in
00:01:48.680 your account that supports vectors with
00:01:50.040 10,24 Dimensions let me show you how to
00:01:52.320 do that after signing up on pine con's
00:01:54.360 website you'll see an option to create
00:01:56.200 indexes in your dashboard let's create
00:01:58.399 an index called image bind 1024
00:02:01.880 Dimensions I like naming indexes after
00:02:04.039 the embedding models that generate the
00:02:05.560 vectors they will hold after we have an
00:02:07.719 image bind compatible index we can run
00:02:09.720 seed scripts to upload vectors
00:02:11.120 representing our
00:02:14.280 [Music]
00:02:19.160 media after we see vectors in the index
00:02:21.840 we'll be able to perform multimodel
00:02:23.360 searches multimodel embeddings are
00:02:25.640 amazing for creatives and media editors
00:02:27.879 as they allow for easier search across
00:02:29.560 media assets when producing content full
00:02:32.239 stack vectors pine cone Edition GP
00:02:35.000 Tuesday edition 305 Edition like share
00:02:38.239 comment subscribe Edition
