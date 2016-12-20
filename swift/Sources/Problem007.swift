// 10001st prime
// Problem 7
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?

import Swiftest

class Problem007Spec : Swiftest.Spec {
  let spec = describe("Problem 007 - 10,001st prime") {
    it("should give 6th prime = 13") {
      expect(primes().dropFirst(5).first).to.equal(13)
    }
    it("should give 10,001st prime = 104743") {
      expect(primes().dropFirst(10000).first).to.equal(104743)
    }
  }
}  

