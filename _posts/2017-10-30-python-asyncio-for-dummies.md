---
layout: post
title: Python asyncio for dummies.
---

I read several articles on `asyncio` python module. Watched several conf talks on it. But once I had to deal with it - I was confused. I have solid knowledge of python and can say that I'm a bit used to async programming with node. But it wasn't easy for me to get my hands wet with `asyncio`. That's why I'd like to share a simple but clear example of how it can be used and some basics of it.

# What we'll be looking at
Let's assume we are developing a sort of CI script that should build frontend project (install dependencies, compile/transpile, bundle, other stuff). We assume that our frontend project uses at least 2 package managers (`npm` & `bower` - btw [don't use bower for new projects](https://bower.io/blog/2017/how-to-migrate-away-from-bower/)), so we have to install all dependencies first and then run bundler (e.g. `webpack`).
So even that's a bit artificial example, but it's not that mystic and should be clear for those who know a bit about frontend stuff. With that said let's start.

# Without `asyncio`
Initially, we can write everything sequentially. This way we'll first install `npm` dependencies, then `bower` dependencies and then run `webpack` to bundle our project. 
<script src="https://gist.github.com/sepulchered/409448aab7ce2f571bfbe65660b4ef2e.js"></script>
It can be fast if you have a really short list of dependencies in both package managers, fast internet connection, and enough luck. But if you have `bower` already installed (as well as `npm`) - they are not dependent and can be run in parallel, or at least not block each other's execution.

# Let's add some `asyncio` magic
<script src="https://gist.github.com/sepulchered/4e9cf729e38b44129d0db87ded91bacd.js"></script>
Well even though it actually uses `asyncio`, we added 2 asynchronous functions, but run them synchronously as we did without any additional library. But we can see what changed in the file. 

* Marked npm & bower functions with `async`
* Added `await` before those functions
* Added getting of the [event loop](https://docs.python.org/3/library/asyncio-eventloop.html#base-event-loop) and run `main` until it's finished withing that `event loop` with method `run_until_complete`.

# Getting things right
This time let's get it right. We want processes of installing `bower` & `npm` dependencies to be asynchronous and wait for both to finish, only after doing so we want to start with `webpack`. We can use [gather](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) method to generate awaitable (future) object from several async methods.
<script src="https://gist.github.com/sepulchered/ca904e9f17e443091d7f807a1c89e6ed.js"></script>

# Conclusion
Now you can see that functions that use some async stuff or should get a result from async function or wait for an async function to execute should be marked as `async def`. To wait for a result of async function `result = await` is used (if you don't want to store result - just `await`).


Hope this example will give you some minimal understanding of how things from `asyncio` library work.
