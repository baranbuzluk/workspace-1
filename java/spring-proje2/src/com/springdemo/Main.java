package com.springdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.sun.org.apache.bcel.internal.util.ClassPath;

public class Main {
	public static void main(String[] args) {
		ClassPathXmlApplicationContext context=
				new ClassPathXmlApplicationContext("applicationContext.xml");
		
		//ICustomerService manager=new CustomerManager(context.getBean("database",ICustomerDAL.class));
		ICustomerDAL manager=context.getBean("database",ICustomerDAL.class);
		manager.add();
	}
}
