# Generator =>

def simple_generator():
    # yield "Hello"
    # yield "World"
    # yield "We are learning python"
    for i in range(10):
        yield i

gen = simple_generator()

print(next(gen))
print("I need second value")
print("Second value is important")
print(next(gen))
# # print(next(gen))
# print(gen)