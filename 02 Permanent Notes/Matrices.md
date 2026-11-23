---
created: 2026-11-16 14:41
aliases:
  - Matrix multiplication
tags:
  - linear_algebra
---
# 🧠 Feynman Summary

> [!summary] _Matrices transform a [[vector space]] and are analogous to functions, then matrix multiplication is analogous to function composition_

## 📝 Core Concept

One possible view of a matrix is a function $T(\vec{v}) = \vec{w}$ on a [[Vector space]], where each column is the function evaluated in one of the basis of $V$ decomposed in the basis of $W$. 

Therefore matrix multiplication is composition of functions, not all functions are invertible and that is why not all matrices are invertible, one can check if a matrix if invertible if the determinant $|M| ≠ 0$. 

- **Mechanism:** How does it work? 
	Let's take the Fibonacci recurrence relation as example
	We have the following relation: $f(n) = f(n - 1) + f(n - 2)$ 
	With $f(1) = 0$ and $f(2) = 1$
	If we use linear algebra to express this we have	$$F(\begin{pmatrix} a \\ b \end{pmatrix}) = \begin{pmatrix} a+b \\ a \end{pmatrix}$$
	The we eval the function on the basis of $V$ and express the result as the basis of $W$.	$$F(\begin{pmatrix}1 \\ 0\end{pmatrix}) = \begin{pmatrix}1 \\ 1\end{pmatrix} = 1 \begin{pmatrix}1 \\ 0\end{pmatrix} + 1\begin{pmatrix}0 \\ 1\end{pmatrix}$$	$$F(\begin{pmatrix}0 \\ 1\end{pmatrix}) = \begin{pmatrix}1 \\ 0\end{pmatrix} = 1 \begin{pmatrix}1 \\ 0\end{pmatrix} + 0\begin{pmatrix}0 \\ 1\end{pmatrix}$$
	Then, as I mentioned before, the coefficients of a column are the function evaluated the basis of $V$ expressed in the basis of $W$, so we have the matrix:	$$M = \begin{pmatrix}1 & 1 \\ 1 & 0\end{pmatrix}$$
	If we apply the function we have that, for example: 
		$$F(\vec{v}_1) = \begin{pmatrix} f(1)+f(0) \\ f(1) \end{pmatrix} = \begin{pmatrix} f(2) \\ f(1) \end{pmatrix} = \vec{v}_2$$
	Therefor we have that $$F(n) = F(...F(F(\vec{v}))$$ where $\vec{v}$ are the base cases of the Fibonacci function.
	Continuing with this example we can show why matrix multiplication is considered to be composition of functions so we can use matrix multiplication to calculate this
	$$\begin{pmatrix}F(n)\\F(n - 1)\end{pmatrix} = M^n\vec{v}$$you can do this with almost all linear recurrences, I don't think you can do this if there is a variable squared but I have to check. 
	_Check [[linear recurrences]] to see how to calc $F(n)$ in $O(k^3logn)$ where k is the amount of previous terms required or the dimension of the recurrence matrix_
### 💡 Self-Test (Active Recall)

> [!question]- Matrix multiplication is analogous to? _function composition or  space transformation_

## 🔗 Connections & Cross-Pollination

_How does this connect to what you already know?_

- **Up (MOC):** [[MOC - Quantum Computing]]
  
## 📚 References

- Page / Chapter:
    Quantum Computing An Applied Approach by Jack D. Hidary. Chapter 12 
- Links: