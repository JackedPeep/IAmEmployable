public class JulianDate extends Date{

    public JulianDate (int year, int month, int day){
        super(year,month,day);
    }

    public JulianDate(){
        super(1969,12,19);
        long mSec = (System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset());
        long lDays = (mSec/1000/60/60/24);
        addDays((int)lDays);
    }

    @Override
    public boolean isLeapYear() {
        //A method that returns true/false
        // if the calendar date is part of a leap year
        //They follow a simple cycle of three normal years
        // and one leap year, giving an average year that is 365.25 days long.
        if (super.getYear() %4 == 0){
            return true;
        }
        else{
            return false;
        }

    }

}
