class Solution:
    def minMutation(self,startGene,endGene,bank):
        
        bank_set = set(bank)

        if endGene not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']

        queue = deque([startGene])

        visited = set([startGene])

        mutations = 0

        while queue:

            for _ in range(len(queue)):

                current = queue.popleft()

                if current == endGene:
                    return mutations

                arr = list(current)

                for i in range(8):

                    old = arr[i]

                    for ch in genes:

                        arr[i] = ch
                        next_gene = "".join(arr)

                        if next_gene in bank_set and next_gene not in visited:
                            visited.add(next_gene)
                            queue.append(next_gene)

                    arr[i] = old

            mutations += 1

        return -1