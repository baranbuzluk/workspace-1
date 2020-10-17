package com.javaproject.hibernateAndJPA.DataAcces;

import java.util.List;

import javax.persistence.EntityManager;

import org.hibernate.Session;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import com.javaproject.hibernateAndJPA.Entities.Car;
@Repository
public class HibernateCarDao implements ICarDao {

	private EntityManager entityManager;
	
	@Autowired
	public HibernateCarDao(EntityManager entityManager) {
		// TODO Auto-generated constructor stub
		this.entityManager=entityManager;
	}
	@Override
	@Transactional
	public List<Car> getAll() {
		// TODO Auto-generated method stub
		Session session=entityManager.unwrap(Session.class);
		List<Car> list=session.createQuery("from cars",Car.class).getResultList();
		return list;
	}

	@Override
	public void add(Car item) {
		// TODO Auto-generated method stub

	}

	@Override
	public void update(Car item) {
		// TODO Auto-generated method stub

	}

	@Override
	public void delete(Car item) {
		// TODO Auto-generated method stub

	}

}
