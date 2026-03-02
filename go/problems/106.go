package problems

func buildTree(inorder []int, postorder []int) *TreeNode {

	ihash := map[int]int{}
	for i, v := range inorder {
		ihash[v] = i
	}

	var build func(idx, start, end int) *TreeNode
	build = func(idx, start, end int) *TreeNode {
		if !(0 <= idx && idx < len(postorder)) {
			return nil
		}

		m := ihash[postorder[idx]]
		if start >= end || !(start <= m && m < end) {
			return nil
		}

		root := &TreeNode{Val: postorder[idx]}
		rightSize := end - m - 1
		root.Left = build(idx-1-rightSize, start, m)
		root.Right = build(idx-1, m+1, end)

		return root
	}

	return build(len(postorder)-1, 0, len(postorder))

}
