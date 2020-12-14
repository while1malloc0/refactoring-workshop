# Refactoring

---

# What is refactoring?

---

## What is refactoring?
Changing the _structure_ of code without changing its _behavior_

---

# Context

---

## The mechanics of refactoring
Who, what, when, where, why

---

## Who refactors?
You and a pair

---

## What do you refactor?
Code smells

---

## When do you refactor?
When you need to _tested_ change code

---

## When do you refactor?
...OR when you want to *explore* code

---

## Where do you refactor?
In the files where the change will be implemented

---

## Why do you refactor?
To make code easier to change

---

# Code smells

---

# Smell #1: Long class or function

---

### Long class or function
A class or function is too long to understand easily

---

# Solution 
Extract smaller functions

---

# Smell #2: Data clump

---

### Data clump
Arguments to functions that always go together

---

# Solution
Combine related arguments into an object

---

# Smell #3: Primitive Obsession

---

### Primitive Obsession
Using primitive types where objects with behavior would be easier

---

# Solution
Write an object to wrap the type

---

# Smell #4: Law of Demeter Violations

---

### Law of Demeter Violations
A chain of several collaborators is called in a function

---

# Solution
Use only what you need in a function

---

# Smell #5: Unencapsulated Side Effects

---

### Unencapsulated side effects
A function can't be called without triggering its dependencies side effects

---

# Solution
Dependency inject code with side effects

---

# Questions?