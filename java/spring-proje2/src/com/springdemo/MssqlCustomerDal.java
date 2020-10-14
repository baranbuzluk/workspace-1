package com.springdemo;

import org.springframework.stereotype.Component;

@Component("database")
public class MssqlCustomerDal implements ICustomerDAL {
	
	private String connectionString;

	public void setConnectionString(String connectionString) {
		this.connectionString = connectionString;
	}
	public String getConnectionString() {
		return connectionString;
	}
	@Override
	public void add() {
		System.out.println("Connection String: "+this.connectionString);
		System.out.println("MSSQL veritabanýna eklendi..");

	}
}
