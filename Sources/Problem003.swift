//Largest prime factor
//Problem 3
//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?

import Swiftest

func largestPrimeFactor(n:Int) -> Int {
  let factors = primeFactors(n)
  return factors.maxElement()!
}

class Problem003Spec : Swiftest.Spec {
  let spec = describe("Problem 003 - Largest Prime Factor") {
    it("should be 29 for 13195") {
      expect(largestPrimeFactor(13195)).to.equal(29)
    }
    it("should be 6857 for 600851475143") {
      expect(largestPrimeFactor(600851475143)).to.equal(6857)
    }
  }
}

