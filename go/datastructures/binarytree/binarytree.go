package binarytree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type NodeR struct {
	Val   int
	Left  *NodeR
	Right *NodeR
	Next  *NodeR
}

func InOrderTraversal(root *NodeR, fn func(*NodeR)) {
	if root == nil {
		return
	}

	InOrderTraversal(root.Left, fn)
	fn(root)
	InOrderTraversal(root.Right, fn)
}
