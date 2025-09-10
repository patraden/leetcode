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

	counter := make(map[int]int)
	for _, i := range people {
		for _, l := range languages[i-1] {
			counter[l]++
		}
	}

	res := len(people)
	for _, v := range counter {
		res = min(res, len(people)-v)
	}

	return res
}
