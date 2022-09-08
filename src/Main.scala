import solutions.TreeNodeModified
import solutions.Solution.{fib, uniquePaths, maxPathSum, twoSum, trap}

object Main extends App {
  val nullInt = null.asInstanceOf[Int]

  val a = Array(0,1,0,2,1,0,1,3,2,1,2,1,0,0)
  println(a.mkString("Array(", ", ", ")"))
  println(trap(a))

  val b = Array(4,2,0,3,2,5)
  println(b.mkString("Array(", ", ", ")"))
  println(trap(b))


  import solutions.MergeSort.binarySearch

//  val sumOfTwo1 = twoSum(Array(2,7,11,15), 9)
//  println(sumOfTwo1.mkString("Array(", ", ", ")"))
//  val sumOfTwo2 = twoSum(Array(3,2,4), 6)
//  println(sumOfTwo2.mkString("Array(", ", ", ")"))
//  val sumOfTwo3 = twoSum(Array(3,3), 6)
//  println(sumOfTwo3.mkString("Array(", ", ", ")"))

  import solutions.MergeSort.{sortRec, binarySearch}
//  val a = Array((3,0),(3,1))
//  implicit val ord: Ordering[(Int, Int)] =
//    (x: (Int, Int), y: (Int, Int)) => (x, y) match {
//      case ((numx, ix), (numy, iy)) =>
//        if (numx == numy && ix == iy ) -1
//        else if (numx == numy && ix != iy) 0
//        else numx - numy
//    }
//  println(sortRec(a.toList))
  //  (0 to 30).foreach(n => println(fib(n)))

//  println(uniquePaths(3,7))
//  println(uniquePaths(3,2))
//  println(uniquePaths(3,3))

//  val tree = TreeNodeModified(Array(50))
//  println(maxPathSum(tree))
//  val tree2 = TreeNodeModified(Array(1,2,3))
//  println(maxPathSum(tree2))
//  println(maxPathSum(tree2.left.get))
//  println(maxPathSum(tree2.right.get))
//  val tree3 = TreeNodeModified(Array(-10, 9, 20, null.asInstanceOf[Int], null.asInstanceOf[Int], 15, 7))
//  println(maxPathSum(tree3))
//
//  val tree4 = TreeNodeModified(
//    Array(10,
//      -11, 24,
//      12, 15, 70, -42,
//      nullInt, nullInt, nullInt, nullInt, -5, nullInt, 2, 10
//  )
//  )
//  println(maxPathSum(tree4))
//
//  val tree5 = TreeNodeModified(
//    Array(24,
//      70, -42,
//      -5, nullInt, 2, 10
//    )
//  )
//  println(maxPathSum(tree5))
//
//  val tree6 = TreeNodeModified(
//    Array(-42,
//      2, 10,
//    )
//  )
//  println(maxPathSum(tree6))
}
