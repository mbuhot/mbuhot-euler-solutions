extension SequenceType where Self.Generator.Element:IntegerType {
  func sum() -> Self.Generator.Element { 
    return self.reduce(0, combine: +)
  }
}

extension SequenceType {
  func takeWhile(predicate: (Self.Generator.Element -> Bool)) -> AnyGenerator<Self.Generator.Element> {
    var g = self.generate()
    return AnyGenerator {
      return g.next().flatMap { predicate($0) ? $0 : nil }
    }
  }
}
