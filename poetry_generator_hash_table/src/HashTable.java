
// QuadraticProbing Hash table class
//
// CONSTRUCTION: an approximate initial size or default of 101
//
// ******************PUBLIC OPERATIONS*********************
// bool insert( x )       --> Insert x
// bool remove( x )       --> Remove x
// bool contains( x )     --> Return true if x is present
// void makeEmpty( )      --> Remove all items


/**
 * Probing table implementation of hash tables.
 * Note that all "matching" is based on the equals method.
 * @author Mark Allen Weiss (based on code from)
 */
public class HashTable<K, V> {
    /**
     * Construct the hash table.
     */
    public HashTable() {
        this(DEFAULT_TABLE_SIZE);
    }

    /**
     * Construct the hash table.
     *
     * @param size the approximate initial size.
     */
    public HashTable(int size) {
        allocateArray(size);
        doClear();
    }

    /**
     * Insert into the hash table. If the item is
     * already present, do nothing.
     * Implementation issue: This routine doesn't allow you to use a lazily deleted location.  Do you see why?
     *
     * @param key the item to insert.
     * @param value the location of the "key" in the hashtable.
     */
    public boolean insert(K key,V value) {
        // Insert key as active
        int currentPos = findPos(key);
        // If we already have it in the hash table, update with the new value
        if (isActive(currentPos)) {
            storage[currentPos].value = value;
            return false;
        }

        storage[currentPos] = new HashEntry<>(key, value, true);
        currentActiveEntries++;

        // Rehash; see Section 5.5
        if (++occupiedCount > storage.length / 2) {
            rehash();
        }

        return true;
    }

    public String toString(int limit) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (int i = 0; i < storage.length && count < limit; i++) {
            if (storage[i] != null && storage[i].isActive) {
                sb.append(String.format("%d: %s[%s]\n", i, storage[i].key, storage[i].value));
                count++;
            }
        }
        return sb.toString();
    }

    /**
     * Expand the hash table.
     */
    private void rehash() {
        HashEntry<K, V>[] oldArray = storage;

        // Create a new double-sized, empty table
        allocateArray(2 * oldArray.length);
        occupiedCount = 0;
        currentActiveEntries = 0;

        // Copy table over
        for (var entry : oldArray) {
            if (entry != null && entry.isActive) {
                insert(entry.key, entry.value);

            }
        }
    }

    /**
     * Method that performs quadratic probing resolution.
     *
     * @param x the item to search for.
     * @return the position where the search terminates.
     * Never returns an inactive location.
     */
    private int findPos(K x) {
        int offset = 1;
        int currentPos = myHash(x);

        while (storage[currentPos] != null && !storage[currentPos].key.equals(x)) {
            currentPos += offset;  // Compute ith probe
            offset += 2;
            if (currentPos >= storage.length) {
                currentPos -= storage.length;
            }
        }

        return currentPos;
    }

    /**
     * Remove from the hash table.
     *
     * @param x the item to remove.
     * @return true if item removed
     */
    public boolean remove(K x) {
        int currentPos = findPos(x);
        if (isActive(currentPos)) {
            storage[currentPos].isActive = false;
            currentActiveEntries--;
            return true;
        } else {
            return false;
        }
    }

    /**
     * Get current size.
     *
     * @return the size.
     */
    public int size() {
        return currentActiveEntries;
    }

    /**
     * Get length of internal table.
     *
     * @return the size.
     */
    public int capacity() {
        return storage.length;
    }

    /**
     * Find an item in the hash table.
     *
     * @param x the item to search for.
     * @return true if item is found
     */
    public boolean contains(K x) {
        int currentPos = findPos(x);
        return isActive(currentPos);
    }

    /**
     * Find an item in the hash table.
     *
     * @param x the item to search for.
     * @return the matching item.
     */
    public V find(K x) {
        int currentPos = findPos(x);
        if (!isActive(currentPos)) {
            return null;
        } else {
            return storage[currentPos].value;
        }
    }

    /**
     * Return true if currentPos exists and is active.
     *
     * @param currentPos the result of a call to findPos.
     * @return true if currentPos is active.
     */
    private boolean isActive(int currentPos) {
        return storage[currentPos] != null && storage[currentPos].isActive;
    }

    /**
     * Make the hash table logically empty.
     */
    public void makeEmpty() {
        doClear();
    }

    private void doClear() {
        occupiedCount = 0;
        for (int i = 0; i < storage.length; i++) {
            storage[i] = null;
        }
    }

    private int myHash(K x) {
        int hashVal = x.hashCode();

        hashVal %= storage.length;
        if (hashVal < 0) {
            hashVal += storage.length;
        }

        return hashVal;
    }

    private class HashEntry<K, V> {
        public K key;   // the position
        public V value; // the value
        public boolean isActive;  // false if marked deleted

        public HashEntry(K key, V value, boolean active) {
            this.key = key;
                this.value = value;
            this.isActive = active;
        }
    }

    private static final int DEFAULT_TABLE_SIZE = 101;

    private HashEntry<K, V>[] storage; // The array of elements
    private int occupiedCount;         // The number of occupied cells: active or deleted
    private int currentActiveEntries;                  // Current size

    /**
     * Internal method to allocate array.
     *
     * @param arraySize the size of the array.
     */
    private void allocateArray(int arraySize) {
        storage = new HashEntry[nextPrime(arraySize)];
    }

    /**
     * Internal method to find a prime number at least as large as n.
     *
     * @param n the starting number (must be positive).
     * @return a prime number larger than or equal to n.
     */
    private static int nextPrime(int n) {
        if (n % 2 == 0) {
            n++;
        }

        for (; !isPrime(n); n += 2)
            ;

        return n;
    }

    /**
     * Internal method to test if a number is prime.
     * Not an efficient algorithm.
     *
     * @param n the number to test.
     * @return the result of the test.
     */
    private static boolean isPrime(int n) {
        if (n == 2 || n == 3) {
            return true;
        }

        if (n == 1 || n % 2 == 0) {
            return false;
        }

        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}
