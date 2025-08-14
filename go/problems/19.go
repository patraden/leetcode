package problems

import "leetcode/datastructures/linkedlist"

func RemoveNthFromEnd(head *linkedlist.ListNode, n int) *linkedlist.ListNode {
	ref := &linkedlist.ListNode{
		Val:  -1,
		Next: head,
	}
	root := ref

	node := head
	count := 1
	for node != nil {
		if count > n {
			ref = ref.Next
		}
		node = node.Next
		count++
	}

	// delete node
	ref.Next = ref.Next.Next

	return root.Next
}
