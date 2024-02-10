// Program Description: This program seeks to reverse a given string.

package Samples.Java.ChatGPT;
import java.util.Scanner;

public class StringReversal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        String reversed = ""; // Intentional bug: StringBuilder not used for reversal
        
        for (int i = input.length() - 1; i >= 0; i--) {
            reversed += input.charAt(i);
        }
        
        System.out.println("Reversed string: " + reversed);
        
        scanner.close();
    }
}

