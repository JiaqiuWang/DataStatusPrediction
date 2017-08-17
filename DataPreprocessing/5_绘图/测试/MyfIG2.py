"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

# 划分横坐标区间
x1 = np.linspace(0, 25, num=25)
x2 = np.linspace(0, 25, num=25)

# 划分纵坐标区间
y1 = np.linspace(0, 25)  # 每个用户使用服务的总数
y2 = np.array(["Quora", "Reddit", "Stack Overflow", "Goodreads",
               "Github", "CodePen", "Openhub", "Bitbucket", "Gitlib",
               "Twitter", "Facebook", "Google +", "Foursquare", "Tumblr",
               "Bloger", "Google Scholar", "Youtube", "Vimeo", "Last.fm",
               "SoundClick", "MuseScore", "Behance", "dribbble", "Linkedin"
               , "Amazon"])  # 每个人使用最多的前3个服务

plt.subplot(2, 1, 1)
plt.plot(x1, y1, '.-')
# plt.title('A tale of 2 subplots')
# plt.xlabel('a')
plt.ylabel('Data Volume'
           '(Ten thousand)')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('Each User (1~120)')
plt.ylabel('Time Span(Year)')

plt.show()
