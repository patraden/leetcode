package problems

func replaceNonCoprimes(nums []int) []int {
	stack := make([]int, 0, len(nums))
	stack = append(stack, nums[0])

	gdc := func(a, b int) int {
		if b > a {
			a, b = b, a
		}

		for b > 0 {
			a, b = b, a%b
		}

		return a
	}

	for i := 1; i < len(nums); i++ {
		num := nums[i]

		for len(stack) > 0 {
			prev := stack[len(stack)-1]
			g := gdc(num, prev)
			if g == 1 {
				break
			}

			num = prev * num / g
			stack = stack[:len(stack)-1]
		}

		stack = append(stack, num)
	}

	return stack
}
