import java.util.Scanner;
import java.time.LocalDate;
import java.time.Period;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = input.nextLine();
        System.out.println("Enter your birth year: ");
        int year = input.nextInt();
        System.out.println("Enter your birth month: ");
        int month = input.nextInt();
        System.out.println("Enter your birth day: ");
        int day = input.nextInt();
        LocalDate birthDate = LocalDate.of(year, month, day);
        Person person = new Person(name, birthDate);
        System.out.println("Heyy " + name + "!!!. You are " + person.age() + " years old!!!");
    }
}

class Person {
    private String name;
    private LocalDate birthDate;
    public Person(String name, LocalDate birthDate) {
        this.name = name;
        this.birthDate = birthDate;
    }
    public int age() {
        LocalDate today = LocalDate.now();
        Period period = Period.between(birthDate, today);
        return period.getYears();
    }
}
