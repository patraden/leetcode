package problems

import (
	"sort"
	"strconv"
)

func largestNumber(nums []int) string {

	sort.Slice(nums, func(i, j int) bool {
		n1, n2 := strconv.Itoa(nums[i]), strconv.Itoa(nums[j])
		c1, _ := strconv.Atoi(n1 + n2)
		c2, _ := strconv.Atoi(n2 + n1)
		return c1 > c2
	})

	var res string

	if nums[0] == 0 {
		return "0"
	}

	for _, num := range nums {
		res += strconv.Itoa(num)
	}

	return res

}
