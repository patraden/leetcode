package problems

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {

	stack := []*TreeNode{}
	res := root.Val
	current := root
	count := 0

	for count < k {
		if current != nil {
			stack = append(stack, current)
			current = current.Left
		} else if len(stack) > 0 {
			elem := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			count += 1
			res = elem.Val
			if elem.Right != nil {
				current = elem.Right
			}
		} else {
			panic("not enough elements")
		}
	}

	return res
}
