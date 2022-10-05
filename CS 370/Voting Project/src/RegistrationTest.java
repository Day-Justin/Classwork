import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class RegistrationTest {

    Registration registration = new Registration();
    String[] firstNames = {"John", "Jane","J", "D"};

    // This checks if hasNext returns correct value
    @org.junit.jupiter.api.Test
    public void hasNext() {
        Iterator iter = registration.getIterator();
        assertFalse(iter.hasNext());
    }
    public void addData() {
        for (String name : firstNames) {
            registration.addNames(name, name);
            registration.addAddresses(name);
        }
    }

    @org.junit.jupiter.api.Test
    public void hasNext2() {
        addData();
        Iterator iter = registration.getIterator();
        assertTrue(iter.hasNext());
    }

    // Checking if next() returns the correct list of data
    @org.junit.jupiter.api.Test
    public void next() {
        ArrayList<String> person = new ArrayList<String>();
        person.add("John");
        person.add("John");
        person.add("John");
        addData();
        Iterator iter = registration.getIterator();
        assertEquals(iter.next(),person);
    }



}