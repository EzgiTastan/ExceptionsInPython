# You are making a program to post tweets. Each tweet must not exceed 42 characters.
# Complete the program to raise an exception, in case the length of the tweet is more than 42 characters.
# You can use the len() function to calculate the length of the string.

tweet = input()

try:
    if len(tweet) > 42:
        raise ValueError("Tweet length exceeds 42 characters")

except:
    print("Error")
else:
    print("Posted")