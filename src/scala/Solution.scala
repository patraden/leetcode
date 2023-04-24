package solutions

import scala.annotation.tailrec

object Solution {

  @tailrec
  def fib(n: Int, preprevious: Int = 0, previous: Int = 1): Int = {
    n match {
      case 0 => preprevious
      case 1 => previous
      case 2 => preprevious + previous
      case n => fib(n - 1, previous, preprevious + previous)
    }
  }

  def uniquePaths(m: Int, n: Int): Int = {
    val paths = Array.ofDim[Int](m, n)
    for {
      i <- 0 until m
      j <- 0 until n
    } paths(i)(j) = 0
    for (i <- 0 until m) paths(i)(0) = 1
    for (j <- 0 until n) paths(0)(j) = 1
    for {
      i <- 1 until m
      j <- 1 until n
    } paths(i)(j) = paths(i-1)(j) + paths(i)(j-1)
    paths(m-1)(n-1)
  }

  def maxPathSum(root: TreeNodeModified): Int = {
    val (maxDiconnected, maxConnected) = maxPathSumHelper(root)
    maxDiconnected max maxConnected
  }

  /**
   *  Tree structure
   *        root value
   *        /      \
   *  left tree    right tree
   *
   *  Algo does depth first traversal starting from left most leaves.
   * @return tuple of two paths:
   *  1. maxConnected: Max path between left and right subtrees CONNECTED to root value (might be root value itself).
   *  2. maxDisconnected: Max path within this subtree which might be DISCONNECTED from root tree.
   *
   *  Some other considerations:
   *  I assume DFS traversal should be stack safe. In theory stack should not exceed O(2*logN) calls.
   *  With initial conditions of up to 3 * 10000 nodes it should max of 30 calls in a stack.
   */
  def maxPathSumHelper(root: TreeNodeModified): (Int, Int) =
    root match {
      case TreeNodeModified(value, None, None) => (value, value)

      case TreeNodeModified(value, Some(left), None) =>
        val (lmaxDisconnected, lmaxConnected) = maxPathSumHelper(left)
        val maxConnected = value max (value + lmaxConnected)
        val maxDisconnected = maxConnected max lmaxDisconnected
        (maxDisconnected, maxConnected)

      case TreeNodeModified(value, None, Some(right)) =>
        val (rmaxDisconnected, rmaxConnected) = maxPathSumHelper(right)
        val maxConnected = value max (value + rmaxConnected)
        val maxDisconnected = maxConnected max rmaxDisconnected
        (maxDisconnected, maxConnected)

      case TreeNodeModified(value, Some(left), Some(right)) =>
        val (lmaxDisconnected, lmaxConnected) = maxPathSumHelper(left)
        val (rmaxDisconnected, rmaxConnected) = maxPathSumHelper(right)
        val maxConnected = value max (value + (lmaxConnected max rmaxConnected))
        val maxDiconnected =
          maxConnected max
          lmaxDisconnected max
          rmaxDisconnected max
          (lmaxConnected + value + rmaxConnected)
        (maxDiconnected, maxConnected)
    }

  /**
   * n*log(n) algorithm
   */
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    import MergeSort.{sortRec, binarySearch}
    val numsFiltered = nums.zipWithIndex.filter{ case(num,_) => num < target }
    val twins = numsFiltered.filter{ case (num, _) => num * 2 == target }.map{ case (_, i) => i}
    if (twins.length == 2)
      twins
    else {
      implicit val ord: Ordering[(Int, Int)] =
        (x: (Int, Int), y: (Int, Int)) => (x, y) match {
          case ((numx,ix), (numy, iy)) =>
            if (numx == numy && ix == iy) -1 // avoid self find in binary search
            else numx - numy
        }
      val numsSorted = sortRec(numsFiltered.toList).toArray
      numsSorted.
        filter{ case(num,i) => binarySearch((target-num, i), numsSorted) > -1 }.
        map{ case (_, i) => i }
    }
  }

  def trap(height: Array[Int]): Int = {
    @tailrec
    def trapHelper(height: Array[Int], acc: Int = 0): Int = {
      val zeroCount = height.dropWhile(_ == 0).reverse.dropWhile(_ == 0).count(_ == 0)
      if (zeroCount == 0) acc
      else trapHelper(height.map{num => if (num != 0) num - 1 else num }, acc + zeroCount)
    }
    trapHelper(height)
  }

}
