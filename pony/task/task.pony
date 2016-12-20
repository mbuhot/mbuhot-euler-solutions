use "promises"

primitive Task
  fun async[T: Any #share](f: {(): T} val, p: Promise[T]=Promise[T].create()): Promise[T] =>
    let t = object
      let _p: Promise[T] = p
      let _f: {(): T} val = f
      be run() =>
        _p(_f())
    end
    t.run()
    p

  fun zip[T1: Any val, T2: Any val, R: Any val](
      p1: Promise[T1],
      p2: Promise[T2],
      f: {(T1, T2): R} val): Promise[R] =>

    let p = Promise[R]
    p1.next[None]({(x: T1)(p, p2, f) =>
      p2.next[None]({(y: T2)(p, f, x) =>
        Task.async[R]({()(f, x, y): R => f(x, y)} val, p)
      } iso)
    } iso)
    p

    fun zip3[T1: Any val, T2: Any val, T3: Any val, R: Any val](
        p1: Promise[T1],
        p2: Promise[T2],
        p3: Promise[T3],
        f: {(T1, T2, T3): R} val): Promise[R] =>

        let p = Promise[R]
        p1.next[None]({(x: T1)(p, p2, p3, f) =>
          p2.next[None]({(y: T2)(p, p3, f, x) =>
            p3.next[None]({(z: T3)(p, f, x, y) =>
              Task.async[R]({()(f, x, y, z): R => f(x, y, z)} val, p)
            } iso)
          } iso)
        } iso)
        p
