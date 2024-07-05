# Homework 3: Multi-Agent Search

## Overview
In this assignment, adversarial search algorithms for Pac-Man is implemented. The goal is to design agents using Minimax, Alpha-Beta Pruning, and Expectimax to compete against ghosts in the Pac-Man environment.

## Tasks
1. Minimax Search
   * Implement a MinimaxAgent to handle worst-case scenarios against random ghost actions. Ensure correct evaluation of game states based on depth.
2. Alpha-Beta Pruning
   * Develop an AlphaBetaAgent for efficient pruning of non-promising branches in the search tree. Maintain order of child state exploration as per game state actions.
3. Expectimax Search
   * Create an ExpectimaxAgent to model probabilistic ghost behavior with uniform random action selection. Adjust strategies to accommodate potential suboptimal ghost decisions.
4. Evaluation Function
   * Enhance the betterEvaluationFunction to accurately assess game states, improving Pac-Man's decision-making capability.

## Files Included
* `multiAgents.py`: Implement all multi-agent search algorithms.
* `pacman.py`: Main file to run Pac-Man games and manage game states.
* `game.py`: Defines Pac-Man world mechanics and supporting types like AgentState and Direction.
* `util.py`: Provides data structures for implementing search algorithms, though not required for this assignment.

## Results
* Alpha-Beta Pruning vs Minimax Agent:<br>
  Alpha-Beta Pruning proved faster and more efficient than Minimax Agent on the smallClassic layout. It achieved a win with a score of 1349 in 63 seconds, while Minimax Agent lost with a score of 42 in 66 seconds. Alpha-Beta Pruning's advantage lies in its ability to prune unnecessary nodes, optimizing search efficiency.
* Expectimax Search: <br>
  Unlike Minimax and Alpha-Beta, Expectimax Search uses max-value and expected-value functions, incorporating probabilities into decision-making. This approach led to a higher win rate compared to Alpha-Beta Agent, which consistently lost. Expectimax reflects average-case outcomes, whereas Minimax reflects worst-case scenarios.
* Evaluation Function: <br>
  After iterative adjustments to feature weights, the improved betterEvaluationFunction achieved scores exceeding one thousand on test cases. It also ran efficiently within reasonable time limits, demonstrating effective performance.
