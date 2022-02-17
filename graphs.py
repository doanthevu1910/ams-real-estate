import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.figure()
plt.scatter(df['size'], df['price'], s=20, c='orange', edgecolors='orange', label = 'Size')
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Price vs. Size')
plt.legend()
plt.show()
plt.close()

plt.figure()
plt.scatter(df['size'], df['price']/df['size'], s=20, c='orange', edgecolors='orange', label = 'Size')
plt.xlabel('Size')
plt.ylabel('Price/Size')
plt.title('Price/Size vs. Size')
plt.legend()
plt.show()
plt.close()

plt.figure()
plt.scatter(df['kamers'], df['price'], s=10, c='orange', edgecolors='orange', label = 'Size')
plt.xlabel('Kamers')
plt.ylabel('Price')
plt.title('Price vs. Kamers')
plt.legend()
plt.show()
plt.close()