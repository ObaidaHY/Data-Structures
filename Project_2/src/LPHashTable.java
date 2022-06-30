

public class LPHashTable extends OAHashTable {
	ModHash h ;
	int m; 
	
	public LPHashTable(int m, long p) {
		super(m);
		h = ModHash.GetFunc(m,p);
		this.m=m;
	}
	
	@Override
	public int Hash(long x, int i) {
		return (((h.Hash(x)+i)%m)+m)%m;
	}
	
}
