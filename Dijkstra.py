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


def find_lowest_node(stations):
    distance = float("inf")
    node = None
    if stations:
        for station in stations:
            distance_to_station = stations[station]
            if distance_to_station < distance:
                distance = distance_to_station
                node = station
    return node


def result(fin):
    if fin == "start":
        return "start"
    else:
        father = parents[fin]
        return result(father), fin


node = find_lowest_node(graph["start"])
#print(node)


while node:
    cost = costs[node]
    neighbours = graph[node]
    if neighbours:
        for neighbour in graph[node]:
            new_cost = graph[node][neighbour] + cost
            old_cost = costs[neighbour]
            if new_cost < old_cost and neighbour not in processed:
                costs[neighbour] = new_cost
                parents[neighbour] = node
        processed.append(graph[node])
    node = find_lowest_node(graph[node])


print(result("fin"), costs["fin"])


