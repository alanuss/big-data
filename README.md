# Big data portfolio

This repository contains a collection of all the activities related to big data, like pandas, numpy, matplotlib, seaborn, plotly, and many more.

## Requirements

This project uses 'uv' to manage the dependencies. You can install it using curl:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Also, it doesn't use `.ipynb` files, but instead `.py` files that are interpreted by `ipython` as notebooks, where each cell is separated by `# %%`. To run the files, you need to have a way to parse them and execute them. Heavily recommended using `nvim` and `iron.nvim` to run these files.

## Commands (iron.nvim)

- `<space>rr`: Starts/ends the Replyt session.
- `<space>sb`: Sends the current cell to the Replyt session.
- `<space>sl`: Sends the current line to the Replyt session.
