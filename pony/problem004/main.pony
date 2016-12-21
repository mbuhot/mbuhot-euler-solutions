use "promises"
use "../task"

/*
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/

primitive Problem004
  fun run(): Promise[String] =>
    Task.async[String]({():String =>
      for palindrome in PalindromeGenerator do
        if Problem004.three_digit_factorization(palindrome) then
          return "Problem 004: " + palindrome.string()
        end
      end
      "Problem 004: No solution"
    })

  fun three_digit_factorization(x: I64): Bool =>
    var y: I64 = 999
    while y >= 100 do
      let z = x / y
      if z >= 1000 then
        return false
      elseif (z >= 100) and ((y * z) == x) then
        return true
      end
      y = y - 1
    end
    false


class PalindromeGenerator
  var _next: I64

  new iso create() =>
    _next = 999

  fun has_next(): Bool =>
    _next >= 100

  fun ref next(): I64 =>
    let result = (_next * 1000) + ((_next % 10) * 100) + (((_next / 10) % 10) * 10) + ((_next / 100) % 10)
    _next = _next - 1
    result
