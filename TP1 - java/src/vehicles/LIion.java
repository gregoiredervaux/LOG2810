package vehicles;

public class LIion extends Vehicule {

    public LIion(){
        super();
    }

    public LIion(Priority priority){
        super();
        setPriority(priority);
    }

    @Override
    protected int getBatteryStep() {
        switch(this.getPriority()){

            case low:
                return 5;

            case medium:
                return 10;

            case high:
                return 30;
        }
        return 0;
    }
}
