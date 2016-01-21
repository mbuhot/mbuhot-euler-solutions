struct PrimeGenerator : GeneratorType {
    typealias Element = Int
    private var compositeToPrime = [(9,3), (25, 5), (49, 7)]
    private var i = 2
    
    mutating func next() -> Element? {
        // Handle small primes specially
        if (i < 9) {
            let p = i;
            i += (i%2) + 1;
            return p
        }
        while true {
            let p = i
            i += 2
            let (composite, prime) = compositeToPrime[0]
            if p == composite {
                compositeToPrime[0] = (composite + 2*prime, prime)
                sort()
            } else {
                compositeToPrime.append((p*p, p))
                return p
            }
        }
    }
    
    private mutating func sort() {
        var (composite, prime) = compositeToPrime[0]
        for j in 0..<compositeToPrime.count-1 {
            let next = compositeToPrime[j+1]
            if (composite < next.0)  {
                break;
            }
            if (composite == next.0) {
                composite += 2*prime
            }
            compositeToPrime[j] = next
            compositeToPrime[j+1] = (composite, prime)
        }
    }
}

struct PrimeSequence : SequenceType {
    typealias Generator = PrimeGenerator
    func generate() -> Generator {
        return PrimeGenerator()
    }
}

func primes() -> PrimeSequence {
    return PrimeSequence()
}

 
