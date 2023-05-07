public class GregorianDate{

    public GregorianDate(int year, int month, int day){
        gDay = day;
        gMonth = month;
        gYear = year;
    }

    public GregorianDate(){
        gDay = 1;
        gMonth = 1;
        gYear = 1970;
        long mSec = (System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset());
        long lDays = (mSec/1000/60/60/24);
        addDays((int)lDays);
    }

    private int gDay;
    private int gMonth;
    private int gYear;


    void addDays(int days) {
        for(int i = 0; i<days; i++){
            gDay++;
            if(gDay > getNumberOfDaysInMonth()){
                gDay = 1;
                gMonth++;
                if( gMonth > 12){
                    gMonth = 1;
                    gYear++;
                }
                else;


            }
            else;
        }

    }

    void subtractDays(int days) {
        for(int i = 0; i<days; i++){
            gDay--;
            if(gDay < 1){
                gMonth--;
                if( gMonth < 1){
                    gMonth = 12;
                    gYear--;
                }
                else;

                gDay = getNumberOfDaysInMonth();

            }
            else;
        }

    }

    boolean isLeapYear() {
        if (gYear % 4 == 0) {
            if (gYear % 100 == 0) {
                if (gYear % 400 == 0) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return true;
            }
        } else {
            return false;
        }


    }

    void printShortDate() {
        //A method that prints the calendar date(without a carriage return)
        // in mm/dd/yyyy format
        System.out.printf("%d/%d/%d",gMonth,gDay,gYear);
    }

    void printLongDate() {
        //A method that prints the calendar date

        // (without a carriage return) in Monthname dd, yyyy format
        System.out.printf("%s %d, %d",getMonthName(),gDay,gYear);
    }

    //The following 'get' accessor methods. These aren't used by the sample driver code,
    // but would normally be part of a class like this.
    // These accessor methods are used by the unit tests.
    // These methods return values about the calendar date the object represents, which might be today
    // or it might be something else...
    // whatever the current state of the date object is.
    public String getMonthName() {
        switch (gMonth) {
            case 1:
                return "January";
            case 2:
                return "February";
            case 3:
                return "March";
            case 4:
                return "April";
            case 5:
                return "May";
            case 6:
                return "June";
            case 7:
                return "July";
            case 8:
                return "August";
            case 9:
                return "September";
            case 10:
                return "October";
            case 11:
                return "November";
            case 12:
                return "December";
            default:
                return "Not a month!";


        }
    }

    public int getMonth() {
        return gMonth;
    }

    public int getYear() {
        return gYear;
    }

    public int getDayOfMonth() {
        return gDay;
    }
    private int getNumberOfDaysInMonth(){
        switch (gMonth){
            case 1: return 31;
            case 2: if(isLeapYear()){
                return 29;
            }
            else{
                return 28;
            }
            case 3: return 31;
            case 4: return 30;
            case 5: return 31;
            case 6: return 30;
            case 7: return 31;
            case 8: return 31;
            case 9: return 30;
            case 10: return 31;
            case 11: return 30;
            case 12: return 31;
            default: return 0;

        }
    }
    private int getNumberOfDaysInYear(){
        if(isLeapYear()){
            return 366;
        }
        else{
            return 365;
        }
    }
}
