** This repository is still under construction. **

# Scala Syntax

__Author:__ Alex Nakagawa

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
    len * wid // Last expression automatically becomes return value, no need for return keyword
}
```

## 4. Collections

There are four types of Collections most widely used in Scala:

### 4.1. Array

Arrays are collections of items all with the same type, and a FIXED length

```scala
val arr = new Array[Int](10) // declaring an int array full of 10 zeros
arr(0) = 1 // assigns int 1 to zero index
```

### 4.2. ArrayBuffer

ArrayBuffer objects can grow in size, you do not need to specify a size on declaration.

```scala
import scala.collection.mutable.ArrayBuffer
val arr = new ArrayBuffer[Int]()
arr += 10
arr += (20, 30)
arr ++= Array(40, 50, 60)
arr -= 60
arr // ArrayBuffer(10, 20, 30, 40, 50) ////// 60 was deleted.
```

Some common operations with Arrays and ArrayBuffers:

```scala
a.trimEnd(2) // trims last two elements
a.insert(2, x) // adds x at second index
a.insert(2, 10, 11, 12) // adds list (10,11,12) at second index
a.remove(2) // removes item at second index

// For traversal:
for (el <- a)

// Others:
Array(1, 2, 3, 4).sum // returns 10
Array(1, 5, 9, 8).max // returns 9
Array(1, 7, 2, 9)
```

### 4.3. Map

A collection of key-value pairs. The key and the value don't necessarily have to be the same type.

```scala
import scala.collection.immutable.Map
import scala.collection.mutable.Map
val mapping = Map('Alex' -> 'K', 'Nakagawa' -> 'V')
```

### 4.4. Tuple

More generalized list.

```scala
val a = (100, 'John', 'France') // once values are initialized, they cannot be changed
a._2 // returns 'John', tuples indexing starts from 1

```

