
public class Recursion {
    public static void main(String[] args) {
        Integer[] v1 = {25, 10, 60, 55, 58, 56, 14, 63, 8, 50, 6, 9};
        Integer[] v2 = {200, 15, 3, 65, 83, 70, 90};
        //Integer[] v2 = {10, 1, 3, 5, 15, 12, 16};
        //Integer[] v2 = {30, 20, 10, 15, 25, 23, 39, 35, 42};

        Tree<Integer> tree1 = new Tree<>(v1, "Tree 1");
        Tree<Integer> tree2 = new Tree<>(v2, "Tree 2");
        Tree<Integer> tree3 = new Tree<>(v2, "Tree 3");

        //System.out.println("-- tree1.getByKey --");
        //System.out.println(tree1.getByKey(v1[2]).key);
        System.out.println("-- tree1.toString() --");
        System.out.println(tree1.toString());
        System.out.println("-- tree2.toString() --");
        System.out.println(tree2.toString());

        System.out.println("-- tree1.inOrderToString() --");
        System.out.println(tree1.inOrderToString());
        System.out.println("-- tree2.inOrderToString() --");
        System.out.println(tree2.inOrderToString());
        System.out.println();

        System.out.println("-- tree2.balanceTree() --");
        tree2.balanceTree();
        System.out.println(tree2.toString());
        System.out.println();

        System.out.println("-- tree1.flip() --");
        tree1.flip();
        System.out.println(tree1.toString());
        tree1.flip();   // restore it back to normal
        System.out.println();

        System.out.println("-- tree1.nodesInLevel(...) --");
        System.out.printf("Nodes in level 0: %d\n", tree1.nodesInLevel(0));
        System.out.printf("Nodes in level 1: %d\n", tree1.nodesInLevel(1));
        System.out.printf("Nodes in level 2: %d\n", tree1.nodesInLevel(2));
        System.out.printf("Nodes in level 3: %d\n", tree1.nodesInLevel(3));
        System.out.printf("Nodes in level 4: %d\n", tree1.nodesInLevel(4));
        System.out.printf("Nodes in level 5: %d\n", tree1.nodesInLevel(5));
        System.out.println();

        System.out.println("-- tree1.printAllPaths() --");
        tree1.printAllPaths();
        System.out.println("-- tree3.printAllPaths() --");
        tree3.printAllPaths();
        System.out.println();

        System.out.println("-- tree1.inOrderSuccessor(...) --");
        System.out.printf("In-order successor of 25 is: %s\n", tree1.inOrderSuccessor(tree1.getByKey(25)));
        System.out.printf("In-order successor of 6 is: %s\n", tree1.inOrderSuccessor(tree1.getByKey(6)));
        System.out.printf("In-order successor of 9 is: %s\n", tree1.inOrderSuccessor(tree1.getByKey(9)));
        System.out.printf("In-order successor of 58 is: %s\n", tree1.inOrderSuccessor(tree1.getByKey(58)));
        System.out.println();

        System.out.println("-- tree1.countBST() --");
        System.out.printf("# of BSTs is: %d\n", tree1.countBST());
        tree1.flip();
        System.out.printf("# of BSTs after calling .flip() is: %d\n", tree1.countBST());
        System.out.println("-- tree3.countBST() --");
        System.out.printf("# of BSTs is: %d\n", tree3.countBST());
        tree3.flip();
        System.out.printf("# of BSTs after calling .flip() is: %d\n", tree3.countBST());
    }
}
