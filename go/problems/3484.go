package problems

import (
	"strconv"
	"strings"
)

type Spreadsheet struct {
	cells [26][]int
	size  int
}

func ConstructorSpreadsheet(rows int) Spreadsheet {
	cells := [26][]int{}
	for i := range cells {
		cells[i] = make([]int, rows)
	}

	return Spreadsheet{
		size:  rows,
		cells: cells,
	}
}

func (sh *Spreadsheet) index(cell string) (int, int, bool) {
	c := cell[0]
	if c >= 'A' && c <= 'Z' {
		col := int(c - 'A')
		row, err := strconv.Atoi(cell[1:])
		if err != nil || row <= 0 || row > sh.size {
			return -1, -1, false
		}
		// convert 1-based row to 0-based index
		return col, row - 1, true
	}
	return -1, -1, false
}

func (sh *Spreadsheet) SetCell(cell string, value int) {
	if col, row, ok := sh.index(cell); ok {
		sh.cells[col][row] = value
	}
}

func (sh *Spreadsheet) ResetCell(cell string) {
	sh.SetCell(cell, 0)
}

func (sh *Spreadsheet) GetValue(formula string) int {
	formula = strings.TrimPrefix(formula, "=")
	tokens := strings.Split(formula, "+")
	sum := 0

	for _, tok := range tokens {
		tok = strings.TrimSpace(tok)
		if col, row, ok := sh.index(tok); ok {
			sum += sh.cells[col][row]
			continue
		}
		// try number
		if n, err := strconv.Atoi(tok); err == nil {
			sum += n
		}
	}
	return sum
}
