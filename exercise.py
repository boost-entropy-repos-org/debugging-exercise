def minCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    if len(costs) == 0:
        return 0
    
    return min(
        costs[0][0] + minCost([[float('inf'), costs[0][1], costs[0][2]]] + costs[1:]),
        costs[0][1] + minCost([[costs[0][0], float('inf'), costs[0][2]]] + costs[1:]),
        costs[0][2] + minCost([[costs[0][0], costs[0][1], float('inf')]] + costs[1:])
    )