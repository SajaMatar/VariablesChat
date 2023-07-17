import java.net.*;
import java.io.*;

public class Client{
  public static void main(String[] args){
    String host=args[0];
    int port = 4444;
       
    try {
      Socket socket = new Socket(host,port);
    
      // takes standard input and turns it into a char buffer :
      BufferedReader userInput =new BufferedReader (new InputStreamReader(System.in));
      // writes into the servers socket   
      PrintWriter out =new PrintWriter (socket.getOutputStream(),true);
      //  reads from the servers socket 
      BufferedReader reply= new BufferedReader (new InputStreamReader(socket.getInputStream()));
          
      System.out.print("Enter your message >> ");
      String s ,  message_reply; 
      
      // the while condition updates the string 
      while((s = userInput.readLine()) != null ){
      // send the message you have just entered 
        out.println(s);

      //get the reply : 
        message_reply = reply.readLine();
      // chech weather the server is down or not (in the simplest way possible )
         if(message_reply != null) {  
          System.out.println(message_reply);
          System.out.print("\nEnter your message >> ");
          }
         else{
          System.out.println("Server is Down....");
          break;
         } 
       } 

    } catch (IOException ios) {
            System.out.println("Server is Down.");
       }
         
    }


}
