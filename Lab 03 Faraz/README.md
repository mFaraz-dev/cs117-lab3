
# Comparison between Assembly and Python

**1. What did you notice about registers and instructions?**

**Registers**
* Registers are small and fast storage units within the CPU
* They store data temporarily
* Using registers is much faster

**Instructions**
* Instructions are command that tell CPU what to do
* Each instruction carry out only one operation

**2. How is coding in Assembly different from Python?**

Assembly is more difficult to understand and include complexity while python is simple and more understandable. On the other hand, assembly is much faster and efficient and python is less memory efficient. Assembly is more likely giving one by one instruction directly to CPU.

**3. Why is Python easier/faster for building the same project?**

Python is simple language with plain syntax. It is more understandable and readable. It contains many built-in functions. It does not rely on hardware. And it is faster as it can produce more results with less code.

**4. Which features of Python help abstraction (variables, functions, loops)?**
* Variables let you store data and values
* Functions let you convert code in reusable modules
* Loops can do similar task for certain number of times without writing again and again

# 3. Comparison Table

| Feature             | Assembly Example        | Python Example          | Notes                                                                 |
|---------------------|-------------------------|-------------------------|----------------------------------------------------------------------|
| Variable storage    | `MOV EAX, 5`            | `x = 5`                 | Assembly uses CPU registers, Python uses memory variables.           |
| Printing output     | `INT 21h`               | `print("Hello")`        | Python has built-in print, Assembly uses OS interrupts.              |
| Arithmetic          | `ADD AX, BX`            | `x + y`                 | Python is simpler, Assembly requires explicit instructions.          |
| Input               | `INT 21h (AH=1)`        | `input()`               | Python input is one line, Assembly requires interrupts.              |
`# comment`             | Syntax differs but both supported.                                   |