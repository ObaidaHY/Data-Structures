

public class QPHashTable extends OAHashTable {
	ModHash h ;
	int m; 

	public QPHashTable(int m, long p) {
		super(m);
		h = ModHash.GetFunc(m,p);
		this.m=m; 
	}
	
	@Override
	public int Hash(long x, int i) {
		return (int)(((h.Hash(x)+((long)i*i))%m)+m)%m;
	}
}
