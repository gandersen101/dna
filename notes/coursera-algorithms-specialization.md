# Coursera Algorithms Specialization (Stanford University)

As someone with minimal formal computer science education, I decided to work my way through of Stanford's [Coursera Algorithms Specialization](https://www.coursera.org/specializations/algorithms). The specialization consists of four, four week courses. Please see the synopsis of each below (to be filled out upon completion).

## Part 1. Divide and Conquer, Sorting and Searching, and Randomized Algorithms

Part one of the Algorithms Specialization illustrates several famous algorithms framed within an introduction asymptotic analysis. It also touches on the power of randomization in algorithm design, and begins to introduce graph structures and algorithms.

### Week 1 - Intro and Asymptotic Analysis

#### Intro

Week one starts by walking the student through implementing a multiplication algorithm, first by designing a naive, grade school approach; then by demonstrating how [Karatsuba multiplication ](https://en.wikipedia.org/wiki/Karatsuba_algorithm) eliminates a recursive call from the grade school approach. This demonstration aims to get the student thinking about how the number of recursive calls an algorithm makes may influence its runtime.

The course then covers [merge sort](https://en.wikipedia.org/wiki/Merge_sort), noting how this divide-and-conquer (more on this later) algorithm cuts the work each recursive call does in half, while each recursive call spawns two more calls. An analysis of the algorithm demonstrates it has an asymptotic runtime of `n*log*n`, which segues into an overview of asymptotic analysis.

#### Asymptotic Analysis

*Asymptotic notation in seven words:* suppress constant factors and lower-order terms.
- Constant factors are too system dependent.
- Lower-order terms are irrelevant for large inputs.

[Big-O](https://en.wikipedia.org/wiki/Big_O_notation), [Big-Omega](https://en.wikipedia.org/wiki/Big_O_notation#Big_Omega_notation), Big-Theta, [Little-o](https://en.wikipedia.org/wiki/Big_O_notation#Little-o_notation), and Little-omega notation have their respective definitions elucidated.

For example given that function `f` is `O(n^2)` (quadratic):
- Big-O: `f <= n^2`
- Big-Omega: `f >=  n^2`
- Big-Theta: `f == n^2`
- Little-o: `f < n^2`
- Litte-omega: `f > n^2`

 However, the instructor notes that
1. Big-O is often used as a catch-all when talking about algorithm upper-bounds even if another notation may be more appropriate.
2. The course will focus on Big-O.

### Week 2 - Divide & Conquer Algorithms and The Master Method

#### Divide & Conquer Algorithms

Week two focuses on divide-and-conquer algorithms and a method for ascertaining the runtime of most divide-and-conquer algorithms.

*A divide-and-conquer algorithm divides the input into smaller subproblems, conquers the subproblems recursively, and combines the subproblem solutions into a solution for the original  problem.*[^1]

Three divide-and-conquer algorithms are covered in detail:

1. Counting inversions with a modified merge sort in `O(n*log*n)`time.
2. [Strassen's matrix multiplication algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm) (run time to be revealed later).
	- Saves a recursive call over the naive implementation.
3. A `O(n*log*n)` closest pair algorithm[^2].

#### The Master Method

Divide-and-conquer algorithms can be expressed in the form of a recurrence:

A recurrence expresses  a running time bound `T(n)` in terms of the number of operations  performed by recursive calls.[^3]

A standard recurrence takes the form of:

**Base Case**
Can be solved in constant, `O(1)`, time.

**General Case**
`T(n) <= a * T(n/b) + O(n^d)`

**Parameters**
- *a* = number of recursive calls
- *b* = rate of reduction in input size
- d = exponent in the running time of the combine step

Once the divide-and-conquer algorithm is expressed as a recurrence, the master method can determine the upper bound on the algorithm's runtime.

- *Case 1*: `a = b^d`
	- `O(n^d*log*n)`
- *Case 2*: `a < b^d`
	- O(n^d)
- *Case 3*:  `a > b^d`
	- `O(n^logb*a)`

Notably `a` represents the rate of subproblem proliferation, while `b^d` represents the rate of reduction in input size fed to each subproblem. Ideally, divide-and-conquer algorithms have a rate of reduction greater than the rate of subproblem proliferation, and therefore the runtime is dominated by the work done at the root of the recursion. Less than optimally, divide-and-conquer algorithms have a rate of reduction less than the rate of subproblem proliferation, and therefore the runtime is dominated by the work done at the leaves of the recursion.

Some examples:
1. Merge sort: Case 1, `n*log*n`
2. Binary search: Case 1, simplifies to `log*n`
3. Recursive, naive, integer multiplication: Case 3, simplifies to `n^2`
4. Karatsuba Multiplication: Case 3, simplifies to `n^1.59`
5. Recursive, naive, matrix multiplication: Case 3, simplifies to `n^3`
6. Strassen's matrix multiplication: Case 3, simplifies to `n^2.81`

## Week 3 - QuickSort and Probability Review

### QuickSort

Week focuses on QuickSort as a means of introducing the power of randomization via the divide-and-conquer paradigm students have become comfortable with. Like merge sort, Quicksort has an upper-bound runtime of `n*log*n`. Unlike merge sort, QuickSort runs in place on the array it's sorting, which means it has a tiny memory footprint.

The crux of QuickSort revolves around picking a pivot element to partition two sides of the array around. Therefore, picking a "good" pivot (one that close to evenly splits the array) is essential for the algorithm to run efficiently.

As it turns out, randomly selecting a pivot uniformly at random, has an average running time of `O(n*log*n)` even though choosing the "worst" pivot would result in a runtime of `n(n^2)`, due to the [linearity of expectation](https://en.wikipedia.org/wiki/Expected_value) (the expected size of the subarray passed to a recursive call of QuickSort is `n/2` , which is an even split).

#### Probability Review

For the sake of brevity, I'm going to mostly skip over probability review. In addition to the expected values, the review covers [independence](https://en.wikipedia.org/wiki/Independence_(probability_theory)), [random variables](https://en.wikipedia.org/wiki/Random_variable), and [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability).

### Week 4 - Linear Time Selection and Graphs & A Contraction Algorithm

#### Linear-Time Selection

Week four begins with studying the selection problem, where the goal is to identify the ith order statistic of an array (the ith smallest entry), and an algorithm that can solve this problem in linear, `O(n)`, time. 

One can [reduce](https://en.wikipedia.org/wiki/Reduction_(complexity)) the selection problem to sorting then selecting the ith element via `Array[i]`, which would select in `O(n*log*n)` time. However, the [rselect (or Quickselect)](https://en.wikipedia.org/wiki/Quickselect) algorithm beats this reduction by running in `O(n)` time.

Despite running faster than QuickSort, rselect, essentially performs the same routine as QuickSort. Its improved runtime comes from the elimination of a recursive call (from 2 to 1). Once the input array is partitioned around the pivot element, the pivot element ends up at the correct index in the array. Therefore, rselect only needs to recurse on the partitioned half of the array where the ith order could statistic be - either the half before the pivot, the half after the pivot, or if you're lucky; the pivot element was the ith order statistic!

rselect, like QuickSort, utilizes randomization to select a pivot element, which leads to the algorithms average-case runtime of `O(n)`, although the worst pivot choice still results in a worst-case runtime of `O(n^2).` The instructor does note that a deterministic select algorithm exists, dselect, which uses the [median of medians](https://en.wikipedia.org/wiki/Median_of_medians) to choose a pivot. However, the instructor also notes that this algorithm is less efficient than the randomized approach in practice due to higher constant factors and increased memory allocation.

#### Graphs & A Contraction Algorithm

The final module of the class introduces basic graph concepts and nomenclature.

`G = (V, E)` means a graph, `G` which vertices `V` and edges `E`. There are two flavors of graphs, directed and undirected. In an undirected graph, an edge with endpoints at vertices `{v, w}` has no order, and can thusly be represented as `(v, w)` or `(w, v)`. In an ordered graph, `(v, w)` is an ordered pair distinct from `(w, v)`.

The size of a graph is expressed by the number of its vertices, `n`, and its edges, `m`. A connected, undirected graph with no parallel edges can have a minimum of `n-1` edges and a maximum `(n(n-1))/2` edges.

A graph is considered sparse if the number of edges is close to linear to the number of vertices. A graph is considered dense if the number of edges is close to quadratic to the number of vertices.

There are two common forms for representing a graph for algorithmic consumption: [adjacency lists](https://en.wikipedia.org/wiki/Adjacency_list) and an [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix)

Adjacency lists are the primary graph data structure used in this course. It consists of two arrays: one for containing the graph's vertices, and another for containing the graph's edges. Each edge holds a pointer to its two endpoints, and each vertex holds a pointer to each of its incident edges. A nice quality of adjacency lists is that the data structure has a linear memory requirement.

The adjacency matrix is the typical square, `n x n` matrix representation, where `Matrix[i, j]` represent a potential edge between nodes `i` and `j`. In its simplest form 0 would encode no edge and 1 would encode the presence of an edge. Adjacency matrices have a quadratic memory requirement, but they are easy to work with (linear algebra). When a graph is dense, using an adjacency matrix makes a lot of sense, but they waste a lot of memory when encoding a sparse graph.

The course wraps up by describing [Karger's minimum cut algorithm](https://en.wikipedia.org/wiki/Karger%27s_algorithm) (on undirected, connected graphs). A cut of a graph separates the vertices of a connected graph into two joint sets, and the minimum cut is the partition with the fewest number of edges connecting the two partitions. Brute forcing a solution to the minimum cut would run in `O(2^n)` time, which is an impractical on even medium-size graphs. Karger's algorithm makes use of many independent, randomized trials to achieve the far more efficient runtime of `O(n^4*log*n)`.

Each iteration of Karger's algorithm randomly deletes an edge from the graph, merges the nodes, and then deletes self loops before continuing until only two nodes remain. The number of edges between the two remaining nodes is the size of the cut. A single iteration of this algorithm only has a `1/(n^2)` probability of successfully finding the minimum cut and runs in `O(n^2)` time. This probability seems less than useful, but by running a sufficient number of repeated trials, `>= Constant * n^2*log*n`, the probability jumps all the way up to `1 - (1/n^C)`. Given that we run `n^2*log*n` trials that take `O(n^2)` time each, the final runtime of Karger's algorithm is `O(n^4*log*n)` - (the constant factor gets surpressed).

[^1]: Roughgarden, Tim. Algorithms Illuminated: Part 1: The Basics (p. 102). (Function). Kindle Edition. 
[^2]: An academic example as [closest pair algorithms exist](https://en.wikipedia.org/wiki/Closest_pair_of_points_problem#Time_bounds) that run in `O(nloglogn)` and even `O(n)` time.
[^3]: Roughgarden, Tim. Algorithms Illuminated: Part 1: The Basics (p. 108). (Function). Kindle Edition.
