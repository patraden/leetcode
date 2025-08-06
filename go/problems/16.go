package problems

import (
	"sort"
)

func Abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

// Brute force algo O(N^3)
func ThreeSumClosestBrute(nums []int, target int) int {
	res := nums[0] + nums[1] + nums[2]
	for i := range nums {
		for j := i + 1; j < len(nums); j++ {
			for m := j + 1; m < len(nums); m++ {
				if Abs(target-nums[i]-nums[j]-nums[m]) < Abs(target-res) {
					res = nums[i] + nums[j] + nums[m]
				}
			}
		}
	}

	return res
}

// Two pointers algo O(N*Log(N))
func TwoSumClosesTwoPointers(nums []int, start, target int) int {
	p1, p2 := start, len(nums)-1
	s := nums[p1] + nums[p2]
	d := Abs(target - s)

	for p1 < p2 {
		if d == 0 {
			return s
		}

		if Abs(target-nums[p1]-nums[p2]) < d {
			d = Abs(target - nums[p1] - nums[p2])
			s = nums[p1] + nums[p2]
		}

		if (nums[p1] + nums[p2]) > target {
			p2--
		} else {
			p1++
		}
	}

	return s
}

// Two pointers algo O(N*N*Log(N))
func ThreeSumClosesTwoPointers(nums []int, target int) int {
	s := nums[0] + nums[1] + nums[2]
	if len(nums) == 3 {
		return s
	}

	sort.Ints(nums)
	d := Abs(target - s)

	var st int

	for i := 0; i < len(nums)-2; i++ {
		if d == 0 {
			return s
		}

		st = TwoSumClosesTwoPointers(nums, i+1, target-nums[i])
		if Abs(target-st-nums[i]) < d {
			d = Abs(target - st - nums[i])
			s = st + nums[i]
		}
	}

	return s
}

func ThreeSumClosest(nums []int, target int) int {
	// return threeSumClosestBrute(nums, target)
	return ThreeSumClosesTwoPointers(nums, target)
}
