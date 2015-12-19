func primes() -> AnyGenerator<Int> {
  var compositeToPrime = Dictionary<Int,Int>() 
  var i = 1
  return AnyGenerator {
    while true {
      i += 1
      if !compositeToPrime.keys.contains(i) {
        compositeToPrime[i*i] = i
        return i
      }
      else {
        let prime = compositeToPrime[i]!
        var nextComposite = i + prime
        while compositeToPrime.keys.contains(nextComposite) { 
          nextComposite += prime
        }
        compositeToPrime[nextComposite] = prime
        compositeToPrime.removeValueForKey(i)
      }
    }
  }
}
