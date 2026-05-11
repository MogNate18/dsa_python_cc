








print(f"***********************************************")
print(f"Indirect Recursion.")
def function_a(n:{_gt_}):
    if n > 0:
        print("Function A:", n)
        function_b(n-1)
    
def function_b(n:{_gt_}):
    if n > 0:
        print("Function B:", n)
        function_a(n-1)    
    
function_a (5)  

print(f"***********************************************")

print(f"Tail recursion.")
def basics(n:{_it_,_sub_}):
    if n <= 0:
        return n
    
    print(n)
    return basics(n-1)
 
basics(5)

print(f"************************************************")
print(f"Head Recursion")
def head_recusrion(n:{_it_,_sub_}):
    if n <= 0:
        return n
    
    head_recusrion(n-1)
    print(n)

head_recusrion(5)