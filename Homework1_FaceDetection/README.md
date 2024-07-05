# Homework 1: Face Detection

## Overview
This assignment focuses on implementing the Viola-Jones face detection algorithm, a foundational technique in computer vision. The goal is to develop a program capable of detecting faces in images through a supervised learning approach using Adaboost.

## Steps
1. Dataset Preparation:
   * Load and prepare images for training.
   * Convert images into a format suitable for machine learning, tagged with labels (1 for face, 0 for non-face).

2. Adaboost Algorithm:
   * Train a strong classifier using a linear combination of weak classifiers.

3. Experiments and Testing:
   * Conduct experiments by varying the parameter T in the Adaboost algorithm and evaluate its impact on detection accuracy.
   * Apply the trained classifier to new images and visualize detection results.

## Usage
* Ensure Python environment setup with necessary dependencies (OpenCV, NumPy).
* Use `main.py` or `main.ipynb` to execute and test implementations.

## Files Included
* `dataset.py`: Functions for loading and preparing image datasets.
* `adaboost.py`: Implementation of the Adaboost algorithm for feature selection.
* `classifier.py`: Weak classifier definition and implementation.
* `detection.py`: Functions for detecting faces in images using the trained classifier.
* `main.py` or `main.ipynb`: Entry points for testing and running the implemented algorithms.
