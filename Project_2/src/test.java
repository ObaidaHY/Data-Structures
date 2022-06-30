import java.util.HashSet;
import java.util.Set;

public class test {
	public static void main(String[] args) throws IHashTable.TableIsFullException, IHashTable.KeyAlreadyExistsException, IHashTable.KeyDoesntExistException {
		
		/*IHashTable lp = new QPHashTable(7, 17);
		for(int i = 0; i < 7; i++) {
			System.out.println(i);
			lp.Insert(new HashTableElement(i, 5));
		}
		System.out.println(lp.Find(0).GetKey());
		lp.Delete(3);
		lp.Insert(new HashTableElement(3, 0));*/
		
		
		/*int count = 0;
		for(int i = 0; i < 100; i++) {
			System.out.println("__________________________________________________");
			System.out.println("iteration :   " + i);
			int num = 0;
			try {
				IHashTable qp = new AQPHashTable(6571, 1000000007);
				for(int j = 0; j < 6571; j++) {
					int b = (int)(Math.random()*(100));
					qp.Insert(new HashTableElement(100*j + b,17));
					num = j;
				}
			}
			catch(Exception e) {
				System.out.println("Exception Type :   " + e.getClass());
				count++;
				System.out.println("num of insertions =   " + num);
				
			}
		}
		System.out.println("");
		System.out.println("");
		System.out.println("");
		System.out.println("");
		System.out.println("");
		System.out.println("");
		System.out.println("total number of Exceptions we've encounterd :    " + count);*/
		
		
		
		
		/*int m = 10000019;
		long p = 1000000007;
		int n = (Math.floorDiv(m, 2));
		IHashTable qp = new DoubleHashTable(m, p);
		long totalTime = 0;
		for(int j = 0; j < 3;j++) {
			Set<Integer> s = new HashSet<>();
			for(int i = 0; i < n; i++) {
				s.add(100*i + (int)(Math.random()*(100)));
			}
			
			long startTime = System.nanoTime();
			for(int k : s) {
				qp.Insert(new HashTableElement(k,17));
			}
			
			for(int k : s) {
				qp.Delete(k);
			}
			
			long endTime   = System.nanoTime();
			totalTime += endTime - startTime;
			//System.out.println("after iteration number   " + j +  "   " + (endTime - startTime));
			
		}
		
		System.out.println("after 3 iterations :    " + totalTime);
		
		totalTime = 0;
		for(int j = 3; j < 6;j++) {
			Set<Integer> s = new HashSet<>();
			for(int i = 0; i < n; i++) {
				s.add(100*i + (int)(Math.random()*(100)));
			}
			
			long startTime = System.nanoTime();
			for(int k : s) {
				qp.Insert(new HashTableElement(k,17));
			}
			
			for(int k : s) {
				qp.Delete(k);
			}
			
			long endTime   = System.nanoTime();
			totalTime += endTime - startTime;
			//System.out.println("after iteration number   " + j +  "   " + (endTime - startTime));
			
		}
		
		

		System.out.println("after 3 iterations :    " + totalTime);*/
		
		
		/*int m = 10000019;
		long p = 1000000007;
		int n = 19*(Math.floorDiv(m, 20));
		long total = 0;
		for(int k = 0; k < 20;k++) {
		IHashTable qp = new DoubleHashTable(m, p);
		long startTime = System.nanoTime();
		for(int i = 0; i < n; i++) {
			qp.Insert(new HashTableElement(100*i + (int)(Math.random()*(100)),17));
		}
		long endTime   = System.nanoTime();
		total += endTime - startTime;
		}
		System.out.println(total/20);*/
		
	}
}
