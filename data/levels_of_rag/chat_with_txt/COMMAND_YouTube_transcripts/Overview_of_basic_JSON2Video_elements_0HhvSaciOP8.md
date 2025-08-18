---
title: "Overview of basic JSON2Video elements (audio, video, voice, etc.)"
description: "Transcript for a video on the COMMAND YouTube channel"
url: "https://youtu.be/0HhvSaciOP8"
publish_date: "4-15-2025"
---

# tactiq.io free youtube transcript
# Overview of basic JSON2Video elements (audio, video, voice, etc.)
# https://www.youtube.com/watch/0HhvSaciOP8

00:00:00.160 We are now going to walk through the
00:00:01.600 elements or basic building blocks of a
00:00:03.679 platform called JSON to video. JSON to
00:00:06.080 video is exactly what it sounds like.
00:00:07.600 It's an API that you can send some JSON
00:00:09.440 to and in response it'll render a video
00:00:11.440 for you according to the details of your
00:00:13.559 JSON. Now would be the time to sign up
00:00:15.839 to jsontovideo.com. If it's your first
00:00:17.840 time signing up, you will get some free
00:00:19.760 credits, which is great. And as a heads
00:00:22.160 up, when you run out of those free
00:00:23.359 credits, you will need to make a
00:00:24.560 purchase of about 50 bucks. But my goal
00:00:27.519 is to avoid you having to make that
00:00:28.880 purchase. And the other thing that
00:00:30.480 you're going to have to set up is a file
00:00:32.159 storage system like for example Dropbox
00:00:34.000 or Google Drive. And if you're more
00:00:36.079 technical, you can even set up your own
00:00:37.360 file server. But I recommend you use
00:00:39.120 Dropbox. Dropbox is free, it's simple,
00:00:42.000 and it integrates really well with the
00:00:43.840 automation platform we're going to be
00:00:45.200 using,
00:00:46.120 make.com. And the other pro tip I'll
00:00:48.320 give you before we jump in is to make
00:00:50.079 sure that while you're learning this
00:00:51.280 platform,
00:00:52.199 jsonthe.com, make sure that each video
00:00:54.239 you render is max 2 seconds to 5
00:00:56.960 seconds. For context, one JSON to video
00:00:59.840 credit gives you about one second of
00:01:01.520 rendered video. So if you make the
00:01:03.039 videos really short, it'll stretch those
00:01:04.879 free credits really far. Make sense?
00:01:07.760 Here is the complete list of elements
00:01:09.840 supported by JSON to videos API. Audio
00:01:13.040 elements, video elements, voice
00:01:14.320 elements, image elements, subtitles,
00:01:16.320 HTML, text, components, and
00:01:18.600 audiograms. We're going to walk through
00:01:20.560 each one one by one. Let's get started
00:01:23.600 by creating a new scenario.
00:01:27.680 And the first module we're going to add
00:01:30.880 is going to be in the tools app. We're
00:01:33.040 going to add a set variable module. And
00:01:38.079 we're going to call this
00:01:39.479 variable
00:01:43.079 movie.
00:01:45.640 And we will provide the variable value
00:01:50.200 soon. Let's add another module. And this
00:01:54.240 one is going to
00:01:55.640 be JSON to
00:01:59.240 video. Right? The exact module that we
00:02:02.399 want is going to be this one. Create a
00:02:05.520 movie from
00:02:08.919 JSON. So now we have to sign up to JSON
00:02:13.280 to video and get an API key. If you've
00:02:18.640 already signed up to JSON to
00:02:21.160 video, you can come over to your
00:02:24.360 dashboard and you see this page here
00:02:27.280 that says API keys. I'm going to mask
00:02:30.560 mine out, but this is where you can find
00:02:33.920 an API key for connecting make with JSON
00:02:36.720 to
00:02:42.680 video. And that's it.
00:02:45.840 And we could write our JSON in here, but
00:02:50.000 I prefer to reference
00:02:53.000 the variable value out
00:02:56.920 here. And let's save this and align
00:03:01.959 everything. All right, let's get going
00:03:04.959 by starting with this baseline JSON. And
00:03:09.040 I'm going to be using this tool called
00:03:10.879 JSON formatter. This is a tool that
00:03:13.760 makes it a little bit easier to work
00:03:15.120 with JSON, you can collapse sections of
00:03:17.440 the JSON when it starts to get large.
00:03:20.480 And if and when the JSON gets a little
00:03:22.959 bit
00:03:23.640 misformatted, you can easily fix that by
00:03:26.800 clicking this format button. Right? So,
00:03:30.640 let's bring that back over here. Here
00:03:32.799 you can see the overview of a movie.json
00:03:36.720 object. According to the JSON to video
00:03:39.480 API, each movie or video is going to
00:03:43.040 have a certain
00:03:44.120 resolution. This is a code that means
00:03:47.200 1920 pixels by 1080 pixels, right? This
00:03:52.480 has to do with how pixelated the video
00:03:54.720 is going to be.
00:03:57.000 Lower or low, I should say, will make
00:04:01.200 the video more pixelated, but it'll
00:04:02.640 render faster.
00:04:04.599 And we're actually going to put SD here.
00:04:07.760 SD, I think, is 720 pixels across and
00:04:10.560 maybe like 480 pixels up. I might have
00:04:13.200 that wrong, but anyways, we're setting
00:04:16.160 things up so that as we learn, it's
00:04:18.160 cheap and it's fast. That's the
00:04:20.600 rationale. And the other aspect of a
00:04:22.800 movie is it's going to consist of
00:04:24.320 scenes, right? And each scene has a
00:04:27.040 comment where we can put the scene's
00:04:28.479 name is going to be scene one. And each
00:04:30.800 scene is comprised of elements. Haha.
00:04:33.759 And you can see there's also a key for
00:04:37.360 elements that sits at the base of the
00:04:40.240 movie object. So this would be useful
00:04:42.240 for putting like a backing track across
00:04:43.919 the entire video. But we'll learn about
00:04:46.560 this stuff as we get deeper.
00:04:49.160 Anyways, let's
00:04:51.400 now add a audio element. So I'm going to
00:04:56.080 add a JSON object inside of this
00:04:58.240 elements array. And the way that we add
00:05:01.040 an audio element is by adding the key
00:05:04.759 type colon space another set of quotes
00:05:08.479 and then here we're going to type audio.
00:05:10.639 We're going to provide the source key
00:05:13.440 right src colon space and then another
00:05:16.320 set of quotes. Here we're going to
00:05:19.199 provide the URL to some audio file. I
00:05:22.400 think JSON to video supports MP3, wave,
00:05:25.680 maybe a couple other file types as well.
00:05:27.199 But
00:05:27.960 anyways, I've shared all these media
00:05:30.000 assets with you so you don't have to
00:05:31.120 waste time finding your own. And here in
00:05:33.919 the audio folder, if you copy the link
00:05:37.680 to this
00:05:38.680 file and then come back to the JSON, you
00:05:41.600 can paste it here. The only thing that
00:05:43.680 we have to change is this last URL
00:05:45.520 param. We have to change this to be raw
00:05:48.080 equals 1. This tells Dropbox that we
00:05:51.039 want to download the file, not view it
00:05:53.120 inside of the Dropbox application. And
00:05:56.039 because we're trying to avoid that $50
00:06:00.400 credits charge from JSON to video, let's
00:06:04.800 make sure that this video is going to be
00:06:07.520 very short. So we'll say duration 3
00:06:11.720 seconds. And I think that'll work. So if
00:06:14.800 we format this,
00:06:16.759 yeah, this is important. So sometimes
00:06:20.960 there's characters that you're not
00:06:22.479 seeing in the UI but are embedded in the
00:06:25.319 JSON has to be formatted properly in
00:06:27.919 order for it to work. So you can click
00:06:29.600 that format button. Copy
00:06:32.199 this. And then if we come back to
00:06:34.840 make.com, let's paste in our first
00:06:37.759 official
00:06:39.160 movie. Save that. And if everything's
00:06:42.479 set up, we can run this. And you see it
00:06:47.360 looked like it completed
00:06:48.759 successfully. If we come to our JSON to
00:06:52.639 video dashboard over to the render logs
00:06:55.639 page, we should see a new entry. Was
00:06:59.520 that right? I said 720x 480. I was
00:07:02.400 wrong. It's 640x 480. I was close. But
00:07:06.319 we can see the video is 3 seconds. It
00:07:07.840 took 3 seconds to make. We click this.
00:07:10.800 We can see
00:07:13.479 it. Right. So that's our first movie.
00:07:16.479 It's just an audio file. All right,
00:07:19.599 let's rinse and repeat. So let's start
00:07:22.520 with that
00:07:24.360 same base
00:07:27.960 movie.
00:07:29.800 And because we're professional,
00:07:33.160 SD
00:07:35.000 low and
00:07:37.960 then let's add a video element. So let's
00:07:42.319 add that JSON object to the elements
00:07:44.639 array of the first scene
00:07:47.560 and put
00:07:51.240 type
00:07:56.039 video and here we put the
00:08:00.039 URL of the video. I've provided
00:08:05.360 uh video files so you don't have to
00:08:07.680 waste time looking for your
00:08:10.120 own. Technically, this could be whatever
00:08:12.400 you want.
00:08:13.560 Anyhow, let's come back here and paste
00:08:16.560 in the URL. And we have
00:08:18.919 to fix
00:08:22.199 this. This
00:08:25.400 Let's JSON the video download the file
00:08:28.639 instead of trying to view it in the
00:08:30.240 Dropbox UI.
00:08:33.279 And the last thing that we'll do is make
00:08:37.760 sure we don't burn our free credits if
00:08:40.799 we're still on
00:08:42.360 them. And let's make this video only 3
00:08:47.480 seconds. So, let's format this. It's
00:08:50.320 hidden behind this ad.
00:08:52.600 Unfortunately, we're using a free JSON
00:08:54.959 formatter. It is very spammy with the
00:08:57.360 ads. Yeah, we can click format and copy
00:09:02.360 this into
00:09:07.000 make and save. And let's run this
00:09:13.160 again. And come back to the render
00:09:22.279 logs. And here we are.
00:09:27.680 There we go. Okay. Now that you're
00:09:30.480 familiar with the general pattern of
00:09:31.839 what we're doing here, we're walking
00:09:33.120 through each of the basic elements
00:09:34.800 provided by the JSON to video API, we're
00:09:37.120 going to move a little bit faster. So
00:09:38.959 the next element is going to be the
00:09:42.800 voice
00:09:43.800 element. And if we come over to the JSON
00:09:47.200 formatter application, paste this in.
00:09:50.320 Here is how we specify a voice element.
00:09:52.640 So type voice. Here's where we put the
00:09:54.720 text that we want spoken. There are two
00:09:58.399 or three model providers I guess you
00:10:01.440 could say for powering the text to
00:10:04.040 speech. There's Azure and then 11 Labs,
00:10:08.320 right? But using 11 Labs is going to
00:10:11.040 burn some of your credits. So that's why
00:10:13.040 I'm suggesting Azure. There's this other
00:10:15.279 page on the JSON to video documentation
00:10:17.279 where you can choose the specific Azure
00:10:20.079 voice. And let's keep this simple. Let's
00:10:22.640 go with English. And just to mix it up,
00:10:25.519 let's go with
00:10:27.640 Duncan. And let's replace
00:10:31.320 Emma with
00:10:33.560 Duncan and format
00:10:36.200 this.
00:10:38.600 Copy it into the make.com
00:10:43.079 automation. Save.
00:10:46.360 Run. That looked like it
00:10:48.839 worked.
00:10:50.760 And let's refresh the render logs.
00:10:57.360 and play this. Hello world.
00:11:01.640 Great. Next up is the image
00:11:04.760 element. So let's come back to the JSON
00:11:08.800 formatter. Paste this
00:11:11.399 in. We have to provide the URL to the
00:11:15.320 image. So let's come back here. I've
00:11:18.560 provided an example image to you. Want
00:11:21.040 to use it? Use your own as
00:11:24.760 well. Copy this. Come back to JSON
00:11:29.640 formatter.
00:11:32.519 Paste. Fix
00:11:34.839 that.
00:11:36.839 And we're positioning the image in the
00:11:39.519 center of the
00:11:42.760 window. And we're going to show the
00:11:45.440 image for one second. Let's format this.
00:11:49.800 Copy and paste it
00:11:52.700 [Music]
00:11:54.519 into.com. Save.
00:11:59.000 Run. Let's come back to the render logs.
00:12:06.360 Refresh. Take a look.
00:12:09.639 Perfect. The next element will be the
00:12:12.399 subtitles element. So, let's come back
00:12:16.360 to JSON formatter application and paste
00:12:19.120 this in. As you can see, the JSON's
00:12:21.680 starting to get a little bit
00:12:23.240 larger. We can collapse it to get a
00:12:27.440 better
00:12:29.800 overview.
00:12:32.040 Right. So, for the subtitles element,
00:12:34.880 you're going to need actually two
00:12:36.560 elements. You're going to need a voice
00:12:41.000 element or some audio that has audible
00:12:46.839 dialogue. If you use the subtitles
00:12:49.519 element
00:12:50.680 with nonaudible dialogue or like a piece
00:12:54.800 of audio that doesn't have dialogue, who
00:12:56.800 knows what it might spit out. But
00:12:57.920 anyways, you'll see how it works. Here
00:13:00.560 I've customized
00:13:03.240 this and
00:13:06.120 I am showing you here how to use a
00:13:09.200 custom font. JSON the video comes with
00:13:11.519 some pre-built fonts or some built-in
00:13:14.040 fonts, but for branding, you're probably
00:13:16.480 going to want to choose your own font.
00:13:17.959 So, all you have to do is come over to
00:13:22.920 Google
00:13:25.240 Fonts and you can download one of these
00:13:28.560 TTF files
00:13:31.240 and place it somewhere on the internet.
00:13:35.360 I've included it in the media assets
00:13:38.720 that I'm
00:13:39.800 sharing. You get the link and reference
00:13:43.519 it like this. Make sure to change the
00:13:45.360 URL param if you're using
00:13:47.639 Dropbox. And these are styling changes.
00:13:50.320 Anyways, I'm being a little bit
00:13:51.680 pedantic. So, let's format
00:13:54.839 this. Copy it into
00:13:59.000 make.com. Save that. Run
00:14:02.600 it. That looked like it worked. Let's
00:14:05.600 come back to our render logs.
00:14:08.839 Refresh. Take a look. Hello world.
00:14:12.160 Right. So, it generates on the-fly
00:14:15.120 captions based on some audible audio.
00:14:17.760 That's what the subtitles element does.
00:14:20.399 Next up is the HTML element. And this
00:14:25.440 element is pretty cool except that you
00:14:27.760 cannot do animations. That's my only
00:14:30.000 gripe with it. But here we
00:14:34.440 are. So, we're going to paste this
00:14:37.320 in. And here you can see some HTML code.
00:14:43.399 And let's format it.
00:14:47.639 Copy. Paste this
00:14:50.680 into make.com. Save.
00:14:55.720 Run. Come back to the render logs.
00:14:59.480 Refresh. Take a look.
00:15:03.079 Right. So, this could be useful. The
00:15:07.279 next element is the text element.
00:15:12.839 And it does come with
00:15:16.199 some animations and customizability.
00:15:19.519 We're just going to test it with this
00:15:20.880 plain Jane version. But yeah, you can
00:15:24.320 customize the font
00:15:26.040 and do some things, right? It does have
00:15:30.399 some
00:15:32.199 animation templates, I guess you could
00:15:34.320 say,
00:15:36.440 right? So, you can do some things with
00:15:38.680 this. Let's come back here. Format it.
00:15:43.079 Copy. Paste. Save.
00:15:46.839 Run. Render
00:15:48.759 logs. Refresh. Play it.
00:15:53.399 Right. Next up is the component element.
00:15:56.800 This is a fancier or more spruced up
00:16:00.160 text like
00:16:02.360 element. This is what it looks like.
00:16:05.759 And let me show you some
00:16:07.720 other components that come with JSON to
00:16:12.120 video. I wish the JSON to video platform
00:16:14.720 let you build your own custom
00:16:16.480 components. Hopefully that's on the road
00:16:19.160 map. Yeah, definitely get creative with
00:16:22.560 some of
00:16:25.160 these also
00:16:33.160 these. All right.
00:16:35.560 Format. Copy.
00:16:38.600 Paste. Save.
00:16:42.920 Run. Render
00:16:44.759 logs.
00:16:47.079 Refresh. There we go. Let's play
00:16:50.120 it. Right. We got a little newslike
00:16:53.839 title, little news crawl. The next
00:16:56.639 element is the audiogram element, which
00:16:59.519 believe it or not, I was not able to get
00:17:01.600 working. This is what the audiogram
00:17:04.079 element looks like though. It's pretty
00:17:07.880 cool. I guess you have to play some
00:17:10.000 audio in the background and then it'll
00:17:12.000 animate this waveform according to the
00:17:15.280 amplitude of the waves in the audio. But
00:17:17.679 anyways, if you're wondering how I
00:17:19.039 figured out all this stuff, I pretty
00:17:21.280 much read through all the documentation.
00:17:22.959 So, as a heads up, there are two
00:17:25.280 versions of the JSON to video docs. This
00:17:29.200 to me looks like it's the V1 version and
00:17:31.360 then there is the V2 version over here.
00:17:35.679 Right, the documentation is pretty good.
00:17:38.799 Some of the information is a bit
00:17:40.080 sprawled across V1 and V2, but anyhow,
00:17:44.559 that covers all of the JSON to video
00:17:46.720 elements or basic building blocks that
00:17:48.799 you can combine with each other to
00:17:50.320 automate the creation of your videos.
