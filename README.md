# Algorithm Performance Analyzer

### Analyzing and Comparing the Performance of Sorting Algorithms

A Python-based algorithm analysis project that implements and compares five fundamental sorting algorithms. The project explores how different algorithms perform across various input sizes and dataset arrangements through execution-time measurements, operation counting, and data visualization.

## Project Overview

Sorting algorithms are essential to computer science, but their efficiency can vary significantly depending on the input data.

This project was developed to investigate these differences through practical implementation and experimentation.

Rather than relying on Python's built-in sorting functions, the five sorting algorithms were implemented manually to better understand their underlying logic, computational complexity, and performance characteristics.

## Features

- **Five sorting algorithms:** Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort.
- **Performance benchmarking:** Measure execution time and track algorithm operations.
- **Dataset generation:** Generate random, ascending, and descending datasets.
- **Performance visualization:** Compare algorithm results using graphs.
- **Algorithm testing:** Verify sorting correctness through automated tests.
- **Modular architecture:** Separate algorithm implementations, benchmarking, dataset generation, and visualization.

## Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Bubble Sort | O(n)* | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

*Bubble Sort's best-case complexity assumes an early-exit optimization.*

## Technologies Used

- **Python** – Algorithm implementation and benchmarking
- **Git & GitHub** – Version control and collaboration
- **VS Code** – Development environment

## Project Structure

```text
Algorithm-Performance-Analyzer/
│
├── main.py
├── algorithms.py
├── dataset_generator.py
├── benchmark.py
├── visualization.py
├── test_algorithms.py
├── requirements.txt
├── results/
└── README.md
```

**File responsibilities:**

- `main.py` – Main program entry point
- `algorithms.py` – Sorting algorithm implementations
- `dataset_generator.py` – Dataset generation
- `benchmark.py` – Performance measurement
- `visualization.py` – Graph generation
- `test_algorithms.py` – Algorithm correctness testing
- `results/` – Generated benchmark results

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/parajulibiplov10-lgtm/algorithm-performance-analyzer.git
```

### 2. Navigate to the project

```bash
cd algorithm-performance-analyzer
```

### 3. Install dependencies

If the project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

### 5. Run tests

```bash
python -m unittest test_algorithms.py
```

## Learning Objectives

This project focuses on developing practical skills in:

- Design and analysis of algorithms
- Time complexity and Big-O notation
- Performance benchmarking
- Experimental comparison of sorting algorithms
- Data visualization
- Python programming and debugging
- Collaborative software development using Git

## Future Improvements

- Expand benchmarking to larger datasets.
- Explore additional sorting algorithms.
- Improve the presentation of benchmark results.
- Investigate memory usage and space complexity.
- Develop an interactive interface for algorithm comparisons.

## Contributors

**Biplov Parajuli**  
Computer Science Graduate  
[GitHub](https://github.com/parajulibiplov10-lgtm)

**Sandip Kandel**  
Project Collaborator

## Project Background

Developed as part of **CSCE 4110 – Algorithms** at the University of North Texas.

The project demonstrates the practical application of algorithm analysis concepts through implementation, experimentation, and performance evaluation.
