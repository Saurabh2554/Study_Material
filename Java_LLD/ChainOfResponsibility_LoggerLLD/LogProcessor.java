package ChainOfResponsibility_LoggerLLD;

public abstract class LogProcessor {
    public LogLevel logLevel;
    public LogProcessor nextLogProcessor;

    public LogProcessor(LogProcessor nextLogProcessor){
      this.nextLogProcessor = nextLogProcessor;
    }

    public void Log(LogLevel lgLevel, String message){
        if(nextLogProcessor!=null){
           nextLogProcessor.Log(lgLevel, message);
        }
        
    }
}
