


public class OracleCustomerDal implements ICustomerDAL{
	private String connectionString;

	public void setConnectionString(String connectionString) {
		this.connectionString = connectionString;
	}
	public String getConnectionString() {
		return connectionString;
	}
	public void add() {
		System.out.println("Connection String: "+this.connectionString);
		System.out.println("Oracle Database eklendi..");
	}

}
