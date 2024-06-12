import sys
def buildLast(s):
    last = [-1]*sys.maxunicode # jumlah maximum unicode
    for i in range(len(s)):
        last[ord(s[i])] = i
    return last

def bmMatch(text, pattern):
    last = buildLast(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1
    if(i > n-1):
        return -1
    j = m -1
    while i <= n - 1:
        if pattern[j] == text[i]:
            if j == 0:
                return i
            else:  # looking-glass
                i -= 1
                j -= 1
        else:  # character jump 
            lo = last[ord(text[i])]  # last occurrence
            i = i + m - min(j, 1 + lo)
            j = m - 1

    return -1

def checkLink(listPattern):
    text = input("Masukkan text: ")
    if(bmMatch(text,"http://") != -1):
        print("Tautan berbahaya!")
        return
    
    for i in range(len(listPattern)):
        if (bmMatch(text,listPattern[i]) != -1):
            print("Tautan aman")
            return
    
    print("Tautan berbahaya!")

patterns = [
    "google.com",
    "facebook.com",
    "twitter.com",
    "linkedin.com",
    "instagram.com",
    "reddit.com",
    "youtube.com",
    "amazon.com",
    "wikipedia.org",
    "github.com",
    "stackoverflow.com",
    "medium.com",
    "netflix.com",
    "spotify.com",
    "apple.com",
    "microsoft.com",
    "tumblr.com",
    "pinterest.com",
    "quora.com",
    "wordpress.com",
    "tokopedia.com",
    "shopee.co.id",
]

checkLink(patterns)