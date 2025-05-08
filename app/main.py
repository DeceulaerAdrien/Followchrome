import json
import os

base_path = os.path.dirname(os.path.dirname(__file__))
file_path= os.path.join(base_path,"data","vallejo.json")

# Load paints from the JSON file
with open(file_path, 'r') as f:
    paints = json.load(f)

# Main loop
print("💥 Vallejo Paint Catalog 💥")
print("Type a color name, part of a name, or just hit Enter to list all.")

while True:
    user_input = input('🔎 Search (or type exit to quit): ').strip().lower()
    if user_input == 'exit':
        print("👋 Goodbye!")
        break

    # Filter paints based on the input
    results = [paint for paint in paints if user_input in paint['name'].lower() or user_input in paint['code'].lower()]
    
    # Display the results
    if results:
        print(f"\n🎨 Found {len(results)} matches:")
        for paint in results:
            print(f"🔹 {paint['code']} - {paint['name']}")
    else:
        print("❌ No matches found.")
    
    print()