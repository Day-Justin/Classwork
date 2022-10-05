public class VoterFactory{
  public voterInstance newVoter(String type, int age, int ssn, String fn, String ln){
    if (age < 18){
      System.out.println("Voter can't be under 18") ;
    } else {
      if("B".equalsIgnoreCase(type)){
        return new voterInstance(type, age, ssn, fn, ln);
      } else if("A".equalsIgnoreCase(type)){
        return new voterInstance(type, age, ssn, fn, ln);
      }
    }
    return null;
  } 
  
  private class voterInstance implements Vote{
    private int age;
    private int SSN;
    private String firstName;
    private String lastName;
    private String candidate;
    
    private voterInstance(String c, int a, int s, String f, String l){
    this.age = a;
    this.SSN = s;
    this.firstName = f;
    this.lastName = l;
    this.candidate = c;
    }
    
    public void castVote(){
      System.out.println(this.firstName + " " + this.lastName + " has voted for candidate " + this.candidate);
    }
  }
  
}