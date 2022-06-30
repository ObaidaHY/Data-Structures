

public class AQPHashTable extends OAHashTable {
	ModHash h ;
	int m;

	public AQPHashTable(int m, long p) {
		super(m);
		h = ModHash.GetFunc(m,p);
		this.m=m;
	}
	
	@Override
	public int Hash(long x, int i) {
		int sign = i%2 == 0 ? 1 : -1;
		return (int)(((h.Hash(x)+(sign*((long)i*i)))% m)+ m)%m;
	}
}
