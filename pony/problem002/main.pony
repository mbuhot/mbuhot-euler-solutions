// Even Fibonacci Numbers
// Each new term in the Fibonacci sequence is generated by adding the previous two terms.
// By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.

use "../task"
use "promises"

primitive Problem002
  fun run(env: Env): Promise[String] =>
    Task.async[String]({():String =>
      var a: I64 = 1
      var b: I64 = 2
      var sum: I64 = 0
      while a < 4_000_000 do
        if (a % 2) == 0 then
          sum = sum + a
        end
        a = b = (a + b)
      end
      "Problem 002: " + sum.string()
    })
