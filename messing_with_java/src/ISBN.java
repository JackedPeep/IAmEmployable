import java.util.Scanner;

public class ISBN {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the first 9 digits of an ISBN: ");
        int iSPN = input.nextInt();

        int iSPN_d1 = (iSPN/100000000);
        int iSPN_n1 = iSPN - (iSPN_d1 * 100000000);
        int iSPN_d2 = (iSPN_n1/10000000);
        int iSPN_n2 = iSPN_n1 - (iSPN_d2 * 10000000);
        int iSPN_d3 = (iSPN_n2/1000000);
        int iSPN_n3 = iSPN_n2 - (iSPN_d3 * 1000000);
        int iSPN_d4 = (iSPN_n3/100000);
        int iSPN_n4 = iSPN_n3 - (iSPN_d4 * 100000);
        int iSPN_d5 = (iSPN_n4/10000);
        int iSPN_n5 = iSPN_n4 - (iSPN_d5 * 10000);
        int iSPN_d6 = (iSPN_n5/1000);
        int iSPN_n6 = iSPN_n5 - (iSPN_d6 * 1000);
        int iSPN_d7 = (iSPN_n6/100);
        int iSPN_n7 = iSPN_n6 - (iSPN_d7 * 100);
        int iSPN_d8 = (iSPN_n7/10);
        int iSPN_n8 = iSPN_n7 - (iSPN_d8 * 10);
        int iSPN_d9 = (iSPN_n8/1);

        int iSPN_d10 = ((iSPN_d1 * 1 + iSPN_d2 * 2 + iSPN_d3 * 3 + iSPN_d4 * 4 + iSPN_d5 * 5 + iSPN_d6 * 6 + iSPN_d7 * 7 + iSPN_d8 * 8 + iSPN_d9 *9) % 11);

        if (iSPN_d10 == 10){
        System.out.println("The ISBN-10 number is: " + iSPN_d1 + iSPN_d2 + iSPN_d3 + iSPN_d4 + iSPN_d5 + iSPN_d6 + iSPN_d7 + iSPN_d8 + iSPN_d9 + "X");

            }
        else {
            System.out.println("The ISBN-10 number is: " + iSPN_d1 + iSPN_d2 + iSPN_d3 + iSPN_d4 + iSPN_d5 + iSPN_d6 + iSPN_d7 + iSPN_d8 + iSPN_d9 + iSPN_d10);

        }
        }
    }


