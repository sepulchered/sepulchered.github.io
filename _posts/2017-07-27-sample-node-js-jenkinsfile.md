---
layout: post
title: Sample node.js Jenkinsfile
---

So you want to run CI or even CD of your node.js project using [Jenkins](https://jenkins.io/). Even though Jenkins interface is good enough to handle everything you need and Jenkinsfile syntax is easy to understand you may need default template to start with. So here it will be. You can use, update and do whatever you want with it until you do it for good :).

First, make sure you have Jenkins 2.x or later. Then you would need [Pipline plugin](https://plugins.jenkins.io/workflow-aggregator) - it may be already installed, check it first.

If you haven't created pipelines in Jenkins you could start from [official docs](https://jenkins.io/doc/pipeline/tour/hello-world/). After you configure pipeline for the project you should copy [sample Jenkinsfile](https://gist.github.com/sepulchered/2e97b29b2c3b95e0ee2501f7c6dcf037) into to the project root. Note: my Jenkinsfile uses [nodeenv](https://github.com/ekalinin/nodeenv) for isolated node.js environment creation.

<script src="https://gist.github.com/sepulchered/2e97b29b2c3b95e0ee2501f7c6dcf037.js"></script>

So what it actually does:

1. If you don't know what `agent` means - stick with `any` value. (or you can read [Jenkins docs](https://wiki.jenkins.io/display/JENKINS/Distributed+builds))
2. Environment variables are created to store values that will be used later
3. Then we define stages (that will be shown separately in the Jenkins interface)
4. Each stage can have title e.g. `Pre-cleanup` and have several actions in it.
5. After all the steps are passed we can do stuff on failure and success in the corresponding parts.

So if you want to notify your chat with the build status - `post` is a good place to do it. Actually, you can check the branch and auto deploy it to the proper server if the build is successful.

Hope it'll help you.
