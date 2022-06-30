

public class DoubleHashTable extends OAHashTable {
	ModHash h1 ;
	ModHash h2 ;
	int m; 
	long p; 


	public DoubleHashTable(int m, long p) {
		super(m);
		h1 = ModHash.GetFunc(m,p);
		h2 = ModHash.GetFunc(m-1,p);
		this.m= m;
		this.p=p;

	}
	
	@Override
	public int Hash(long x, int i) {
		return (int)(((h1.Hash(x) + ((long)i*((long)h2.Hash(x)+1)))%m)+m)%m;
		
	}
	
}
