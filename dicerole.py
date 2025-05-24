from typing import Dict, Tuple
import matplotlib.pyplot as plt

def role() -> Dict[int, int]:
    counts: Dict[int, int] = {}
    for x in range(1, 7):
        for y in range(1, 7):
            for num in [x, y, x + y, abs(x - y)]:
                counts[num] = counts.get(num, 0) + 1
    return counts

if __name__ == "__main__":
    counts = role()
    total = sum(counts.values())
    keys = sorted(counts.keys())
    values = [counts[k] / total * 100 for k in keys]

    # Plot histogram
    plt.bar(keys, values, color='skyblue', edgecolor='black')
    plt.xlabel("Value")
    plt.ylabel("Percentage (%)")
    plt.title("Combined Histogram of Values from x, y, x+y, and |x−y|")
    plt.xticks(keys)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
