// Smallest multiple
// Problem 5
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import Swiftest

func productOfFactors(factorDict: [Int:Int]) -> Int {
  var product = 1
  for (factor, exponent) in factorDict {
    product = product * Int(pow(Double(factor), Double(exponent)))
  }
  return product
}

func smallestMultiple(divisors:Range<Int>) -> Int { 
  let factorizations = divisors.map(primeFactors)
  var combinedFactors = [Int:Int]()
  for factorDict in factorizations {
    for (factor, exponent) in factorDict {
      combinedFactors[factor] = max(exponent, combinedFactors[factor] ?? 0)
    }
  }
  return productOfFactors(combinedFactors)
}

class Problem005Spec : Swiftest.Spec {
  let spec = describe("Problem 005 - Smallest Multiple") {
    it("should be 2520 for 1...10") {
      expect(smallestMultiple(1...10)).to.equal(2520)
    }
    it("should be 232792560 for 1...20") {
      expect(smallestMultiple(1...20)).to.equal(232792560)
    }
  }
}
