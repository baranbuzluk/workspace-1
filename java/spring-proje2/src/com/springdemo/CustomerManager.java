package com.springdemo;


public class CustomerManager implements ICustomerService {
	private ICustomerDAL customerDAL;

	//Construction-Injection
	public CustomerManager(ICustomerDAL customerDal) {
		this.customerDAL = customerDal;
	}

	
	//setter injection
/*	public void setCustomerDAL(ICustomerDAL customerDAL) {
		this.customerDAL = customerDAL;
	}
	*/
	public void add() {

		customerDAL.add();
	}
}
