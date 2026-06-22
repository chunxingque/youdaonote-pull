#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'youdaonote/最后others/前路探寻/方向和能做的事情.lxtable'

print(f'正在读取文件：{input_file}')
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print('JSON 解析成功')
sheets = data.get('data', {}).get('sheets', {})
print(f'找到 {len(sheets)} 个 sheet')

# 解析第一个 sheet
first_sheet_key = list(sheets.keys())[0]
first_sheet = sheets[first_sheet_key]
cells = first_sheet.get('cells', {})
print(f'Sheet {first_sheet_key} 有 {len(cells)} 个单元格')

# 找出最大行和列
max_row, max_col = 0, 0
for cell_key in cells.keys():
    try:
        row, col = map(int, cell_key.split(','))
        max_row = max(max_row, row)
        max_col = max(max_col, col)
    except:
        pass

print(f'表格大小：{max_row+1} 行 x {max_col+1} 列')

# 生成 Markdown
md_lines = []
md_lines.append('# 方向和能做的事情\n')

headers = []
for col in range(max_col + 1):
    cell_key = f'0,{col}'
    cell_data = cells.get(cell_key, {})
    header_value = cell_data.get('0', f'列{col+1}')
    headers.append(str(header_value))

md_lines.append('## Sheet 0\n')
md_lines.append('| ' + ' | '.join(headers) + ' |')
md_lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')

for row in range(1, max_row + 1):
    row_data = []
    for col in range(max_col + 1):
        cell_key = f'{row},{col}'
        cell_data = cells.get(cell_key, {})
        cell_value = cell_data.get('0', '')
        row_data.append(str(cell_value) if cell_value else '')
    md_lines.append('| ' + ' | '.join(row_data) + ' |')

# 保存
output_file = os.path.splitext(input_file)[0] + '.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f'成功：已转换为 Markdown：{output_file}')
