package com.intro;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SessionFactory factory=new Configuration().configure("hibernate.cfg.xml").
				addAnnotatedClass(Car.class).buildSessionFactory();
		
		Session session=factory.getCurrentSession();
		session.beginTransaction();
		
		
	}

}
