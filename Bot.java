import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.io.FileWriter;

public class Bot {

	public static void main(String[] args) throws FileNotFoundException {

		// Takes in input from javaCom.py and assigns it to content
		String content = new Scanner(new File("info.txt")).useDelimiter("\\Z").next();
		String send = "";

		if (content.equals("hello")) {

			send = "Hello is true";

		}
		else {

			send = "Hello is false";

		}

		// Writes to "result.txt" whatever send is set to
		PrintWriter output = new PrintWriter("result.txt");
		output.write("");
		output.append(send);
		output.close();


	}

}

/* Content is what is typed in, and send is what will be printed back to Discord. */