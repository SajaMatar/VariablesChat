import java.net.*;
import java.io.*;

public class Server{
    public static void main(String[] args) {
    System.out.println("Waiting for clients ....... ");
    int port = 4444;
    ServerSocket server = null;

    try {
// create the a waiting socket 
      server = new ServerSocket(port);
      System.out.println("you are running on port "+port+" ......\n");
    
      while(true){
 // create the client socket (using a blocking function)
      Socket client = server.accept();
      System.out.println("**conncetion established **");   
            
// read from the clients socket 
        BufferedReader message = new BufferedReader (new InputStreamReader(client.getInputStream()));
        String wut; 

        while((wut = message.readLine())!= null ){
        PrintWriter out = new PrintWriter (client.getOutputStream(), true);
// send to the output stream this message 
       out.println("[Server] >> "+wut);
        }
      }

    }
       catch (Exception e) {
        System.out.println("error");
        }
    


        
    }
    


}
