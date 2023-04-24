package solutions

import scala.math.{log, pow}

/**
 * I have changed original definition a little bit for a beauty of pattern matching.
 * And to avoid of working with nulls by using Option class.
 * However additional constructor accepts Array of nullable integers in case you have additional test cases.
 */
case class TreeNodeModified(
                             value: Int,
                             var left: Option[TreeNodeModified] = None,
                             var right: Option[TreeNodeModified] = None)

object TreeNodeModified {
  private val log2 = (x: Double) => log(x) / log(2.0)
  /**
   * Constructs root [[TreeNodeModified]] from an Array of nullable integers.
   */
  def apply(values: Array[Int]): TreeNodeModified = {
    assert(values.nonEmpty)
    val depth: Int = log2(values.length + 1).toInt
    val lastLevelSize = pow(2, depth - 1).toInt
    val n = values.length - lastLevelSize
    val nodes: Array[Option[TreeNodeModified]] = values.map{
      num =>
        if (num == null.asInstanceOf[Int]) None
        else Some(TreeNodeModified(value = num))
    }
    nodes.take(n).zipWithIndex.foreach{
        case (Some(node), i) =>
            node.left = nodes(2 * i + 1)
            node.right = nodes(2 * i + 2)
        case _ => throw new Exception("Unexpected behaviour")
    }
    nodes(0).get
  }
}
