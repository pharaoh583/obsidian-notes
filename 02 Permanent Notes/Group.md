---
created: 2026-11-23 13:23
tags:
  - abstract_algebra
aliases:
  - Abelian group
---
# 🧠 Feynman Summary

> [!summary] _A group is a set of elements and one operation that combines them, where every operation stays inside the set and there is a way to undone or reverse the operation_

## 📝 Core Concept

- **Context / Problem:**
	A Group $(S, *)$ is a set $S$ equipped with an operation $*$, it should satisfy the following axioms:
	- It should have closure on the operation, that means $a, b \in S$ then  $a * b \in S$
	- It should be associative: $(a * b) * c = a * (b * c)$
	- It should have an operation neutral or identity element: $a*0 = 0*a = a$ (Where $0 \in S$ represent the identity and might not represent the number 0, it depends of the set)
	- Each element $a \in S$ should have an inverse such that $a*a^{-1} = a^{-1}*a = 0$ 
	There is another type of group called _Abelian group_ that also satisfies commutativity: $a*b = b*a$
	
	For example the set of real number ($\mathbf{R}$) does form an _Abelian group_ over the sum (+)
	- It satisfies the closure since $a + b \in \mathbf{R}$
	- It satisfies to be associative 
	- It has the neutral element or operation neutral $e = 0$ since $a + 0 = a$
	- It has an inverse $a^{-1} = -a$ , if we define the sum as $a + a^{-1} = a + (-a) = 0$
	- It satisfies commutativity 
	On the other hand, the set on natural numbers $\mathbf{N}$ does not form a group over the sum since there is no inverse or neutral element.

### 💡 Self-Test (Active Recall)
	
> [!question]- What is a group? _Is a set that supports an operation, each element should have an inverse, a neutral element, it should have closure and should be associative_

## 🔗 Connections & Cross-Pollination
- **Related:** [[Field]] [[Ring]]    

## 📚 References

- Page / Chapter:
    _Quantum Computing An Applied Approach_ (Hidary) page 269, 270