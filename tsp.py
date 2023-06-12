def generate_permutations(cities):
    # Helper function to generate all possible permutations of the cities
    n = len(cities)
    permutations = []

    def permute(arr, city0, city1):
        if city0 == city1:
            permutations.append(arr.copy())
            print("permutations={}, len={}".format(arr, len(permutations)))
        else:
            for i in range(city0, city1 + 1):
                arr[city0], arr[i] = arr[i], arr[city0]
                permute(arr, city0 + 1, city1)
                arr[city0], arr[i] = arr[i], arr[city0]

    permute(cities, 0, n - 1)

    return permutations


def calculate_total_weight(permutation, weights):
    total_weight = 0
    num_cities = len(permutation)

    for i in range(num_cities - 1):
        city1 = permutation[i]
        city2 = permutation[i + 1]
        weight = weights[city1][city2]
        total_weight += weight

    city1 = permutation[num_cities - 1]
    city2 = permutation[0]
    weight = weights[city1][city2]
    total_weight += weight

    return total_weight


def brute_force_tsp(cities, weights):
    permutations = generate_permutations(list(range(len(cities))))

    best_tour = None
    best_weight = float('inf')
    comparisons = 0  # Counter for comparisons made

    for permutation in permutations:
        last_weight = calculate_total_weight(permutation, weights)
        comparisons += 1

        if last_weight < best_weight:
            best_tour = permutation
            best_weight = last_weight

    return best_tour, best_weight, comparisons


# Matrix Generation
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return int((x2 - x1) ** 2 + (y2 - y1) ** 2)


def generate_weight_matrix(cities):
    n = len(cities)
    weights = [[0] * n for _ in range(n)]

    i_counter, operations = 0, 0
    for i in range(n):
        i_counter += 1
        j_counter = 0
        for j in range(i + 1, n):
            j_counter += 1
            operations += i_counter * j_counter

            city1 = cities[i]
            city2 = cities[j]
            weight = calculate_distance(city1, city2)
            weights[i][j] = weight
            weights[j][i] = weight

        print("Complexity 'generate_weight_matrix' O(n^2) {}*{}={}".format(i_counter, j_counter, operations))

    return weights


# Example usage
cities_map = [(0, 0), (1, 1), (2, 2), (3, 3)]
weight_matrix = generate_weight_matrix(cities_map)

for row in weight_matrix:
    print(row)

t, w, comps = brute_force_tsp(cities_map, weight_matrix)
print("Best Tour:", t)
print("Best Weight:", w)
print("Total Comparisons:", comps)

# Complexity Analysis

