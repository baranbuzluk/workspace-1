package com.javaproject.hibernateAndJPA.business;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.javaproject.hibernateAndJPA.DataAcces.ICarDao;
import com.javaproject.hibernateAndJPA.Entities.Car;
@Service
public class CarManager  implements ICarService{

	private ICarDao carDao;
	
	
	@Autowired
	public CarManager(ICarDao carDao) {
		this.carDao = carDao;
	}

	@Override
	@Transactional
	public List<Car> getAll() {
		// TODO Auto-generated method stub
		return carDao.getAll();
	}

	@Override
	@Transactional
	public void add(Car item) {
		// TODO Auto-generated method stub
		
	}

	@Override
	@Transactional
	public void update(Car item) {
		// TODO Auto-generated method stub
		
	}

	@Override
	@Transactional
	public void delete(Car item) {
		// TODO Auto-generated method stub
		
	}

}
