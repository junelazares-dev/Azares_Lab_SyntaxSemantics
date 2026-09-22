# CS413 — Laboratory Activity No. 2  
From Syntax to Semantics: Grammar Checker and Evaluator

Group Members:  
- Junel Azares  
- Robylyn Flores  
- Aira Joy Hitta  
- Kc Oseo

Section: BSCS 4-1 
Date: September 22, 2026  

## Overview

This repository contains our implementation of a recursive-descent parser that:

- Checks the **syntax** of arithmetic expressions  
- Evaluates the **semantics** (computes the value) if the expression is valid  
- Follows the grammar: `expr → term → factor` to enforce operator precedence  
- Supports digits, `+`, `-`, `*`, `/`, and parentheses  

## Files

- `syntax_semantics.py` — Main Python source code  
- `flowchartdrawio.png` — Recursive-descent flowchart  
- `Required_Test_Cases.docx` — Screenshots/text of required test cases  
- `Reflection Question-Answers.docx` — Answers to reflection questions  

## How to Run

```bash
python syntax_semantics.py
```

Then enter an expression such as:

```text
3+4*2
(3+4)*2
8/2-1
3++4
(3+4
2+3*4
```

## Grammar

```text
expr   → term { (+ | -) term }
term   → factor { (* | /) factor }
factor → ( expr ) | digit
digit  → 0 | 1 | 2 | ... | 9
```

## Notes

- Only single-digit integers are supported (as required by the activity).  
- Division by zero is detected and reported as an evaluation error.  
- The program rejects invalid syntax and leftover/unexpected tokens.
