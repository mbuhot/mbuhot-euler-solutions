func primeFactors(n:Int) -> [Int:Int] {
  var n = n
  var result = [Int:Int]() 
  for prime in primes() {
    if (n == 1) { return result }
    var exponent = 0
    while (n % prime == 0) {
      n = n / prime
      exponent += 1
    }
    result[prime] = exponent
  }
  preconditionFailure("Unreachable")
}
