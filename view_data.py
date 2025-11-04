from qa_data import get_all_data

data = get_all_data()

if not data:
    print("No chat history found.")
else:
    for row in data:
        print(f"ID: {row[0]}")
        print(f"Question: {row[1]}")
        print(f"Answer: {row[2]}")
        print("-" * 40)
