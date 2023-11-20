import pyshorteners
# Initialize the URL shortener with TinyURL
s = pyshorteners.Shortener()
# Enter the URL you want to shorten
original_url = input("Enter the Link:-")
# Shorten the URL
short_url = s.tinyurl.short(original_url)
# Print the shortened URL
print("Shortened URL:", short_url)