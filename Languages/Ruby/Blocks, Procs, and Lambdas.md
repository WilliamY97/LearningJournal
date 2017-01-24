#Blocks, Procs, and Lambdas

- Blocks can be combined with methods like ```.each``` and ```.times``` to execute an instruction for each element in a collection.

##Collect Method

- Takes a block and applies the expression in the block to every element in an array.

```
my_nums = [1, 2, 3]
my_nums.collect { |num| num ** 2 }
# ==> [1, 4, 9]
```
##Yielding With Parameters

```
def yield_name(name)
  puts "In the method! Let's yield."
  yield("Kim")
  puts "In between the yields!"
  yield(name)
  puts "Block complete! Back in the method."
end
```

- yield_name method is defined with one parameter, name.

- You can use yield to call whatever is between {-} during a method.
