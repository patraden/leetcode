package solutions

import scala.annotation.tailrec

object MergeSort {

  /**
   * Generic sorted array binary search log(n)
   * @return found index in Array or -1
   */
  def binarySearch[T](item: T, array: Array[T])(implicit ord: Ordering[T]): Int = {
    @tailrec
    def binarySearchHelper(start: Int, end: Int, item: T, array: Array[T]): Int =
      if (end < start) -1
      else {
        val mid = (start + end) / 2
        if (ord.equiv(item, array(mid)))
          mid
        else if (ord.lt(item, array(mid)))
          binarySearchHelper(start, mid - 1, item, array)
        else binarySearchHelper(mid + 1, end, item, array)
      }

    binarySearchHelper(0, array.length - 1, item, array)
  }

  def mergeRec[T](xs: List[T], ys: List[T])(implicit ord: Ordering[T]): List[T] =
    (xs, ys) match {
      case (Nil, _) => ys
      case (_, Nil) => xs
      case (x :: xs1, y :: ys1) =>
        if (ord.lt(x, y)) x :: mergeRec(xs1, ys)
        else y :: mergeRec(xs, ys1)
    }

  /**
   * List Merge Sort Recursively.
   * Complexity is n*log(n):
   */
  def sortRec[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = {
    val n = xs.length / 2
    if (n == 0) xs
    else {
      val (ys, zs) = xs splitAt n
      mergeRec(sortRec(ys), sortRec(zs))
    }
  }
}