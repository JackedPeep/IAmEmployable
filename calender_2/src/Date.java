public abstract class Date {
    //initializer
    public Date(int dYear,int dMonth,int dDay) {
         day = dDay;
         month = dMonth;
         year = dYear;

    }
    public Date() {

    }
    private int day;
    private int month;
    private int year;



        void addDays ( int days){
            for (int i = 0; i < days; i++) {
                day++;
                if (day > getNumberOfDaysInMonth()) {
                    day = 1;
                    month++;
                    if (month > 12) {
                        month = 1;
                        year++;
                    } else ;


                } else ;
            }

        }

        void subtractDays ( int days){
            for (int i = 0; i < days; i++) {
                day--;
                if (day < 1) {
                    month--;
                    if (month < 1) {
                        month = 12;
                        year--;
                    } else ;

                    day = getNumberOfDaysInMonth();

                } else ;
            }


        }
        void printShortDate() {
            //A method that prints the calendar date(without a carriage return)
            // in mm/dd/yyyy format
            System.out.printf("%d/%d/%d",month,day,year);
        }

        void printLongDate() {
            //A method that prints the calendar date

            // (without a carriage return) in Monthname dd, yyyy format
            System.out.printf("%s %d, %d",getMonthName(),day,year);
        }

        //The following 'get' accessor methods. These aren't used by the sample driver code,
        // but would normally be part of a class like this.
        // These accessor methods are used by the unit tests.
        // These methods return values about the calendar date the object represents, which might be today
        // or it might be something else...
        // whatever the current state of the date object is.
        public String getMonthName() {
            switch (month) {
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
        public boolean isLeapYear(){
            return false;
        }
        public int getMonth() {
            return month;
        }

        public int getYear() {
            return year;
        }

        public int getDayOfMonth() {
            return day;
        }
        private int getNumberOfDaysInMonth(){
            switch (month){
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