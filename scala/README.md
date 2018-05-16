# Scala Syntax

This is an example program written in Scala as an exercise for syntax. Below are a few notes taken while learning the language.

## 0. Introduction

* Scala is a compiled language, similar to Java.
* Scala is also supported BOTH as a functional and an object oriented programming language

### 0.1 Requirements

* IntelliJ IDEA 2016.3
* Scala 2.12.6
* sbt 1.1.5
* macOS 10.13.4

## 1. Variables

There are two types of variables:

* `var`: mutable variable (it can be changed)
* `val`: immutable variable (it cannot be changed)

To declare variables (Scala does not support primitive and wrapper classes):

```scala
var x: Int = 10
val y: String = "Alex"
val z: Float = 10f
val a: Double = 10
val b: Boolean = true
val c = false // Scala will take a smart variable type guess
```

### 1.1 Blocks

When we need to perform quick operations between variables, we can put them between curly braces `{}`. The last expression is returned. For example:
```scala
var x = {val a = 100; val b = 200; a + b}
// This returns x: Int = 300
```

*__Note__: We do not need semicolons to show the end of statements, unless there are multiple on the same line. A newline character is sufficient. So another way to write the same exact statement above:

```scala
var x = {val a = 100
         val b = 200
         a + b}
// This returns x: Int = 300
```
#### 1.2 Lazy Interpretation

This feature of Scala is important for clustering and large computations (and the underlying tech behind [Apache Spark](https://spark.apache.org/)). When declaring a new variable, the memory is allocated immediately for whatever you assigned. This is the case for the majority of declarations. For example:

```scala
val x: Int = 100
```

This one line will store the value x as an Integer object with the value 100.

However, what if we took a list of integers and we wanted to find the multiples of each number? It would take A LOT of memory to store the initial list and its multiples in different variables. Scala finds a way around that using lazy computing.

```scala
lazy val x = 100 // This is a lazy object, no memory is stored locally yet.
x * 2 // This will return 200. The value is initialized AT computation.
```

## 2. Loops

### 2.1 Foreach Loops

```scala
val str: String = "Test"
str.foreach(println);
// T
// e
// s
// t
```

### 2.2 For Loops

```scala
for (i <- 5 to 1 by -1 if i % 2 == 1) println(i)
// 5
// 3
// 1
```

The above code block is called a for loop with a guard statement.

### 2.3  Yield

Let's say I wanted to store all active customers on a website in a list (or as a vector).

For a yield statement, the result of each for loop iteration is stored in a list.

```scala
val activeCustomers = for (cust <- custList if cust.isActive()) yield(cust)
// activeCustomers: scala.collection.immutable.IndexedSeq[Int] = Vector(...)
```

## 3. Functions

### 3.1 Syntax

```scala
def function_name(function params): return type = {
    code...
}

// Example:
def areaRect(len: Float, wid: Float) Float = {
    len * wid // Last expression automatically becomes return value
}



