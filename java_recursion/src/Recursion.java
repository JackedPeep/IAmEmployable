import java.sql.Array;

public class Recursion {
    public static void main(String[] args) {

        int[] sumMe = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89};
        System.out.printf("Array Sum: %d\n", arraySum(sumMe, 0));

        int[] minMe = {0, 1, 1, 2, 3, 5, 8, -42, 13, 21, 34, 55, 89};
        System.out.printf("Array Min: %d\n", arrayMin(minMe, 0));

        String[] amISymmetric = {
                "You can cage a swallow can't you but you can't swallow a cage can you",
                "I still say cS 1410 is my favorite class"
        };
        for (String test : amISymmetric) {
            String[] words = test.toLowerCase().split(" ");
            System.out.println();
            System.out.println(test);
            System.out.printf("Is word symmetric: %b\n", isWordSymmetric(words, 0, words.length - 1));
        }

        double weights[][] = {
                {51.18},
                {55.90, 131.25},
                {69.05, 133.66, 132.82},
                {53.43, 139.61, 134.06, 121.63}
        };
        System.out.println();
        System.out.println("--- Weight Pyramid ---");
        for (int row = 0; row < weights.length; row++) {
            for (int column = 0; column < weights[row].length; column++) {
                double weight = computePyramidWeights(weights, row, column);
                System.out.printf("%.2f ", weight);
            }
            System.out.println();
        }

        char image[][] = {
                {'*', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' '},
                {' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' '},
                {' ', ' ', ' ', ' ', ' ', ' ', '*', '*', ' ', ' '},
                {' ', '*', ' ', ' ', '*', '*', '*', ' ', ' ', ' '},
                {' ', '*', '*', ' ', '*', ' ', '*', ' ', '*', ' '},
                {' ', '*', '*', ' ', '*', '*', '*', '*', '*', '*'},
                {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' '},
                {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' '},
                {' ', ' ', ' ', '*', '*', '*', ' ', ' ', '*', ' '},
                {' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', '*', ' '}
        };
        int howMany = howManyOrganisms(image);
        System.out.println();
        System.out.println("--- Labeled Organism Image ---");
        for (char[] line : image) {
            for (char item : line) {
                System.out.print(item);
            }
            System.out.println();
        }
        System.out.printf("There are %d organisms in the image.\n", howMany);

    }


    public static boolean isWordSymmetric(String[] words, int start, int end) {
        //checks to see if the item +1 and
        //-1 in the list are equal to each other until it reaches the end?
        if (words.length == 0){
            return true;
        }
        if (words[start].toLowerCase().equals(words[end].toLowerCase())) {
            if (end - start > 1) {
                isWordSymmetric(words, (start + 1), (end - 1));

            }
        } else {
            return false;
        }
        return true;
    }

    public static long arraySum(int[] data, int position) {
        //Description: Write a recursive method that
        // returns the total of all elements in the array.
        if (data.length == 0)
            return 0;
        long sum = 0;
        if (position != data.length - 1) {
            sum = (arraySum(data, position + 1) + data[position]);
        } else {

            return data[position];
        }
        return sum;

    }

    public static int arrayMin(int[] data, int position) {
        //Description: Write a recursive function that returns the
        // minimum value of the elements in the array.
        // You may assume there is at least one value in the array.
        int lowestNumber = 0;
        if (position != data.length - 1) {
            lowestNumber = arrayMin(data, position + 1);
            if (lowestNumber < data[position]) {
                return lowestNumber;
            }
        }
        return data[position];

    }

    public static double computePyramidWeights(double[][] weights, int row, int column) {

        //Don't call function if row or column will be less then 0, return 0
        if(weights.length == 0) return 0;
        if (row < 0 || column < 0) {
            return 0;
        }
        //Don't call function if column is greater then row, return 0
        else if (column > row) {
            return 0;
        }
        if (row > weights.length-1) return 0;
        if (weights[row].length == 0) return 0;

        //weights above are positions row-1,col-1 and row-1, col
        double left = computePyramidWeights(weights, row - 1, column - 1);
        double right = computePyramidWeights(weights, row - 1, column);
        return ((left + right) / 2) + weights[row][column];


    }

    public static int howManyOrganisms(char[][] image) {
        int row = 0, col = 0, count = 0;
        for (char[] line : image) {

            for (char item : line) {

                if (item == '*') {
                    organismStamp(image, count, row, col);
                    count++;
                    System.out.print(count);
                    System.out.print(row);
                    System.out.println(col);
                }
                col++;
            }
            col = 0;
            row++;


        }
        return count;
    }
    public static void organismStamp( char[][] image, int count, int row, int col){
        int ASCII = 97 + count;

        image[row][col] = (char)ASCII;


        if (row-1 >= 0) {
            if(col <  image[row-1].length) {
                if (image[row - 1][col] == '*') {
                    organismStamp(image, count, row - 1, col);
                }
            }
        }
        if (row+1 < image.length) {
            if(col <  image[row+1].length) {
                if (image[row + 1][col] == '*') {
                    organismStamp(image, count, row + 1, col);
                }
            }
        }
        if (col-1 >= 0) {
            if (image[row][col - 1] == '*') {
                organismStamp(image, count, row, col- 1);
            }
        }
        if (col + 1 < image[row].length) {
            if (image[row][col + 1] == '*') {
                organismStamp(image, count, row, col + 1);
            }
        }




    }


}