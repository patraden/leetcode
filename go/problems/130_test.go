package problems

import "testing"

func TestSolve130(t *testing.T) {
	tests := []struct {
		name  string
		board [][]byte
		want  [][]byte
	}{
		{
			name: "test 1",
			board: [][]byte{
				{'X', 'X', 'X', 'X'},
				{'X', 'O', 'O', 'X'},
				{'X', 'X', 'O', 'X'},
				{'X', 'O', 'X', 'X'},
			},
			want: [][]byte{
				{'X', 'X', 'X', 'X'},
				{'X', 'X', 'X', 'X'},
				{'X', 'X', 'X', 'X'},
				{'X', 'O', 'X', 'X'},
			},
		},
		{
			name: "test 2",
			board: [][]byte{
				{'X', 'X', 'X', 'X'},
				{'X', 'X', 'O', 'X'},
				{'X', 'O', 'O', 'X'},
				{'X', 'X', 'X', 'X'},
			},
			want: [][]byte{
				{'X', 'X', 'X', 'X'},
				{'X', 'X', 'X', 'X'},
				{'X', 'X', 'X', 'X'},
				{'X', 'X', 'X', 'X'},
			},
		},
		{
			name: "test 3",
			board: [][]byte{
				{'X', 'X', 'X', 'X'},
				{'O', 'X', 'O', 'X'},
				{'X', 'O', 'O', 'X'},
				{'X', 'X', 'O', 'X'},
			},
			want: [][]byte{
				{'X', 'X', 'X', 'X'},
				{'O', 'X', 'O', 'X'},
				{'X', 'O', 'O', 'X'},
				{'X', 'X', 'O', 'X'},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			solve130(tt.board)
			for i := range tt.board {
				for j := range tt.board[i] {
					if tt.board[i][j] != tt.want[i][j] {
						t.Errorf("diff at index (%v, %v) got = %v, want %v", i, j, tt.board[i][j], tt.want[i][j])
					}
				}
			}
		})
	}
}
