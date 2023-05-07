import com.sun.source.tree.BinaryTree;

import java.util.*;

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
    private String toStringTraverse(BinaryTreeNode node, String depth){
        if (node == null){
            return "";
        }
        String rightTraverse = toStringTraverse(node.right, depth + " ");
        String leftTraverse = toStringTraverse(node.left, depth + " ");
        String parent = " [no parent]";
        if(node.parent != null){

            parent = " [" + node.parent.key + "]";
        }


        return  rightTraverse + depth + node.key + parent + "\n" + leftTraverse;
    }
    /**
     * Return a string containing the tree contents as a tree with one node per line
     */
    public String toString() {
        return toStringTraverse(root, "|");

    }

    private String inOrderToStringTraverse(BinaryTreeNode node){
        if (node == null){
            return"";
        }
        String leftTraverse = inOrderToStringTraverse(node.left);
        String rightTraverse = inOrderToStringTraverse(node.right);

        return leftTraverse + node.key + " " + rightTraverse;

    }
    /**
     * Return a string containing the tree contents as a single line
     */
    public String inOrderToString() {

        return inOrderToStringTraverse(root);

    }
    private void traverseAndFlip(BinaryTreeNode node){
        if (node == null) {
            return;
        }
        traverseAndFlip(node.left);
        traverseAndFlip(node.right);
        BinaryTreeNode left = node.left; //node.left place-holder after node.left has been swapped
        node.left = node.right;
        node.right = left;

    }
    /**
     * reverse left and right children recursively
     */
    public void flip() {
        traverseAndFlip(root);
    }

    /**
     * Returns the in-order successor of the specified node
     * @param node node from which to find the in-order successor
     */
    public BinaryTreeNode inOrderSuccessor(BinaryTreeNode node) {

       ArrayList<BinaryTreeNode> inOrderTree = inOrderTraverse(root);
       for(int i =0; i < inOrderTree.size()-1; i++){
           if(node.key.compareTo(inOrderTree.get(i).key) == 0){
               return inOrderTree.get(i+1);
           }
       }
        return null;
    }
    private int nodesInLevelTraversal(BinaryTreeNode node, int level, int currentLevel, int numNode){
        if(node == null){
            return numNode;
        }
        if (level == currentLevel){
               numNode++;
        return numNode;
        }
        numNode = nodesInLevelTraversal(node.left, level, currentLevel+1, numNode);
        return nodesInLevelTraversal(node.right, level, currentLevel+1, numNode);
    }
    /**
     * Counts number of nodes in specified level
     *
     * @param level Level in tree, root is zero
     * @return count of number of nodes at specified level
     */
    public int nodesInLevel(int level) {
        int currentLevel = 0;
        int numNode = 0;
        return nodesInLevelTraversal(root, level, currentLevel, numNode);

    }
    private void printAllPathsTraverse(BinaryTreeNode node, String path){
        if(node == null){
            return;
        }
        if(node.right == null && node.left == null){
            System.out.println(path + node.key);
        }
        else{
        printAllPathsTraverse(node.left, path + node.key + " ");
        printAllPathsTraverse(node.right, path + node.key + " ");

        }
    }
    /**
     * Print all paths from root to leaves
     */
    public void printAllPaths() {
        printAllPathsTraverse(root, "");

    }
    private int countBSTTraverse(BinaryTreeNode node){

        if(node == null){
            return 0;
        }
        int currentNumBST = 0;
        if(node.left == null && node.right == null){
            currentNumBST++;

        }
        else if(node.left != null && node.right != null) {
            if (node.left.key.compareTo(node.key) < 0 && node.right.key.compareTo(node.key) > 0) {
                currentNumBST++;
            }
        }
        else if(node.left != null){
            if(node.left.key.compareTo(node.key) < 0){
                currentNumBST++;
            }
        }
        else{
            if(node.right.key.compareTo(node.key) > 0){
                currentNumBST++;
            }
        }

        int right = 0;
        if(node.right != null){
            right = countBSTTraverse(node.right);
        }
        int left = 0;
        if(node.left != null) {
            left = countBSTTraverse(node.left);
        }
        return right + left + currentNumBST;
    }
    /**
     * Counts all non-null binary search trees embedded in tree
     *
     * @return Count of embedded binary search trees
     */
    public int countBST() {
        return countBSTTraverse(root);

    }

    /**
     * Insert into a bst tree; duplicates are allowed
     *
     * @param x the item to insert.
     */
    public void insert(E x) {
        root = insert(x, root, null);
    }

    private BinaryTreeNode getKeyTraversal(BinaryTreeNode node, E key){
        if(node == null){
            return null;
        }
        if(node.key.compareTo(key) == 0){

            return node;
        }
        if(node.key.compareTo(key) > 0){

            return getKeyTraversal(node.left, key);
        }

        BinaryTreeNode right = getKeyTraversal(node.right, key);
        return right;
    }
    public BinaryTreeNode getByKey(E key) {
        return getKeyTraversal(root, key);

    }

private ArrayList<BinaryTreeNode> inOrderTraverse(BinaryTreeNode node) {
    ArrayList<BinaryTreeNode> nodeList = new ArrayList<>();
    if (node == null) {
        return nodeList;
    }
    nodeList.addAll(inOrderTraverse(node.left));
    nodeList.add(node);
    nodeList.addAll(inOrderTraverse(node.right));

    return nodeList;
}

    private void balanceTreeTraverse(ArrayList<BinaryTreeNode> tree){

        if (tree.size() == 0) {
            return;
        }
        else if(tree.size() == 1){
            insert(tree.get(0).key);
            return;
        }
        else if (tree.size() == 2) {
            insert(tree.get(0).key);
            insert(tree.get(1).key);
            return;
        }
        BinaryTreeNode node = tree.get(tree.size() / 2);
        if (node == null) {
            return;
        }
        insert(node.key);
        ArrayList<BinaryTreeNode> leftTree = new ArrayList<>(tree.subList(0,tree.size()/2));
        balanceTreeTraverse(leftTree);
        ArrayList<BinaryTreeNode> rightTree = new ArrayList<>(tree.subList((tree.size()/2+1),tree.size()));
        balanceTreeTraverse(rightTree);

    }

    /**
     * Balance the tree
     */
    public void balanceTree() {
        ArrayList<BinaryTreeNode> tree = new ArrayList<>(inOrderTraverse(root));
        root = new BinaryTreeNode(tree.get(tree.size()/2).key);

        ArrayList<BinaryTreeNode> leftTree = new ArrayList<>(tree.subList(0,tree.size()/2));
        balanceTreeTraverse(leftTree);
        ArrayList<BinaryTreeNode> rightTree = new ArrayList<>(tree.subList((tree.size()/2+1),tree.size()));
        balanceTreeTraverse(rightTree);

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


    /**
     * Internal method to find an item in a subtree.
     * This routine runs in O(log n) as there is only one recursive call that is executed and the work
     * associated with a single call is independent of the size of the tree: a=1, b=2, k=0
     *
     * @param x is item to search for.
     * @param t the node that roots the subtree.
     *          SIDE EFFECT: Sets local variable curr to be the node that is found
     * @return node containing the matched item.
     */
    private boolean contains(E x, BinaryTreeNode t) {
        if (t == null)
            return false;

        int compareResult = x.compareTo(t.key);

        if (compareResult < 0)
            return contains(x, t.left);
        else if (compareResult > 0)
            return contains(x, t.right);
        else {
            return true;    // Match
        }
    }

    // Basic node stored in unbalanced binary trees
    public class BinaryTreeNode {
        E key;            // The data/key for the node
        BinaryTreeNode left;   // Left child
        BinaryTreeNode right;  // Right child
        BinaryTreeNode parent; //  Parent node

        // Constructors
        BinaryTreeNode(E theElement) {
            this(theElement, null, null, null);
        }

        BinaryTreeNode(E theElement, BinaryTreeNode lt, BinaryTreeNode rt, BinaryTreeNode pt) {
            key = theElement;
            left = lt;
            right = rt;
            parent = pt;
        }

        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("Node:");
            sb.append(key);
            if (parent == null) {
                sb.append("<>");
            } else {
                sb.append("<");
                sb.append(parent.key);
                sb.append(">");
            }

            return sb.toString();
        }
    }
}
