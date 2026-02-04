package ChainOfResponsibility_LoggerLLD;

public class ErrorLogProcessor extends LogProcessor{
    public ErrorLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
     }
     @Override
     public void Log(LogLevel lgLevel, String message){
        if(lgLevel==LogLevel.ERROR){
            System.out.println("Info Log");
        }else{
            super.Log(lgLevel, message);
        }
     } 
}
