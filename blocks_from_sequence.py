def chunker(seq, size):
    for i in range(0, len(seq), size):
      yield s[i:i+size] 
