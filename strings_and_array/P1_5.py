__author__ = 'SunnyYan'
# Implement a method to perform basic string compression using
# the counts of repeated characters. For example, the string
# aabcccccaaa would become a2b1c5a3. If the "compressed" string
# would not become smaller than the original string, you method
# should return the original string.

def compressString(string):
    result = []
    last = string[0]
    counter = 1
    for i in range(1,len(string)):
        if(string[i] == last):
            counter += 1
        else:
            result.append(last)
            result.append(str(counter))
            counter = 1
            last = string[i]
    compressed = ''.join(result)
    return ((len(compressed) < len(string)) and compressed or string)

testing = "aabbcceeddddeeffff"
testing2 = "abcdefg"
print compressString(testing)
print compressString(testing2)