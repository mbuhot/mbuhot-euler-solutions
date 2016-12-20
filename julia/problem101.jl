#! /usr/bin/env julia

module problem101

function polyval(coefficients :: Vector, x :: Number)
  powers = [x^p for p = 0:length(coefficients)-1]
  return sum(coefficients .* powers)
end

function polyfit(x :: Vector, y :: Vector)
  return polyfit(x, y, length(x))
end

function polyfit(x :: Vector, y :: Vector, n :: Int)
  A = [xi^p for xi = x, p = 0:(n-1)]
  return A \ y
end

function bad_opt_poly(poly, n)
  xs = [1:n]
  ys = [polyval(poly, x) for x = xs]
  return polyfit(xs, ys)
end

function bad_opt_polys(poly)
  return {bad_opt_poly(poly, n) for n = 1:length(poly)-1}
end

function first_incorrect_terms(polys)
  return [polyval(p, length(p)+1) for p = polys]
end

function sum_of_fits(poly)
  return sum(first_incorrect_terms(bad_opt_polys(poly)))
end

using Base.Test

@test polyval([1, 2, 3], 5) == 1 +  2*5 + 3*5*5
@test polyfit([1, 2, 3], [1, 8, 27]) == [6, -11, 6]
@test first_incorrect_terms(bad_opt_polys([0, 0, 0, 1])) == [1, 15, 58]
@test sum_of_fits([0, 0, 0, 1]) == 74

end

println(int(problem101.sum_of_fits([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])))

