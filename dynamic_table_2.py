paint_services = [
    "Paint Supplied by the PAINT SHOP",
    "New Paint Livery drawings",
    "New Paint Livery Service Bulletin",
    "Production of Exterior Technical markings",
    "Exterior markings kit language",
    "Installation of Exterior Technical markings",
    "Production of new Registration kit in stencil",
    "Production of Stencil and Mylar new livery kit",
    "Replacement of any damaged PR SEALANT",
    "Aircraft Weighing",
    "Release PART 145 after paint/ decals application",
    "Potential Daily/Weekly check after paint service completion"
]

required_during_RFQ = {"Aircraft 1": "Yes", "Aircraft 2": "No"}
service_provider_reply = {"Aircraft 1": "Ok", "Aircraft 2": "Not Ok", "Aircraft 3": "Ok"}

# Extract unique headers from both dictionaries
# all_headers = set(list(required_during_RFQ.keys()) + list(service_provider_reply.keys()))

# Create HTML table
html_table = f"""
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
        <tr>
            <td></td>
            <th colspan="{len(required_during_RFQ.keys())}">Required during RFQ</th>
            <th colspan="{len(service_provider_reply.keys())}">Service Provider Reply</th>
        <tr>
        <tr>
          <th>Paint Service</th>
"""

# Add headers for "Required during RFQ"
for header in required_during_RFQ.keys():
    html_table += f"          <th>{header}</th>\n"

# Add headers for "Service Provider Reply"
for header in service_provider_reply.keys():
    html_table += f"          <th>{header}</th>\n"

html_table += """
        </tr>
      </thead>
      <tbody>
"""

# Populate table rows with data
for service in paint_services:
    html_table += f"""
        <tr>
          <td>{service}</td>
"""

    # Add data for "Required during RFQ"
    for header in required_during_RFQ.keys():
        html_table += f"          <td>{required_during_RFQ.get(header, '')}</td>\n"

    # Add data for "Service Provider Reply"
    for header in service_provider_reply.keys():
        html_table += f"          <td>{service_provider_reply.get(header, '')}</td>\n"

    html_table += "        </tr>\n"

# Complete HTML table
html_table += """
      </tbody>
    </table>
  </div>

</body>
</html>
"""

# Save the HTML content to a file
with open("dynamic_table_new.html", "w") as file:
    file.write(html_table)

print("HTML file generated successfully.")
