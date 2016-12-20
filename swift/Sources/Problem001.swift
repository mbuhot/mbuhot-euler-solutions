//if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//Find the sum of all the multiples of 3 or 5 below 1000.
import Swiftest

func SumOfArithmeticSequence(a : Int, n : Int) -> Int {
  return a * n * (n+1) / 2
}

public func SumOfMultiplesOf(x:Int, and y: Int, lessThan n: Int) -> Int {  
  let multiplesOfx = SumOfArithmeticSequence(x, n: (n-1) / x)
  let multiplesOfy = SumOfArithmeticSequence(y, n: (n-1) / y)
  let multiplesOfBoth = SumOfArithmeticSequence(x*y, n: (n-1) / (x*y))
  let result = multiplesOfx + multiplesOfy - multiplesOfBoth
  return result;
}

class Problem001Spec : Swiftest.Spec {
  let spec = describe("Problem 001 - Multiples of 3 and 5") {
    it("Sums to 23 for multiples below 10") {
      expect(SumOfMultiplesOf(3, and: 5, lessThan: 10)).to.equal(23)
    }
    it("Sums to 233168 for multiples below 1000") {
      expect(SumOfMultiplesOf(3, and: 5, lessThan: 1000)).to.equal(233168)
    }
  }
}
