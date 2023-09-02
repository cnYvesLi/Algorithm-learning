infinity = float("inf")

graph = {}
graph["start"] = {}
graph["A"] = {}
graph["B"] = {}
graph["start"]["A"] = 5
graph["start"]["B"] = 2
graph["A"]["fin"] = 3
graph["B"]["A"] = 1
graph["B"]["fin"] = 6
graph["fin"] = None

costs = {}
costs["A"] = 5
costs["B"] = 2
costs["fin"] = infinity

parents = {}
parents["A"] = "start"
parents["B"] = "start"
parents["fin"] = None

processed = []


def find_lowest_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_node(costs)


while node:
    cost = costs[node]
    neighbours = graph[node]
    if neighbours:
        for neighbour in neighbours.keys():
            new_cost = neighbours[neighbour] + cost
            old_cost = costs[neighbour]
            if new_cost < old_cost:
                costs[neighbour] = new_cost
                parents[neighbour] = node
    processed.append(node)
    node = find_lowest_node(costs)


#Show the result
print(processed, costs["fin"])
