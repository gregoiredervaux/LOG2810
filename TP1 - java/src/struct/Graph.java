package struct;

import java.util.ArrayList;
import java.util.List;

public class Graph {


    private List<Sommet> sommets;

    public Graph(){
        sommets = new ArrayList<>();
    }

    public Sommet getSommetById(String name){
        for (Sommet s : sommets){
            if(s.getId().equals(name)){
                return s;
            }
        }
        return null;
    }

    public boolean addSommet(Sommet s){
        return sommets.add(s);
    }
    public List<Sommet> getSommets(){
        return sommets;
    }

    @Override
    public String toString(){

        String res = "(";

        for(Sommet s : sommets){
            res+=s+"\n";
        }

        return res+")";
    }

}
