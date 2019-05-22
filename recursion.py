def sum_recu(n):
    '''
    1 to n,The sum function
    '''

    if n > 5:
       a = n + sum_recu(n - 1)           # 能直接弄到 a = 6, 它放入栈再重新拿出来
       print(n)
       print(a)
       return a
    else:
        return 0

a = sum_recu(10)


def dfs(self, tree):
    if not tree: return
    self.dfs(tree.left)
    self.s.append(tree.val)
    self.dfs(tree.right)
