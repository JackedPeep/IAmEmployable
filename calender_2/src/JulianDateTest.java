import org.junit.Assert;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;
import java.util.Calendar;
import java.util.GregorianCalendar;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class JulianDateTest {
    /**
     * @brief Tests that the default constructor correctly calculates today
     */
    @org.junit.Test
    public void aJulianDateTestDefaultConstructor() {
        JulianDate date = new JulianDate();

        GregorianCalendar today = new GregorianCalendar();
        today.setGregorianChange(new java.util.Date(Long.MAX_VALUE));
        Assert.assertEquals("Default Constructor year is wrong", today.get(Calendar.YEAR), date.getYear());
        Assert.assertEquals("Default Constructor month is wrong", today.get(Calendar.MONTH) + 1, date.getMonth());
        Assert.assertEquals("Default Constructor name is wrong", today.getDisplayName(Calendar.MONTH, Calendar.LONG, new java.util.Locale("en","US")), date.getMonthName());
        Assert.assertEquals("Default Constructor day is wrong", today.get(Calendar.DAY_OF_MONTH), date.getDayOfMonth());
    }

    /**
     * @brief Tests that the constructor correctly sets day, month, and year
     */
    @org.junit.Test
    public void bJulianDateTestConstructorWithParameters() {
        int year = 2026;
        int month = 5;
        int day = 15;
        JulianDate date = new JulianDate(year, month, day);

        Assert.assertEquals("Constructor with parameters year is wrong", year, date.getYear());
        Assert.assertEquals("Constructor with parameters month is wrong", month, date.getMonth());
        Assert.assertEquals("Constructor with parameters name is wrong", "May", date.getMonthName());
        Assert.assertEquals("Constructor with parameters day is wrong", day, date.getDayOfMonth());
    }

    /**
     * @brief This test add days from a known date to jump days, months, and years
     */
    @org.junit.Test
    public void cJulianDateTestAddDaysMethod() {
        int year = 2016;
        int month = 4;
        int day = 15;

        // Test an increase in days
        for (int i = 0; i < 10; i++) {
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::addDays failed to handle " + Integer.toString(i) + " days";
            date.addDays(i);

            Assert.assertEquals(msg + ". Incorrect day calculation", day + i, date.getDayOfMonth());
            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test an increase in months
        for (int i = 0; i < 5; i++) {
            int dayIncrease = i * 28;
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::addDays failed to handle a month offset based on " + Integer.toString(dayIncrease) + " days";
            date.addDays(dayIncrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month + i, date.getMonth());
        }

        // Test an increase in years
        for (int i = 0; i < 10; i++) {
            int dayIncrease = i * 365;
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::addDays failed to handle a year offset based on " + Integer.toString(dayIncrease) + " days";
            date.addDays(dayIncrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year + i, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test an increase in decades
        for (int i = 0; i < 5; i++) {
            int dayIncrease = i * 3650;
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::addDays failed to handle a decade offset based on " + Integer.toString(dayIncrease) + " days";
            date.addDays(dayIncrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year + (i * 10), date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }
    }


    /**
     * @brief This test subtracts days from a known date to jump days, months, and years
     */
    @org.junit.Test
    public void dJulianDateTestSubtractDaysMethod() {
        int year = 2016;
        int month = 12;
        int day = 15;

        // Test a decrease in days
        for (int i = 0; i < 10; i++) {
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::subtractDays failed to handle " + Integer.toString(i) + " days";
            date.subtractDays(i);

            Assert.assertEquals(msg + ". Incorrect day calculation", day - i, date.getDayOfMonth());
            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test a decrease in months
        for (int i = 0; i < 5; i++) {
            int dayDecrease = i * 28;
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::subtractDays failed to handle a month offset based on " + Integer.toString(dayDecrease) + " days";
            date.subtractDays(dayDecrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month - i, date.getMonth());
        }

        // Test a decrease in years
        for (int i = 0; i < 10; i++) {
            int dayDecrease = i * 365;
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::subtractDays failed to handle a year offset based on " + Integer.toString(dayDecrease) + " days";
            date.subtractDays(dayDecrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year - i, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test a decrease in decades
        for (int i = 0; i < 5; i++) {
            int dayDecrease = i * 3650;
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The JulianDate::subtractDays failed to handle a decade offset based on " + Integer.toString(dayDecrease) + " days";
            date.subtractDays(dayDecrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year - (i * 10), date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }
    }

    /**
     * @brief Tests that the leap year is correctly calculated
     */
    @org.junit.Test
    public void eJulianDateTestIsLeapYearMethod() {
        int month = 12;
        int day = 15;

        for (int year = 1; year < 4000; year++) {
            JulianDate date = new JulianDate(year, month, day);
            String msg = "The Julian::isLeap year incorrectly classified " + Integer.toString(year);

            if (year % 4 == 0) {
                Assert.assertTrue(msg + " as NOT a leap year", date.isLeapYear());
            }
            else {
                Assert.assertFalse(msg + " as a leap year", date.isLeapYear());
            }
        }
    }

    /**
     * @brief This test adds lots of days to well-known days
     */
    @org.junit.Test
    public void fTestJulianDateDateTestAddLotsOfDays() {
        JulianDate date = new JulianDate(1989, 11, 9);
        date.addDays(10000);
        Assert.assertEquals("Year wrong adding lots of days, test 1", 2017, date.getYear());
        Assert.assertEquals("Month wrong adding lots of days, test 1", 3, date.getMonth());
        Assert.assertEquals("Day wrong adding lots of days, test 1", 27, date.getDayOfMonth());

        date = new JulianDate(1980, 1, 6);
        date.addDays(30000);
        Assert.assertEquals("Year adding lots of days wrong, test 2", 2062, date.getYear());
        Assert.assertEquals("Month adding lots of days wrong, test 2", 2, date.getMonth());
        Assert.assertEquals("Day adding lots of days wrong, test 2", 24, date.getDayOfMonth());

        date = new JulianDate(1970, 1, 1);
        date.addDays(24855);
        Assert.assertEquals("Year adding lots of days wrong, test 3", 2038, date.getYear());
        Assert.assertEquals("Month adding lots of days wrong, test 3", 1, date.getMonth());
        Assert.assertEquals("Day adding lots of days wrong, test 3", 19, date.getDayOfMonth());
    }

    /**
     * @brief This test subtracts a lot of days from a known day
     */
    @org.junit.Test
    public void gTestJulianDateDateTestSubtractLotsOfDays() {
        JulianDate date = new JulianDate(2017, 3, 27);
        date.subtractDays(10000);
        Assert.assertEquals("Year subtracting lots of days wrong, test 1", 1989, date.getYear());
        Assert.assertEquals("Month subtracting lots of days wrong, test 1", 11, date.getMonth());
        Assert.assertEquals("Day subtracting lots of days wrong, test 1", 9, date.getDayOfMonth());

        date = new JulianDate(2062, 2, 24);
        date.subtractDays(30000);
        Assert.assertEquals("Year subtracting lots of days wrong, test 2", 1980, date.getYear());
        Assert.assertEquals("Month subtracting lots of days wrong, test 2", 1, date.getMonth());
        Assert.assertEquals("Day subtracting lots of days wrong, test 2", 6, date.getDayOfMonth());

        date = new JulianDate(2038, 1, 19);
        date.subtractDays(24855);
        Assert.assertEquals("Year subtracting lots of days wrong, test 3", 1970, date.getYear());
        Assert.assertEquals("Month subtracting lots of days wrong, test 3", 1, date.getMonth());
        Assert.assertEquals("Day subtracting lots of days wrong, test 3", 1, date.getDayOfMonth());
    }
}