import org.junit.Assert;

import java.util.ArrayList;

public class BinarySearchTreeTest {

    @org.junit.Test
    public void BinarySearchTreeConstructor() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();

        Assert.assertNotNull ("BinarySearchTree must not be null", intBst);
    }

    @org.junit.Test
    public void BinarySearchTreeInsertTest1() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                4,
                2, 6,
                1, 3, 5, 7
        };
        int count = 0;

        for (int item : array) {
            count++;
            Assert.assertTrue(String.format("BST failed to insert %s and return true", Integer.toString(item)), intBst.insert(item));
            Assert.assertEquals("BST Insert must correctly handle the number of nodes", count, intBst.numberNodes());
        }
    }

    @org.junit.Test
    public void BinarySearchTreeInsertTest2() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                10,
                6,           14,
                4, 8,        12, 16,
                3, 5, 7, 9,  11, 13, 15, 17
        };
        int count = 0;

        for (int item : array) {
            count++;
            Assert.assertTrue(String.format("BST failed to insert %s and return true", Integer.toString(item)), intBst.insert(item));
            Assert.assertEquals("BST Insert must correctly handle the number of nodes", count, intBst.numberNodes());
        }

        for (int item : array) {
            Assert.assertFalse(String.format("BST failed to handle re-inserting %s and returning false", Integer.toString(item)), intBst.insert(item));
        }
    }

    @org.junit.Test
    public void BinarySearchTreeRemoveLeafTest1() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                4,
                2, 6,
                1, 3, 5, 7
        };
        int count = array.length;

        for (int item : array) {
            intBst.insert(item);
        }

        Assert.assertEquals("BST returned incorrect number of nodes", count, intBst.numberNodes());
        Assert.assertTrue(intBst.remove(1));
        Assert.assertEquals("BST returned incorrect number of nodes after remove", --count, intBst.numberNodes());

        Assert.assertTrue(intBst.remove(3));
        Assert.assertEquals("BST returned incorrect number of nodes after remove", --count, intBst.numberNodes());

        Assert.assertTrue(intBst.remove(5));
        Assert.assertEquals("BST returned incorrect number of nodes after remove", --count, intBst.numberNodes());

        Assert.assertTrue(intBst.remove(7));
        Assert.assertEquals("BST returned incorrect number of nodes after remove", --count, intBst.numberNodes());

        Assert.assertTrue(intBst.remove(2));
        Assert.assertEquals("BST returned incorrect number of nodes after remove", --count, intBst.numberNodes());

        Assert.assertTrue(intBst.remove(6));
        Assert.assertEquals("BST returned incorrect number of nodes after remove", --count, intBst.numberNodes());

        Assert.assertTrue(intBst.remove(4));
        Assert.assertEquals("BST returned incorrect number of nodes after remove", --count, intBst.numberNodes());
    }

    @org.junit.Test
    public void BinarySearchTreeRemoveParentTest1() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                10,
                6,           14,
                4, 8,        12, 16,
                3, 5, 7, 9,  11, 13, 15, 17
        };
        int count = array.length;

        for (int item : array) {
            intBst.insert(item);
        }

        for (int item : array) {
            Assert.assertTrue(String.format("BST returned response when removing parent %d", item), intBst.remove(item));
            Assert.assertEquals(String.format("BST returned incorrect number of nodes after removal of parent %d", item), --count, intBst.numberNodes());
        }
    }

    @org.junit.Test
    public void BinarySearchTreeSearchTest1() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                10,
                6,           14,
                4, 8,        12, 16,
                3, 5, 7, 9,  11, 13, 15, 17
        };

        for (int item : array) {
            intBst.insert(item);
            Assert.assertTrue(String.format("BST failed to find node %d", item), intBst.search(item));
        }
    }

    @org.junit.Test
    public void BinarySearchTreeSearchTest2() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                10,
                6,           14,
                4, 8,        12, 16,
                3, 5, 7, 9,  11, 13, 15, 17
        };
        ArrayList<Integer> curIntList = new ArrayList<>();

        for (int item : array) {
            intBst.insert(item);
            Assert.assertTrue(String.format("BST failed to find node %d", item), intBst.search(item));

            for ( int tmpItem : curIntList) {
                Assert.assertTrue(String.format("BST failed to find node %d after inserting %d", tmpItem, item), intBst.search(tmpItem));
            }

            curIntList.add(item);
        }
    }

    @org.junit.Test
    public void BinarySearchTreeSearchTest3() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                10,
                6,           14,
                4, 8,        12, 16,
                3, 5, 7, 9,  11, 13, 15, 17
        };
        ArrayList<Integer> curIntList = new ArrayList<>();

        for (int item : array) {
            intBst.insert(item);
            curIntList.add(item);
        }


        for (int item : array) {
            intBst.remove(item);
            curIntList.remove(0); // Pop the top
            Assert.assertFalse(String.format("BST still find node %d after it was removed", item), intBst.search(item));

            for ( int tmpItem : curIntList) {
                Assert.assertTrue(String.format("BST failed to find node %d after removing %d", tmpItem, item), intBst.search(tmpItem));
            }

        }
    }

    @org.junit.Test
    public void BinarySearchTreeNumberNodesTest1() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                4,
                2, 6,
                1, 3, 5, 7
        };
        int count = 0;

        for (int item : array) {
            count++;
            intBst.insert(item);
            Assert.assertEquals("BST Insert must correctly handle the number of nodes", count, intBst.numberNodes());
        }
    }

    @org.junit.Test
    public void BinarySearchTreeNumberNodesTest2() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                10,
                6,           14,
                4, 8,        12, 16,
                3, 5, 7, 9,  11, 13, 15, 17
        };
        int count = 0;

        for (int item : array) {
            count++;
            intBst.insert(item);
            Assert.assertEquals("BST Insert must correctly handle the number of nodes", count, intBst.numberNodes());
        }

        for (int item : array) {
            count--;
            intBst.remove(item);
            Assert.assertEquals("BST remove must correctly handle the number of nodes", count, intBst.numberNodes());
        }
    }

    @org.junit.Test
    public void BinarySearchTreeNumberLeafNodeTest1() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                4,
                2, 6,
                1, 3, 5, 7
        };

        for (int item : array) {
            intBst.insert(item);
        }

        Assert.assertEquals("BST must correctly identify leaf nodes on a balanced tree", 4, intBst.numberLeafNodes());
    }

    @org.junit.Test
    public void BinarySearchTreeNumberLeafNodeTest2() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {1, 2, 3, 4, 5, 6, 7, 8};

        for (int item : array) {
            intBst.insert(item);
        }

        Assert.assertEquals("BST must correctly identify leaf nodes on an unbalanced tree", 1, intBst.numberLeafNodes());

        // Removed these tests because the number of leaf nodes can change depending upon the 'delete' implementation
        // for (int item : array) {
        //     Assert.assertEquals("BST must correctly identify leaf nodes on an unbalanced tree after a root removal", 1, intBst.numberLeafNodes());
        //     intBst.remove(item);
        // }
    }

    @org.junit.Test
    public void BinarySearchTreeHeightTest1() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {1, 2, 3, 4, 5, 6, 7, 8};
        int height = 0;

        for (int item : array) {
            intBst.insert(item);
            Assert.assertEquals("BST must correctly calculate height on an unbalanced tree", height, intBst.height());
            height++;
        }
    }

    @org.junit.Test
    public void BinarySearchTreeHeightTest2() {
        BinarySearchTree<Integer> intBst = new BinarySearchTree<>();
        int [] array = {
                4,
                2, 6,
                1, 3, 5, 7
        };
        int count = 0;

        for (int item : array) {
            intBst.insert(item);
            count++;

            int logVal = (int)(Math.log(count) / Math.log(2));
            Assert.assertEquals("BST must correctly calculate height on a balanced tree", logVal, intBst.height());
        }
    }
}
