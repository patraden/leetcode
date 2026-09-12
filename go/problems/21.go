package problems

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	root := &ListNode{}

	f, s, res := list1, list2, root

	for f != nil && s != nil {
		if f.Val < s.Val {
			res.Next = f
			f = f.Next
		} else {
			res.Next = s
			s = s.Next
		}
		res = res.Next
	}

	if s != nil {
		res.Next = s
	}

	if f != nil {
		res.Next = f
	}

	return root.Next
}
