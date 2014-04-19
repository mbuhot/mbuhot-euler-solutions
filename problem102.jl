#! /usr/bin/env julia

module problem102
export countTrianglesContainingOrigin

immutable Point
  x :: Int64
  y :: Int64
end

immutable Line
  a :: Point
  b :: Point
end

immutable Triangle
  a :: Point
  b :: Point
  c :: Point
end

function sideOfLine(pt :: Point, ln :: Line)
  return sign((ln.b.x - ln.a.x)*(pt.y - ln.a.y) - (ln.b.y - ln.a.y)*(pt.x - ln.a.x))
end

function pointInTriangle(pt :: Point, tri :: Triangle)
  s1 = sideOfLine(pt, Line(tri.a, tri.b))
  s2 = sideOfLine(pt, Line(tri.b, tri.c))
  s3 = sideOfLine(pt, Line(tri.c, tri.a))
  return (s1 == s2) && (s2 == s3)
end

function triangleContainsOrigin(tri :: Triangle)
  return pointInTriangle(Point(0,0), tri)
end

function readTriangles(filename :: String)
  data = readcsv(filename, Int64)
  return [Triangle(Point(data[i, 1], data[i, 2]), Point(data[i, 3], data[i, 4]), Point(data[i, 5], data[i, 6])) for i = 1:size(data,1)]
end

function countTrianglesContainingOrigin()
  tris = readTriangles("triangles.txt")
  return count(triangleContainsOrigin, tris)
end

using Base.Test

@test triangleContainsOrigin(Triangle(Point(-340,495), Point(-153,-910), Point(835,-947)))
@test !triangleContainsOrigin(Triangle(Point(-175,41), Point(-421,-714), Point(574,-645)))

end

println(problem102.countTrianglesContainingOrigin())
