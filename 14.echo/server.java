/*
TITLE : Implement a Multi-threading application for echo server using socket programming in JAVA.
ASSIGNMENT NO. : B9
BATCH NO. : T3
Roll no. :
*/

//server.java

import java.io.*;
import java.net.*;
//import java.io.BufferedInputStream;
//import java.io.FileInputStream;
import java.io.IOException;
//import java.io.InputStream;

public class server
{
	public static void main(String args[])
	{
		int port = 6789;  //we can't choose a port less than 1024 if we are not privileged users (root)
		server s = new server( port );
		s.startServer();
    	}
    
    // declare a server socket and a client socket for the server
    
	ServerSocket echoServer = null;
	Socket client_socket = null;
    	int port;
    
    	public server( int port )
	{
		this.port = port;
   	}
    
	public void stopServer()
	{
		System.out.println( "Server is cleaned and exiting." );
		System.exit(0);
    	}
    
    	public void startServer()
	{
	        try
		{
			echoServer = new ServerSocket(port);
        	}
        	 catch (IOException e) 
		{
		    	System.out.println(e); // display whatever is read from the client
	        }   
	
		System.out.println( "Waiting for connections. Only one connection is allowed." );// it is displayed when client is not running
	
		while ( true )
		{
			try
			{
				client_socket = echoServer.accept();
				Server_Connection oneconnection = new Server_Connection(client_socket, this);
				oneconnection.run();
			}   
			catch (IOException e)
			{
				System.out.println(e);
		    	}
		}
	}    

}

class Server_Connection
{
	BufferedReader is;
	PrintStream os;
	Socket client_socket;
	server server;
    
	public Server_Connection(Socket client_socket, server server) 
	{
		this.client_socket = client_socket;
		this.server = server;
		System.out.println( "Connection established with : " + client_socket );
		try
	  	{
	    		is = new BufferedReader(new InputStreamReader(client_socket.getInputStream()));
		        os = new PrintStream(client_socket.getOutputStream());
	   	} catch (IOException e)
		{
	    		System.out.println(e);
		}
    	}
    
	public void run() 
	{
	        String line;
		try
		{
			boolean serverStop = false;
	                while (true) 
			{
				line = is.readLine(); // read line using the buffer reader meant for client socket
				System.out.println( "Received " + line );
		                int n = Integer.parseInt(line);
				if ( n == -1 ) // it indicates that client wants to stop.
				{
					serverStop = true;	
					break;
				}
				if ( n == 0 )
 				{
					System.out.println("want to start another client?  y/n");
					BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
					line=br.readLine();
					
					if(line=="n")
					 break;
					server.startServer();
					
				}
				else
				{	
		                	os.println("" + n*n ); 
				}

			}
	    		System.out.println( "Connection closed." );
		        is.close();
		        os.close(); // close the buffer readers
			client_socket.close();
	    		if ( serverStop ) 
				server.stopServer();
		} catch (IOException e)
		{
			System.out.println(e);
		}
    	}
}
