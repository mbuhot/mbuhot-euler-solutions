func + <A : GeneratorType, B : GeneratorType, Element where Element == A.Element, Element == B.Element>(a: A, b: B) -> AnyGenerator<Element> {
  var a = a
  var b = b
  var aComplete = false
  return AnyGenerator {
    if !aComplete { 
      if let x = a.next() {
        return x
      } else { 
        aComplete = true
      }
    }
    return b.next()
  }
}
