package problems

import "testing"

func TestShortestPalindrome(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want string
	}{
		{
			name: "test 1",
			s:    "aacecaaa",
			want: "aaacecaaa",
		},
		{
			name: "test 2",
			s:    "abcd",
			want: "dcbabcd",
		},
		{
			name: "test 3",
			s:    "abba",
			want: "abba",
		},
		{
			name: "test 4",
			s:    "x",
			want: "x",
		},
		{
			name: "test 5",
			s:    "",
			want: "",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := shortestPalindrome(tt.s); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}

}
