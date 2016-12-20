use problem001 = "problem001"
use problem002 = "problem002"

use "promises"

actor Main
  let tasks: Array[Promise[String]]
  let env: Env

  new create(env': Env) =>
    env = env'
    tasks = [
      problem001.Problem001.run(env),
      problem002.Problem002.run(env)
    ]
    await(0)

  be await(i: USize) =>
    let self : Main tag = this
    try
      tasks(i).next[None]({(msg: String)(env, i, self) =>
        env.out.print(msg)
        self.await(i+1)
      } iso)
    end
