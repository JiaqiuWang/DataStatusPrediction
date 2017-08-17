"""
====================
Horizontal bar chart
====================

This example showcases a simple horizontal bar chart.
"""
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ("Quora", "Reddit", "Stack Overflow", "Goodreads",
               "Github", "CodePen", "Openhub", "Bitbucket", "Gitlib",
               "Twitter", "Facebook", "Google +", "Foursquare", "Tumblr",
               "Bloger", "Google Scholar", "Youtube", "Vimeo", "Last.fm",
               "SoundClick", "MuseScore", "Behance", "dribbble", "Linkedin"
               , "Amazon")
y_pos = np.arange(len(people))
# performance = 120 + 10 * np.random.rand(len(people))
x = np.linspace(1, 120, 25)


ax.barh(y_pos, x, align='center',
        color='blue', )
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Each User')

# ax.set_title('How fast do you want to go today?')

plt.show()
