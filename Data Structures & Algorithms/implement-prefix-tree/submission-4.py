
class GraphNode:

    def __init__(self, val):
        self.val = val
        self.neighbours = {}
        self.isLast = False


class PrefixTree:

    def __init__(self):
        self._startCharacters = {}

    def insert(self, word: str) -> None:
        if word[0] not in self._startCharacters:
            char = GraphNode(word[0])
            self._startCharacters[word[0]] = char
        else:
            char = self._startCharacters[word[0]]
        
        for c in word[1:]:
            if c not in char.neighbours:
                nextChar = GraphNode(c)
                char.neighbours[c] = nextChar
                char = nextChar
            else:
                char = char.neighbours[c]
        
        char.isLast = True


    def search(self, word: str) -> bool:
        if word[0] not in self._startCharacters:
            return False
        
        char = self._startCharacters[word[0]]
        
        for c in word[1:]:
            if c not in char.neighbours:
                return False
            char = char.neighbours[c]
        
        return char.isLast
        

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self._startCharacters:
            return False
        
        char = self._startCharacters[prefix[0]]
        
        for c in prefix[1:]:
            if c not in char.neighbours:
                return False
            char = char.neighbours[c]
        
        return True
        
        