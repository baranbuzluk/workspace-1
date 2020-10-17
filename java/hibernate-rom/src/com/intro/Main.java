package com.intro;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Car.class)
				.buildSessionFactory();

		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();
			/*List<Car> list=session.createQuery("from Car").getResultList();
			for (Car car : list) {
				System.out.println(car.getCarId());
			}*/
			// inserrt
		/*	Car car=new Car();
			car.setCarLicense("06 test 15");
			car.setCarCompanyName("COOMPANY");
			car.setCarId((10));
			session.save(car);
			*/
			// delete
			Car c=session.get(Car.class, 10);
			session.delete(c);
			session.getTransaction().commit();
		} finally {
			session.close();
		}

	}

}
