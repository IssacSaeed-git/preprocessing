import re

        #--------------------exercise_1------------------------
        
t="Contact us at info@company.com or sales@shop.org. Our next event is on 25-10-2025, and registration closes 15/10/2025. We already have 120 participants and 99 seats left!"
# extract email address
e=re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",t)
print(e)
# extract all dates
d=re.findall(r"\b\d{2}[-/]\d{2}[-/]\d{4}\b",t)
print(d)
# extract all num>=100
n=re.findall(r"\b[1-9]\d{2,}\b",t)
print(n)

       #----------------------exercise_2-----------------------

t2="Great session on #AI and #NLP today! Follow @DataLab and @AI_Community for updates."
# remove all punctuation
p=re.findall(r"[^\w\s#@]",t2)
print(p)
# extract all hashtags
h=re.findall(r"#\w+",t2)
print(h)
# extract mentions
m=re.findall(r"@\w+",t)
print(m)


