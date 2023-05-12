/**
 * Assignment 4 for CS 1410
 * This program evaluates the linear and binary searching, along
 * with comparing performance difference between the selection sort
 * and the built-in java.util.Arrays.sort.
 *
 * @author James Dean Mathias
 */
public class EvaluationDriver {
    static final int MAX_VALUE = 1_000_000;
    static final int MAX_ARRAY_SIZE = 100_000;
    static final int ARRAY_INCREMENT = 20_000;
    static final int NUMBER_SEARCHES = 50_000;

    public static void main(String[] args) {

        demoLinearSearchUnsorted();
        demoLinearSearchSorted();
        demoBinarySearchSelectionSort();
        demoBinarySearchFastSort();
    }

    public static int[] generateNumbers(int howMany, int maxValue) {
        if (howMany < 1){
            return null;

        }
        int[] randArr = new int[howMany];
        int numbers = 0;
        for (int i = 0; i < howMany; i++) {
            numbers = (int) Math.round(Math.random() * maxValue);
            randArr[i] = numbers;
        }

        return randArr;

    }

    public static boolean linearSearch(int[] data, int search) {
        for (int i = 0; i < data.length; i++) {
            if (data[i] == search) {
                return true;
            }

        }
        return false;

    }

    public static boolean binarySearch(int[] data, int search) {
        int low = 0;
        int high = data.length - 1;

        while (high >= low) {
            int mid = (low + high) / 2;
            if (search < data[mid])
                high = mid - 1;
            else if (search == data[mid])
                return true;
            else
                low = mid + 1;
        }
        return false;
    }

    public static void selectionSort(int[] data) {
        for (int i = 0; i < data.length - 1; i++) {
            int currentMin = data[i];
            int currentMinIndex = i;

            for (int j = i + 1; j < data.length; j++) {
                if (currentMin > data[j]) {
                    currentMin = data[j];
                    currentMinIndex = j;
                }
            }

            if (currentMinIndex != i) {
                data[currentMinIndex] = data[i];
                data[i] = currentMin;
            }

        }



    }
    public static void demoLinearSearchUnsorted() {
        System.out.println("--- Liner Search Timing (unsorted) ---");
        double timeI = System.currentTimeMillis();
        for (int arrSize = 20000; arrSize <= MAX_ARRAY_SIZE; arrSize += ARRAY_INCREMENT){
            int[] randArr = generateNumbers(arrSize, MAX_VALUE);
            int found = 0;

            for (int i = 0; i < NUMBER_SEARCHES; i++) {
                int search = (int) Math.round(Math.random() * MAX_VALUE);
                if (linearSearch(randArr, search)) {
                    found++;
                }
            }
            double timeF = System.currentTimeMillis();
            double timeT = timeF - timeI;
            System.out.printf("Number of items       : %d%n", arrSize);
            System.out.printf("Times value was found : %d%n", found);
            System.out.printf("Total search time     : %.0f ms%n", timeT);
            System.out.println();
        }

    }
    public static void demoLinearSearchSorted() {
        System.out.println("--- Liner Search Timing (selection sort) ---");
        double timeI = System.currentTimeMillis();
        for (int arrSize = 20000; arrSize <= MAX_ARRAY_SIZE; arrSize += ARRAY_INCREMENT) {
            int[] randArr = generateNumbers(arrSize, MAX_VALUE);

            selectionSort(randArr);

            int found = 0;

            for (int i = 0; i < NUMBER_SEARCHES; i++) {
                int search = (int) Math.round(Math.random() * MAX_VALUE);
                if (linearSearch(randArr, search)) {
                    found++;
                }
            }
            double timeF = System.currentTimeMillis();
            double timeT = timeF - timeI;
            System.out.printf("Number of items       : %d%n", arrSize);
            System.out.printf("Times value was found : %d%n", found);
            System.out.printf("Total search time     : %.0f ms%n", timeT);
            System.out.println();
        }
    }
    public static void demoBinarySearchSelectionSort() {
        System.out.println("--- Binary Search Timing (selection sort) ---");
        double timeI = System.currentTimeMillis();
        for (int arrSize = 20000; arrSize <= MAX_ARRAY_SIZE; arrSize += ARRAY_INCREMENT) {
            int[] randArr = generateNumbers(arrSize, MAX_VALUE);

            selectionSort(randArr);

            int found = 0;

            for (int i = 0; i < NUMBER_SEARCHES; i++) {
                int search = (int) Math.round(Math.random() * MAX_VALUE);
                if (binarySearch(randArr, search)) {
                    found++;
                }
            }
            double timeF = System.currentTimeMillis();
            double timeT = timeF - timeI;
            System.out.printf("Number of items       : %d%n", arrSize);
            System.out.printf("Times value was found : %d%n", found);
            System.out.printf("Total search time     : %.0f ms%n", timeT);
            System.out.println();
        }


    }
    public static void demoBinarySearchFastSort() {
        System.out.println("--- Binary Search Timing (Arrays.sort) ---");
        double timeI = System.currentTimeMillis();
        for (int arrSize = 20000; arrSize <= MAX_ARRAY_SIZE; arrSize += ARRAY_INCREMENT) {
            int[] randArr = generateNumbers(arrSize, MAX_VALUE);

            java.util.Arrays.sort(randArr);

            int found = 0;

            for (int i = 0; i < NUMBER_SEARCHES; i++) {
                int search = (int) Math.round(Math.random() * MAX_VALUE);
                if (binarySearch(randArr, search)) {
                    found++;
                }
            }
            double timeF = System.currentTimeMillis();
            double timeT = timeF - timeI;
            System.out.printf("Number of items       : %d%n", arrSize);
            System.out.printf("Times value was found : %d%n", found);
            System.out.printf("Total search time     : %.0f ms%n", timeT);
            System.out.println();
        }
    }

}













