import java.util.Scanner;

public class Pyramid1 {


    public static void main(String[] args) {
        // 1. Take user input as int.
        Scanner input = new Scanner(System.in);
        System.out.print("User, input a number: ");
        int seed = input.nextInt();
        int seedLength = String.valueOf(seed).length();

        // 2. If user inputs invalid character then return error.


        // 3. Returns pyramid of numbers.
    for (int row = 1; row <= seed; row++){
            System.out.printf("%n");
            int nSpace = (seed-row+1)*(seedLength+1);
            System.out.printf("%"+nSpace+"s" , "");

        for (int col = 0; col <= (seed*2)-2; col++){
            if(row-col > 0) {

                System.out.printf("%"+(-seedLength-1)+"s" , String.valueOf(row - col));

            }
            else if(col < row*2-1){

                System.out.printf("%"+(-seedLength-1)+"s" , String.valueOf(col - row + 2));


            }


//            for (double chr = 0; chr < seedLength+1; chr++) {

                // Reminder: formatting for a string width looks like this
                // system.out.printf("'%15s' %n", "baeldung");
                // This returns '       baeldung'
                // You can also do this in the opposite direction with this
                // printf("'%-10s' %n", "baeldung");
                // This prints 'baeldung  '
                // The field width is the length of the largest number +1




                }
            }
        }

   }
//}