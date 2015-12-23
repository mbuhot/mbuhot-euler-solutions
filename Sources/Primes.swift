struct PrimeGenerator : GeneratorType {
    typealias Element = Int
    private var compositeToPrime = [(4,2), (9,3)]
    private var i = 1
    
    mutating func next() -> Element? {
        i += 1
        if i < 4 { return i }
        while true {
            let (composite, prime) = compositeToPrime[0]
            if i == composite {
                i += 1
                compositeToPrime[0] = (composite+prime, prime)
                sort()
            } else {
                compositeToPrime.append((i*i, i))
                return i
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
                composite += prime
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

 
