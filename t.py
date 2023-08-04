import toml
data=toml.load("./poulstar/pyproject.toml")
print(data["tool"]["poetry"]["version"])