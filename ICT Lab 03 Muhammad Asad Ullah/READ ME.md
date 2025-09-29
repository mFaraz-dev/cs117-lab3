
# Comparison between Assembly and Python

**1. What did you notice about registers and instructions?**

* Registers are small, fast storage locations inside the CPU. They hold data temporarily for calculations and memory operations.
* Instructions in Assembly are very low-level and specific (e.g., MOV AX, 5, ADD AX, BX). Each instruction corresponds directly to hardware operations.
* Unlike high-level languages, you must manage memory and registers manually, which requires more attention to detail.

**2. How is coding in Assembly different from Python?**

* Assembly is low-level and hardware-specific, while Python is high-level and abstract.
* In Assembly, you must explicitly manage registers, memory addresses, and instruction sequences.
* In Python, variables, memory management, and operations are abstracted away. You focus on logic, not hardware.
* Assembly code is longer and harder to read/write compared to Python’s concise and human-readable syntax.

**3. Why is Python easier/faster for building the same project?**

* Python provides built-in data types, libraries, and functions, reducing the amount of code needed.
* It is cross-platform and does not depend on hardware registers or CPU instructions.
* Python automatically manages memory, variables, and operations, which makes development much faster.

**4. Which features of Python help abstraction (variables, functions, loops)?**
* Variables: No need to manage registers manually; just assign with x = 5.
* Functions: Enable modularity and code reuse (def my_function(): ...).
* Loops: Provide simple iteration structures (for, while) instead of manually handling jump instructions.
* Libraries: Abstract away complex functionality (e.g., math, file handling, data analysis).

# 3. Comparison Table

| Feature             | Assembly Example        | Python Example          | Notes                                                                 |
|---------------------|-------------------------|-------------------------|----------------------------------------------------------------------|
| Variable storage    | `MOV EAX, 5`            | `x = 5`                 | Assembly uses CPU registers, Python uses memory variables.           |
| Printing output     | `INT 21h`               | `print("Hello")`        | Python has built-in print, Assembly uses OS interrupts.              |
| Arithmetic          | `ADD AX, BX`            | `x + y`                 | Python is simpler, Assembly requires explicit instructions.          |
| Input               | `INT 21h (AH=1)`        | `input()`               | Python input is one line, Assembly requires interrupts.              |
`# comment`             | Syntax differs but both supported.                                   |