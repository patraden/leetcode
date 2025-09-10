package problems

func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	hasIntersection := func(a, b []int) bool {
		seen := make(map[int]struct{}, len(a))
		for _, x := range a {
			seen[x] = struct{}{}
		}
		for _, y := range b {
			if _, ok := seen[y]; ok {
				return true
			}
		}
		return false
	}

	people := []int{}
	seen := make(map[int]struct{})

	for _, pair := range friendships {
		if hasIntersection(languages[pair[0]-1], languages[pair[1]-1]) {
			continue
		}

		for _, u := range pair {
			if _, ok := seen[u]; !ok {
				seen[u] = struct{}{}
				people = append(people, u)
			}
		}
	}

	res := 0
	counter := make([]int, n+1)

	for _, i := range people {
		for _, lan := range languages[i-1] {
			counter[lan]++
			res = max(res, counter[lan])
		}
	}

	return len(people) - res
}
