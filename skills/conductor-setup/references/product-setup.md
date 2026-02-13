# Product and Tech Stack Setup Protocol

## General Questioning Guidelines
- Ask questions **sequentially** (one by one).
- Categorize as **Additive** (select all that apply) or **Exclusive Choice** (singular commitment).
- Provide 2-3 plausible options + "Type your own answer" + "Autogenerate and review".

## 1. Generate Product Guide (`product.md`)
- Ask up to 5 questions (Users, Goals, Features).
- **Existing Projects:** Ask context-aware questions based on code analysis.
- **Autogenerate Logic:** Infer remaining details if user chooses option E.
- **Write File:** Append to `conductor/product.md`, preserving `# Initial Concept`.

## 2. Generate Product Guidelines (`product-guidelines.md`)
- Ask up to 5 questions (Prose style, Brand messaging, Visual identity).
- Provide rationale for suggested answers.
- Write to `conductor/product-guidelines.md`.

## 3. Generate Tech Stack (`tech-stack.md`)
- **New Projects:** Ask up to 5 questions (Languages, Frameworks, Databases).
- **Existing Projects:** State inferred stack and ask for confirmation.
- **Write File:** Write to `conductor/tech-stack.md`.
