def countletters(s):
    s=s.lower()
    vowels='aeiou'
    vowelscount=sum(1 for char in s if char in vowels)
    consonantcount=sum(1 for char in s if char.isalpha() and char not in vowels)
    print(f"{vowelscount},{consonantcount}")
s=input()
countletters(s)
