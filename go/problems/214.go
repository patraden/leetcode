package problems

const P int = 31
const M int = 1000_000_007

func shortestPalindrome(s string) string {
	hf, hb, pow := 0, 0, 1
	length := 0

	for i := 0; i < len(s); i++ {
		hf = (hf + int(s[i])*pow) % M
		hb = (hb*P + int(s[i])) % M
		pow = (pow * P) % M

		if hf == hb {
			length = i + 1
		}
	}

	runes := []rune(s[length:])
	n := len(runes)
	for i := 0; i < n/2; i++ {
		runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
	}

	return string(runes) + s
}
