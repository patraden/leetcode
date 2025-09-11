package problems

func sortVowels(s string) string {

	b := []byte(s)
	counter := make([]int, 10)
	runeIndex := func(r rune) int {
		switch r {
		case 'A':
			return 0
		case 'E':
			return 1
		case 'I':
			return 2
		case 'O':
			return 3
		case 'U':
			return 4
		case 'a':
			return 5
		case 'e':
			return 6
		case 'i':
			return 7
		case 'o':
			return 8
		case 'u':
			return 9
		default:
		}
		return -1
	}

	indexRune := func(i int) rune {
		switch i {
		case 0:
			return 'A'
		case 1:
			return 'E'
		case 2:
			return 'I'
		case 3:
			return 'O'
		case 4:
			return 'U'
		case 5:
			return 'a'
		case 6:
			return 'e'
		case 7:
			return 'i'
		case 8:
			return 'o'
		case 9:
			return 'u'
		default:
		}
		return '0'
	}

	for _, c := range s {
		if runeIndex(c) > -1 {
			counter[runeIndex(c)]++
		}
	}

	p := 0
	for i, c := range s {
		if runeIndex(rune(c)) > -1 {
			for p < 10 && counter[p] == 0 {
				p++
			}

			b[i] = byte(indexRune(p))
			counter[p]--
		}
	}

	return string(b)
}
