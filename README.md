# mmfont

[![Build Status](https://travis-ci.org/emoosx/mmfont.svg?branch=master)](https://travis-ci.org/emoosx/mmfont)

A simple python module which converts zawgyi <=> unicode strings. It is generated from [paytan](https://github.com/trhura/paytan) which utilizes the conversion rules from [parabaik](https://github.com/ngwestar/parabaik).

# Usage

The two main functions are named `uni512zg1` and `zg12uni51` for conversion between Zawgyi 1 and Unicode 5.1 encodings.

```python
from mmfont.converter import uni512zg1, zg12uni51
```

# License

MIT
