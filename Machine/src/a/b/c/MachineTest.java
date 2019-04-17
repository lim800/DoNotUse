package a.b.c;

import java.util.ArrayList;

import net.sf.classifier4J.ClassifierException;
import net.sf.classifier4J.vector.HashMapTermVectorStorage;
import net.sf.classifier4J.vector.TermVectorStorage;
import net.sf.classifier4J.vector.VectorClassifier;

public class MachineTest {

	public static void main(String[] args) {
		String correct = "Java Program";
		ArrayList<String> arrayList = new ArrayList<String>();
		arrayList.add("Java Program");
		arrayList.add("java program");
		arrayList.add("javae program");
		arrayList.add("javaeee Program");
		arrayList.add("javaeeee programeeeee");
		arrayList.add("Python");
//		System.out.println(arrayList);
		
		TermVectorStorage storage = new HashMapTermVectorStorage();
//		System.out.println(storage);
		
		VectorClassifier vectorClassifier = new VectorClassifier(storage);
//		System.out.println(vectorClassifier);
		
		for (String term : arrayList) {
			
			try {
				vectorClassifier.teachMatch(correct);
				double result = (double) vectorClassifier.classify(term);
				System.out.println(result);
				
			} catch (ClassifierException e) {
				e.printStackTrace();
			}
			
		}

	}

}
