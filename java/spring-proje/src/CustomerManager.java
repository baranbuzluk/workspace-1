
public class CustomerManager {
	private ICustomerDAL customerDAL;
	
	public CustomerManager(ICustomerDAL customerDal) {
		this.customerDAL=customerDal;
	}
public void add() {
	
	customerDAL.add();
}
}
