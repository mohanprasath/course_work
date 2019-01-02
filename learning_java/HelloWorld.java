public class HelloWorld
{

    private void data_types(){
        System.out.println("Data Types Function:-");
        // int
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);

        // float
        System.out.println(Float.MAX_VALUE);
        System.out.println(Float.MIN_VALUE);

        // double
        System.out.println(Double.MAX_VALUE);
        System.out.println(Double.MIN_VALUE);
    }

    private void looping(){
        // Loops
        int sum = 0;
        for (int i=0;i<100 ;i++ ) {
            sum += i;
        }
        System.out.println("Sum from for loop is " + sum);
    }

	public static void main(String[] args)
	{
        //System.out.println("");
		System.out.println("Hello World!");
        HelloWorld helloWorld = new HelloWorld();
        helloWorld.data_types();
        helloWorld.looping();
	}
}
