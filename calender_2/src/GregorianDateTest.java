import org.junit.Assert;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;
import java.util.Calendar;
import java.util.GregorianCalendar;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class GregorianDateTest {
    /**
     * @brief This test verifies that the default constructor successfully sets the current day, month, and year
     */
    @org.junit.Test
    public void aGregorianDateTestDefaultConstructor() {
        GregorianDate date = new GregorianDate();

        GregorianCalendar today = new GregorianCalendar();
        today.setGregorianChange(new java.util.Date(Long.MIN_VALUE));
        Assert.assertEquals("Default Constructor year is wrong", today.get(Calendar.YEAR), date.getYear());
        Assert.assertEquals("Default Constructor month is wrong",today.get(Calendar.MONTH) + 1, date.getMonth());
        Assert.assertEquals("Default Constructor name is wrong",today.getDisplayName(Calendar.MONTH, Calendar.LONG, new java.util.Locale("en","US")), date.getMonthName());
        Assert.assertEquals("Default Constructor day is wrong",today.get(Calendar.DAY_OF_MONTH), date.getDayOfMonth());
    }

    /**
     * @brief This test checks that the constructor correctly sets the year, month, and day
     */
    @org.junit.Test
    public void bGregorianDateTestConstructorWithParameters() {
        int year = 2016;
        int month = 4;
        int day = 25;
        GregorianDate date = new GregorianDate(year, month, day);

        Assert.assertEquals("Constructor with parameters year is wrong", year, date.getYear());
        Assert.assertEquals("Constructor with parameters month is wrong",month, date.getMonth());
        Assert.assertEquals("Constructor with parameters name is wrong", "April", date.getMonthName());
        Assert.assertEquals("Constructor with parameters day is wrong", day, date.getDayOfMonth());
    }

    /**
     * @brief This test adds days from a known date to jump days, months, and years
     */
    @org.junit.Test
    public void cGregorianDateTestAddDaysMethod() {
        int year = 2016;
        int month = 4;
        int day = 15;

        // Test an increase in days
        for (int i = 0; i < 10; i++) {
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::addDays failed to handle " + Integer.toString(i) + " days";
            date.addDays(i);

            Assert.assertEquals(msg + ". Incorrect day calculation", day + i, date.getDayOfMonth());
            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test an increase in months
        for (int i = 0; i < 5; i++) {
            int dayIncrease = i * 28;
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::addDays failed to handle a month offset based on " + Integer.toString(dayIncrease) + " days";
            date.addDays(dayIncrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month + i, date.getMonth());
        }

        // Test an increase in years
        for (int i = 0; i < 10; i++) {
            int dayIncrease = i * 365;
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::addDays failed to handle a year offset based on " + Integer.toString(dayIncrease) + " days";
            date.addDays(dayIncrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year + i, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test an increase in years
        for (int i = 0; i < 5; i++) {
            int dayIncrease = i * 3650;
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::addDays failed to handle a decade offset based on " + Integer.toString(dayIncrease) + " days";
            date.addDays(dayIncrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year + (i * 10), date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }
    }

    /**
     * @brief This test subtracts days from a known date to jump days, months, and years
     */
    @org.junit.Test
    public void dGregorianDateTestSubtractDaysMethod() {
        int year = 2016;
        int month = 12;
        int day = 15;

        // Test a decrease in days
        for (int i = 0; i < 10; i++) {
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::subtractDays failed to handle " + Integer.toString(i) + " days";
            date.subtractDays(i);

            Assert.assertEquals(msg + ". Incorrect day calculation", day - i, date.getDayOfMonth());
            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test a decrease in months
        for (int i = 0; i < 5; i++) {
            int dayDecrease = i * 28;
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::subtractDays failed to handle a month offset based on " + Integer.toString(dayDecrease) + " days";
            date.subtractDays(dayDecrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month - i, date.getMonth());
        }

        // Test a decrease in years
        for (int i = 0; i < 10; i++) {
            int dayDecrease = i * 365;
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::subtractDays failed to handle a year offset based on " + Integer.toString(dayDecrease) + " days";
            date.subtractDays(dayDecrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year - i, date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }

        // Test a decrease in years
        for (int i = 0; i < 5; i++) {
            int dayDecrease = i * 3650;
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::subtractDays failed to handle a decade offset based on " + Integer.toString(dayDecrease) + " days";
            date.subtractDays(dayDecrease);

            Assert.assertEquals(msg + ". Incorrect year calculation", year - (i * 10), date.getYear());
            Assert.assertEquals(msg + ". Incorrect month calculation", month, date.getMonth());
        }
    }

    /**
     * @brief This test runs through a set of years and checks if they are leap years using an array of known leap years
     */
    @org.junit.Test
    public void eGregorianDateTestIsLeapYearMethod() {
        int [] leapYears = {2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096};
        int leapYearIndex = 0;
        int month = 12;
        int day = 15;

        for (int year = leapYears[0]; year < leapYears[leapYears.length - 1]; year++) {
            GregorianDate date = new GregorianDate(year, month, day);
            String msg = "The GregorianDate::isLeap year incorrectly classified " + Integer.toString(year);

            if (year == leapYears[leapYearIndex]) {
                Assert.assertTrue(msg + " as NOT a leap year", date.isLeapYear());
                leapYearIndex++;
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
    public void fTestGregorianDateTestAddLotsOfDays() {
        GregorianDate date = new GregorianDate(1989, 11, 9);
        date.addDays(10000);
        Assert.assertEquals("Adding lots of days year wrong, test 1", 2017, date.getYear());
        Assert.assertEquals("Adding lots of days month wrong, test 1", 3, date.getMonth());
        Assert.assertEquals("Adding lots of days day wrong, test 1", 27, date.getDayOfMonth());

        date = new GregorianDate(1980, 1, 6);
        date.addDays(30000);
        Assert.assertEquals("Adding lots of days year wrong, test 2", 2062, date.getYear());
        Assert.assertEquals("Adding lots of days month wrong, test 2", 2, date.getMonth());
        Assert.assertEquals("Adding lots of days day wrong, test 2", 24, date.getDayOfMonth());

        date = new GregorianDate(1970, 1, 1);
        date.addDays(24855);
        Assert.assertEquals("Adding lots of days year wrong, test 3", 2038, date.getYear());
        Assert.assertEquals("Adding lots of days month wrong, test 3", 1, date.getMonth());
        Assert.assertEquals("Adding lots of days day wrong, test 3", 19, date.getDayOfMonth());
    }

    /**
     * @brief This test subtracts a lot of days from a known day
     */
    @org.junit.Test
    public void gTestGregorianDateTestSubtractLotsOfDays() {
        GregorianDate date = new GregorianDate(2017, 3, 27);
        date.subtractDays(10000);
        Assert.assertEquals("Subtracting lots of days year wrong, test 1", 1989, date.getYear());
        Assert.assertEquals("Subtracting lots of days month wrong, test 1", 11, date.getMonth());
        Assert.assertEquals("Subtracting lots of days day wrong, test 1", 9, date.getDayOfMonth());

        date = new GregorianDate(2062, 2, 24);
        date.subtractDays(30000);
        Assert.assertEquals("Subtracting lots of days year wrong, test 2", 1980, date.getYear());
        Assert.assertEquals("Subtracting lots of days month wrong, test 2", 1, date.getMonth());
        Assert.assertEquals("Subtracting lots of days day wrong, test 2", 6, date.getDayOfMonth());

        date = new GregorianDate(2038, 1, 19);
        date.subtractDays(24855);
        Assert.assertEquals("Subtracting lots of days year wrong, test 3", 1970, date.getYear());
        Assert.assertEquals("Subtracting lots of days month wrong, test 3", 1, date.getMonth());
        Assert.assertEquals("Subtracting lots of days day wrong, test 3", 1, date.getDayOfMonth());
    }
}