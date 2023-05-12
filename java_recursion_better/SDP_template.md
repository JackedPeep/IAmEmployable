# Software Development Plan

## Phase 0: Requirements Specification *(10%)*\

[] complete the tree implementation 

[] Override the ``public String toString()`` method so that it returns a sideways tree

[] Write a ``public String inOrderToString()`` that returns a string from an in order traversal method.

[] Write a ``public void balanceTree()`` method that balences the binary search tree.

[] ``public void flip()`` flips every child in the tree ex. right = left && left = right.

[] ``public BinaryTreeNode<E> getByKey(E key) `` returns the node searched for

[] ``public int nodesInLevel(int level)`` returns the number of nodes in the lvl.

[] ``public void printAllPaths()`` prints out all possible paths a root node has to the leaf node.

[] ``public BinaryTreeNode<E> inOrderSuccessor(BinaryTreeNode<E> node)`` returns the node that just greater than the input node

[] `` public int countBST()``returns the number of binary search trees.

## Phase 1: System Analysis *(10%)*
Just a bunch of pieces that are unfinished. apart they don't form a system.


## Phase 2: Design *(30%)*
```java
public class Tree<E extends Comparable<? super E>> {
    private BinaryTreeNode root;  // Root of tree
    private String name;     // Name of tree

    /**
     * Create an empty tree
     *
     * @param label Name of tree
     */
    
    
    public Tree(String label) {
        name = label;
        
    }

    /**
     * Create BST from ArrayList
     *
     * @param arr   List of elements to be added
     * @param label Name of tree
     */
    public Tree(ArrayList<E> arr, String label) {
        name = label;
        for (E key : arr) {
            insert(key);
        }
    }

    /**
     * Create BST from Array
     *
     * @param arr   List of elements to be added
     * @param label Name of  tree
     */
    public Tree(E[] arr, String label) {
        name = label;
        for (E key : arr) {
            insert(key);
        }
    }

    /**
     * Return a string containing the tree contents as a tree with one node per line
     */
    public String toString(tree) {
        if node == null return "";
       //toStringTraverse(node.right);
//       append string of right
//       back to the top of the tree;
//       toStringTraverse(node.left);
//       append string of left
//       return rightString + the current node.key + leftString
    


    
        
        
    }

    /**
     * Return a string containing the tree contents as a single line
     */
    public String inOrderToString(node) {
        
        
        //       if node == null then return "";
//
//       toStringTraverse(node.left);
//       append string of left
//       back to the top of the tree;
//       toStringTraverse(node.right);
//       append string of right
//       return leftString + the current node.key + rightString
        
        
    }

    /**
     * reverse left and right children recursively
     */
    public void flip(node) {
//        if node.left==null & node.right == null 
//               break;
   
        // right = node.right
       // left = node.left
       // node.right = left
       // node.left = right
       // flip(node.left)
       // flip(node.right)
            
    }

    /**
     * Returns the in-order successor of the specified node
     * @param node node from which to find the in-order successor
     */
    public BinaryTreeNode inOrderSuccessor(BinaryTreeNode node) {
       
//        if node.right == null && node.left == null
//               return node.parent;
//        if node.key == key
//            return node.right;
//
//       inOrderToString(node);
//       return null;

    /**
     * Counts number of nodes in specified level
     *
     * @param level Level in tree, root is zero
     * @return count of number of nodes at specified level
     */
    public int nodesInLevel(int level) {
//        currentLevel = 0;
//        numNode = 0;
//    
//        if level == 0 && node != null{
//          return 1;
//       }
//        
//        if level == current Level
//               numNode++;
//        return numNode;
        
               
        
    }

    /**
     * Print all paths from root to leaves
     */
    public void printAllPaths() {
        
        // if node.left == null && node.right == null
          //int pathEnd = node.key
          //print(rootNode);
        // if pathEnd > node.key
            //traverse(node.right)
          //print(node.key);
        // if pathEnd < node.key
          //traverse(node.left)
          //print(node.key);
    }

    /**
     * Counts all non-null binary search trees embedded in tree
     *
     * @return Count of embedded binary search trees
     */
    public int countBST() {
        // BTS rules.
          // If all of the nodes to the left is less than the parent
          // and all of the nodes to the right are greater than the parent
          // and  it is a binary search tree.
          // program 
        return 0;
    }

    /**
     * Insert into a bst tree; duplicates are allowed
     *
     * @param x the item to insert.
     */
    public void insert(E x) {
        root = insert(x, root, null);
    }

    public BinaryTreeNode getByKey(E key) {
//        if node.key == key 
//               return node;
//    
//        inOrderToString(node);
//        return null;
    }

    /**
     * Balance the tree
     */
    public void balanceTree() {
        // TODO:
    }

    /**
     * Internal method to insert into a subtree.
     * In tree is balanced, this routine runs in O(log n)
     *
     * @param x the item to insert.
     * @param t the node that roots the subtree.
     * @return the new root of the subtree.
     */
    private BinaryTreeNode insert(E x, BinaryTreeNode t, BinaryTreeNode parent) {
        if (t == null) return new BinaryTreeNode(x, null, null, parent);

        int compareResult = x.compareTo(t.key);
        if (compareResult < 0) {
            t.left = insert(x, t.left, t);
        } else {
            t.right = insert(x, t.right, t);
        }

        return t;
    }

```


## Phase 3: Implementation *(15%)*


## Phase 4: Testing & Debugging *(30%)*

    

## Phase 5: Deployment *(5%)*



## Phase 6: Maintenance


*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
1) What parts of your program are sloppily written and hard to understand?
2) Are there parts of your program which you aren't quite sure how/why they work?
3) If a bug is reported in a few months, how long would it take you to find the cause?
   *   Will your documentation make sense to...
4) ...anybody besides yourself?
5) ...yourself in six month's time?
6) How easy will it be to add a new feature to this program in a year?
   *   Will your program continue to work after upgrading...
7) ...your computer's hardware?
8) ...the operating system?
9) ...to the next version of Python?
<br></br>
   * **Answers**
   1) 
   2) 
   3) 
   4) 
   5) 
   6) 
   7) 
   8) 
   9) 
