public class Primaries {

    public String politicalParty;
    public String ballot;

    public void party(String party){
       politicalParty = party;
    }

    public void ballot (){
        if (politicalParty == "Democrat"){
            ballot = "Democrat";
        }
        if (politicalParty == "Republican"){
            ballot = "Republican";
        }
        if (politicalParty == "Working Families"){
            ballot = "Working Families";
        }
        if (politicalParty == "Conservative"){
            ballot = "Conservative";
        }
    }
}
