/**
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 *
 * Constraints:
 * The number of nodes in each linked list is in the range [1, 100].
 * 0 <= Node.val <= 9
 * It is guaranteed that the list represents a number that does not have leading zeros.
 */

class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
  override def toString =
    if (next != null)
      s"${x}->${next.toString}"
    else
      s"${x}"
 }

object Solution extends App {

  private def toListNode(l: List[Int]): ListNode =
    if (l.tail.isEmpty) new ListNode(l.head)
    else new ListNode(l.head, toListNode(l.tail))

  private val l1E1 = toListNode(2 :: 4 :: 3 :: Nil)
  private val l2E1 = toListNode(5 :: 6 :: 4 :: Nil)
  private val loE1 = toListNode(7 :: 0 :: 8 :: Nil)

  private val l1E2 = toListNode(0 :: Nil)
  private val l2E2 = toListNode(0 :: Nil)
  private val loE2 = toListNode(0 :: Nil)

  private val l1E3 = toListNode(9 :: 9 :: 9 :: 9 :: 9 :: 9 :: 9 :: Nil)
  private val l2E3 = toListNode(9 :: 9 :: 9 :: 9 :: Nil)
  private val loE3 = toListNode(8 :: 9 :: 9 :: 9 :: 0 :: 0 :: 0 :: 1 :: Nil)

  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
    import scala.annotation.tailrec

    @tailrec
    def reverseListNode(node: ListNode, acc: ListNode = null): ListNode =
      if (node.next == null)
        new ListNode(node.x, acc)
      else
        reverseListNode(node.next, new ListNode(node.x, acc))

    @tailrec
    def addTwoNumbersRec(l1: ListNode, l2: ListNode, digit: Int = 0, acc: ListNode = null): ListNode = {
      (l1, l2) match {
        case (null, null) =>
          if (digit == 1) new ListNode(digit, acc) else acc
        case (null, l2) => addTwoNumbersRec(
            l1,
            l2.next,
            (l2.x + digit) / 10,
            new ListNode((l2.x + digit) % 10, acc)
        )
        case (l1, null) => addTwoNumbersRec(
          l1.next,
          l2,
          (l1.x + digit) / 10,
          new ListNode((l1.x + digit) % 10, acc)
        )
        case (l1, l2) => addTwoNumbersRec(
          l1.next,
          l2.next,
          (l1.x + l2.x + digit) / 10,
          new ListNode((l1.x + l2.x + digit) % 10, acc)
        )
      }
    }
    reverseListNode(addTwoNumbersRec(l1, l2))
  }

  println(addTwoNumbers(l1E1, l2E1))

}