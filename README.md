```markdown
# HashTable Implementation in Python

## Overview
This project implements a simple HashTable data structure in Python from scratch. The HashTable stores key-value pairs and uses a basic hashing function to manage data efficiently. It demonstrates core operations such as adding, removing, and looking up data within the hash table.

## Features
- Initialize an empty hash table.
- Compute hash values by summing Unicode (ASCII) values of string keys.
- Add key-value pairs, handling hash collisions with nested dictionaries.
- Remove specific key-value pairs safely.
- Lookup values by key, returning `None` if the key does not exist.

## Implementation Details
- The `HashTable` class contains:
  - `collection`: a dictionary that maps hash values to nested dictionaries of key-value pairs.
  - `hash(key)`: computes the sum of Unicode values of characters in the key.
  - `add(key, value)`: inserts or updates key-value pairs.
  - `remove(key)`: deletes a specific key-value pair.
  - `lookup(key)`: retrieves the value associated with a key.

## Usage Example

```python
# Create a new hash table
ht = HashTable()

# Add key-value pairs
ht.add('golf', 'sport')
ht.add('dear', 'friend')
ht.add('read', 'book')
ht.add('rose', 'flower')

# Lookup values
print(ht.lookup('golf'))   # Output: 'sport'
print(ht.lookup('dear'))   # Output: 'friend'
print(ht.lookup('unknown')) # Output: None

# Remove a key
ht.remove('golf')
print(ht.lookup('golf'))   # Output: None

# Check internal structure
print(ht.collection)
``

## Testing
The implementation is designed to pass specific unit tests that verify:
- Correct initialization.
- Proper hashing.
- Correct addition and collision handling.
- Safe removal.
- Accurate lookup results.

## Notes
- This hash table uses a very simple hash function suitable for educational purposes.
- Collisions are handled by storing multiple key-value pairs in nested dictionaries under the same hash key.
- For production use, consider more advanced hashing and collision resolution techniques.

## License
This project is for educational purposes and does not include any licensing restrictions.
