// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

use "../task"
use "promises"

primitive Problem001
  fun run(env: Env): Promise[String] =>
    let p1 = Task.async[I64]({(): I64 => Problem001.sumOfMultiples(3, 1000)})
    let p2 = Task.async[I64]({(): I64 => Problem001.sumOfMultiples(5, 1000)})
    let p3 = Task.async[I64]({(): I64 => Problem001.sumOfMultiples(15, 1000)})

    Task.zip3[I64, I64, I64, String](p1, p2, p3, {(x: I64, y: I64, z: I64)(env):String =>
        "Problem 001: " + ((x + y) - z).string()
      } val)

  fun sumOfMultiples(x: I64, max: I64): I64 =>
    var y = x
    var total: I64 = 0
    while y < max do
      total = total + y
      y = y + x
    end
    total
