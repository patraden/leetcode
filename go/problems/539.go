package problems

import "time"

const MinutesPerDay = 24 * 60

// Convert a time.Time object to an integer (0-1439)
func timeToMinutes(timestr string) int {
	t, err := time.Parse("15:04", timestr)
	if err != nil {
		return 0
	}

	minutes := t.Hour()*60 + t.Minute()
	if minutes == 0 {
		minutes = MinutesPerDay
	}
	return minutes
}

func FindMinDifference(timePoints []string) int {
	times := [MinutesPerDay + 1]bool{}

	for _, tstr := range timePoints {
		i := timeToMinutes(tstr)

		// duplicate time value
		if times[i] {
			return 0
		}

		if i > 0 {
			times[i] = true
		}
	}

	res := MinutesPerDay - 1
	last, first := 0, 0

	for j := 1; j < len(times); j++ {
		if ok := times[j]; ok {
			if first == 0 {
				first = j
			}

			if last > 0 && j-last < res {
				res = j - last
			}
			last = j
		}
	}

	if first+MinutesPerDay-last < res {
		res = first + MinutesPerDay - last
	}

	return res
}
