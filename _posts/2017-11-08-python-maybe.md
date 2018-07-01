---
layout: post
title: Maybe Python? Explaining Haskell (to myself) with Python.
---

Do you miss functional stuff in Python? I personally don't :)

But recently I started reading a lot of stuff on functional programming and it definitely has some advantages over good old OOP. Can't say that I like to see it in Python, but it definitely helps to stretch one's mind.

In this post, I'll try to implement something similar to `Maybe` type & related functions (see [Haskell's Data.Maybe](https://hackage.haskell.org/package/base-4.10.0.0/docs/Data-Maybe.html)) in Python.

# What is `Maybe`?
As it's said in Haskell docs:

> The Maybe type encapsulates an optional value. A value of type Maybe a either contains a value of type a (represented as Just a), or it is empty (represented as Nothing). Using Maybe is a good way to deal with errors or exceptional cases without resorting to drastic measures such as error.

We can illustrate it by the following division function: `divide(float, float) -> Maybe float` (pseudo PyHaskell notation :) ). `Maybe float` here because in Python if we try to divide by `0` we'll get runtime error `ZeroDivisionError`.
In Python `typing` module for type hints, there is [such type annotation](https://docs.python.org/3/library/typing.html#typing.Optional): `Optional[T]`

# Implementation
So let's approach it with division function from the example.

<script src="https://gist.github.com/sepulchered/b67cc22e51a0cd016dfcd5dcac4cf919.js"></script>

In this example, we won't actually get `None` value, instead `ZeroDivisionError` will be thrown. So let's update it to handle the exception.

<script src="https://gist.github.com/sepulchered/89744afc3e67084b9074575c567504ce.js"></script>

So we can see now how we can generalize it to be used with any function, that throws an exception.

<script src="https://gist.github.com/sepulchered/09afd8c6e1aed477819097e36d6ff26f.js"></script>

Or better with a decorator:

<script src="https://gist.github.com/sepulchered/d06ea509b271daae85cdea3980c3d917.js"></script>

# Related functions
As you can see there are several related functions in [`Data.Maybe` docs](https://hackage.haskell.org/package/base-4.10.0.0/docs/Data-Maybe.html)
Let's start with `isJust` & `isNothing`:

<script src="https://gist.github.com/sepulchered/06b439c780910d7e06cd3fbd09a8f644.js"></script>

Then `maybe` but as we already have decorator function called `maybe` we'll call it `maybe_fn`:

<script src="https://gist.github.com/sepulchered/ab22efb167dbbf0bdfe61d34d3842df8.js"></script>

And all the rest:

<script src="https://gist.github.com/sepulchered/b25bd52f2337918c4da70ab1463e4c10.js"></script>

# Updates
After posting to Reddit I got several comments (special thanks to [subtly_homoerotic](https://www.reddit.com/user/subtly_homoerotic) & [frankreyes](https://www.reddit.com/user/frankreyes/)) on the post, noting that there is a problem.

Let's assume we have following function (don't ask me how my brain created it or where can you utilize it in the real world): 

<script src="https://gist.github.com/sepulchered/9be1315b5bd5a49d4e61fca93ea7bdd9.js"></script>

If we'll try to utilize our `@maybe` decorator to the function we'll get to the point where we won't be able to distinguish between normal function execution (i.e function returns `None` intentionally) and some exceptional case (`ZeroDivisionError` happened)

To resolve the issue we'll add one more class `Just` and update our `maybe` decorator:

<script src="https://gist.github.com/sepulchered/d65ad2e43106a4c0e0373f1a491bbf6a.js"></script>

So this way we'll be able to distinguish `Just(None)` and plain `None` and thus separate intentional `None` return value and "empty" `None` value.

Finally, we'll have to rewrite functions to utilize `Just` value:

<script src="https://gist.github.com/sepulchered/73eda12d86d58eb70513211989ae04df.js"></script>

# What it's all about?
I cannot say that it'll help you in everyday work with Python. Neither it will give you a good grasp of Haskell knowledge. But it definitely can help you with an understanding of some Haskell concepts and ideas (though they are easy to understand in Haskell docs). At least it helped me :).
