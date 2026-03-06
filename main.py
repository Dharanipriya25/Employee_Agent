from graph_builder import build_graph
from utils import print_separator

def main():
    app = build_graph()

    print("🤖 Smart Support Agent (Offline Mode)")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        result = app.invoke({"question": user_input})
        print("\nAgent:", result["answer"])

        print_separator()


if __name__ == "__main__":
    main()