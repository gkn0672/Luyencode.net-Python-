while True:
    try:
        n = input()
        print("YES" if n[0] == n[-1] else "NO")
    except EOFError:
        break
  