package problems

import "testing"

func TestMinExtraChar2707(t *testing.T) {
	tests := []struct {
		name       string
		s          string
		dictionary []string
		want       int
	}{
		{
			name:       "test 1",
			s:          "leetscode",
			dictionary: []string{"leet", "code", "leetcode"},
			want:       1,
		},
		{
			name:       "test 2",
			s:          "sayhelloworld",
			dictionary: []string{"hello", "world"},
			want:       3,
		},
		{
			name: "test 3",
			s:    "dwmodizxvvbosxxw",
			dictionary: []string{
				"ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq",
				"r", "txhe", "e", "wmo", "cehy", "tskz", "ds", "kzbu",
			},
			want: 7,
		},
		{
			name: "test 4",
			s:    "azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf",
			dictionary: []string{
				"na", "i", "edd", "wobow", "kecv", "b", "n", "or",
				"jj", "zul", "vk", "yeb", "qnfac", "azv", "grtjba",
				"yswmjn", "xowio", "u", "xi", "pcmatm", "maqnv",
			},
			want: 15,
		},
		{
			name: "test 5",
			s:    "cxyhamygqut",
			dictionary: []string{
				"r", "t", "h", "j", "ygq", "ut", "o", "b", "e", "rsn", "vr", "lxp", "tx",
				"az", "sqn", "nh", "yn", "yha", "fai", "zv", "rc", "q", "phd", "lyh",
				"uja", "ti", "pmu", "mkc", "cxl", "jgg", "twf", "p", "yr", "we", "qy",
				"xf", "ha", "v", "kd", "adx", "fni", "qwc", "mbj",
			},
			want: 3,
		},
		{
			name: "test 6",
			s:    "metzeaencgpgvsckjrqafkxgyzbe",
			dictionary: []string{
				"zdzz", "lgrhy", "r", "ohk", "zkowk", "g", "zqpn", "anoni", "ka", "qafkx", "t",
				"jr", "xdye", "mppc", "bqqb", "encgp", "yf", "vl", "ctsxk", "gn", "cujh", "ce",
				"rwrpq", "tze", "zxhg", "yzbe", "c", "o", "hnk", "gv", "uzbc", "xn", "kk", "ujjd",
				"vv", "mxhmv", "ugn", "at", "kumr", "ensv", "x", "uy", "gb", "ae", "jljuo", "xqkgj",
			},
			want: 5,
		},
		{
			name: "test 7",
			s:    "kevlplxozaizdhxoimmraiakbak",
			dictionary: []string{
				"yv", "bmab", "hv", "bnsll", "mra", "jjqf", "g", "aiyzi", "ip", "pfctr", "flr", "ybbcl", "biu",
				"ke", "lpl", "iak", "pirua", "ilhqd", "zdhx", "fux", "xaw", "pdfvt", "xf", "t", "wq", "r",
				"cgmud", "aokas", "xv", "jf", "cyys", "wcaz", "rvegf", "ysg", "xo", "uwb",
				"lw", "okgk", "vbmi", "v", "mvo", "fxyx", "ad", "e",
			},
			want: 9,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minExtraChar2707(tt.s, tt.dictionary); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}

}
