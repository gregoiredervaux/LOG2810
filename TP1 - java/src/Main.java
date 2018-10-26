import struct.Graph;
import struct.Sommet;
import tools.P;
import vehicles.NIMH;
import vehicles.Priority;
import vehicles.Vehicule;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {

    private static final String GRAPHPATH = "centresLocaux.txt";
    private static Graph graph;


    public static void main(String[] args) {
        try {
            graph = creerGraphe();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        lireGraph(graph);
        plusCourtChemin(Priority.high,"23","27");
    }


    private static Graph creerGraphe() throws FileNotFoundException {


        File file = new File(GRAPHPATH);

        Scanner sc = new Scanner(file);

        Graph res = new Graph();
        String line = "";
        while(!(line = sc.nextLine()).equals("")){
            String id = line.substring(0,line.indexOf(","));
            boolean hasCharge = line.substring(line.indexOf(",")+1).equals("1");
            res.addSommet(new Sommet(id,hasCharge));
        }

        while(sc.hasNextLine()){
            line = sc.nextLine();
            String idx1 = line.substring(0,line.indexOf(","));
            String idx2 = line.substring(line.indexOf(",")+1,line.lastIndexOf(","));
            int dist = Integer.parseInt(line.substring(line.lastIndexOf(",")+1));
            res.getSommetById(idx1).addVoisin(res.getSommetById(idx2),dist);
            res.getSommetById(idx2).addVoisin(res.getSommetById(idx1),dist);
        }
        return res;

    }
    private static void lireGraph(Graph g){
        System.out.println(g);
    }
    private static void plusCourtChemin(Priority priority, String dep, String arr){

        Sommet depart = graph.getSommetById(dep);
        Sommet goal = graph.getSommetById(arr);
        Map<Sommet,Integer> distances = dijkstra(depart,goal);
        printmap(distances);
        Vehicule v = new NIMH(priority);
        int dist = getDistanceFromMap(goal,distances);
        float batt = v.updateBattery(dist);
        if(batt < 20){
            v.recharge();
            batteryDijkstra(depart,goal,v);
        }

    }
    private static Map<Sommet,Integer> dijkstra(Sommet depart, Sommet goal){
        Sommet current = depart;

        Map<Sommet,Integer> distances = new HashMap<>();

        for(Sommet s : graph.getSommets()){
            s.setSource(current);
            distances.put(s,current.getDistanceFrom(s));
        }
        distances.put(current,0);

        List<Sommet> nodes = new ArrayList<>(current.getVoisins().keySet());
        List<Sommet> fixed = new ArrayList<>();

        fixed.add(current);


        while(!nodes.isEmpty()){
    /*
            for(Sommet s : distances.keySet()){
                P.rintln("ID: "+s.getId() + " / Source: "+s.getSource().getId());
            }
    */
            Sommet closest = null;
            for(Sommet s : nodes){
                if (closest == null) {
                    closest = s;
                } else if (distances.get(s) < distances.get(closest)) {
                    closest = s;
                }
            }

            if(closest.equals(goal)){
                return distances;
            }

            nodes.remove(closest);
            fixed.add(closest);

            for(Sommet s : nodes){
                if ((distances.get(closest) + closest.getDistanceFrom(s)) < distances.get(s)) {
                    s.setSource(closest);
                    distances.put(s, distances.get(closest) + closest.getDistanceFrom(s));

                }
            }
            current = closest;
            for(Sommet s : current.getVoisins().keySet()){
                if(!fixed.contains(s) && !nodes.contains(s)){
                    s.setSource(current);
                    nodes.add(s);
                    distances.put(s,distances.get(current)+current.getDistanceFrom(s));
                }
            }
        }
        return distances;
    }


    private static void batteryDijkstra(Sommet depart, Sommet goal, Vehicule vehicule){
        List<Sommet> recharge = new ArrayList<>();

        for(Sommet s : graph.getSommets()){
            if(s.hasCharge()){
                recharge.add(s);
            }
        }

        P.rintln("------------------");
        Sommet bestCharger = null;
        int bestTime = 999999;
        float bestBattery = 0;
        Set<Sommet> bestToCharge = null;
        Set<Sommet> bestFromCharge = null;
        for(Sommet s : recharge){
            vehicule.recharge();
            Map<Sommet,Integer> mapToCharge;
            mapToCharge = dijkstra(depart,s);
            int timeToCharge = getDistanceFromMap(s,mapToCharge);
            Set<Sommet> distances = cloneSommetSet(mapToCharge.keySet());

            if(vehicule.updateBattery(timeToCharge) >= 20) {
                vehicule.recharge();
                Map<Sommet,Integer> mapFromCharge;
                int timeFromCharge = getDistanceFromMap(goal, mapFromCharge = dijkstra(s, goal));
                if(vehicule.updateBattery(timeFromCharge) >= 20) {
                    if (bestCharger == null || bestTime > timeFromCharge + timeToCharge) {
                        bestCharger = s;
                        bestTime = timeFromCharge + timeToCharge;
                        bestToCharge = distances;
                        bestFromCharge = cloneSommetSet(mapFromCharge.keySet());
                        bestBattery = vehicule.getBattery();
                        P.rintln(bestFromCharge);
                    }
                }
            }
        }

        if (bestCharger != null) {
            P.rintln("------------------");
            P.rintln(bestToCharge);
            P.rintln("------------------");
            P.rintln(bestFromCharge);
            P.rintln("------------------");
            P.rintln(bestTime);

            List<Sommet> pathToCharge = new ArrayList<>(bestToCharge);
            List<Sommet> pathFromCharge = new ArrayList<>(bestFromCharge);

            Sommet current=null;
            for(Sommet s : pathFromCharge){
                if(s.equals(goal)) {
                    current = s;
                    break;
                }
            }
            List<String> path = new ArrayList<>();

            while(!(current.equals(bestCharger))){
                path.add(0,current.getId());
                current = current.getSource();
            }
            path.add(0,"["+bestCharger.getId()+"]");

            for(Sommet s : pathToCharge){
                if(s.equals(bestCharger)) {
                    current = s;
                    break;
                }
            }
            current = current.getSource();
            while(!(current.getSource().equals(current))){
                path.add(0,current.getId());
                current = current.getSource();
            }
            path.add(0,depart.getId());

            P.rintln(path);
            P.rintln("Battery left : "+bestBattery);

        }
    }


    private static int getDistanceFromMap(Sommet goal, Map<Sommet,Integer> distances){
        return distances.get(goal);
    }

    private static void printmap(Map map){
        for(Object o : map.keySet()){
            System.out.println(o+" -> "+map.get(o));
        }
    }


    private static Set<Sommet> cloneSommetSet(Set<Sommet> toClone){
        Set<Sommet> toReturn = new HashSet<>();

        for(Sommet s : toClone){
            Sommet toAdd = new Sommet(s.getId(),s.getVoisins(),s.hasCharge());
            toAdd.setSource(s.getSource());
            toReturn.add(toAdd);
        }

        return toReturn;
    }

}
