import java.util.ArrayList;

public class Registration implements IteratorContainer{


    ArrayList<String> firstName = new ArrayList<String>();
    ArrayList<String> lastName = new ArrayList<String>();
    ArrayList<String> address = new ArrayList<String>();

    public void addNames(String fname, String lname){
        firstName.add(fname);
        lastName.add(lname);
    }

    public void addAddresses(String home){
        address.add(home);
    }
/*

*/
    // Instantiating an Iterator inside the class so it can access its attributes
    @Override
    public Iterator getIterator() {
        return new ClassIterator();
    }

    private class ClassIterator implements Iterator {
        int index = 0;

        @Override
        public boolean hasNext() {

            if(index < firstName.size()){
                return true;
            }
            return false;
        }

        @Override
        public Object next() {

            if(this.hasNext()){
                ArrayList<String> person = new ArrayList<String>();
                person.add(firstName.get(index));
                person.add(lastName.get(index));
                person.add(address.get(index));
                index++;
                return person;
            }
            return null;
        }
    }
}

