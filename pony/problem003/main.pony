use "promises"
use "../task"

/*
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/

primitive Problem003
  fun run(): Promise[String] =>
    Task.async[String]({():String =>
      var n: U64 = 600851475143
      var p: U64 = 1
      while n > 1 do
        p = p + 2
        while (n % p) == 0 do
          n = n / p
        end
      end
      "Problem 003: " + p.string()
    })
