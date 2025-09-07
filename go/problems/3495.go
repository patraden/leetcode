package problems

func minOperations3495(queries [][]int) int64 {
	var res int64

	m := map[int][3]int{
		1:  {1, 3, 3},
		2:  {4, 15, 12},
		3:  {16, 63, 48},
		4:  {64, 255, 192},
		5:  {256, 1023, 768},
		6:  {1024, 4095, 3072},
		7:  {4096, 16383, 12288},
		8:  {16384, 65535, 49152},
		9:  {65536, 262143, 196608},
		10: {262144, 1048575, 786432},
		11: {1048576, 4194303, 3145728},
		12: {4194304, 16777215, 12582912},
		13: {16777216, 67108863, 50331648},
		14: {67108864, 268435455, 201326592},
		15: {268435456, 1073741823, 805306368},
	}

	detectRange := func(num int) int {
		res := 0
		for num > 0 {
			res++
			num = num >> 2
		}
		return res
	}

	var count int64
	for _, query := range queries {
		count = 0
		nl, nr := query[0], query[1]
		l, r := detectRange(nl), detectRange(nr)
		switch {
		case l == r:
			count += int64((nr - nl + 1) * l)
		case r-l > 1:
			count += int64((m[l][1] - nl + 1) * l)
			count += int64((nr - m[r][0] + 1) * r)
			for k := l + 1; k < r; k++ {
				count += int64(m[k][2] * k)
			}
		default:
			count += int64((m[l][1] - nl + 1) * l)
			count += int64((nr - m[r][0] + 1) * r)
		}

		res += count/2 + count%2
	}

	return res
}
