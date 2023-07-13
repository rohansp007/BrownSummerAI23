from typing import Callable

from adversarialsearchproblem import (
    Action,
    AdversarialSearchProblem,
    State as GameState,
)


def minimax(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    Implement the minimax algorithm on ASPs, assuming that the given game is
    both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
    """
    state = asp.get_start_state()
    player = state.player_to_move()
    bestval = float("-inf")
    bestmove = None
    for a in asp.get_available_actions(state):
        next_state = asp.transition(state,a)
        val = minvalue(asp,next_state,player) 
        if val > bestval:
            bestval,bestmove = val,a
    return bestmove

def maxvalue(asp: AdversarialSearchProblem[GameState,Action],state,player):
    if asp.is_terminal_state(state):
        return asp.evaluate_terminal(state)[player]
    bestval = float("-inf")
    for a in asp.get_available_actions(state):
        next_state = asp.transition(state,a)
        val = minvalue(asp,next_state,player)
        bestval = max(val,bestval)
    return bestval

def minvalue(asp: AdversarialSearchProblem[GameState,Action],state,player):
    if asp.is_terminal_state(state):
        return asp.evaluate_terminal(state)[player]
    bestval = float("inf")
    for a in asp.get_available_actions(state):
        next_state = asp.transition(state,a)
        val = maxvalue(asp,next_state,player)
        bestval = min(bestval,val)
    return bestval




def alpha_beta(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    Implement the alpha-beta pruning algorithm on ASPs,
    assuming that the given game is both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    state = asp.get_start_state()
    player = state.player_to_move()
    bestval = float("-inf")
    alpha = float("-inf")
    beta = float("inf")
    bestmove = None
    for a in asp.get_available_actions(state):
        next_state = asp.transition(state,a)
        val = minvalue_for_alphabeta(asp,next_state,player,alpha,beta) 
        if val > bestval:
            bestval,bestmove = val,a
        if val >= beta:
            break
        alpha = max(alpha,val)
    return bestmove

def maxvalue_for_alphabeta(asp: AdversarialSearchProblem[GameState,Action],state,player,alpha,beta):
    if asp.is_terminal_state(state):
        return asp.evaluate_terminal(state)[player]
    bestval = float("-inf")
    for a in asp.get_available_actions(state):
        next_state = asp.transition(state,a)
        val = minvalue_for_alphabeta(asp,next_state,player,alpha,beta)
        bestval = max(val,bestval)
        if bestval >= beta:
            return bestval
        alpha = max(alpha,bestval)
    return bestval

def minvalue_for_alphabeta(asp: AdversarialSearchProblem[GameState,Action],state,player,alpha,beta):
    if asp.is_terminal_state(state):
        return asp.evaluate_terminal(state)[player]
    bestval = float("inf")
    for a in asp.get_available_actions(state):
        next_state = asp.transition(state,a)
        val = maxvalue_for_alphabeta(asp,next_state,player,alpha,beta)
        bestval = min(bestval,val)
        if bestval <= alpha:
            return bestval
        beta = min(beta,bestval)
    return bestval

def alpha_beta_cutoff(
    asp: AdversarialSearchProblem[GameState, Action],
    cutoff_ply: int,
    # See AdversarialSearchProblem:heuristic_func
    heuristic_func: Callable[[GameState], float],
) -> Action:
    """
    This function should:
    - search through the asp using alpha-beta pruning
    - cut off the search after cutoff_ply moves have been made.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_ply - an Integer that determines when to cutoff the search and
            use heuristic_func. For example, when cutoff_ply = 1, use
            heuristic_func to evaluate states that result from your first move.
            When cutoff_ply = 2, use heuristic_func to evaluate states that
            result from your opponent's first move. When cutoff_ply = 3 use
            heuristic_func to evaluate the states that result from your second
            move. You may assume that cutoff_ply > 0.
        heuristic_func - a function that takes in a GameState and outputs a
            real number indicating how good that state is for the player who is
            using alpha_beta_cutoff to choose their action. You do not need to
            implement this function, as it should be provided by whomever is
            calling alpha_beta_cutoff, however you are welcome to write
            evaluation functions to test your implemention. The heuristic_func
            we provide does not handle terminal states, so evaluate terminal
            states the same way you evaluated them in the previous algorithms.
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...
