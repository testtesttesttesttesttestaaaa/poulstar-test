import toml

def get_version():
  data=toml.load("../../poulstar/pyproject.toml")
  version = data["tool"]["poetry"]["version"]
  return version

if __name__ == '__main__':
  get_version()
  
