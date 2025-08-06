package problems

import "fmt"

func maxNumber321(nums1 []int, nums2 []int, k int) []int {
	res := []int{}

	max1 := make([]int, len(nums1))
	// max2 := make([]int, len(nums2))
	stack := []int{}

	for i, num := range nums1 {
		for len(stack) > 0 && nums1[stack[len(stack)-1]] < num {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			max1[j] = i
		}
		stack = append(stack, i)
	}

	fmt.Println(nums1, max1, stack)

	return res

}
