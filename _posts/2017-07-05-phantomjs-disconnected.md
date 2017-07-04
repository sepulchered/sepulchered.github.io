---
layout: post
title: PhantomJS ERROR: Disconnected, because no message in 10000 ms.
date: 2017-07-05
---

Today I was trying to run test for the project on ci and encountered an error `PhantomJS ERROR: Disconnected, because no message in 10000 ms.`. After googling for a while i found that it's widespread issue with a lot of disscussions around [[1][1st-discussion]], [[2][2nd-discussion]], etc. but i couldn't find stable solution. So here is the stuff that helped me: I increased karma configs for timeout and number of retries:
`--browser-no-activity-timeout 100000 --browser-disconnect-tolerance 10 --retry-limit 10`
and it worked for my case.

What these configs do (from [karma site](http://karma-runner.github.io/)):

+ `--browser-no-activity-timeout` (`browserNoActivityTimeout` in config file) - `How long will Karma wait for a message from a browser before disconnecting from it (in ms).`
+ `--browser-disconnect-tolerance` (`browserDisconnectTolerance`) - `The number of disconnections tolerated.`
+ `--retry-limit` (`retryLimit`) - `When a browser crashes, karma will try to relaunch. This defines how many times karma should relaunch a browser before giving up.`

PS: it's not actual solution to the problem, but the way to postpone solving the issue by utilising some workaround.

[1st-discussion]: https://github.com/karma-runner/karma-phantomjs-launcher/issues/126
[2nd-discussion]: https://github.com/jasmine/jasmine/issues/1327
