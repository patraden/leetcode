package linkedlist

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func PrintList(node *ListNode) {
	cur := node
	for cur != nil {
		fmt.Println(cur.Val)
		cur = cur.Next
	}
}

func ArrayToList(a []int) *ListNode {
	if len(a) == 0 {
		return nil
	}

	res := &ListNode{Val: a[0]}
	cur := res

	for i := 1; i < len(a); i++ {
		cur.Next = &ListNode{Val: a[i]}
		cur = cur.Next
	}

	return res
}

func ListToArray(head *ListNode) []int {
	n := head
	res := make([]int, 0, 1000)

	for n != nil {
		res = append(res, n.Val)
		n = n.Next
	}

	return res
}
