package ChainOfResponsibility_LoggerLLD;

public class DebugLogProcessor extends LogProcessor{
    public DebugLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
     }
     @Override
     public void Log(LogLevel lgLevel, String message){
        if(lgLevel==LogLevel.DEBUG){
            System.out.println("Debug Log");
        }else{
            super.Log(lgLevel, message);
        }
     } 
}
