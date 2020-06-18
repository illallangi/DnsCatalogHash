def main():
  from .hash import hash
  import sys
  for arg in sys.argv[1:]:
    print(f'{arg} {hash(arg)}')
