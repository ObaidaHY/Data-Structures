

public class ModHash {
	
	long a;
	long b;
	int m;
	long p;
	
	public static ModHash GetFunc(int m, long p){
		return new ModHash(m , p,(long)(Math.random()*(p-1))+1,(long)(Math.random()*(p)));
	}
	
	public ModHash(int m, long p ,long a, long b) {
		this.m = m;
		this.p = p;
		this.a = a;
		this.b = b;
	}
	
	public int Hash(long key) {	
		return (int) (((((long)(a*key+b))%p)%m)+m)%m;
	}
}
