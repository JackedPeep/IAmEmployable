public class JulianDate{

    public JulianDate(int year, int month, int day){
        jDay = day;
        jMonth = month;
        jYear = year;
    }

    public JulianDate(){
        jDay = 19;
        jMonth = 12;
        jYear = 1969;
        long mSec = (System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset());
        long lDays = (mSec/1000/60/60/24);
        addDays((int)lDays);
    }
    private int jDay;
    private int jMonth;
    private int jYear;
    void addDays(int days) {
        for(int i = 0; i<days; i++){
            jDay++;
            if(jDay > getNumberOfDaysInMonth()){
                jDay = 1;
                jMonth++;
                if( jMonth > 12){
                    jMonth = 1;
                    jYear++;
                }
                else;


            }
            else;
        }

    }

    void subtractDays(int days) {
        for(int i = 0; i<days; i++){
            jDay--;
            if(jDay < 1){
                jMonth--;
                if( jMonth < 1){
                    jMonth = 12;
                    jYear--;
                }
                else;

                jDay = getNumberOfDaysInMonth();

            }
            else;
        }

    }
    public boolean isLeapYear() {
        //A method that returns true/false
        // if the calendar date is part of a leap year
        //They follow a simple cycle of three normal years
        // and one leap year, giving an average year that is 365.25 days long.
        if (jYear %4 == 0){
            return true;
        }
        else{
            return false;
        }

    }
    void printShortDate() {
        //A method that prints the calendar date(without a carriage return)
        // in mm/dd/yyyy format
        System.out.printf("%d/%d/%d",jMonth,jDay,jYear);
    }

    void printLongDate() {
        //A method that prints the calendar date

        // (without a carriage return) in Monthname dd, yyyy format
        System.out.printf("%s %d, %d",getMonthName(),jDay,jYear);
    }
    //The following 'get' accessor methods. These aren't used by the sample driver code,
    // but would normally be part of a class like this.
    // These accessor methods are used by the unit tests.
    // These methods return values about the calendar date the object represents, which might be today
    // or it might be something else...
    // whatever the current state of the date object is.
    public String getMonthName(){
        switch (jMonth){
            case 1: return "January";
            case 2: return "February";
            case 3: return "March";
            case 4: return "April";
            case 5: return "May";
            case 6: return "June";
            case 7: return "July";
            case 8: return "August";
            case 9: return "September";
            case 10: return "October";
            case 11: return "November";
            case 12: return "December";
            default: return "Not a month!";

        }
    }
    public int getMonth(){
        return jMonth;
    }
    public int getYear(){
        return jYear;
    }
    public int getDayOfMonth(){
        return jDay;
    }
    private int getNumberOfDaysInMonth(){
        switch (jMonth){
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
