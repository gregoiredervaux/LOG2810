package vehicles;

public abstract class Vehicule {

    private float battery = 100;
    private Priority priority;
    protected abstract int getBatteryStep();

    public Vehicule(){
        priority = Priority.low;
    }

    public Vehicule(Priority p){
        priority=p;
    }

    public void recharge(){
        battery=100;
    }
    public void setPriority(Priority priority) {
        this.priority = priority;
    }

    public Priority getPriority(){
        return priority;
    }

    public float updateBattery(int min_passed){
        battery -= (getBatteryStep() * ((float)min_passed/60));
        return battery;
    }

    public float getBattery(){
        return battery;
    }
}
