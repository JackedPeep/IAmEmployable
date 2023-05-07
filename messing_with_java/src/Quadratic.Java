import java.util.Scanner;

public class Quadratic{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // System assigns quadratic formula variables based on user inputs.

        System.out.print("Enter a, b, c: ");
        double coefficientA = input.nextDouble();

        //System.out.print("Thank you! Now please type your coefficient B:");
        double coefficientB = input.nextDouble();

        //System.out.print("Ok now the final, coefficient C:");
        double coefficientC = input.nextDouble();

        // Calculations for the quadratic formula are here \/\/\/\/

        double apex = (Math.pow(coefficientB,2)-(4 * coefficientA * coefficientC));


        double plusX = ((-coefficientB + Math.sqrt((Math.pow(coefficientB,2)-(4 * coefficientA * coefficientC)))) / (2 * coefficientA));

        double minusX = ((-coefficientB - Math.sqrt((Math.pow(coefficientB,2)-(4 * coefficientA * coefficientC)))) / (2 * coefficientA));

        if (apex > 0) {
            System.out.println("There are two roots for the quadratic equation with these coefficients.");
            System.out.println("r1 = " + plusX);
            System.out.println("r1 = " + minusX);
        }
        if (apex < 0) {
            System.out.println("There are no roots for the quadratic equation with these coefficients.");

        }
        if (apex == 0) {
            System.out.println("There is one root for the quadratic equation with these coefficients.");
            System.out.println("r1 = " + minusX);
        }
    }

}