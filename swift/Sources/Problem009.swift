/*
Problem 9 - Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

import Swiftest

/*
Euclids formula:
 for all m and n with m > n. The formula states that the integers
 a = m^2 - n^2, b = 2mn, c = m^2 + n^2 
 are a pythagorean triple

 We have
   1000 = a + b + c
        = 2m^2 + 2mn
 => 500 = m^2 + mn
        = m(m + n)
 factors of 500 are: 1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500
 only 20 x 25 fits: m(m+n), for m > n: m = 20, n = 5
*/

func pythagoreanTriples() -> AnyGenerator<(a:Int, b:Int, c:Int)> {
    var m = 2
    var n = 1
    return AnyGenerator {
        let triple = (a: m*m - n*n, b: 2*m*n, c: m*m + n*n)
        n += 1
        if (n == m) {
            m += 1
            n = 1
        }
        return triple
    }
}

func findTripleWithSum(n: Int) -> (a:Int, b:Int, c:Int) {
    return pythagoreanTriples().lazy.filter { (a, b, c) in a + b + c == n }.first
}

class Problem009Spec : Swiftest.Spec {
    let spec = describe("Problem 009 - Special Pythagorean tiplet") {
        it("should find a+b+c == 1000, a*b*c = 31875000") {
            let (a, b, c) = findTripleWithSum(1000)
            expect(a * b * c).to.equal(31875000)
        }
    }
}