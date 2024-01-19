# Sample data for the table
data = [
    {"name": "John Doe", "city": 25, "city1": 25, "city2": 25},
    {"name": "Jane Smith", "city": 30, "city1": 25, "city2": 25},
    {"name": "Bob Johnson", "city": 22, "city1": 25, "city2": 25},
    {"name": "Bob Johnson", "city": 22, "city1": 25, "city2": 25},
    {"name": "Bob Johnson", "city": 22, "city1": 25, "city2": 25},
    {"name": "Bob Johnson", "city": 22, "city1": 25, "city2": 25},
]

first_col = [
    "Aircraft type (source: RFQ:Aircraft Table<< airplanelataType>>)",
    "Aircraft MSN (source: RFQ:Aircraft MSN >>)",
    "Aircraft Registration Number Operator (source: AirlineName)",
    "Services requested [Service Name] stripping and painting / sanding and painting",
    "Areas to be painted (Source RFQ Step1 field 7)",
    "New livery type (Source RFQ Step1 field 11 - list all areas selected)"
]

# Generate table header
header_row = "".join(["<th>{}</th>".format(key) for key in data[0].keys()])
z = "<th></th>"
z+=header_row
table_header = "<tr>{}</tr>".format(z)


for index, i in enumerate(data):
    print(index, i)



# Generate table body
table_body = ""
for index, item in enumerate(data):
    x = f"<td>{first_col[index]}</td>"
    row = "".join(["<td>{}</td>".format(value) for value in item.values()])
    x+=row
    table_body += "<tr>{}</tr>".format(x)

# Generate HTML string for the table
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic Table</title>
  <style>
    /* Your CSS styles here */
    table {{
      border-collapse: collapse;
      width: 100%;
      margin-top: 20px;
    }}

    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }}

    th {{
      background-color: #f2f2f2;
    }}
  </style>
</head>
<body>

  <h1>Dynamic Table</h1>

  <!-- Container for the table -->
  <div id="table-container">
    <table>
      <thead>
        {table_header}
      </thead>
      <tbody>
        {table_body}
      </tbody>
    </table>
  </div>

</body>
</html>
"""

# Save the HTML content to a file
with open("dynamic_table.html", "w") as file:
    file.write(html_content)

print("HTML file generated successfully.")
