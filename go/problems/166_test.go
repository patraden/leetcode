package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFractionToDecimal(t *testing.T) {
	tests := []struct {
		name        string
		numerator   int
		denominator int
		want        string
	}{
		{"case 1", 1, 2, "0.5"},
		{"case 2", 2, 1, "2"},
		{"case 3", -2, 1, "-2"},
		{"case 4", 4, 333, "0.(012)"},
		{"case 5", 2, 3, "0.(6)"},
		{"case 6", 1, -3, "-0.(3)"},
		{"case 7", 1, 6, "0.1(6)"},
		{"case 8", -1, -2147483648, "0.0000000004656612873077392578125"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := fractionToDecimal(tt.numerator, tt.denominator)
			assert.Equal(t, tt.want, got)

		})
	}
}
