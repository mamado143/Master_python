def say_hello(name): return f"Hello {name}"



Hello = lambda name: f"Hello {name}"
print(say_hello.__name__)
print(Hello.__name__)

print(type(Hello))
