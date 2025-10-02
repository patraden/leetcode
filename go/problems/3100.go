package problems

func maxBottlesDrunk3100(numBottles int, numExchange int) int {
	res := numBottles
	empty := numBottles
	full := 0
	for {
		if empty >= numExchange {
			full++
			empty -= numExchange
			numExchange++
			continue
		}

		if full > 0 {
			res += full
			empty += full
			full = 0
			continue
		}

		break
	}

	return res
}
