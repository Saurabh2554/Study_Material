package ChainOfResponsibility_LoggerLLD;

public class InfoLogProcessor extends LogProcessor {
     public InfoLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
     }
     @Override
     public void Log(LogLevel lgLevel, String message){
        if(lgLevel==LogLevel.INFO){
            System.out.println("Info Log");
        }else{
            super.Log(lgLevel, message);

            //Insted can also do --->
            //nextLogProcessor.Log(lgLevel, message);

            // Second option is not correct because --->
                 // Easier to change later:
                    //Suppose in the future, the way you forward logs changes (e.g., you want to log a trace before forwarding). If all subclasses use super.Log(...), you change it in one place.
                // It must be the responsibility of base class to do forwarding to next child class not of the children. 
        }
     } 
}
