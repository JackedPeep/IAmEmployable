import org.junit.Assert;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class RecursionTest {

    @org.junit.Test
    public void aRecursionTestIsWordSymmetricInputTest() {
        String [] emptyArray = {};
        String [] array = {"I"};
        String [] array2 = "I have to push the pram a lot!".split(" ");

        Assert.assertEquals("IsWordSymmetric must be able to handle an empty array", true, Recursion.isWordSymmetric(emptyArray, 0, 0));
        Assert.assertEquals("IsWordSymmetric must be able to handle a single word", true, Recursion.isWordSymmetric(array, 0, 0));
        Assert.assertEquals("IsWordSymmetric must be able to handle a start and end position at the end of the array", false, Recursion.isWordSymmetric(array2, array2.length - 2, array2.length - 1));
        Assert.assertEquals("IsWordSymmetric must be able to handle a start and end position at the end of the array", true, Recursion.isWordSymmetric(array2, array2.length - 1, array2.length - 1));
    }

    @org.junit.Test
    public void bRecursionTestIsWordSymmetricTest() {
        String [] array = "I have to push the pram a lot!".split(" ");
        String [] array1 = "this easy this".split(" ");
        String [] array2 = "You can cage a swallow can't you but you can't swallow a cage can you".split(" ");

        Assert.assertEquals(false, Recursion.isWordSymmetric(array, 0, array.length - 1));
        Assert.assertEquals(true, Recursion.isWordSymmetric(array1, 0, array1.length - 1));
        Assert.assertEquals("IsWordSymmetric must be case insensitive", true, Recursion.isWordSymmetric(array2, 0, array2.length - 1));

        String [] arrayEven = "Aa bb bb Aa".split(" ");
        Assert.assertEquals("IsWordSymmetric must be able to handle an even number of items", true, Recursion.isWordSymmetric(arrayEven, 0, arrayEven.length - 1));

        String [] arrayOdd = "Aa bb ccc bb Aa".split(" ");
        Assert.assertEquals("IsWordSymmetric must be able to handle an odd number of items", true, Recursion.isWordSymmetric(arrayOdd, 0, arrayOdd.length - 1));
    }

    @org.junit.Test
    public void cRecursionTestArraySumInputTest() {
        int [] emptyArray = {};

        Assert.assertEquals("ArraySum must be able to handle an empty array", 0, Recursion.arraySum(emptyArray, 0));
        Assert.assertEquals("ArraySum must be able to handle bad position values", 0, Recursion.arraySum(emptyArray, 1));
    }

    @org.junit.Test
    public void dRecursionTestArraySumTest() {
        int[] array = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        int position = 4;

        Assert.assertEquals("ArraySum calculated an incorrect sum", 232, Recursion.arraySum(array, 0));
        Assert.assertEquals(String.format("ArraySum calculated an incorrect sum when starting at position %d", position), 225, Recursion.arraySum(array, position));

        position = array.length - 1;
        Assert.assertEquals(String.format("ArraySum calculated an incorrect sum when starting at position %d (end of array)", position), 89, Recursion.arraySum(array, position));

        int[] array2 = { 1, 1, 2, 3, 5, 8, 13, 21, 34, -45, 89 };
        Assert.assertEquals("ArraySum calculated an incorrect sum with a negative number in the array", 132, Recursion.arraySum(array2, 0));
    }

    @org.junit.Test
    public void eRecursionTestArrayMinInputTest() {
        int[] inOrder = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        int position = inOrder.length - 1;

        Assert.assertEquals(String.format("ArrayMin must be able to handle position of ", position), 89, Recursion.arrayMin(inOrder, position));
    }

    @org.junit.Test
    public void fRecursionTestArrayMinTest() {
        int[] inOrder = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        int[] reverseOrder = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 };
        int[] randomOrder = { 5, 1, 100, 7, 6, 2, 0 };
        int[] randomWithNeg = { 5, 1, 100, -6, 7, 6, 2, 0, -1 };

        Assert.assertEquals("ArrayMin must be able to find the correct min with an in-order array", 1, Recursion.arrayMin(inOrder, 0));
        Assert.assertEquals("ArrayMin must be able to find the correct min with a reverse-ordered array", 1, Recursion.arrayMin(reverseOrder, 0));
        Assert.assertEquals("ArrayMin must be able to find the correct min with a random-ordered array", 0, Recursion.arrayMin(randomOrder, 0));
        Assert.assertEquals("ArrayMin must be able to find the correct min with a random-ordered array with negatives", -6, Recursion.arrayMin(randomWithNeg, 0));
    }

    @org.junit.Test
    public void gRecursionTestComputePyramidWeightsInputTest() {
        double [][] weights = {{}};
        double [][] weights1 = {
                { 51.18 },
                { 55.90, 131.25 },
                { 69.05, 133.66, 132.82 },
                { 53.43, 139.61, 134.06, 121.63 }
        };

        Assert.assertEquals("ComputePyramidWeights must be able to handle an empty array", 0.0, Recursion.computePyramidWeights(weights, 0, 0), 0.001);
        Assert.assertEquals("ComputePyramidWeights must be able to handle negative row values", 0.0, Recursion.computePyramidWeights(weights, -1, 0), 0.001);
        Assert.assertEquals("ComputePyramidWeights must be able to handle negative col values", 0.0, Recursion.computePyramidWeights(weights, 0, -1), 0.001);
        Assert.assertEquals("ComputePyramidWeights must be able to handle invalid column", 0.0, Recursion.computePyramidWeights(weights1, 0, 3), 0.001);
        Assert.assertEquals("ComputePyramidWeights must be able to handle invalid row", 0.0, Recursion.computePyramidWeights(weights1, 4, 0), 0.001);
    }

    @org.junit.Test
    public void hRecursionTestComputePyramidWeightsTest() {
        double weights[][] = {
                           { 51.18 },
                        { 55.90, 131.25 },
                    { 69.05, 133.66, 132.82 },
                { 53.43, 139.61, 134.06, 121.63 }
        };

        Assert.assertEquals("ComputePyramidWeights must be able to handle an array with a single row and col", 51.18, Recursion.computePyramidWeights(weights, 0, 0), 0.001);
        Assert.assertEquals("ComputePyramidWeights must be able to handle an array with multiple rows and one col", 108.327, Recursion.computePyramidWeights(weights, 3, 0), 0.001);
        Assert.assertEquals("ComputePyramidWeights must be able to handle an array with multiple cols and rows", 227.25, Recursion.computePyramidWeights(weights, 3, 3), 0.001);
    }

    @org.junit.Test
    public void iRecursionTestHowManyOrganismsInputTest() {
        char [][] image = {{}};
        char [][] image1 = {{'*'}};
        char [][] image2 = {{'*', ' '}};
        char [][] image3 = {{'*', ' '}, {'*'}, {'*', '*', '*'}};

        Assert.assertEquals("HowManyOrganisms must be able to handle an empty image", 0, Recursion.howManyOrganisms(image));
        Assert.assertEquals("HowManyOrganisms must be able to handle an image with a single row/col", 1, Recursion.howManyOrganisms(image1));
        Assert.assertEquals("HowManyOrganisms must be able to handle a rectangular image", 1, Recursion.howManyOrganisms(image2));
        Assert.assertEquals("HowManyOrganisms must be able to handle a ragged image", 1, Recursion.howManyOrganisms(image3));
    }

    @org.junit.Test
    public void jRecursionTestHowManyOrganismsTest() {
        char [][] image = {
                {'*',' ',' ','*',' ',' ',' ',' ','*',' '},
                {' ','*',' ',' ',' ',' ',' ',' ',' ',' '},
                {' ',' ',' ',' ',' ',' ','*',' ',' ',' '},
                {' ','*',' ','*',' ','*',' ',' ',' ',' '},
                {' ',' ',' ',' ','*',' ','*',' ','*',' '},
                {' ','*',' ',' ',' ','*',' ','*',' ','*'},
                {' ',' ',' ','*',' ',' ',' ',' ','*',' '},
                {' ',' ','*',' ',' ',' ',' ',' ',' ',' '},
                {' ',' ',' ',' ','*',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ','*',' ',' ',' ',' '}
        };

        char [][] image1 = {
                {'*','*',' ','*','*','*','*','*','*','*'},
                {'*','*',' ',' ','*',' ',' ',' ','*','*'},
                {'*',' ',' ',' ','*',' ','*','*',' ','*'},
                {'*','*',' ','*','*','*','*',' ',' ','*'},
                {'*','*','*',' ','*',' ','*',' ','*','*'},
                {'*','*','*',' ','*','*','*','*','*','*'},
                {'*',' ',' ','*',' ',' ',' ',' ','*','*'},
                {'*',' ','*','*',' ',' ',' ',' ','*','*'},
                {'*',' ','*','*','*','*',' ',' ','*','*'},
                {'*','*','*','*','*','*','*','*','*','*'}
        };
        Assert.assertEquals(21, Recursion.howManyOrganisms(image));
        Assert.assertEquals("HowManyOrganisms should be able to handle cascading",1, Recursion.howManyOrganisms(image1));
    }

    @org.junit.Test
    public void kRecursionTestHowManyOrganismsInputRaggedTest() {
        char [][] image = {{'*', ' '},
                            {' '},
                            {'*', ' ', '*'}};
        char [][] image1 = {{'*', ' '},
                            {'*'},
                            {'*', '*', '*'}};

        Assert.assertEquals("HowManyOrganisms must be able to handle a ragged image", 3, Recursion.howManyOrganisms(image));
        Assert.assertEquals("HowManyOrganisms must be able to handle a ragged image with cascading", 1, Recursion.howManyOrganisms(image1));
    }
}
