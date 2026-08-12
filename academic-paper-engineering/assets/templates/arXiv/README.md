# arXiv 模板

## 快速开始

1. 复制 `main.tex` 并重命名
2. 修改内容，编译：

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## 模板类型

当前使用 NeurIPS 2018 模板，适用于：
- arXiv预印本投稿
- NeurIPS会议论文
- ICML会议论文
- ICLR会议论文

## 模板选项

修改 \usepackage 中的选项：

```latex
% 投稿版本（默认）
\usepackage[preprint]{nips_2018}

% 最终版本
\usepackage[final]{nips_2018}

% 不使用natbib
\usepackage[preprint, nonatbib]{nips_2018}
```

## 文件说明

- `nips_2018.sty` - NeurIPS 2018样式文件
- `main.tex` - 主文件示例

## arXiv提交指南

1. 使用 `[preprint]` 选项编译
2. 生成PDF文件
3. 上传到 https://arxiv.org/submit
4. 填写元数据（标题、作者、摘要、分类等）

## 常见会议模板

如需其他会议模板，可参考：
- NeurIPS: https://nips.cc/
- ICML: https://icml.cc/
- ICLR: https://iclr.cc/

## 编译器

推荐使用 pdfLaTeX

## 注意事项

1. arXiv接受PDFLaTeX编译的PDF
2. 确保所有图片文件都在同一目录
3. 如使用BibTeX，确保.bbl文件已生成
4. 可使用latexmk自动编译：`latexmk -pdf main.tex`
