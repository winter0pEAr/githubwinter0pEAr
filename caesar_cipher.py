def encrypt(text, key):
    result = ""
  
    # 모든 문자열을 알파벳 n만큼 이동시켜 암호화
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
  
    return result
  
def decrypt(text, key):
    result = ""
  
    # 암호화된 문자열을 알파벳 n만큼 반대로 이동시켜 복호화
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char
  
    return result
