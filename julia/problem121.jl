module problem121

description = """
Disc game prize fund

A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.
The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.
If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.
Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
"""

# A brute force calculation of the probability of winning with given number of turns
function pwin(turns :: Int)
  p = zero(Rational)
  for numblues = (div(turns, 2) + 1) : turns		# Win when num blues is over half the turns
    for blueturns  in combinations(1:turns, numblues)   # Find all combinations of turns that could produce the blues
      ps = [n//(n+1) for n = 1:turns]			# Calculate probability of getting a red at every turn
      for t in blueturns				# Update for getting a blue at some turns
        ps[t] = 1 // (t+1)
      end
      p += prod(ps)					# take the product for overall probability of winning exactly this way
    end 
  end
  return p
end

# The maximum prize fund that should be allocated given the chance of winning
prizefund(pwin :: Rational) = int(floor(inv(pwin)))

# Solver 
solve(n = 15) = println("prize fund for $n turns should be: $(prizefund(pwin(n)))")

using Base.Test

@test pwin(4) == 11//120
@test prizefund(pwin(4)) == 10

end