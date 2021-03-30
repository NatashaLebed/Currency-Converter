
Description

On this stage, you need to specify what currency you want to exchange. Imagine that you came to the bank with some money in your pocket. You want to choose the best currency to exchange your money for. First, read the currency to exchange, then read the currency you might exchange your money for and the amount of money you want to exchange. Notice that the input number can have a fractional part!

There is a different amount of currencies in different tests. Checking if input is empty might be really useful.
Parse the data from FloatRates. You can store it in any collection you want. It's called caching – a simple way to speed up the program. If we need to exchange the same currencies that we have already changed, we won't need to connect to the Internet, we only need to refer to the data in our cache.

Check the cache — the required currency might be already in there, print the result afterward. Output the amount of money that the bank employee should give you.


Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

ILS

USD

45

Checking the cache...

Oh! It is in the cache!

You received 13.84 USD.

RSD

57

Checking the cache...

Sorry, but it is not in the cache!

You received 1684.41 RSD.

EUR

33

Checking the cache...

Oh! It is in the cache!

You received 8.38 EUR.


