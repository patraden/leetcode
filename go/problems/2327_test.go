package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPeopleAwareOfSecret(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name   string
		n      int
		delay  int
		forget int
		want   int
	}{
		{"test 1", 6, 2, 4, 5},
		{"test 2", 4, 1, 3, 6},
		{"test 3", 6, 1, 2, 2},
		{"test 4", 684, 18, 496, 653668527},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := peopleAwareOfSecret(tt.n, tt.delay, tt.forget)
			assert.Equal(t, tt.want, got)
		})
	}
}
