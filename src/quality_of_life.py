# To install dependencies, run in terminal:
# pip install beautifulsoup4 pandas matplotlib


# Library for parsing HTML documents
from bs4 import BeautifulSoup

# Library for working with tables and data analysis
import pandas as pd

# Library for data visualization
import matplotlib.pyplot as plt

# Load the local HTML file
with open("data/quality_of_life_2025.html", "r", encoding="utf-8") as f:
    html = f.read()

# Create a BeautifulSoup object to parse the HTML using the built-in "html.parser"
soup = BeautifulSoup(html, "html.parser")

# Find the desired table by its id
table = soup.find("table", {"id": "t2"})

# Display the first 500 characters of the table (to check its structure)
print(table.prettify()[:500])


# Get the list of table headers (column names) —
# iterate over all <th> tags and extract text, stripping unnecessary spaces
headers = [th.get_text(strip=True) for th in table.find_all("th")]

# Create an empty list to store the table rows
rows = []

# Iterate over all <tr> rows, starting from the second one — skip the first as it contains headers
for tr in table.find_all("tr")[1:]:
    
    # Extract all <td> cells and get their text content without leading/trailing spaces
    cols = [td.get_text(strip=True) for td in tr.find_all("td")]
    
    # Add the row to the list if it's not empty
    if cols:
        rows.append(cols)

# Convert the data into a pandas DataFrame
df_2025 = pd.DataFrame(rows, columns=headers)

# Display the first 20 rows of the table
df_2025.head(20)


# Check for missing values in the table
df_2025.isnull().sum()


# Save the table to a CSV file without indexes
df_2025.to_csv("output/quality_of_life_2025.csv", index=False)


# Convert the relevant columns to numeric types (in case of parsing issues)
df_2025["Quality of Life Index"] = df_2025["Quality of Life Index"].astype(float)
df_2025["Safety Index"] = df_2025["Safety Index"].astype(float)
df_2025["Health Care Index"] = df_2025["Health Care Index"].astype(float)

# Sort the data by each index and extract the TOP-20 cities
top_quality = df_2025.sort_values(by="Quality of Life Index", ascending=False).head(20)
top_safety = df_2025.sort_values(by="Safety Index", ascending=False).head(20)
top_health = df_2025.sort_values(by="Health Care Index", ascending=False).head(20)

# Display the TOP-5 cities for each index as a preview
print("\n Top-5 cities by Quality of Life Index:")
print(top_quality[["City", "Quality of Life Index"]].head(5))

print("\n Top-5 cities by Safety Index:")
print(top_safety[["City", "Safety Index"]].head(5))

print("\n Top-5 cities by Health Care Index:")
print(top_health[["City", "Health Care Index"]].head(5))


# Create a function for plotting horizontal bar charts

def plot_horizontal_bar(ax, data, x_col, y_col, color, title):
    """
    Displays a horizontal bar chart with value labels.

    :param ax: the Axes object to draw the chart on
    :param data: DataFrame containing the data to visualize
    :param x_col: column name for the Y-axis (usually city names — "City")
    :param y_col: column name for the X-axis (e.g., "Quality of Life Index")
    :param color: color of the bars
    :param title: chart title
    """
    # Plot a horizontal bar chart on the given axis
    data.plot(
        kind="barh",      # Chart type — horizontal bars
        x=x_col,          # City names on the Y-axis
        y=y_col,          # Index values on the X-axis
        ax=ax,            # Axis to draw on
        color=color,      # Bar color
        title=title       # Chart title
    )

    # Invert the Y-axis so the highest values appear at the top
    ax.invert_yaxis()

    # Add value labels next to each bar
    for i, v in enumerate(data[y_col]):
        ax.text(v + 1, i, f"{v:.1f}", va="center")  # v + 1 shifts the label slightly to the right

# === Create a figure with 3 subplots (1 column, 3 rows) ===
fig, axs = plt.subplots(3, 1, figsize=(12, 14))  # 3 rows, 1 column; figure size 12x14 inches

# === Chart 1 — Quality of Life Index ===
plot_horizontal_bar(
    axs[0],                        # First axis (top chart)
    top_quality,                  # Data: Top 20 cities by quality of life
    "City",                       # City names on Y-axis
    "Quality of Life Index",     # Index values on X-axis
    "skyblue",                    # Bar color
    "Top-20 Cities by Quality of Life Index (2025)"  # Title
)

# === Chart 2 — Safety Index ===
plot_horizontal_bar(
    axs[1],                        # Second axis (middle chart)
    top_safety,                   # Data: Top 20 cities by safety
    "City", 
    "Safety Index", 
    "lightgreen", 
    "Top-20 Cities by Safety Index (2025)"
)

# === Chart 3 — Health Care Index ===
plot_horizontal_bar(
    axs[2],                        # Third axis (bottom chart)
    top_health,                   # Data: Top 20 cities by healthcare
    "City", 
    "Health Care Index", 
    "mediumseagreen", 
    "Top-20 Cities by Health Care Index (2025)"
)

# === Automatically adjust spacing between subplots ===
plt.tight_layout()

# === Save the final image in two formats ===
plt.savefig("images/top_20_indexes_2025.png", dpi=300)  # PNG — for presentations and reports
plt.savefig("images/top_20_indexes_2025.svg")           # SVG — for scalable print or web use

# === Display the final chart ===
plt.show()


# Read the CSV file from the output folder
with open("output/quality_of_life_2025.csv", "r", encoding="utf-8") as f:
    csv_content = f.read()
    print(csv_content[:500])  # Display the first 500 characters

# Set paths to image files located in the images/ folder
svg_path = "images/top_20_indexes_2025.svg"
png_path = "images/top_20_indexes_2025.png"

# Print confirmation messages
print(f"\nSaved PNG chart as: {png_path}")
print(f"Saved SVG chart as: {svg_path}")

