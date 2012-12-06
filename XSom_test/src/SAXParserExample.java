
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;

import org.xml.sax.helpers.DefaultHandler;

public class SAXParserExample extends DefaultHandler{

	List myEmpls;
	
	private String tempVal;
	
	
	
	public SAXParserExample(){
		myEmpls = new ArrayList();
	}
	
	public void runExample() {
		parseDocument();
		printData();
	}

	private void parseDocument() {
		
		//get a factory
		SAXParserFactory spf = SAXParserFactory.newInstance();
		try {
		
			//get a new instance of parser
			SAXParser sp = spf.newSAXParser();
			
			//parse the file and also register this class for call backs
			sp.parse("schema.xsd", this);
			
		}catch(SAXException se) {
			se.printStackTrace();
		}catch(ParserConfigurationException pce) {
			pce.printStackTrace();
		}catch (IOException ie) {
			ie.printStackTrace();
		}
	}

	/**
	 * Iterate through the list and print
	 * the contents
	 */
	private void printData(){
		
		System.out.println("No of Employees '" + myEmpls.size() + "'.");
		
		Iterator it = myEmpls.iterator();
		while(it.hasNext()) {
			System.out.println(it.next().toString());
		}
	}
	

	//Event Handlers
	public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
		//reset
		tempVal = "";
		System.out.print(uri);
		System.out.print(localName);
		System.out.println(qName);
	/*	if(qName.equalsIgnoreCase("Employee")) {
			//create a new instance of employee
			tempEmp = new Employee();
			tempEmp.setType(attributes.getValue("type"));
		}*/
	}
	

	public void characters(char[] ch, int start, int length) throws SAXException {
		 tempVal= new String(ch);

	}
	
	public void endElement(String uri, String localName, String qName) throws SAXException {
		System.out.print(uri);
		System.out.print(localName);
		System.out.println(qName);
		System.out.print(tempVal);
		if(qName.equalsIgnoreCase("Employee")) {
			
			//add it to the list
			//myEmpls.add(tempEmp);
			
		}else if (qName.equalsIgnoreCase("Name")) {
			//tempEmp.setName(tempVal);
		}else if (qName.equalsIgnoreCase("Id")) {
			//tempEmp.setId(Integer.parseInt(tempVal));
		}else if (qName.equalsIgnoreCase("Age")) {
			//tempEmp.setAge(Integer.parseInt(tempVal));
		}
		
	}
	

	
}
