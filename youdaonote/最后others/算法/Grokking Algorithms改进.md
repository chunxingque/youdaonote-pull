p106, 

Does it matter if you write

graph[“claire”] = [“thom”, “jonny”]

graph[“anuj”] = []

instead of

graph[“anuj”] = []

graph[“claire”] = [“thom”, “jonny”]

Think back to the previous chapter. Answer: It doesn’t matter. 



Yes, as you have said in the book that "Hash tables have no ordering, so it doesn’t matter what order you add key/value pairs in."

But since Python  3.7, Python  dicts remember the order that items were inserted, so there is a difference .



p110, 

person in searched

The 'in' operation for "searched"(a list) is O(n), I think it would be better to use searched = set() instead , The 'in' operation for a set is  O(1).



p163, 语法错误

Dynamic programming starts by solving subproblems and builds up to solving the big problem.

















