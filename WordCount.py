#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0 
  letters = 0
  for line in textFile:
      lineCount +=1
      words = line.split()


      for word in  words:
         print(word)
         wordcount += 1

         for letter in words:
            print(letter)
            letter += 1
  
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letters)
if __name__ == '__main__':
  main()
