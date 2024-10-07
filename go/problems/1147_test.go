package problems

import "testing"

func TestLongestDecomposition(t *testing.T) {
	tests := []struct {
		name string
		text string
		want int
	}{
		{
			name: "test 1",
			text: "ghiabcdefhelloadamhelloabcdefghi",
			want: 7,
		},
		{
			name: "test 2",
			text: "merchant",
			want: 1,
		},
		{
			name: "test 3",
			text: "antaprezatepzapreanta",
			want: 11,
		},
		{
			name: "test 4",
			text: "abba",
			want: 4,
		},
		{
			name: "test 4",
			text: "z",
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestDecomposition(tt.text); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}
}
