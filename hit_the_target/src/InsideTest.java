import org.junit.Assert;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;

class Pair<X, Y> {
    public X x;
    public Y y;
    public Pair(X x, Y y) {
        this.x = x;
        this.y = y;
    }
}

/**
 * Unit tests for the isPointInsideCircle and isPointInsideRectangle methods.
 *
 * @author Brandon Holdaway, Karl Mortensen
 */
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class InsideTest {

    /**
     * @brief Test if all the methods are existent, or at least stubbed out. Fail to compile if not.
     * @author kmort
     */
    @org.junit.Test
    public void aDoYouHaveAllTheMethodsDefined() {
        double x = 9.1;
        double y = 8.7;
        double r = 4.2;
        double left = 1.2;
        double top = 1.3;
        double width = 1.4;
        double height = 1.5;
        double ptX = 1.6;
        double ptY = 1.7;
        double circleX = 1.8;
        double circleY = 1.9;
        double circleRadius = 2.01;

        Inside.reportPoint(x, y);
        Inside.reportCircle(x, y, r);
        Inside.reportRectangle(left, top, width, height);
        boolean result = Inside.isPointInsideCircle(ptX, ptY, circleX, circleY, circleRadius);
        result = Inside.isPointInsideRectangle(ptX, ptY, left, top, width, height);
    }

    /**
     * @brief Test if reportPoint() prints out correctly.
     * @author kmort
     */
//    @org.junit.Test
//    public void bDoesReportPointPrintRight() {
//        double x = 3.56;
//        double y = 412.0;
//
//        // Portions based on code from https://stackoverflow.com/questions/8708342/redirect-console-output-to-string-in-java
//        ByteArrayOutputStream baos = new ByteArrayOutputStream();
//        PrintStream ps = new PrintStream(baos);
//        PrintStream old = System.out;         // IMPORTANT: Save the old System.out!
//        System.setOut(ps);         // Tell Java to use your special stream
//        Inside.reportPoint(x, y);
//        System.out.flush(); // Put things back
//        System.setOut(old);
//        String resultRegular = baos.toString();
//        Assert.assertEquals(0, resultRegular.compareTo("Point(3.56, 412.0)"));
//
//        y = -412.0;
//        ByteArrayOutputStream baosNegative = new ByteArrayOutputStream();
//        ps = new PrintStream(baosNegative);
//        old = System.out;
//        System.setOut(ps);
//        Inside.reportPoint(x, y);
//        System.out.flush();
//        System.setOut(old);
//        String resultNegative = baosNegative.toString();
//        Assert.assertEquals(0, resultNegative.compareTo("Point(3.56, -412.0)"));
//
//        x = 0.0;
//        ByteArrayOutputStream baosZero = new ByteArrayOutputStream();
//        ps = new PrintStream(baosZero);
//        old = System.out;
//        System.setOut(ps);
//        Inside.reportPoint(x, y);
//        System.out.flush();
//        System.setOut(old);
//        String resultZero = baosZero.toString();
//        Assert.assertEquals(0, resultZero.compareTo("Point(0.0, -412.0)"));
//    }
//
//    /**
//     * @brief Test if reportCircle() prints out correctly.
//     * @author kmort
//     */
//    @org.junit.Test
//    public void cDoesReportCirclePrintRight() {
//        double x = 3.56;
//        double y = 412.0;
//        double r = 7.71;
//
//        // Portions based on code from https://stackoverflow.com/questions/8708342/redirect-console-output-to-string-in-java
//        ByteArrayOutputStream baos = new ByteArrayOutputStream();
//        PrintStream ps = new PrintStream(baos);
//        PrintStream old = System.out;         // IMPORTANT: Save the old System.out!
//        System.setOut(ps);         // Tell Java to use your special stream
//        Inside.reportCircle(x, y, r);
//        System.out.flush(); // Put things back
//        System.setOut(old);
//        String resultRegular = baos.toString();
//        Assert.assertEquals(0, resultRegular.compareTo("Circle(3.56, 412.0) Radius: 7.71"));
//
//        x = -3.56;
//        ByteArrayOutputStream baosNegative = new ByteArrayOutputStream();
//        ps = new PrintStream(baosNegative);
//        old = System.out;
//        System.setOut(ps);
//        Inside.reportCircle(x, y, r);
//        System.out.flush();
//        System.setOut(old);
//        String resultNegative = baosNegative.toString();
//        Assert.assertEquals(0, resultNegative.compareTo("Circle(-3.56, 412.0) Radius: 7.71"));
//
//        x = 0.0;
//        ByteArrayOutputStream baosZero = new ByteArrayOutputStream();
//        ps = new PrintStream(baosZero);
//        old = System.out;
//        System.setOut(ps);
//        Inside.reportCircle(x, y, r);
//        System.out.flush();
//        System.setOut(old);
//        String resultZero = baosZero.toString();
//        Assert.assertEquals(0, resultZero.compareTo("Circle(0.0, 412.0) Radius: 7.71"));
//    }
//
//    /**
//     * @brief Test if reportRectangle() prints out correctly.
//     * @author kmort
//     */
//    @org.junit.Test
//    public void dDoesReportRectanglePrintRight() {
//        double left = 1.2;
//        double top = 1.3;
//        double width = 1.4;
//        double height = 1.5;
//
//        // Portions based on code from https://stackoverflow.com/questions/8708342/redirect-console-output-to-string-in-java
//        ByteArrayOutputStream baos = new ByteArrayOutputStream();
//        PrintStream ps = new PrintStream(baos);
//        PrintStream old = System.out;         // IMPORTANT: Save the old System.out!
//        System.setOut(ps);         // Tell Java to use your special stream
//        Inside.reportRectangle(left, top, width, height);
//        System.out.flush(); // Put things back
//        System.setOut(old);
//        String resultRegular = baos.toString();
//
//        //  If I did this right, it should put the doubles at index 10, 12, 14, and 16 IFF your code EXACTLY MATCHES the assignment. If not, this will not pass. Ever.
//        String[] numbers = resultRegular.split("[, a-zA-Z\\(\\)]");
//        double answer = Math.abs(Double.parseDouble(numbers[10]) - left);
//        Assert.assertTrue (answer < 0.001);
//
//        answer = Math.abs(Double.parseDouble(numbers[12]) - top);
//        Assert.assertTrue (answer < 0.001);
//
//        double right = left + width;
//        answer = Math.abs(Double.parseDouble(numbers[14]) - right);
//        Assert.assertTrue (answer < 0.001);
//
//        double bottom = top - height;
//        answer = Math.abs(Double.parseDouble(numbers[16]) - bottom);
//        Assert.assertTrue (answer < 0.001);
//
//        left = -1.2;
//        ByteArrayOutputStream baosNegative = new ByteArrayOutputStream();
//        ps = new PrintStream(baosNegative);
//        old = System.out;
//        System.setOut(ps);
//        Inside.reportRectangle(left, top, width, height);
//        System.out.flush();
//        System.setOut(old);
//        String resultNegative = baosNegative.toString();
//        numbers = resultNegative.split("[, a-zA-Z\\(\\)]");
//        answer = Math.abs(Double.parseDouble(numbers[10]) - left);
//        Assert.assertTrue (answer < 0.001);
//
//        answer = Math.abs(Double.parseDouble(numbers[12]) - top);
//        Assert.assertTrue (answer < 0.001);
//
//        right = left + width;
//        answer = Math.abs(Double.parseDouble(numbers[14]) - right);
//        Assert.assertTrue (answer < 0.001);
//
//        bottom = top - height;
//        answer = Math.abs(Double.parseDouble(numbers[16]) - bottom);
//        Assert.assertTrue (answer < 0.001);
//
//        top = 0.0;
//        ByteArrayOutputStream baosZero = new ByteArrayOutputStream();
//        ps = new PrintStream(baosZero);
//        old = System.out;
//        System.setOut(ps);
//        Inside.reportRectangle(left, top, width, height);
//        System.out.flush();
//        System.setOut(old);
//        String resultZero = baosZero.toString();
//        numbers = resultZero.split("[, a-zA-Z\\(\\)]");
//        answer = Math.abs(Double.parseDouble(numbers[10]) - left);
//        Assert.assertTrue (answer < 0.001);
//
//        answer = Math.abs(Double.parseDouble(numbers[12]) - top);
//        Assert.assertTrue (answer < 0.001);
//
//        right = left + width;
//        answer = Math.abs(Double.parseDouble(numbers[14]) - right);
//        Assert.assertTrue (answer < 0.001);
//
//        bottom = top - height;
//        answer = Math.abs(Double.parseDouble(numbers[16]) - bottom);
//        Assert.assertTrue (answer < 0.001);
//    }

    /**
     * @brief Test if a point is inside of a circle
     */
    @org.junit.Test
    public void eIsPointInsideCircle() {
        double circleX = 2.3;
        double circleY = 4.2;
        double circleR = 5.1;
        ArrayList<Pair<Pair<Double, Double>, Boolean>> pointList = new ArrayList<Pair<Pair<Double, Double>, Boolean>>();
        pointList.add(new Pair<>(new Pair<>(1.123, 2.234), true));
        pointList.add(new Pair<>(new Pair<>(2.123, 3.234), true));
        pointList.add(new Pair<>(new Pair<>(3.123, 4.234), true));
        pointList.add(new Pair<>(new Pair<>(4.123, 5.234), true));
        pointList.add(new Pair<>(new Pair<>(5.123, 6.234), true));
        pointList.add(new Pair<>(new Pair<>(6.123, 7.234), true));
        pointList.add(new Pair<>(new Pair<>(7.123, 8.234), false));
        pointList.add(new Pair<>(new Pair<>(8.123, 9.234), false));
        pointList.add(new Pair<>(new Pair<>(9.123, 10.234), false));
        pointList.add(new Pair<>(new Pair<>(10.123, 111.234), false));

        pointList.add(new Pair<>(new Pair<>(-2.8, 4.2), true));
        pointList.add(new Pair<>(new Pair<>(7.3999, 4.2), true));
        pointList.add(new Pair<>(new Pair<>(2.3, 9.2999), true));
        pointList.add(new Pair<>(new Pair<>(2.3, -0.8999), true));

        for (Pair<Pair<Double, Double>, Boolean> item : pointList)
        {
            System.out.printf("Circle - testing point (%.2f,%.2f)\n", item.x.x, item.x.y);
            Assert.assertEquals(item.y, Inside.isPointInsideCircle(item.x.x, item.x.y, circleX, circleY, circleR));
        }
    }

    /**
     * @brief Test if a point is inside of a rectangle
     */
    @org.junit.Test
    public void fIsPointInsideRectangle() {
        double rLeft = 3.2;
        double rTop = 2.4;
        double width = 1.5;
        double height = 7.2;
        ArrayList<Pair<Pair<Double, Double>, Boolean>> pointList = new ArrayList<Pair<Pair<Double, Double>, Boolean>>();
        pointList.add(new Pair<>(new Pair<>(1.123, 2.234), false));
        pointList.add(new Pair<>(new Pair<>(2.123, 3.234), false));
        pointList.add(new Pair<>(new Pair<>(3.123, 4.234), false));
        pointList.add(new Pair<>(new Pair<>(4.123, 5.234), false));
        pointList.add(new Pair<>(new Pair<>(5.123, 6.234), false));
        pointList.add(new Pair<>(new Pair<>(6.123, 7.234), false));
        pointList.add(new Pair<>(new Pair<>(7.123, 8.234), false));
        pointList.add(new Pair<>(new Pair<>(8.123, 9.234), false));
        pointList.add(new Pair<>(new Pair<>(9.123, 10.234), false));
        pointList.add(new Pair<>(new Pair<>(10.123, 111.234), false));

        pointList.add(new Pair<>(new Pair<>(3.2, 2.4), true));
        pointList.add(new Pair<>(new Pair<>(4.7, 2.4), true));
        pointList.add(new Pair<>(new Pair<>(3.2, -4.8), true));
        pointList.add(new Pair<>(new Pair<>(4.7, -4.8), true));

        for (Pair<Pair<Double, Double>, Boolean> item : pointList)
        {
            System.out.printf("Rectangle - testing point (%.2f,%.2f)\n", item.x.x, item.x.y);
            Assert.assertEquals(item.y, Inside.isPointInsideRectangle(item.x.x, item.x.y, rLeft, rTop, width, height));
        }
    }
}
