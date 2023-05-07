public class GregorianDate extends Date{

    public GregorianDate(int year, int month, int day){
        super(year,month,day);
    }

    public GregorianDate(){
        super(1970,1,1);
        long mSec = (System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset());
        long lDays = (mSec/1000/60/60/24);
        addDays((int)lDays);
    }

    @Override
    public boolean isLeapYear() {
        if (super.getYear() % 4 == 0) {
            if (super.getYear() % 100 == 0) {
                if (super.getYear() % 400 == 0) {
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
}

