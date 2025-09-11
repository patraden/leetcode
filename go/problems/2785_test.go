package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSortVowels(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		s    string
		want string
	}{
		{"test 1", "lEetcOde", "lEOtcede"},
		{"test 1", "lYmpH", "lYmpH"},
		{"test 3", "lEedadasadsAAAtUUUcOde", "lAAdAdEsOdsUUUtaaacede"},
		{"test 4", "U", "U"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {

			t.Parallel()
			got := sortVowels(tt.s)
			assert.Equal(t, tt.want, got)
		})
	}
}
