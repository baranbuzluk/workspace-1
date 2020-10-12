
public class Main {
	public static void main(String[] args) {
		CustomerManager manager=new CustomerManager(new MysqlCustomerDal());
		manager.add();
	}
}
