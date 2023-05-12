//import org.junit.Assert;
//import org.junit.FixMethodOrder;
//import org.junit.runners.MethodSorters;
//
///**
// * Test the LifeSimulator class
// * kmort 2020
// */
//
//@FixMethodOrder(MethodSorters.NAME_ASCENDING)
//public class TestLifeSimulator {
//    /**
//     * Test the constructor, getters, and initialization
//     */
//    @org.junit.Test
//    public void aTestConstructor() {
//        final int x = 10;
//        final int y = 20;
//        LifeSimulator ls = new LifeSimulator(x, y);
//
//        Assert.assertEquals("X is wrong", ls.getSizeX(), x);
//        Assert.assertEquals("Y is wrong", ls.getSizeY(), y);
//
//        for (int xIterator = 0; xIterator < x; ++xIterator) {
//            for (int yIterator = 0; yIterator < y; ++yIterator) {
//                Assert.assertFalse(ls.getCell(xIterator, yIterator));
//            }
//        }
//        // by getting this far, you have a LifeSimulator with a constructor that ran. Good job.
//    }
//
//    /**
//     * Insert some patterns and see if we can read them out appropriately
//     */
//    @org.junit.Test
//    public void bTestInsertPatterns() {
//        final int x = 10;
//        final int y = 10;
//        final int xStart = 0;
//        final int yStart = 2;
//
//        LifeSimulator ls = new LifeSimulator(x, y);
//        PatternTestTrue testTrue = new PatternTestTrue();
//        ls.insertPattern(testTrue, xStart, yStart);
//
//        // x is down, y is across
//        boolean data[][] = {
//                {false, false, true, true, true, true, false, false, false, false},
//                {false, false, true, true, true, true, false, false, false, false},
//                {false, false, true, true, true, true, false, false, false, false},
//                {false, false, true, true, true, true, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false}};
//
//        for (int yIterator = 0; yIterator < y; ++yIterator) {
//            for (int xIterator = 0; xIterator < x; ++xIterator) {
//                Assert.assertEquals("Wrong pattern in cell", ls.getCell(xIterator, yIterator), data[xIterator][yIterator]);
//            }
//        }
//
//        LifeSimulator ls2 = new LifeSimulator(x, y);
//        PatternTestBlock testBlock = new PatternTestBlock();
//        ls2.insertPattern(testBlock, 2, 2);
//
//        boolean data2[][] = {
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, true, false, true, false, false, false, false},
//                {false, false, true, false, true, false, false, false, false, false},
//                {false, false, false, true, false, true, false, false, false, false},
//                {false, false, true, false, true, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false}};
//
//        for (int yIterator = 0; yIterator < y; ++yIterator) {
//            for (int xIterator = 0; xIterator < x; ++xIterator) {
//                Assert.assertEquals("Wrong pattern in cell", ls2.getCell(xIterator, yIterator), data2[xIterator][yIterator]);
//            }
//        }
//        // By getting this far, you have a LifeSimulator that can hold patterns. Rock on.
//    }
//
//    /**
//     * Run some iterations of update() and see if patterns match appropriately.
//     */
//    @org.junit.Test
//    public void cTestUpdate() {
//        final int x = 10;
//        final int y = 10;
//        final int xStart = 0;
//        final int yStart = 2;
//
//        LifeSimulator ls = new LifeSimulator(x, y);
//        PatternTestBlock testBlock = new PatternTestBlock();
//        ls.insertPattern(testBlock, 2, 2);
//
//        // x is down, y is across
//        boolean update1[][] = {
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, true, true, false, false, false, false, false},
//                {false, false, true, false, false, true, false, false, false, false},
//                {false, false, true, false, false, true, false, false, false, false},
//                {false, false, false, true, true, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false}};
//
//        boolean update2[][] = {
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, true, true, false, false, false, false, false},
//                {false, false, true, false, false, true, false, false, false, false},
//                {false, false, true, false, false, true, false, false, false, false},
//                {false, false, false, true, true, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false}};
//
//        boolean update3[][] = {
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, true, true, false, false, false, false, false},
//                {false, false, true, false, false, true, false, false, false, false},
//                {false, false, true, false, false, true, false, false, false, false},
//                {false, false, false, true, true, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false},
//                {false, false, false, false, false, false, false, false, false, false}};
//
//        ls.update();
//        for (int yIterator = 0; yIterator < y; ++yIterator) {
//            for (int xIterator = 0; xIterator < x; ++xIterator) {
//                Assert.assertEquals("Wrong pattern in update 1", ls.getCell(xIterator, yIterator), update1[xIterator][yIterator]);
//            }
//        }
//
//        ls.update();
//        for (int yIterator = 0; yIterator < y; ++yIterator) {
//            for (int xIterator = 0; xIterator < x; ++xIterator) {
//                Assert.assertEquals("Wrong pattern in update 2", ls.getCell(xIterator, yIterator), update2[xIterator][yIterator]);
//            }
//        }
//
//        ls.update();
//        for (int yIterator = 0; yIterator < y; ++yIterator) {
//            for (int xIterator = 0; xIterator < x; ++xIterator) {
//                Assert.assertEquals("Wrong pattern in update 3", ls.getCell(xIterator, yIterator), update3[xIterator][yIterator]);
//            }
//        }
//    // By getting this far, you have a LifeSimulator that can update patterns appropriately. Well done.
//    }
//}
//
///**
// * Test block pattern.
// */
//class PatternTestBlock extends Pattern {
//    private boolean data[][] = {
//            {false, true, false, true,},
//            {true, false, true, false,},
//            {false, true, false, true,},
//            {true, false, true, false,}};
//
//    public int getSizeX() {
//        return data[0].length;
//    }
//
//    public int getSizeY() {
//        return data.length;
//    }
//
//    public boolean getCell(int x, int y) {
//        return data[y][x];
//    }
//}
//
///**
// * Test block pattern
// */
//class PatternTestTrue extends Pattern {
//    private boolean data[][] = {
//            {true, true, true, true,},
//            {true, true, true, true,},
//            {true, true, true, true,},
//            {true, true, true, true,}};
//
//    public int getSizeX() {
//        return data[0].length;
//    }
//
//    public int getSizeY() {
//        return data.length;
//    }
//
//    public boolean getCell(int x, int y) {
//        return data[y][x];
//    }
//}