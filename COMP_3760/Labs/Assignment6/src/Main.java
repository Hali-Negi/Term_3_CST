//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main
{
    public static void main(String[] args)
    {
        Lab6 lab = new Lab6();

        System.out.println("Testing SW_Recursive directly:");
        System.out.println("SW_Recursive(1,4) = " + lab.SW_Recursive(1, 4));
        System.out.println("SW_Recursive(3,3) = " + lab.SW_Recursive(3, 3));

        System.out.println();

        System.out.println("Running recursive timing test:");
        lab.RunRecursive(0, 5);

        System.out.println();

        System.out.println("Testing SW_DynamicProg directly:");
        System.out.println("SW_DynamicProg(1,4) = " + lab.SW_DynamicProg(1, 4));
        System.out.println("SW_DynamicProg(3,3) = " + lab.SW_DynamicProg(3, 3));

        System.out.println();

        System.out.println("Running dynamic programming timing test:");
        lab.RunDynamicProg(20, 24);

        System.out.println("Donut 1:");
        System.out.println("SW(37,37) = " + lab.SW_Big(37, 37));
    }

}