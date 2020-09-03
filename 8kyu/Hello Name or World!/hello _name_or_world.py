def hello(name="World"):
    if name == "":
        return "Hello, World!"
    return f"Hello, {name.capitalize()}!"
