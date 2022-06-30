
public abstract class OAHashTable implements IHashTable {
	
	private HashTableElement [] table;
	private HashTableElement deleted = new HashTableElement(-1,-1);
	
	public OAHashTable(int m) {
		this.table = new HashTableElement[m];
	}
	
	
	@Override
	public HashTableElement Find(long key) {
		for(int i = 0; i < table.length; i++) {
			int hashcode = Hash(key,i);
			HashTableElement cur = table[hashcode];
			if(cur == null) {break;}
			if (cur.GetKey() == key) {return table[hashcode];}
		}
		return null;
	}
	
	@Override
	public void Insert(HashTableElement hte) throws TableIsFullException,KeyAlreadyExistsException {
		if (Find(hte.GetKey()) == null) {
			for(int i = 0; i < table.length; i++) {
				int hashcode = Hash(hte.GetKey(),i);
				HashTableElement cur = table[hashcode];
				if (cur == null || cur.GetKey() < 0) {
					table[hashcode] = hte;
					return;
				}
			}
			throw new TableIsFullException(hte);
		}
		else {
			throw new KeyAlreadyExistsException(hte);
		}
	}
	
	@Override
	public void Delete(long key) throws KeyDoesntExistException {
		for(int i = 0; i < table.length; i++) {
			int hashcode = Hash(key,i);
			HashTableElement cur = table[hashcode];
			if (cur == null) {break;}
			if(cur.GetKey() == key) {
				table[hashcode] = deleted;
				return;
			}
		}
		throw new KeyDoesntExistException(key);
	}
	
	/**
	 * 
	 * @param x - the key to hash
	 * @param i - the index in the probing sequence
	 * @return the index into the hash table to place the key x
	 */
	public abstract int Hash(long x, int i);
}
