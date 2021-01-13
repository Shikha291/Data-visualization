import numpy as np
import matplotlib.pyplot as plt

languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
x_pos = np.arange(len(languages))
usage = [10, 8, 6, 4, 2, 1]
plt.bar(x_pos, usage)
plt.xticks(x_pos, languages)
plt.ylabel('Usage')
plt.xlabel('Languages')
plt.title('Programming Languages Usage')
plt.show()
