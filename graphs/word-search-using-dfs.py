# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col = len(board[0])
        row = len(board)
        len_of_word = len(word)
        is_possible = False   #starting with it's not possible to form the string.
        visited = set()       #set for visited elements.
         
        def dfs(visited, i, j, k):
            nonlocal is_possible
            
            # base-conditions, exit if already found a match or if trying to search out of               #bounds.
            if is_possible == True or i<0 or i>=row or j<0 or j>=col:  
                return
            
            #add this element to visited
            visited.add((i,j))
            
            if board[i][j] == word[k]:
                #we found the matching string.
                if k == len_of_word - 1:
                    is_possible = True
                    return
                
                #entering the dfs call only if that cell is unvisited.
                if (i+1, j) not in visited:
                    dfs(visited, i+1, j, k+1)
                    
                if (i-1, j) not in visited:
                    dfs(visited, i-1, j, k+1)
                    
                if (i, j+1) not in visited:
                    dfs(visited, i, j+1, k+1)
                    
                if (i, j-1) not in visited:
                    dfs(visited, i, j-1, k+1)
                    
            #processing of this cell is done, so remove it from visited for next iterations.        
            visited.remove((i,j))
        
        #dfs through each cell
        for i in range(row):
            for j in range(col):
                #just return the answer if already found the solution.
                if is_possible == True:
                    return is_possible
                dfs(visited,i,j,0)
                    
        return is_possible