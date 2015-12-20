// Sum square difference
// Problem 6

// The sum of the squares of the first ten natural numbers is,
// 1^2 + 2^2 + ... + 10^2 = 385

// The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)^2 = 55^2 = 3025

// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import Swiftest

func sumSquareDifference(n:Int) -> Int {
  // Use sum of squares formula and sum of integers formula for O(1) solution
  let sumOfSquares = n * (n+1) * (2*n + 1) / 6
  let sumOfN = ((n+1) * n) / 2
  let squareOfSum = sumOfN * sumOfN
  return squareOfSum - sumOfSquares
}

class Problem006Spec : Swiftest.Spec {
  let spec = describe("Problem 006 - Sum square difference") {
    it("should be 2640 for 1...10") {
      expect(sumSquareDifference(10)).to.equal(2640)
    }
    it("should be 25164150 for 1...100") {
      expect(sumSquareDifference(100)).to.equal(25164150)
    }
  }
}

