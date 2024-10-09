class Boggle:
    def __init__(self, grid, dictionary):
        self.setGrid(grid)
        self.setDictionary(dictionary)
        self.solution = set()  # Store found words in a set for uniqueness

    def setGrid(self, grid):
        self.grid = [list(map(str.upper, row)) for row in grid]  # Use map instead of list comprehension
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0
        self.visited = [[False] * self.cols for _ in range(self.rows)]  # Simplified initialization of visited array
        print(f"Grid is now: {self.grid}")  # Debugging info

    def setDictionary(self, dictionary):
        self.dictionary = {word.upper() for word in dictionary}  # Using set comprehension directly
        self.prefix_set = self.build_prefix_set(self.dictionary)
        print(f"Dictionary is set: {self.dictionary}")  # Debug print
        print(f"Prefix set created: {self.prefix_set}")  # Debug print

    def build_prefix_set(self, dictionary):
        prefix_set = set()
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])
        return prefix_set  # No change in logic here, just returning directly

    def getSolution(self):
        self.solution.clear()  # Reset any previously found solutions
        self.findAllWords()  # Start searching for words
        print(f"Final solution found: {self.solution}")  # Debugging print
        return sorted(self.solution)  # No need to convert to list explicitly

    def isValidWord(self, word):
        is_valid = word in self.dictionary and len(word) >= 3  # Changed variable name for clarity
        print(f"Checking word: {word}, Is valid: {is_valid}")  # Debugging
        return is_valid

    def isValidPrefix(self, prefix):
        is_valid = prefix in self.prefix_set  # Using a consistent variable name for validity check
        print(f"Checking prefix: {prefix}, Is valid: {is_valid}")  # Debugging
        return is_valid

    def findAllWords(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.dfs(r, c, "")  # Explore all cells starting with an empty path

    def dfs(self, row, col, path):
        # Return early if out of bounds or already visited
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.visited[row][col]:
            return

        # Build the new path by adding the current letter
        letter = self.grid[row][col]
        path += letter
        print(f"Exploring path: {path}")  # Debug print

        # Check if the current path is a valid prefix
        if not self.isValidPrefix(path):
            return  # Stop if it's not a valid prefix

        # Mark this cell as visited
        self.visited[row][col] = True

        # If the current path forms a valid word, add it to the solution
        if self.isValidWord(path):
            self.solution.add(path)
            print(f"Added word: {path}")  # Debugging print

        # Recurse to all neighboring cells
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            self.dfs(row + dr, col + dc, path)

        # Unmark this cell as visited when backtracking
        self.visited[row][col] = False
