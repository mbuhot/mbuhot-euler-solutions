extension SequenceType where Self.Generator.Element:IntegerType {
    func sum() -> Self.Generator.Element {
        return self.reduce(0, combine: +)
    }
    func product() -> Self.Generator.Element {
        return self.reduce(1, combine: *)
    }
}


extension SequenceType {
    func takeWhile(predicate: (Self.Generator.Element -> Bool)) -> AnyGenerator<Self.Generator.Element> {
        var g = self.generate()
        return AnyGenerator {
            return g.next().flatMap { predicate($0) ? $0 : nil }
        }
    }
    
    var first : Self.Generator.Element {
        var g = self.generate()
        return g.next()!
    }
    
    func window(n : Int) -> AnyGenerator<Array<Self.Generator.Element>> {
        var g = self.generate()
        var buf = (1...n).map { _ in g.next()! }
        return GeneratorOfOne(buf) + AnyGenerator {
            buf[0 ..< buf.count - 1] = buf[1 ..< buf.count]
            if let x = g.next() {
                buf[buf.count - 1] = x
                return buf
            } else {
                return nil
            }
        }
    }
}
