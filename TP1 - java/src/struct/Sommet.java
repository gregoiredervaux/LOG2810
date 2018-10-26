package struct;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Sommet {

    private String id;
    private Sommet source;
    private Map<Sommet,Integer> voisins;
    private boolean hasCharge;

    public Sommet(){
        this.voisins = new HashMap<>();
        this.source = null;
    }

    public Sommet(String id, boolean hasCharge){
        this();
        this.id = id;
        this.hasCharge = true;
    }

    public Sommet(String id, Map<Sommet,Integer> voisins, boolean hasCharge){
        this.source = null;
        this.id = id;
        this.hasCharge = true;
        this.voisins = voisins;

    }

    public Sommet(String id, Map<Sommet,Integer> voisins, boolean hasCharge, Sommet source){
        this.source = null;
        this.id = id;
        this.hasCharge = true;
        this.voisins = voisins;
        this.source = source;

    }

    public void addVoisin(Sommet s,int dist){
            voisins.put(s, dist);
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public boolean hasCharge() {
        return hasCharge;
    }

    public void setHasCharge(boolean hasCharge) {
        this.hasCharge = hasCharge;
    }

    public Map<Sommet, Integer> getVoisins() {
        return voisins;
    }

    public int getDistanceFrom(Sommet s){
            if(voisins.keySet().contains(s)){
                return voisins.get(s);
            }
            return 99999;
    }

    public void setSource(Sommet source) {
        this.source = source;
    }

    public Sommet getSource() {
        return source;
    }

    /*
    @Override
    public String toString(){
        String res = "(id : "+id+" -> ";

        for(Sommet s: voisins.keySet()){
            res += "("+"id : "+s.getId()+", dist : "+voisins.get(s)+")";
        }

        return res+")";
    }
    //*/
    //*
    @Override
    public String toString(){
        return "id : "+id+ (source == null ?"": ", source : "+source.getId()) ;
    }
    //*/

    @Override
    public boolean equals(Object s2){
        if(!(s2 instanceof Sommet)){
            return false;
        }
        return ((Sommet) s2).id.equals(this.id);
    }
}
