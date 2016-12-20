//Largest palindrome product
//Problem 4
//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//Find the largest palindrome made from the product of two 3-digit numbers.

import Swiftest

func isPalindrome(n:Int) -> Bool {
  var m = n
  var r = 0
  while m > 0 {
    r = (r * 10) + (m % 10)
    m /= 10
  }
  return r == n 
}
 
func largestPalindromeProduct(numDigits:Int) -> Int {
  var result = 0
  let lower = Int(pow(10.0, Double(numDigits - 1)))
  let upper = Int(pow(10.0, Double(numDigits)))
  for i in lower..<upper {
    for j in i..<upper {
      let prod = i * j
      if prod > result && isPalindrome(prod) {
        result = prod
      }
    }
  }
  return result
}

class Problem004Spec : Swiftest.Spec {
  let spec = describe("Problem 004 - Largest Palindrome Product") {
    it("should recognise a palindrome") {
      expect(isPalindrome(123454321)).to.equal(true)
    }
    it("should be 9009 for 2 digit product") { 
      expect(largestPalindromeProduct(2)).to.equal(9009)
    }
    it("should be 906609 for 3 digit products") {
      expect(largestPalindromeProduct(3)).to.equal(906609)
    }
  }
}
