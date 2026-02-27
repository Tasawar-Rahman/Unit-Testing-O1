def count(text):
   if not text:
      return 0
   else:
      total= text.split()
      return len(total)
def vowels(text):
   count1=0
   for vow in text:
      if vow in ("a","e","i","o","u"):
         count1+=1
   return count1
def reverse(text):
   return text[::-1]
if __name__=="__main__":
   print(count(input("input a sentence: ")))
   print(vowels(input("input a word: ")))
   print(reverse(input("input a string to reverse: ")))

