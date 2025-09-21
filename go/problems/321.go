package problems

import "slices"

func maxNumber321(nums1 []int, nums2 []int, k int) []int {
	res := make([]int, k)
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}

	maxNum := func(size int, nums []int) []int {
		stack := []int{}
		for i, digit := range nums {
			for len(stack) > size-min(size, len(nums)-i) && digit > stack[len(stack)-1] {
				stack = stack[:len(stack)-1]
			}

			if len(stack) < size {
				stack = append(stack, digit)
			}
		}
		return stack
	}

	merge := func(n1, n2 []int) []int {
		if len(n1) == 0 {
			return n2
		}
		if len(n2) == 0 {
			return n1
		}

		res := make([]int, 0, len(n1)+len(n2))

		p1, p2 := 0, 0
		for p1 < len(n1) && p2 < len(n2) {
			if n1[p1] > n2[p2] {
				res = append(res, n1[p1])
				p1++
				continue
			}

			if n1[p1] < n2[p2] {
				res = append(res, n2[p2])
				p2++
				continue
			}

			i, j := p1, p2
			for i < len(n1) && j < len(n2) && n1[i] == n2[j] {
				i++
				j++
			}

			if i == len(n1) || (j < len(n2) && n1[i] < n2[j]) {
				res = append(res, n2[p2])
				p2++
			}

			if j == len(n2) || (i < len(n1) && n1[i] > n2[j]) {
				res = append(res, n1[p1])
				p1++
			}

		}

		res = append(res, n1[p1:]...)
		res = append(res, n2[p2:]...)

		return res
	}

	for m := range min(len(nums1), k) + 1 {
		if k-m <= len(nums2) {
			n1 := maxNum(m, nums1)
			n2 := maxNum(k-m, nums2)
			num := merge(n1, n2)
			if slices.Compare(num, res) > 0 {
				res = num
			}
		}
	}

	return res

}
