package com.example.personapi.model;

import java.util.Objects;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class Person {

    private @Id @GeneratedValue Long id;
    private String firstName;
    private String lastName;
    private String emailAddress;

    public Person() {}

    public Person(String fName, String lName, String eAddress) {

        this.firstName = fName;
        this.lastName = lName;
        this.emailAddress = eAddress;
    }

    public Long getId() {
        return this.id;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public String getEmailAddress() {
        return this.emailAddress;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setFirstName(String fName) {
        this.firstName = fName;
    }

    public void setLastName(String lName) {
        this.lastName = lName;
    }

    public void setEmailAddress(String eAddress) {
        this.emailAddress = eAddress;
    }


    @Override
    public boolean equals(Object o) {

        if (this == o)
            return true;
        if (!(o instanceof Person))
            return false;
        Person person = (Person) o;
        return Objects.equals(this.id, person.id) && Objects.equals(this.firstName, person.firstName)
                && Objects.equals(this.lastName, person.lastName) && Objects.equals(this.emailAddress, person.emailAddress);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id, this.firstName, this.lastName, this.emailAddress);
    }

    @Override
    public String toString() {
        return "Person{" + "id=" + this.id + ", firstname='" + this.firstName + '\'' + ", lastName='" + this.lastName + '\'' + ", emailAddress='" + this.emailAddress + '\'' + '}';
    }
}