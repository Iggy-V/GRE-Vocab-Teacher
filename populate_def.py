import pandas as pd
import requests

# Load the Excel file
file_path = r'C:\Users\ignas\Downloads\GRE-Prep words (1).xlsx'
excel_data = pd.read_excel(file_path)

# Function to get word definitions using an API
def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Check if the response contains the meaning
        if len(data) > 0 and 'meanings' in data[0] and len(data[0]['meanings']) > 0:
            return data[0]['meanings'][0]['definitions'][0]['definition']
        else:
            return "Definition not found"
    else:
        return "Error fetching definition"

# Populate the 'Meaning' column with definitions
for index, row in excel_data.iterrows():
    word = row['Word']
    definition = get_definition(word)
    excel_data.at[index, 'Meaning'] = definition

# Save the updated Excel file
output_file_path = r'C:\Users\ignas\Downloads\GRE-Prep words with def (1).xlsx'
excel_data.to_excel(output_file_path, index=False)

print(f"Updated file saved to: {output_file_path}")
