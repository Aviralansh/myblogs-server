// The Type of formal gars and actual args must be same

public class File{

    public static void main(String[] args){

        System.out.println(newadd(0, 0));

    }


    public static void add(int a, int b){
        int sum = a + b;
        System.out.println("Sum : " + sum);
    }

    public static int newadd(int a, int b){
        int sum = a + b;
        return sum;
    }



    // The rules of typecasting are applicable on method invocations
    public static void test(int a){
        System.out.println("Value of a : " + a);
    }
    public static void display(char a){
        System.out.println("Value of a : "+ a);
    }




}





