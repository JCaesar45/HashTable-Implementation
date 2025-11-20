class HashTable:
    def __init__(self):
        # Initialize the collection as an empty dictionary
        self.collection = {}

    def hash(self, key):
        # Sum the Unicode values of each character in the key
        return sum(ord(char) for char in key)

    def add(self, key, value):
        # Compute the hash for the key
        hashed_key = self.hash(key)
        # If the hashed key does not exist, create a new dictionary
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        # Add or update the key-value pair in the nested dictionary
        self.collection[hashed_key][key] = value

    def remove(self, key):
        # Compute the hash for the key
        hashed_key = self.hash(key)
        # Check if the hashed key exists
        if hashed_key in self.collection:
            # Remove the specific key if it exists
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]
                # If after deletion, the nested dictionary is empty, remove it entirely
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]
        # If the key does not exist, do nothing

    def lookup(self, key):
        # Compute the hash for the key
        hashed_key = self.hash(key)
        # Return the value if found, else None
        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key)
        return None
