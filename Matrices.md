aliases: [Matrix multiplication] 
tags: [linear algebra]

- seedling date: 2026-11-16 source: ""
    

# 🧠 Feynman Summary

> [!summary] Matrices transform a vector space and are analogous to functions, then matrix multiplication is analogous to function composition

## 📝 Core Concept

One possible view of a matrix a function $T(\vec{v}) = \vec{w}$ on a [[Vector space]], where each column is the function evaluated in one of the basis of $V$ decomposed in the basis of $W$. 

Therefore matrix multiplication is composition of functions, not all functions are invertible and that is why not all matrices are invertible, one can check if a matrix if invertible if the determinant $|M| != 0$. 

- **Mechanism:** How does it work? 
	Let's take the Fibonacci recurrence relation as example
	We have the following relation: $f(n) = f(n - 1) + f(n - 2)$ 
	With $f(1) = 0$ and $f(2) = 1$
	If we use linear algebra to express this we have	$$F(\begin{pmatrix} a \\ b \end{pmatrix}) = \begin{pmatrix} a+b \\ a \end{pmatrix}$$
	The we eval the function on the basis of $V$ and express the result as the basis in $W$.	$$F(\begin{pmatrix}1 \\ 0\end{pmatrix}) = \begin{pmatrix}1 \\ 1\end{pmatrix} = 1 \begin{pmatrix}1 \\ 0\end{pmatrix} + 1\begin{pmatrix}0 \\ 1\end{pmatrix}$$	$$F(\begin{pmatrix}0 \\ 1\end{pmatrix}) = \begin{pmatrix}1 \\ 0\end{pmatrix} = 1 \begin{pmatrix}1 \\ 0\end{pmatrix} + 0\begin{pmatrix}0 \\ 1\end{pmatrix}$$
	Then, as I mentioned before, the coefficients of a column are the function evaluated the basis of $V$ expressed in the basis of $W$, so we have the matrix:	$$M = \begin{pmatrix}1 & 1 \\ 1 & 0\end{pmatrix}$$
	Continuing with this example we can show why matrix multiplication are considered as composition of functions. If we want to get the n term of the Fibonacci sequence we can express it as	$$F(n) = F(...F(F(1))$$
	Is clearly a composition of functions so we can use matrix multiplication to calculate this
	$$\begin{pmatrix}F(n)\\F(n - 1)\end{pmatrix} = M^nv$$ where $v$ is the vector of the base cases, you can do this with almost all linear recurrences, I don't think you can do this if there is a variable squared but I have to check. 
	_Check [[linear recurrences]] to check how to calc $F(n)$ in $O(k^3logn)$ where k is the amount of previous terms required_
### 💡 Self-Test (Active Recall)

> [!question]- Matrix multiplication is analogous to? _function composition or  space transformation_

## 🔗 Connections & Cross-Pollination

_How does this connect to what you already know? Cross boundaries between your topics (e.g., connecting a concept from 'Thinking, Fast and Slow' to Trading Psychology)._

- **Up (MOC):** [[MOC - System Design]] OR [[MOC - Quantum Computing]]
    
- **Related:** [[Name of a related note]]
    
- **Contrasts with:** [[Name of an opposing concept]]
    

## 📚 References

- Page / Chapter:
    Quantum Computing And Applied Approach. Chapter 12 
- Links: