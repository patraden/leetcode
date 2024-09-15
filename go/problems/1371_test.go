package problems

import "testing"

func TestFindTheLongestSubstring(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want int
	}{
		{
			name: "test 1",
			s:    "eleetminicoworoep",
			want: 13,
		},
		{
			name: "test 2",
			s:    "leetcodeisgreat",
			want: 5,
		},
		{
			name: "test 3",
			s:    "bcbcbc",
			want: 6,
		},
		{
			name: "test 4",
			s:    "b",
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FindTheLongestSubstring(tt.s); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}
}
