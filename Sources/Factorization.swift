func primeFactors(n:Int) -> [Int] {
  for prime in primes() {
    if (prime == n) { 
      return [prime]
    } else if (n % prime == 0) { 
      return [prime] + primeFactors(n / prime)
    }
  }
  preconditionFailure("Unreachable")
}
