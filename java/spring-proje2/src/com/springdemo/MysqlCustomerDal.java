package com.springdemo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;


public class MysqlCustomerDal implements ICustomerDAL {
	
	@Value("${sqlConnectionString}")
	private String connectionString;

	public void setConnectionString(String connectionString) {
		this.connectionString = connectionString;
	}
	public String getConnectionString() {
		return connectionString;
	}
	@Override
	public void add() {
		System.out.println("Connection String: " + this.connectionString);
		System.out.println("Mysql veritabaný çalýþtý");

	}
}
