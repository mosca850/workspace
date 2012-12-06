import java.io.File;
import java.io.IOException;
import java.util.Iterator;

import org.xml.sax.ContentHandler;
import org.xml.sax.EntityResolver;
import org.xml.sax.ErrorHandler;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import com.sun.xml.xsom.XSElementDecl;
import com.sun.xml.xsom.XSSchema;
import com.sun.xml.xsom.XSSchemaSet;
import com.sun.xml.xsom.parser.XSOMParser;


public class XssParser implements ErrorHandler, EntityResolver {
	public XssParser(){
		
	}
	public void parseDocument(String document){
		XSOMParser parser = new XSOMParser();
		//parser.setErrorHandler(...);
		//parser.setEntityResolver(...);

		// set up XSLT
		
		try {
			parser.parse( new File("schema.xsd"));
			ContentHandler xsomHandler = parser.getParserHandler();
			parser.setErrorHandler(this);
			parser.setEntityResolver(this);
			// run the transformation and feed the result to XSOM
			

			XSSchemaSet results = parser.getResult();
			Iterator itr = results.iterateSchema();
			while( itr.hasNext() ) {
			  XSSchema s = (XSSchema)itr.next();
			  
			  System.out.println("Target namespace: "+s.getTargetNamespace());
			  
			  Iterator jtr = s.iterateElementDecls();
			  while( jtr.hasNext() ) {
			    XSElementDecl e = (XSElementDecl)jtr.next();
			    e.ge
			    System.out.print( e.getName() );
			    if( e.isAbstract() )
			      System.out.print(" (abstract)");
			    System.out.println();
			  }
			}
		} catch (SAXException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	@Override
	public void error(SAXParseException e) throws SAXException {
		e.printStackTrace();
		
	}
	@Override
	public void fatalError(SAXParseException e) throws SAXException {
		e.printStackTrace();
		
	}
	@Override
	public void warning(SAXParseException e) throws SAXException {
		e.printStackTrace();
		
	}
	@Override
	public InputSource resolveEntity(String arg0, String arg1)
			throws SAXException, IOException {
		System.out.println(arg0);
		return null;
	}
}
