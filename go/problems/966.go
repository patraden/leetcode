package problems

import (
	"strings"
)

func spellchecker966(wordlist []string, queries []string) []string {
	res := []string{}
	m1 := make(map[string][]string)
	m2 := make(map[string][]string)
	m3 := make(map[string][]string)

	for _, w := range wordlist {
		m1[w] = append(m1[w], w)

		wl := strings.ToLower(w)
		m2[wl] = append(m2[wl], w)

		wr := strings.Map(func(r rune) rune {
			switch r {
			case 'a', 'e', 'i', 'o', 'u':
				return '.'
			default:
				return r
			}
		}, wl)

		m3[wr] = append(m3[wr], w)
	}

	// fmt.Println("===========")
	// for k, v := range m1 {
	// 	fmt.Println(k, v)
	// }

	// fmt.Println("===========")
	// for k, v := range m2 {
	// 	fmt.Println(k, v)
	// }
	// fmt.Println("===========")
	// for k, v := range m3 {
	// 	fmt.Println(k, v)
	// }

	for _, q := range queries {
		if v, exists := m1[q]; exists && len(v) > 0 {
			res = append(res, v[0])
			continue
		}

		ql := strings.ToLower(q)
		if v, exists := m2[ql]; exists && len(v) > 0 {
			res = append(res, v[0])
			continue
		}

		qr := strings.Map(func(r rune) rune {
			switch r {
			case 'a', 'e', 'i', 'o', 'u':
				return '.'
			default:
				return r
			}
		}, ql)

		if v, exists := m3[qr]; exists && len(v) > 0 {
			res = append(res, v[0])
			continue
		}

		res = append(res, "")
	}

	return res
}
