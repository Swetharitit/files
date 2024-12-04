 # Node class representing each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data  # The word (data)
        self.next = None  # Reference to the next node

# LinkedList class representing the entire list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list
    
    # Method to add a new node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    # Method to search for a word in the linked list
    def search(self, word):
        current = self.head
        while current:
            if current.data == word:
                return True  # Word found
            current = current.next
        return False  # Word not found

    # Method to remove a node from the linked list
    def remove(self, word):
        current = self.head
        prev = None
        
        # If the word to be deleted is the head node
        if current and current.data == word:
            self.head = current.next
            current = None
            return
        
        # Search for the word to be deleted
        while current and current.data != word:
            prev = current
            current = current.next
        
        # If the word was not found
        if current is None:
            return
        
        # Unlink the node from the linked list
        prev.next = current.next
        current = None
    
    # Method to convert the linked list to a list of words
    def to_list(self):
        words = []
        current = self.head
        while current:
            words.append(current.data)
            current = current.next
        return words

# Method to read the file and load the words into a linked list
def load_words_from_file(filename):
    linked_list = LinkedList()
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            words = content.split()  # Split into words
            for word in words:
                linked_list.append(word)  # Add each word to the linked list
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return linked_list

# Method to save the linked list back into the file
def save_words_to_file(linked_list, filename):
    words = linked_list.to_list()
    with open(filename, 'w') as file:
        file.write(" ".join(words))  # Save words as space-separated

# Main program
def main():
    filename = 'words.txt'  # File name to read and write
    linked_list = load_words_from_file(filename)  # Load the linked list from file

    # Take user input to search a word
    search_word = input("Enter a word to search in the list: ").strip()
    
    if linked_list.search(search_word):
        print(f"'{search_word}' found in the list. Removing it.")
        linked_list.remove(search_word)
    else:
        print(f"'{search_word}' not found in the list. Adding it.")
        linked_list.append(search_word)
    
    # Save the updated list back to the file
    save_words_to_file(linked_list, filename)
    print("Updated list saved to file.")

# Run the program
if __name__ == "__main__":
    main()
