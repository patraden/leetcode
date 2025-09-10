package problems

import (
	"fmt"
	"testing"
)

func TestMerge88(t *testing.T) {
	t.Parallel()

	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3
	merge88(nums1, m, nums2, n)

	fmt.Println(nums1)

	nums1 = []int{5, 6, 7, 0, 0, 0}
	m = 3
	nums2 = []int{1, 2, 2}
	n = 3
	merge88(nums1, m, nums2, n)

	fmt.Println(nums1)

	nums1 = []int{1}
	m = 1
	nums2 = []int{}
	n = 0
	merge88(nums1, m, nums2, n)

	fmt.Println(nums1)

	nums1 = []int{0}
	m = 0
	nums2 = []int{1}
	n = 1
	merge88(nums1, m, nums2, n)

	fmt.Println(nums1)
}
