package problems

func merge88(nums1 []int, m int, nums2 []int, n int) {
	nums1Copy := make([]int, m)
	for i := range m {
		nums1Copy[i] = nums1[i]
	}

	var i, p1, p2 int
	for p1 < m && p2 < n {
		if nums1Copy[p1] < nums2[p2] {
			nums1[i] = nums1Copy[p1]
			p1++
		} else {
			nums1[i] = nums2[p2]
			p2++
		}
		i++
	}

	for p1 < m {
		nums1[i] = nums1Copy[p1]
		p1++
		i++
	}

	for p2 < n {
		nums1[i] = nums2[p2]
		p2++
		i++
	}
}
