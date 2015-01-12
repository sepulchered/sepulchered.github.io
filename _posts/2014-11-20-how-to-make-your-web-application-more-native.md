---
layout: post
title:  "How to make your web application more native"
date:   2014-11-20 12:14:00
categories: hybrid_app native_app web_app
---
In this post I'll show how to make your existing web app look more native for mobile users.

##What is web application, anyway?
Now web app is a buzz word that is used to denote sometimes different things. So obviously you want to know what I'm talking about here.

[Wikipedia](http://en.wikipedia.org/wiki/Web_application) states:
> A web application or web app is any software that runs in a web browser. It is created in a browser-supported programming language (such as the
> combination of JavaScript, HTML and CSS) and relies on a web browser to render the application.

I think that it's great definition and I'll stick with it here.
##Is hybrid application a sort of web application
Well it depends on what you call hybrid application. I could not find some certain definition, but everybody seem to agree that it's some intermediate
between native application and web application. 

But it's still question for me to what extent? Is application written in C# and built with [Xamarin](http://xamarin.com/) to run on ios or android a
hybrid app, or is application written in JavaScript and built with [Titanium](http://www.appcelerator.com/titanium/) a hybrid app.

For me it seems that apps built with these platforms are native applications (as you can create applications for desktop using different programming
languages and different frameworks).
So I propose here definition of hybrid app as:
>Web application that use local resources of device it's running on and can work offline

Now, with rapid development of WebApi's for even [vibration](https://developer.mozilla.org/en-US/docs/Web/Guide/API/Vibration) working offline is
mostly what differentiate "hybrid" application from web application that are served from remote server. 

So **for me hybrid application is a sort of web application**. Even if it's cached web application that is served from local device storage - that is
hybrid app for me.
##How to make it more native
###Manifest is all you need! Actually not :(
First when I read about manifest file for web apps I thought that it's about cache manifest, but it's not. You can read editor's draft of specs on
[w3c github page](https://w3c.github.io/manifest/).

Manifest is simple JSON file that server provides and allows user to "install" your web application to device.
####What can you do with this manifest?
\- Can I enslave the whole world and rule all humanity with manifest? - you ask.

Actually not, but you can try, who knows anyway...
Here is short list of what's included:

- set application name
- set application icons
- set orientation
- set display mode (e.g. fullscreen)
- set application start url
- set application boundaries (application domain or directory of domain) so user won't go outside your application

Unfortunately only Firefox and Chrome will support (yep see **will**) manifest and maybe IE. That's why it's look into the future now than direct
recipe.
####iOS has nothing to do with manifest
If you want to rule ios world with manifest then you're defeated by default. 
But what if I want to rule ios world? - you ask.
I'm here to help you :)

- you can set application title with `<meta name="apple-mobile-web-app-title" content="My Mega App">`
- set icons with `<link rel="apple-touch-icon" sizes="76x76" href="my-mega-cool-app-icon.png">`. You should use **png** image and don't forget that
  there are different screen resolutions and you need to provide different icons for them. Thankfully you can have several icons with different
  `sizes` values to provide this functionality.
  - set application startup image with `<link rel="apple-touch-startup-image" href="my-mega-startup-image.png">`. Unfortunately you can't use `sizes`
    here, but guess what? You can use media queries.
    - hide browser controls with `<meta name="apple-mobile-web-app-capable" content="yes">`.
    - set fullscreen mode with `<meta name="apple-mobile-web-app-capable" content="yes">`
    - set the style for status bar with `<meta name="apple-mobile-web-app-status-bar-style" content="black">` read more on [safari developer
      library](https://developer.apple.com/library/safari/documentation/AppleApplications/Reference/SafariHTMLRef/Articles/MetaTags.html)

      Finally you can clone and use this [gist](https://gist.github.com/tfausak/2222823) by [Taylor Fausak](https://github.com/tfausak).
##What can I do for it to look more native
      I hope that you really want to make great mega application and provide user with good user interface. So here are some hints on how to make your
      app look great and native.
###ios
      First stop for you would be [iOS Human Interface
      Guidelines](https://developer.apple.com/library/ios/documentation/userexperience/conceptual/mobilehig/).

      After you get some knowledge of iOS design principles you can start with your own great mega design for app. 

      But wait is there anything that could help? Yes, there are several frameworks of components made for you:

      - [ChocolateChipUI](http://chocolatechip-ui.com) (free for open source)
      - [Onsen UI](http://onsen.io/) Apache License v2.0
      - [Framework7](http://www.idangero.us/framework7/) MIT Licensed

      I think it's enough to get started, but there are obviously more if you want something different.
###android
      First stop, as for ios, would be [official google design docs](https://developer.android.com/design/index.html)

      Now for Android it's Material Design time (hope you've read about it in official google design docs). So there already are several frameworks
      that can help you create android native ui look:

      - [Angular Material Design](https://material.angularjs.org/) MIT License
      - [Bootstrap Material Design](zvrasta.github.io/bootstrap-material-design/) free only for no-profit projects
      - [Leaf Framework](http://getleaf.com/) author said that it'll be free (but it's in development and things has not settled down)
      - [Material UI](http://material-ui.com) MIT License

      That's enough for good start but there's many more that can be found.
###firefox os
      Yes you didn't mishear Firefox OS. As I don't know any framework that has ui components ready for this os you just can read it's [design
      guides](https://www.mozilla.org/en-US/styleguide/products/firefox-os/) and wish for someone to make it. But wait, why not to make it yourself?
