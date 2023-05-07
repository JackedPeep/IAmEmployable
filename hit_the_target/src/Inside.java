

/**
 * Assignment 3 for CS 1410
 * This program determines if points are contained within circles or rectangles.
 */
public class
Inside {
    /**
     * This is the primary driver code to test the "inside" capabilities of the
     * various functions.
     */
    public static void main(String[] args) {
        double[] ptX = {1, 2, 3, 4};
        double[] ptY = {1, 2, 3, 4};
        double[] circleX = {0, 5};
        double[] circleY = {0, 5};
        double[] circleRadius = {3, 3};
        double[] rLeft = {-2.5, -2.5};
        double[] rTop = {2.5, 5.0};
        double[] rWidth = {6.0, 5.0};
        double[] rHeight = {5.0, 2.5};



        System.out.printf("%n");
        System.out.printf("--- Report of Points and Circles ---%n%n");
        for(int circle = 0; circle < 2; circle++) {
            for (int point = 0; point < 4; point++) {
                if (isPointInsideCircle(ptX[point], ptY[point], circleX[circle], circleY[circle], circleRadius[circle])) {
                    reportPoint(ptX[point], ptY[point]);
                    System.out.printf(" is inside ");
                    reportCircle(circleX[circle], circleY[circle], circleRadius[circle]);
                    System.out.printf("%n");
                } else {
                    reportPoint(ptX[point], ptY[point]);
                    System.out.printf(" is outside ");
                    reportCircle(circleX[circle], circleY[circle], circleRadius[circle]);
                    System.out.printf("%n");
                }

            }
        }
        System.out.printf("%n");
        System.out.printf("--- Report of Points and Rectangles ---%n%n");
        for(int rectangle = 0; rectangle < 2; rectangle++) {
            for (int point = 0; point < 4; point++) {
                if (isPointInsideRectangle(ptX[point], ptY[point], rLeft[rectangle], rTop[rectangle], rWidth[rectangle], rHeight[rectangle])) {
                    reportPoint(ptX[point], ptY[point]);
                    System.out.printf(" is inside ");
                    reportRectangle(rLeft[rectangle], rTop[rectangle], rWidth[rectangle], rHeight[rectangle]);
                    System.out.printf("%n");
                } else {
                    reportPoint(ptX[point], ptY[point]);
                    System.out.printf(" is outside ");
                    reportRectangle(rLeft[rectangle], rTop[rectangle], rWidth[rectangle], rHeight[rectangle]);
                    System.out.printf("%n");
                }

            }
        }

    }

    static void reportPoint(double x, double y){
        //print "Point(x,y)" with both x and y accurate to 1 decimal i.e. 1.0
        System.out.printf("Point(%.1f,% .1f)", x, y);

    }



    static void reportCircle(double x, double y, double r){
        //print "Circle(0.0, 0.0) Radius: 3.0" with x and y accurate to 1 decimal i.e. 1.0
        System.out.printf("Circle(%.1f,% .1f) Radius: %.1f", x, y, r);
    }



    static void reportRectangle(double rLeft, double rTop, double rWidth, double rHeight){
        //print "left: left top: top width: width height: height
        double right = rLeft + rWidth;
        double bottom = rTop - rHeight;

        System.out.printf("Rectangle(%.1f, %.1f, %.1f, %.1f)", rLeft, rTop, right, bottom);

    }



    static boolean isPointInsideCircle(double ptX, double ptY, double circleX, double circleY, double circleRadius){
        // prints "Point(1.0, 1.0) is inside/outside Circle(0.0, 0.0) Radius: 3.0"
       double xLen = ptX - circleX;
       double yLen = ptY - circleY;
       double ptDist = Math.sqrt(Math.pow(xLen,2) + Math.pow(yLen,2));
       if(ptDist <= circleRadius){
           return true;
       }
       else{
           return false;
       }


    }



    static boolean isPointInsideRectangle(double ptX, double ptY, double rLeft, double rTop, double rWidth, double rHeight){
        double right = rLeft + rWidth;
        double bottom = rTop - rHeight;

        if((ptX >= rLeft) & (ptX <= right) & (ptY >= bottom) & (ptY <= rTop)){
            return true;
        }
        else{
            return false;
        }

    }







}
