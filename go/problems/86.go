package problems

import "leetcode/datastructures/linkedlist"

type ListNode = linkedlist.ListNode

func partition(head *ListNode, x int) *ListNode {

	var ls, le *ListNode
	ls = &ListNode{}
	le = ls

	var rs, re *ListNode
	rs = &ListNode{}
	re = rs

	c := head
	for c != nil {
		if c.Val < x {
			le.Next = c
			le = c
		} else {
			re.Next = c
			re = c
		}
		c = c.Next
	}

	re.Next = nil
	le.Next = rs.Next

	return ls.Next
}
