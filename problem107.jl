module problem107

description = """
Minimal network
Problem 107

The following undirected network consists of seven vertices and twelve edges with a total weight of 243.

The same network can be represented by the matrix below.
    	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-

However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.
"""

immutable Edge
  from :: Int
  to :: Int
  cost :: Int
end

immutable Tree
  edges :: Vector{Edge}
end

immutable Forest
  trees :: Vector{Tree}
end

# Find the index of the tree containing node in the forest, or -1 if not found
function tree_index(node :: Int, f :: Forest)
  for i = 1:length(f.trees)
    for j = 1:length(f.trees[i].edges)
      if (f.trees[i].edges[j].from == node || f.trees[i].edges[j].to == node)
        return i
      end
    end
  end
  return -1
end

# Tests if adding Edge e to Forest would connect two previously disconnected trees
function makes_new_connection(e :: Edge, f :: Forest)
  t1 = tree_index(e.from, f)
  t2 = tree_index(e.to, f)
  return t1 < 0 || t2 < 0 || t1 != t2
end

# Creates Add Edge to Forest, joining any trees that become linked
function add_edge(e :: Edge, f :: Forest)
  t1 = tree_index(e.from, f)
  t2 = tree_index(e.to, f)

  # Simple case, neither from/to existed previously, add a new tree
  if t1 < 0 && t2 < 0
    return Forest([Tree([e]); f.trees])
  end

  # One of the trees exists - make a copy and update
  newtrees = copy(f.trees)
  if t1 > 0 && t2 < 0
    newtrees[t1] = Tree([e; f.trees[t1].edges])
  elseif t1 < 0 && t2 > 0
    newtrees[t2] = Tree([e; f.trees[t2].edges])
  else
    newtrees[t1] = Tree([e; f.trees[t1].edges; f.trees[t2].edges])
    splice!(newtrees, t2, Tree[])
  end
  return Forest(newtrees)
end

# Convert from matrix representation to Edge vector
function matrix_to_edges(connections :: Matrix{Int})
  edges = Edge[]
  for i = 1:size(connections, 1)
    for j = i+1:size(connections, 2)
      if connections[i, j] > 0
        push!(edges, Edge(i, j, connections[i,j]))
      end
    end
  end
  return edges
end


# Calculate the minimum spanning tree by adding the minimum cost edge to a forest if it links up previously disconnected trees
function minimum_spanning_tree(connections :: Matrix{Int})
  edges = matrix_to_edges(connections)
  sort!(edges, by = x -> x.cost)
  f = Forest(Tree[])
  for e in edges
    if makes_new_connection(e, f)
      f = add_edge(e, f)
    end
  end
  return f.trees[1]
end

function read_network()
  m = readcsv("network.txt")
  m[m .== "-"] = -1
  connections = int(m)
  return connections
end

function solve107()
  network = read_network()
  t = minimum_spanning_tree(network)
  initial_cost = sum([e.cost for e in matrix_to_edges(network)])
  final_cost = sum([e.cost for e in t.edges])
  println("$initial_cost - $final_cost = $(initial_cost - final_cost)")
end

using Base.Test

testcase = [
-1	16	12	21	-1	-1	-1
16	-1	-1	17	20	-1	-1
12	-1	-1	28	-1	31	-1
21	17	28	-1	18	19	23
-1	20	-1	18	-1	-1	11
-1	-1	31	19	-1	-1	27
-1	-1	-1	23	11	27	-1]

@test sum([e.cost for e in minimum_spanning_tree(testcase).edges]) == 93

end