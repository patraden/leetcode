package problems

func deleteDuplicates(head *ListNode) *ListNode {
	c := map[int]int{}

	n := head
	for n != nil {
		c[n.Val]++
		n = n.Next
	}

	dummy := &ListNode{}
	m := dummy

	n = head
	for n != nil {
		if c[n.Val] == 1 {
			m.Next = n
			m = n
		}
		n, n.Next = n.Next, nil
	}

	return dummy.Next
}
