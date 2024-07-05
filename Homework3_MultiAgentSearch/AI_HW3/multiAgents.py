from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):     # takes a GameState and returns some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]      # evaluate each moves and give them scores
        bestScore = max(scores)                                                             # the ones with the highest scores
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore] # the indices with highest scores
        chosenIndex = random.choice(bestIndices)                                            # pick randomly among the best             

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):     # takes in the current and proposed child GameStates (pacman.py) and returns a number, where higher numbers are better.
        """
        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()                                 #pacman position after moving
        newFood = childGameState.getFood()                                          #remaining food
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]  #number of moves that each ghost will remain scared because of Pacman having eaten a power pellet
        
        # print("child game state\n", childGameState)
        # print("new food\n", newFood)
        # print("new pos \n", newPos)
        # print("ghost state\n", newGhostStates[0].getPosition())

        # closest distance with ghosts
        minGhostDistance = min([manhattanDistance(newPos, state.getPosition()) for state in newGhostStates])

        #the action increase the score
        scoreDiff = childGameState.getScore() - currentGameState.getScore()

        #the action makes the nearest food nearer
        pos = currentGameState.getPacmanPosition()
        nearestFoodDistance = min([manhattanDistance(pos, food) for food in currentGameState.getFood().asList()])
        newFoodsDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
        newNearestFoodDistance = 0 if not newFoodsDistances else min(newFoodsDistances)
        isFoodNearer = nearestFoodDistance - newNearestFoodDistance

        #keep direction to avoid meaningless random movements when upon criteria are not satisfied
        direction = currentGameState.getPacmanState().getDirection()
        
        #reflex formula
        if minGhostDistance <= 1 or action == Directions.STOP:
            return 0
        if scoreDiff > 0:
            return 8
        elif isFoodNearer > 0:
            return 4
        elif action == direction:
            return 2
        else:
            return 1


def scoreEvaluationFunction(currentGameState):                  # returns the score of the state (score akhir)
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (Part 1)
    """
    def getAction(self, gameState): # Returns the minimax action from the current gameState using self.depth and self.evaluationFunction.
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        # Begin your code (Part 1)
        result = self.value(gameState, 0, 0)        
        return result[1]                                        # returns 'action' from result

    def value(self, gameState, index, depth):                   # returns value: pair of [score, action]
        if len(gameState.getLegalActions(index)) == 0 or depth == self.depth:   # for terminal states
            action = ""
            score = self.evaluationFunction(gameState)
            return score, action

        if index == 0: return self.max_value(gameState, index, depth)           # if Pacman (index = 0), use max-agent
        else:          return self.min_value(gameState, index, depth)           # else (index > 0 => Ghost), use min-agent

    def max_value(self, gameState, index, depth):               # returns the max utility value-action for max-agent
        legal_actions = gameState.getLegalActions(index)                        # get all possible actions for all agents
        max_v = float("-inf")                                                   # initialize v as -infinity
        max_action = ""       

        for action in legal_actions:                                            # for each action in the possible actions                           
            
            #          [0,1,2,3,4]
            #            /      \
            # [0,1,2,3,4]       [0,1,2,3,4]

            nextstate = gameState.getNextState(index, action)                   # get the next state after the agent take an action 

            if index + 1 == gameState.getNumAgents():                           # if last agent for that depth, go to next depth (4+1 = 5)
                nextstate_index = 0                                             # starting from index 0 (pacman)
                nextstate_depth = depth + 1                                     # increment depth
            else:                                                               # else continue going through the agents
                nextstate_index = index + 1                                     # by adding 1 to the index
                nextstate_depth = depth                                         # remain in the same depth

            curr_v = self.value(nextstate, nextstate_index, nextstate_depth)[0] # current value from value of the next state

            if curr_v > max_v:                                                  # if current value bigger than maximum value
                max_v = curr_v                                                  # update max_v as curr_v and use the action in loop
                max_action = action                                

        return max_v, max_action

    def min_value(self, gameState, index, depth):               # returns the min utility value-action for min-agent
        legal_actions = gameState.getLegalActions(index)                        # get all possible actions for all agents
        min_v = float("inf")                                                    # initialize v as +infinity
        min_action = ""

        for action in legal_actions:                                            # for loop similar to max_value
            nextstate = gameState.getNextState(index, action)
            
            if index + 1 == gameState.getNumAgents():
                nextstate_index = 0 
                nextstate_depth = depth + 1
            else:
                nextstate_index = index + 1
                nextstate_depth = depth

            curr_v = self.value(nextstate, nextstate_index, nextstate_depth)[0]

            if curr_v < min_v:                                                  # if current value smaller than minimum value, update the min_v and the action
                min_v = curr_v
                min_action = action

        return min_v, min_action

        raise NotImplementedError("To be implemented")
        # End your code (Part 1)

class AlphaBetaAgent(MultiAgentSearchAgent):        # alpha: max's best option on path to root and beta: min's best option on path to root
    """
    Your minimax agent with alpha-beta pruning (Part 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        # Begin your code (Part 2)
        alpha = float("-inf")                                                       # initialize alpha as -infinity 
        beta = float("inf")                                                         # initialize beta as +infinity
        result = self.value(gameState, 0, 0, alpha, beta)                   
        return result[1]                                                            # returns 'action' from the result

    def value(self, gameState, index, depth, alpha, beta):      # returns value: pair of [score, action]
        if len(gameState.getLegalActions(index)) == 0 or depth == self.depth:  
            action = ""
            score = self.evaluationFunction(gameState)
            return score, action

        if index == 0: return self.max_value(gameState, index, depth, alpha, beta) 
        else:          return self.min_value(gameState, index, depth, alpha, beta)  

    def max_value(self, gameState, index, depth, alpha, beta):  # returns the max utility value-action for max-agent
        legal_actions = gameState.getLegalActions(index)                          
        max_v = float("-inf")                                                  
        max_action = ""       

        for action in legal_actions:                                                # similar to minimax except the alpha-beta (including for min_value too)                              
            nextstate = gameState.getNextState(index, action)           

            if index + 1 == gameState.getNumAgents():                             
                nextstate_index = 0                       
                nextstate_depth = depth + 1            
            else:                                       
                nextstate_index = index + 1   
                nextstate_depth = depth  

            curr_v = self.value(nextstate, nextstate_index, nextstate_depth, alpha, beta)[0]

            if curr_v > max_v:                                                  
                max_v = curr_v                                                 
                max_action = action     
                
            alpha = max(alpha, max_v)                                               # update alpha for this function max_value
            if max_v > beta:                                                        # Optimisation: pruning to stop evaluating game state
                return max_v, max_action                           

        return max_v, max_action

    def min_value(self, gameState, index, depth, alpha, beta):  # returns the min utility value-action for min-agent
        legal_actions = gameState.getLegalActions(index)                        
        min_v = float("inf")                                                    
        min_action = ""

        for action in legal_actions:                                           
            nextstate = gameState.getNextState(index, action)
            
            if index + 1 == gameState.getNumAgents():
                nextstate_index = 0 
                nextstate_depth = depth + 1
            else:
                nextstate_index = index + 1
                nextstate_depth = depth

            curr_v = self.value(nextstate, nextstate_index, nextstate_depth, alpha, beta)[0]

            if curr_v < min_v:                                                      # if current value smaller than minimum value, update the min_v and the action
                min_v = curr_v
                min_action = action

            beta = min(beta, min_v)                                                 # update beta for this function min_value
            if min_v < alpha:                                                       # Optimisation: pruning to stop evaluating game state
                return min_v, min_action

        return min_v, min_action
    
        raise NotImplementedError("To be implemented")
        # End your code (Part 2)


class ExpectimaxAgent(MultiAgentSearchAgent):           # use max_value and expected_value(instead of min_value)
    """
      Your expectimax agent (Part 3)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        # Begin your code (Part 3)
        score, action = self.value(gameState, 0, 0)
        return action

    def value(self, gameState, index, depth):           # returns value: pair of [score, action]
        if len(gameState.getLegalActions(index)) == 0 or depth == self.depth:
            score = self.evaluationFunction(gameState)
            action = ""
            return score, action

        if index == 0: return self.max_value(gameState, index, depth)
        else:          return self.expected_value(gameState, index, depth)          # if index > 0 (ghost), take expected value

    def max_value(self, gameState, index, depth):       # returns the max utility value-action for max-agent
        legal_actions = gameState.getLegalActions(index)                          
        max_v = float("-inf")                                                  
        max_action = ""       

        for action in legal_actions:                                                              
            nextstate = gameState.getNextState(index, action)           

            if index + 1 == gameState.getNumAgents():                             
                nextstate_index = 0                       
                nextstate_depth = depth + 1            
            else:                                       
                nextstate_index = index + 1   
                nextstate_depth = depth  

            curr_v = self.value(nextstate, nextstate_index, nextstate_depth)[0]
            
            if curr_v > max_v:                                                  
                max_v = curr_v                                                 
                max_action = action                         

        return max_v, max_action

    def expected_value(self, gameState, index, depth):                         
        legal_actions = gameState.getLegalActions(index)
        exp_v = 0                                                                   # initialize the expected value as 0
        exp_action = ""

        nextstate_p = 1.0 / len(legal_actions)                                      # next state's probability or weight by uniform distribution

        for action in legal_actions:
            nextstate = gameState.getNextState(index, action)

            if index + 1 == gameState.getNumAgents():                             
                nextstate_index = 0                       
                nextstate_depth = depth + 1            
            else:                                       
                nextstate_index = index + 1   
                nextstate_depth = depth  

            curr_v = self.value(nextstate, nextstate_index, nextstate_depth)[0]     # current value from value of the next state
            exp_v += nextstate_p * curr_v                                           # get the expected value from their weights times current value

        return exp_v, exp_action 

        raise NotImplementedError("To be implemented")
        # End your code (Part 3)


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (Part 4).
    """
    # Begin your code (Part 4)

    # get positions of the agents
    pos = currentGameState.getPacmanPosition()
    ghost_pos_list = currentGameState.getGhostPositions()

    # get the current score
    curr_score = currentGameState.getScore()

    # get food distances
    foods = currentGameState.getFood().asList()
    food_distances = [manhattanDistance(pos, food_position) for food_position in foods]

    nearest_food_dist = 1     
    if len(foods) > 0:                                                                      # if there's still food
        nearest_food_dist = min(food_distances)                                             # find the nearest food distance from the food_distances

    min_ghost_dist = min(manhattanDistance(pos, ghost_pos) for ghost_pos in ghost_pos_list) # the closest ghost distance
    if min_ghost_dist < 2:                                                                  # if the ghost is one step away
        nearest_food_dist = 10000000        # let the nearest food distance be really big and it will prioritize of running away instead of eating the nearest food

    features = [curr_score, 1.0 / nearest_food_dist, len(foods), len(currentGameState.getCapsules())]   # factors that affects the pacman 
    weights = [10, 1, -1, -1]                                                                           # weights are tuned by experiment

    return sum([feature * weight for feature, weight in zip(features, weights)])            # sum of all factors times by their weights

    raise NotImplementedError("To be implemented")
    # End your code (Part 4)

# Abbreviation
better = betterEvaluationFunction

# 李嘉玲 109550186