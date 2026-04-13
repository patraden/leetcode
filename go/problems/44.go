package problems

/*
Given an input string (s) and a pattern (p),
implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

p contains only lowercase English letters, '?' or '*'.
s contains only lowercase English letters.
*/
func IsMatch(s string, p string) bool {

	// empty pattern setup
	prv := make([]bool, len(s)+1)
	prv[0] = true

	cur := make([]bool, len(s)+1)

	for j := range p {
		switch p[j] {
		case '*':
			ok := false
			for i := range len(s) + 1 {
				if prv[i] {
					ok = true
				}
				cur[i] = ok
			}
		case '?':
			for i := range len(s) {
				cur[i+1] = prv[i]
			}
		default:
			for i := range len(s) {
				cur[i+1] = prv[i] && s[i] == p[j]
			}
		}
		copy(prv, cur)
		clear(cur)
	}

	return prv[len(s)]
}
