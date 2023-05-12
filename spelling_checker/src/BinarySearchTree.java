public class BinarySearchTree<E extends Comparable <E>> {

    TreeNode root = null;

    public E getRootValue() {
        return root.value;
    }

    public boolean isEmpty() {
        return root == null;
    }

    public void traverseInOrder() {
        traverseInOrder(root);
    }

    private void traverseInOrder(TreeNode node) {
        if (node != null) {
            traverseInOrder(node.left);
            System.out.println(node.value);
            traverseInOrder(node.right);
        }
    }

    public boolean insert(E value) {
        if(!search(value)){
            if (root == null) {
                root = new TreeNode(value);
            } else if(value.compareTo(root.value)<0){
                insert(root, root.left, value);
            }
            else{
                insert(root, root.right, value);
            }
        return true;
        }
        return false;
    }

    private void insert(TreeNode parent, TreeNode node, E value) {
        if (node == null) {
            // Perform the insert
            if (value.compareTo(parent.value)<0) {
                parent.left = new TreeNode(value);
            } else {
                parent.right = new TreeNode(value);
            }
        } else {
            if (value.compareTo(node.value) < 0) {
                insert(node, node.left, value);
            } else {
                insert(node, node.right, value);
            }
        }
    }

    public boolean remove(E value) {
        if(search(value)) {
            TreeNode parent = null;
            TreeNode node = root;

            // Search for the node to remove
            boolean done = false;
            while (!done) {
                if (value.compareTo(node.value) == 0) {
                    done = true;
                } else if (value.compareTo(node.value) < 0) {
                    parent = node;
                    node = node.left;
                } else {
                    parent = node;
                    node = node.right;
                }
            }

            // Check for left child
            if (node.left != null) {
                TreeNode parentOfRight = node;
                TreeNode rightMost = node.left;

                while (rightMost.right != null) {
                    parentOfRight = rightMost;  // This statement was missing
                    rightMost = rightMost.right;
                }
                // rightMost has the largest value in the left subtree
                node.value = rightMost.value;

                if (parentOfRight.right == rightMost) {
                    parentOfRight.right = rightMost.left;
                } else {
                    parentOfRight.left = rightMost.left;    // this statement incorrectly used rightMost.right;
                }
            } else {
                // Remove based on no-left child
                if (parent == null) {
                    root = root.right;
                } else {
                    if (parent.value.compareTo(value) < 0) {
                        parent.right = node.right;
                    } else {
                        parent.left = node.right;
                    }
                }

            }
        return true;
        }
        return false;


    }

    private class TreeNode {
        E value;
        TreeNode left;
        TreeNode right;
        public TreeNode(E value) {
            this.value = value;
        }
    }


    public boolean search(E value){
        if (root == null) {
            return false;
        } else {
            if (root.value.compareTo(value) == 0){
                return true;
            }
            else{
              boolean left =  search(root.left, value);
              boolean right = search(root.right, value);
              return left || right;
            }
        }

    }

    private boolean search(TreeNode node, E value){
        if (node == null) {
            return false;
        } else {
            if (node.value.compareTo(value) == 0) {
                System.out.println("Found");
                return true;
            }
//            else if (node.value.compareTo(value) < 0) {
//                return search(node.left, value);
//            } else {
//                return search(node.right, value);
//            }
            else{
                boolean left =  search(node.left, value);
                boolean right = search(node.right, value);
                return left || right;
            }
        }
    }

    public void display(E message){
        System.out.println(message);
        traverseInOrder();
    }
    public int numberNodes(){
        if (root == null){
            return 0;
        }
        int number = numberNodes(root.left);
        number += numberNodes(root.right);
        return number + 1;
    }
    private int numberNodes(TreeNode node){
        if (node == null){
            return 0;
        }
        int number = numberNodes(node.left);
        number += numberNodes(node.right);
        return number + 1;
    }

    public int numberLeafNodes(){
        if (root == null){
            return 0;
        }
        int rNumber = numberLeafNodes(root.right);
        int lNumber = numberLeafNodes(root.left);
        if (rNumber == 0 && lNumber == 0){
            return 1;
        }
        else{
            return rNumber+lNumber;
        }

    }
    public int numberLeafNodes(TreeNode node){
        if (node == null){
            return 0;
        }
        int rNumber = numberLeafNodes(node.right);
        int lNumber = numberLeafNodes(node.left);
        if (rNumber == 0 && lNumber == 0){
            return 1;
        }
        else{
            return rNumber+lNumber;
        }

    }
    public int height(){
        if (root == null){
            return 0;
        }
        int rNumber = height(root.right);
        int lNumber = height(root.left);
        if (rNumber > lNumber){
            return rNumber;
        }
        else{
            return lNumber;
        }
    }
    public int height(TreeNode node){
        if (node == null){
            return 0;
        }
        int rNumber = height(node.right);
        int lNumber = height(node.left);
        if (rNumber > lNumber){
            return rNumber+1;
        }
        else{
            return lNumber+1;
        }
    }
}