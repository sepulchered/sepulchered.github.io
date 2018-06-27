---
layout: post
title: How to isolate node.js for real good
---

## Per Aspera

All the way through my career I was using [nvm](https://github.com/creationix/nvm) for managing [node.js](https://nodejs.org/) versions. I was completely happy with it for the task of developing different projects with different node.js versions. Things were going smoothly.

But recently I started working on [Jenkins](https://jenkins.io/) based CI for our front end projects. First thought was to use nvm as well. But it turned out to be a nightmare.

First I configured everything and it was running as expected. But when I turned on builds and tests for pull requests something went wrong. In my way to the truth, I was almost lost because I couldn't see any pattern at first: some builds were passing while others were failing without any meaningful message. But at some point, I understood that when there were major differences in `package.json` file for dependencies it was behaving super weird. So I finally realized that it was using the same `node` & `npm` so each concurrent build was installing its own dependencies.

## Ad Astra

So I tried to find a solution for the problem. And I encountered it in [nodeenv project](https://github.com/ekalinin/nodeenv) by [Eugene Kalinin](https://github.com/ekalinin). It works as Python [virtualenv](https://virtualenv.pypa.io/) does. You create a folder for the environment and it holds all the information for your libs and other stuff installed leaving global/nvm environment not polluted.

In order to use it, you should have Python installed. Run `sudo easy_install nodeenv` or `pip install nodeenv` if you have pip installed (you can use it in Python virtualenv as well). To list available node versions run `nodeenv --list`. To install node into folder run 
`nodeenv -n 6.11.1 --prebuilt <env path>`. After installing environment into the folder you can either run node/npm and other globally installed executables with `<env path>/bin/node` or you can activate environment with `. <env path>/bin/activate`. After activating the environment node & npm executables will refer to the environment ones.

So using this approach you can easily have isolated node environment for each build. As well you can use it instead of nvm for project development.
