package com.example;

import java.util.*;  // Import statement

/**
 * This is a block comment
 */

public class Test {

    public static void main(String[] args) {
        // Line comment
        int a = 5;  // decimal_integer_literal
        double b = 5.5;  // decimal_floating_point_literal
        boolean isTrue = true;  // boolean and true keyword
        boolean isFalse = false;  // boolean and false keyword
        String str = "Hello, World!";  // String
        char c = 'A';  // character_literal
        char esc = '\n';  // escape_sequence

        a += 1;  // += operator
        a -= 1;  // -= operator
        a *= 2;  // *= operator
        a /= 2;  // /= operator
        a %= 2;  // % operator
        a++;  // ++ operator
        a--;  // -- operator

        if (a == 5) {  // if and == operator
            System.out.println("Equal to 5");  // Method call
        } else if (a != 5) {  // else if and != operator
            System.out.println("Not equal to 5");
        } else {  // else keyword
            System.out.println("Something else");
        }

        while (a < 10) {  // while and < operator
            a++;  // Increment
        }

        for (int i = 0; i < 10; i++) {  // for loop and < operator
            System.out.println(i);  // Method call
        }

        try {  // try keyword
            throw new Exception("Error!");  // throw and new keyword
        } catch (Exception e) {  // catch keyword
            e.printStackTrace();  // Method call
        } finally {  // finally keyword
            System.out.println("Finally block");
        }

        assert a == 10;  // assert keyword and == operator

        switch (a) {
            case 10:  // case keyword
                System.out.println("Case 10");
                break;  // break keyword
            default:
                System.out.println("Default case");
                break;
        }

        boolean condition = a > 5 && a < 15;  // && and <, > operators
        boolean orCondition = a > 5 || a < 15;  // || operator

        Test test = new Test();
        test.exampleMethod();
    }

    public void exampleMethod() {
        super.toString();  // super keyword
        this.toString();  // this keyword
    }

    public interface ExampleInterface {  // interface keyword
        void example();  // Method in interface
    }

    public abstract class ExampleAbstractClass {  // abstract class
        public abstract void example();  // abstract method
    }

    public class ExampleClass extends ExampleAbstractClass implements ExampleInterface {  // class, extends, implements keywords
        @Override
        public void example() {  // @Override annotation
            // Method implementation
        }
    }

    private final int privateFinalVar = 1;  // private, final keywords
    protected static int protectedStaticVar = 2;  // protected, static keywords
    public int publicVar = 3;  // public keyword

    public void returnVoid() {
        return;  // return keyword
    }

    public int returnInt() {
        return 1;  // return keyword with value
    }

    boolean notCondition = !isTrue;  // ! operator
    boolean ternaryCondition = (a == 10) ? true : false;  // ternary operator ? :

    int[] array = new int[]{1, 2, 3};  // array and new keyword
}
