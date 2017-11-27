# Collatz-Grapher: math and hailstones #

The [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) is a famous unsolved problem in mathematics which asks if all natural numbers will eventually reach 1 if they are continually passed  as arguments to a map <i>f</i>, defined as <i>f(n) = n / 2</i> if <i>n mod 2 = 0</i>, or <i>f(n) = 3n + 1</i> if <i>n mod 2 = 1</i>, for <i>n > 0</i>.

There is no complete formal proof of this conjecture, but it is widely believed to be true, even "large" numbers eventually reaching 1 after a series of steps. Unfortunately, my program does not prove the Collatz conjecture, but it does produce a very pretty graph, which you can see below:

 ![collatz-graph](https://github.com/jyoo980/collatz-grapher/blob/master/media/plot_10000.png) 

You can run Collatz-Grapher just by running some commands like I do below:

![collatz-cmd](https://github.com/jyoo980/collatz-grapher/blob/master/media/collatz_command.png)

Here's what I want to do in the future, if you have any suggestions, feel free to make a PR!
* Application of the collatz map to the input list is an example of an <i>embarassingly parallel problem</i>, I want to leverage 
  parallelism to make this faster. <strong>[Complete]</strong>
* I want to investigate what causes the bottleneck at around `n ~ 1000000`, whether it's due to the limitation of the graphing module, or
  whether it is due to something else.

In closing, here's a quote about the Collatz conjecture by the famous mathematician Paul Erdos:

<p align="center"><strong><i>"Mathematics may not be ready for such problems"</i></strong></p>
