def hash(arg):
  import dns.name
  import hashlib
  return hashlib.sha1(dns.name.from_text(arg).to_wire()).hexdigest()

if __name__ == "__main__":
  import sys
  for arg in sys.argv[1:]:
    print(f'{arg} {hash(arg)}')
