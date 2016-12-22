/*
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

use "promises"
use "collections"

primitive Problem005
  fun run(): Promise[String] =>
    let p = Promise[String]
    let factorizations : Array[Array[(I64, I64)]] = [
      [(2, 1)],
      [(3, 1)],
      [(2, 2)],
      [(5, 1)],
      [(2, 1), (3, 1)],
      [(7, 1)],
      [(2, 3)],
      [(3, 2)],
      [(2, 1), (5, 1)],
      [(11, 1)],
      [(2, 2), (3, 1)],
      [(13, 1)],
      [(2, 1), (7, 1)],
      [(3, 1), (5, 1)],
      [(2, 4)],
      [(17, 1)],
      [(2, 1), (3, 2)],
      [(19, 1)],
      [(2, 2), (5, 1)]
    ]
    try
      let powers = Array[I64].init(0, 21)
      for factorization in factorizations.values() do
        for (base, power) in factorization.values() do
          powers(base.usize()) = powers(base.usize()).max(power)
        end
      end

      var product: I64 = 1
      for base in Range[I64](2, 20) do
        product = product * (base.f64()).powi(powers(base.usize()).i32()).i64()
      end

      p("Problem 005: " + product.string())
    end
    p
