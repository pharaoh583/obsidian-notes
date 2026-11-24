# 🧠 Master Study Vault & Knowledge System

Welcome to the central nervous system for your studies. This vault is designed to support a rigorous 4-hour daily study habit (totaling 33.25 hours/week) alongside an 8-hour workday, focusing on transitioning to Senior/Staff engineer, learning Japanese, mastering economics, understanding Quantum Computing or basically polymath  learning.

## 📊 Weekly Study Distribution

```mermaid
pie title Weekly hour distribution (33.25h Total)
    "Software development (8h)" : 8.0
    "New language / Japanese (7.75h)" : 7.75
    "Finances and economics (7h)" : 7.0
    "Quantum Computing (6h)" : 6.0
    "Other topics (4.5h)" : 4.5
```

## ⏱️ Time & Cognitive Energy Management

To sustain 4 hours of daily study without burning out, sessions follow strict time blocks based on the subject's cognitive load:

- **High-Load Blocks (50/10 Cycles):** 50 minutes of absolute focus followed by a 10-minute break. Used for complex subjects like Quantum Computing and Software Architecture. This prevents breaking your state of flow just as you load complex context into your working memory.
    
- **Dynamic Blocks (25/5 Cycles):** 25 minutes of focus followed by a 5-minute break. Used for subjects studied later at night (20:45 - 22:45), such as Languages and Finance. This shorter cycle keeps an agile pace when accumulated fatigue is highest.
    
- **High-Quality Rest:** During breaks, strictly avoid "cheap dopamine" (social media, short videos). Look out a window, hydrate, or walk around to give your prefrontal cortex the visual silence needed to consolidate information.
    

## 📅 Full Weekly Schedule

![[Schedule.png]]

## ⚙️ Retention & Execution Protocols

Taking notes is only step one. Mastery requires active retrieval and practical application:

- **Active Recall & Feynman Technique:** Never passively reread or highlight text. After reading, close the source and attempt to explain the concept from scratch. Your explanation must be simple enough to teach a beginner.
    
- **Spaced Repetition (Anki):** Use Anki during your morning routine (08:00 - 09:00) to review Japanese kanji, quantum computing formulas, and system design patterns.
    
- **Project-Based Learning (From Book to Repo):** For technical concepts, immediately build a minimal proof of concept. If you read about message queues, spin up a quick Docker environment; if you study quantum gates, write a Python script using Qiskit.
    

## 🔄 The Zettelkasten Workflow: Entry Life Cycle

```mermaid
flowchart TD
    %% Define Styles
    classDef inbox fill:#F3F4F6,stroke:#4B5563,stroke-width:2px,color:#1F2937
    classDef synthesis fill:#DBEAFE,stroke:#1E3A8A,stroke-width:2px,color:#1E3A8A
    classDef filter fill:#FEF3C7,stroke:#B45309,stroke-width:2px,color:#B45309
    classDef discard fill:#FCA5A5,stroke:#991B1B,stroke-width:2px,color:#7F1D1D
    classDef permanent fill:#D1FAE5,stroke:#065F46,stroke-width:2px,color:#065F46

    %% Nodes
    A[1. Inbox Capture<br/>During 50/10 or 25/5 cycles]:::inbox
    B[2. Sunday Synthesis Block<br/>17:30 - 18:30]:::synthesis
    C{3. Filtration}:::filter
    D[Discard]:::discard
    E[4. Translation<br/>Write in your own words]:::permanent
    F[5. Permanent Note<br/>Link to mastered concepts]:::permanent

    %% Flow
    A -->|Wait until Sunday| B
    B -->|Review Inbox| C
    C -->|Irrelevant / Duplicate| D
    C -->|Valuable Concept| E
    E -->|One idea per note| F
```

### The Inbox-to-Permanent Flow

1. **Inbox Capture (Weekdays):** During your high-load (50/10) or dynamic (25/5) study blocks, you will encounter rapid ideas, formulas, or connections. You dump these into your Inbox to avoid breaking your state of flow.
    
2. **Sunday Synthesis Block (17:30 - 18:30):** You leave the Inbox untouched until Sunday at 17:30. During this 1-hour block, you sit down specifically to consolidate everything learned during the week and clear the Inbox to zero.
    
3. **Filtration:** You review each rough idea. If an idea no longer makes sense, is easily found in documentation, or is not relevant to your core goals, you delete it.
    
4. **Translation (The Golden Rule):** For the concepts that survive filtration, you must translate them into your own words. You are strictly forbidden from copying and pasting text directly into a Permanent Note. You must also ensure that each note is atomic, containing only a single idea.
    
5. **Permanent Note Integration:** The final step is linking. Once the atomic note is written, you must connect it to concepts you already master to cross paradigms. For example, if your Inbox note was about an economic concept from your DeFi studies, you might link it to a Permanent Note about cognitive biases from behavioral economics.
    

## 📚 Curriculum Inputs (Current Reading List)

- **Software Architecture and coding:** 
  - [ ] _Clean code_ (Martin)
  - [ ] _AI in AWS_ (Fregly, Barth, Eigenbrode)
  - [ ] _Introduction to Software Architecture_ (Iturralde)
  - [ ] _Designing Data Intensive Applications_
  - [ ] _The Pragmatic Programmer_
  - [ ] _System Design Interview_
  - [ ] _Software Architecture the hard parts_
  - [ ] _Software Architecture Patterns_
  - [ ] _Release It! Design and Deploy Production-Ready Software_
  - [ ] _Observability Engineering Achieving Production Excellence_
  - [ ] _Design Patterns_    
    
- **Quantum Computing:** 
  - [ ] _Computation Conferences_ (Feynman)
  - [ ] _Quantum Supremacy_ (Kaku)
  - [ ] _Linear Algebra Done Right_ (Axler) 
  - [ ] _Quantum Computing: An Applied Approach_ (Hidary) 
  - [ ] _Quantum Random Number Generation_ (Kollmitzer, Schauer, Rass, Rainer)
  - [ ] _Quantum Computing Environments_ (Iyengar, Mastrianim, Kumar)
  - [ ] _IBM Quantum Computing Course_
  - [ ] _Quantum Computation and Quantum Information_ (Nielsen & Chuang).
    
- **Japanese:** 
  - [ ] _Genki I_ 
  - [ ] _Genki II_
  - [ ] _Remembering the Kanji_ (Heisig)
    
- **Finance & Blockchain:** 
  - [ ] _Algorithmic Trading_ (Chan)
  - [ ] _Cryptoassets - The Innovative Investor's Guide to Bitcoin and Beyond_ (Burniske, Tatar)
  - [x] _The Simple Path to Wealth_ (Collins)
  - [ ] _Investments in cryptocurrencies_ (Redondo)
  - [ ] The bogleheads guide to investment (Lindauer, Larimore, LeBoeuf)
    
- **Polymath Explorations:**
	- IOI teaching
	  - [ ] _Preparing for the IOI through Developmental Teaching_
	  - [ ] _Olympiads in informatics Tasks and Training Volume 1 and 2_
	- Cryptography and hacking
	  - [ ] _An Introduction to Mathematical Cryptography_ (Hoffstein, Pipher, Silverman)
	  - [ ] _The Hacker Book_ (Caballero, Serrano)
	  - [ ] _Protecting Privacy through Homomorphic Encryption_ (Lauter, Dai, Laine)
	  - [ ] _Encryption and Decryption Algorithms for Plain Text and Images using Fractional Calculus_ (Martinez, Montesions, Flores)
	  - [ ] _The Complete Guide to SCION_ (Chuat, Legner, Basin, Hausheer, Hitz, Müller, Perrig)
	- Math
	  - [ ] _Problem Solving Strategies_ (Engel)
	  - [ ] _Solving Mathematical Problems_ (Tao)
	  - [ ] _Book of Proof_ (Hammack) 
	  - [ ] _Abstract Algebra Theory and Applications_ (Judson)
	  - [ ] _Math for Machine Learning_ (Deisenroth, Faisal, Ong)
	  - [ ] _Combinatorial Optimization_ (Korte, Vygen)

	- Data
	  - [ ] _Big Data_ (Sosa)
	- Others
	  - [ ] _Man and his Symbols_ (Jung)
	  - [ ] _Big Data_ (Escudero)
	  - [ ] _Poetic Mechanics_ (Clark)
	  - [ ] _Ocultism_ (Greer)
	  - [ ] _The red book_ (Jung)
	  - [ ] _Tarot mirror of the soul_ (Ziegler)