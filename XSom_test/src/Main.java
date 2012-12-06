import java.io.File;
import java.io.IOException;
import java.util.Iterator;


import org.xml.sax.ContentHandler;
import org.xml.sax.SAXException;

import com.sun.xml.xsom.XSElementDecl;
import com.sun.xml.xsom.XSSchema;
import com.sun.xml.xsom.XSSchemaSet;
import com.sun.xml.xsom.parser.XSOMParser;


public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args){
		XssParser xsp=new XssParser();
		xsp.parseDocument("schema.xsd");
	//	SAXParserExample spe = new SAXParserExample();
		//spe.runExample();
	}

}
