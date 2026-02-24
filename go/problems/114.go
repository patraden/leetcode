package problems

func flattenHelper(root *TreeNode) *TreeNode {
	if root.Left == nil && root.Right == nil {
		return root
	}

	if root.Left == nil && root.Right != nil {
		return flattenHelper(root.Right)
	}

	if root.Left != nil && root.Right == nil {
		e := flattenHelper(root.Left)
		l := root.Left
		root.Right = l
		root.Left = nil
		return e
	}

	el := flattenHelper(root.Left)
	er := flattenHelper(root.Right)

	l, r := root.Left, root.Right
	root.Left, root.Right = nil, l

	el.Right = r

	return er
}

func flatten(root *TreeNode) {
	if root != nil {
		flattenHelper(root)
	}
}
