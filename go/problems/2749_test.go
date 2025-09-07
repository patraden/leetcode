package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMakeTheIntegerZero(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		num1 int
		num2 int
		want int
	}{
		{"test 1", 3, -2, 3},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {

			t.Parallel()
			got := makeTheIntegerZero(tt.num1, tt.num2)
			assert.Equal(t, tt.want, got)
		})
	}
}
