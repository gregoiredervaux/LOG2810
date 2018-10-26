package vehicles;

public class NIMH extends Vehicule{

    public NIMH(){
        super();
    }

    public NIMH(Priority priority){
        super();
        setPriority(priority);
    }

    @Override
    protected int getBatteryStep() {
        switch(this.getPriority()){

            case low:
                return 6;

            case medium:
                return 12;

            case high:
                return 48;

        }
        return 0;
    }
}
