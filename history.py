class Node:
    """A class to represent a node in the doubly linked list."""
    def __init__(self, page):
        self.page = page
        self.prev = None
        self.next = None


class HistoryManager:
    """A class to manage browsing history."""
    def __init__(self):
        self.current = None  # Pointer to the current page
        self.head = None     # Start of the history list
    
    def visit_page(self, page):
        """Visits a new page."""
        new_node = Node(page)
        if self.current:  # Update the doubly linked list
            self.current.next = new_node
            new_node.prev = self.current
        else:  # First page
            self.head = new_node
        self.current = new_node
        print(f"Visited: {page}")
    
    def prev_page(self):
        """Goes to the previous page."""
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Moved to previous page: {self.current.page}")
        else:
            print("No previous page available.")
    
    def next_page(self):
        """Goes to the next page."""
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Moved to next page: {self.current.page}")
        else:
            print("No next page available.")
    
    def search_history(self, page_name):
        """Searches for a specific page in the history."""
        temp = self.head
        while temp:
            if temp.page == page_name:
                print(f"Page '{page_name}' found in history.")
                return
            temp = temp.next
        print(f"Page '{page_name}' not found in history.")
    
    def display_history(self):
        """Displays the browsing history."""
        print("Browsing History:")
        temp = self.head
        while temp:
            print(temp.page, end=" -> " if temp.next else "\n")
            temp = temp.next


def main():
    history = HistoryManager()
    while True:
        print("\n--- History Management System ---")
        print("1. Visit a new page")
        print("2. Go to the previous page")
        print("3. Go to the next page")
        print("4. Search for a page")
        print("5. Display browsing history")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            page = input("Enter the name of the page to visit: ").strip()
            history.visit_page(page)
        elif choice == "2":
            history.prev_page()
        elif choice == "3":
            history.next_page()
        elif choice == "4":
            page_name = input("Enter the name of the page to search for: ").strip()
            history.search_history(page_name)
        elif choice == "5":
            history.display_history()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the interactive program
if __name__ == "__main__":
    main()
